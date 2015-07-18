import errno
from io import BytesIO
import os
import re
import requests

try:
    from PIL import Image, ImageOps
except ImportError:
    raise RuntimeError('Image module of PIL needs to be installed')

from boto.s3.connection import S3Connection
from boto.exception import S3ResponseError
from boto.s3.key import Key

from url_for_s3 import url_for_s3

from .settings import * # Set AWS credentials here


def _thumbnail_resize(image, thumb_size, crop=None):
    """Performs the actual image cropping operation with PIL."""

    if crop == 'fit':
        img = ImageOps.fit(image, thumb_size, Image.ANTIALIAS)
    else:
        img = image.copy()
        img.thumbnail(thumb_size, Image.ANTIALIAS)

    return img

def thumbnail_s3(original_url, bucket_name,
                  thumb_size=(400,400), crop=None, quality=85):
    """Finds or creates a thumbnail for the specified image on Amazon S3."""
    scheme ='https'

    thumb_name = original_url.split('/')[::-1][0]

    thumb_url_full = url_for_s3(
        'imgs',
        bucket_name=bucket_name,
        filename=thumb_name,
        scheme=scheme)
    print(thumb_url_full)

    try:
        print('trying open')
        image = Image.open(requests.get(original_url, stream=True).raw)
    except Exception:
        print(Exception)
        return ''

    img = _thumbnail_resize(image, thumb_size)

    temp_file = BytesIO()
    img.save(temp_file, image.format, quality=quality)

    conn = S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    bucket = conn.get_bucket(AWS_STORAGE_BUCKET_NAME)

    path = _get_s3_path(thumb_name)
    k = bucket.new_key(path)

    try:
        k.cache_control = 'max-age=%d, public' % (3600 * 24 * 360 * 2)
        k.set_contents_from_string(temp_file.getvalue())
        k.set_acl('public-read')
    except S3ResponseError:
        return ''

    return k.generate_url(expires_in=0, query_auth=False)

def _get_s3_path(filename):
    static_root_parent = 'images'
    if not static_root_parent:
        raise ValueError('S3Save requires static_root_parent to be set.')

    return re.sub('^\/', '', filename.replace(static_root_parent, ''))

def _get_path(full_path):
    directory = os.path.dirname(full_path)

    try:
        if not os.path.exists(full_path):
            os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

def _get_name(name, fm, *args):
    for v in args:
        if v:
            name += '_%s' % v
    name += fm

    return name