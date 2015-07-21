#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

PUBLISH = True
PLUGINS = [
            'assets',
            'pelican_gdocs',
            'optimize_images'
            ]

SITEURL = 'https://joeahand.com'
RELATIVE_URLS = False

#FEED_ALL_ATOM = 'feeds/all.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

STATIC_PATHS = [
    'extra/CNAME',
    'extra/favicon.ico',
    'extra/favicon-16x16.png',
    'extra/favicon-32x32.png',
    'extra/favicon-96x96.png',
    'extra/robots.txt',
    'extra/humans.txt'
]
EXTRA_PATH_METADATA = {
        'extra/CNAME': {'path': 'CNAME'},
        'extra/favicon.ico': {'path': 'favicon.ico'},
        'extra/favicon-16x16.png': {'path': 'favicon-16x16.png'},
        'extra/favicon-32x32.png': {'path': 'favicon-32x32.png'},
        'extra/favicon-96x96.png': {'path': 'favicon-96x96.png'},
        'extra/robots.txt': {'path': 'robots.txt'},
        'extra/humans.txt': {'path': 'humans.txt'},
}

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = "UA-37465100-3"
