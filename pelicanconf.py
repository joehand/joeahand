#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import time
from urllib.parse import urlparse

############################
##### Pelican Settings #####
############################
# General Pelican settings. You can problably change these without breaking theme.

# Will be set in publish config.
SITEURL = ''
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PATH = 'content'

TIMEZONE = 'US/Mountain'
DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%Y-%B-%d'

DIRECT_TEMPLATES = ('index', 'archives', 'sitemap')

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
ARCHIVES_URL = 'archive/'
ARCHIVES_SAVE_AS = 'archive/index.html'
SITEMAP_SAVE_AS = 'sitemap.xml'
TAG_URL = ''
TAG_SAVE_AS = ''
CATEGORY_URL = ''
CATEGORY_SAVE_AS = ''

# Nicer pagination
# (e.g. site.com/blog/1/ instead of site.com/blog/1.html)
DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/{number}/', '{base_name}/{number}/index.html'),
)


#################################
##### Theme/Custom Settings #####
#################################
# Theme specific settings. These are important and will break theme if missing

THEME = 'themes/joe/'

# These pages will show in nav pages.
# Need to put files in content/pages/
NAV_PAGES = ['about', 'cv']

# We have a special homepage. Blog will go to site.com/blog
INDEX_SAVE_AS = 'blog/index.html'

# These things are used in various places.
AUTHOR = u'Joe Hand'
AUTHOR_LINKS = {
    'INSTAGRAM': 'http://instagram.com/joeahand',
    'GITHUB': 'https://github.com/joehand',
    'TWITTER': 'http://twitter.com/joeahand/',
    # use html entities to obfuscate for spammers
    # (http://stackoverflow.com/questions/748780/best-way-to-obfuscate-an-e-mail-address-on-a-website)
    'EMAIL': '&#106;&#111;&#101;&#064;&#106;&#111;&#101;&#097;&#104;&#097;&#110;&#100;&#046;&#099;&#111;&#109;'
}
SITENAME = u'Joe Hand'
SITESUBTITLE = u'Better cities with local data'

PLUGIN_PATHS = ["plugins", 'plugins/pelican-plugins']
PLUGINS = [
    'assets',
    'pelican_gdocs'
]

# GDOCS PLUGIN Settings
GDOCS = [
    {
        'name': 'instagram',
        'url': 'http://docs.google.com/spreadsheets/d/16KHyJyTGvOIFKTR5uUHrXKWH3kf-UiucCwXfceFet0k/pub?gid=0&single=true&output=csv'
    },
    {
        'name': 'articles',
        'url': 'http://docs.google.com/spreadsheets/d/1Wav1nDxtOTRm3WMLL3RI0oqApxLjBxzTcPftWsCn6x4/pub?gid=0&single=true&output=csv'
    },
    {
        'name': 'fitbit_activity',
        'url': 'http://docs.google.com/spreadsheets/d/1AZRyvrcm-Stk0VlWoPEHD4sxe1PTOdEpU2MejRzHB7s/pub?gid=0&single=true&output=csv'
    },
    {
        'name': 'tweets',
        'url': 'http://docs.google.com/spreadsheets/d/1qRuICBJWHQQ34ujTXkY8jh7obJuVJ_quLbwMrBiQFyg/pub?gid=0&single=true&output=csv'
    },
    {
        'name': 'steps',
        'url': 'http://docs.google.com/spreadsheets/d/1AZRyvrcm-Stk0VlWoPEHD4sxe1PTOdEpU2MejRzHB7s/pub?gid=0&single=true&output=csv'
    },
    {
        'name': 'coffee',
        'url': 'http://docs.google.com/spreadsheets/d/1fsaSy8HJdoTr5iUX7p-iCxUwC-TFzZxnqNzt6mMP26s/pub?gid=0&single=true&output=csv'
    },
]

COPYRIGHT_LINK = 'http://creativecommons.org/licenses/by-nc-nd/4.0/'

home_bundle = [
        "external/pure/base.css",
        "external/pure/menus-core.css",
        "external/pure/menus-horizontal.css",
        "external/pure/menus-skin.css",
        "external/pure/tables.css",
        "external/pure/grids.css",
        "external/pure/grids-responsive.css",
        'critical_home.scss'
        ]

blog_bundle = [
        "external/pure/base.css",
        "external/pure/menus-core.css",
        "external/pure/menus-horizontal.css",
        "external/pure/menus-skin.css",
        "external/pure/tables.css",
        "external/pure/grids.css",
        "external/pure/grids-responsive.css",
        'critical_blog.scss'
        ]

page_bundle = [
        "external/pure/base.css",
        "external/pure/menus-core.css",
        "external/pure/menus-horizontal.css",
        "external/pure/menus-skin.css",
        "external/pure/tables.css",
        "external/pure/grids.css",
        "external/pure/grids-responsive.css",
        'critical_page.scss'
        ]

ASSET_BUNDLES = (
    ('home', home_bundle,
        {'filters':"pyscss,cssmin",
        'output':"../../themes/joe/templates/home.min.css"}),
    ('blog',blog_bundle ,
        {'filters':"pyscss,cssmin",
        'output':"../../themes/joe/templates/blog.min.css"}),
    ('page',page_bundle,
        {'filters':"pyscss,cssmin",
        'output':"../../themes/joe/templates/page.min.css"}),
)

###############################
##### Nice Things to Have #####
###############################
# These can be used anywhere in templates
LAST_UPDATE = str(time.strftime('%m %Y'))
YEAR = str(time.strftime('%Y'))

def get_domain(url):
    ''' Return the domain (and subdomain!) for a url
    '''
    parsed_uri = urlparse(url)
    return '{uri.netloc}'.format(uri=parsed_uri).replace('www.', '')
JINJA_FILTERS = {
    'get_domain': get_domain,
}

