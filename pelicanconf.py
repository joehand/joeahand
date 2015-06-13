#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from urlparse import urlparse

def get_domain(url):
        ''' Return just the domain (and subdomain!) for a url
        '''
        parsed_uri = urlparse(url)
        domain = '{uri.netloc}'.format(uri=parsed_uri)
        domain = domain.replace('www.', '')

        return domain

JINJA_FILTERS = {'get_domain':get_domain}

AUTHOR = u'Joe Hand'
SITENAME = u'Joe Hand'
SITEURL = 'joeahand.com'

THEME = 'themes/joe/'

PATH = 'content'

TIMEZONE = 'US/Mountain'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%Y-%B-%d'

#DIRECT_TEMPLATES = (('index', 'archives', '404'))
PLUGIN_PATHS = ["plugins", ]
#PLUGINS = ["assets",]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_URL = 'archive/{slug}/'
ARTICLE_SAVE_AS = 'archive/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = ''
TAG_SAVE_AS = ''
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
ARCHIVES_URL = 'archive/'
ARCHIVES_SAVE_AS = 'archive/index.html'
#YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/{number}/', '{base_name}/{number}/index.html'),
)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#SPECIAL THEME SETTINGS
HOME_PAGE = {
    'content' : 'home',
    'count' : 0,
    'partial' : True,
}

COPYRIGHT_LINK = 'http://creativecommons.org/licenses/by-nc-nd/4.0/'
