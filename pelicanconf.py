#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import time
from urllib.parse import urlparse

def get_domain(url):
        ''' Return just the domain (and subdomain!) for a url
        '''
        parsed_uri = urlparse(url)
        domain = '{uri.netloc}'.format(uri=parsed_uri)
        domain = domain.replace('www.', '')

        return domain


JINJA_FILTERS = {
    'get_domain':get_domain,
}

LAST_UPDATE = str(time.strftime('%m %Y'))
YEAR = str(time.strftime('%Y'))

SITEURL = ''
AUTHOR = u'Joe Hand'
AUTHOR_LINKS = {
    'INSTAGRAM' : 'http://instagram.com/joeahand',
    'GITHUB' : 'https://github.com/joehand',
    'TWITTER' : 'http://twitter.com/joeahand/',
    # use html entities to obfuscate for spammers (http://stackoverflow.com/questions/748780/best-way-to-obfuscate-an-e-mail-address-on-a-website)
    'EMAIL' : '&#106;&#111;&#101;&#064;&#106;&#111;&#101;&#097;&#104;&#097;&#110;&#100;&#046;&#099;&#111;&#109;'
}
SITENAME = u'Joe Hand'
SITESUBTITLE = u'Better cities with local data'

NAV_PAGES = ['about', '']

THEME = 'themes/joe/'

PATH = 'content'

TIMEZONE = 'US/Mountain'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%Y-%B-%d'

#DIRECT_TEMPLATES = (('index', 'archives', '404'))

STATIC_PATHS = ['images']
PLUGIN_PATHS = ["plugins", 'plugins/pelican-plugins']
PLUGINS = [
            'assets',
            'pelican_gdocs'
            ]
# PLUGIN Settings
GITHUB_USER = 'joehand'
GDOCS = [
    {
        'name':'instagram',
        'url':'http://docs.google.com/spreadsheets/d/16KHyJyTGvOIFKTR5uUHrXKWH3kf-UiucCwXfceFet0k/pub?gid=0&single=true&output=csv'
    },
    {
        'name':'articles',
        'url':'http://docs.google.com/spreadsheets/d/1Wav1nDxtOTRm3WMLL3RI0oqApxLjBxzTcPftWsCn6x4/pub?gid=0&single=true&output=csv'
    },
    {
        'name':'fitbit_activity',
        'url':'http://docs.google.com/spreadsheets/d/1AZRyvrcm-Stk0VlWoPEHD4sxe1PTOdEpU2MejRzHB7s/pub?gid=0&single=true&output=csv'
    },
    {
        'name':'tweets',
        'url':'http://docs.google.com/spreadsheets/d/1qRuICBJWHQQ34ujTXkY8jh7obJuVJ_quLbwMrBiQFyg/pub?gid=0&single=true&output=csv'
    },
    {
        'name':'steps',
        'url':'https://docs.google.com/spreadsheets/d/1AZRyvrcm-Stk0VlWoPEHD4sxe1PTOdEpU2MejRzHB7s/pub?gid=0&single=true&output=csv'
    },
    {
        'name':'coffee',
        'url':'https://docs.google.com/spreadsheets/d/1fsaSy8HJdoTr5iUX7p-iCxUwC-TFzZxnqNzt6mMP26s/pub?gid=0&single=true&output=csv'
    },
]

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
    'links' : [
        ('Projects',SITEURL + '#test'),
        ('Longer Bio',SITEURL + '/about/'),
        ('Writing','http://medium.com/@joehand'),
    ]
}

COPYRIGHT_LINK = 'http://creativecommons.org/licenses/by-nc-nd/4.0/'
