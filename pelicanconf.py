#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = u'\xc9lysson MR'
SITENAME = u'\xc9lysson MR\'s Blog'
SITESUBTITLE = 'My Personal Blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'br'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Static
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}


# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('Facebook', 'http://facebook.com/elyssonmr'),
          ('GitHub', 'http://github.com/elyssonmr'),
          ('Twitter', 'http://twitter.com/elyssonmr'),
          ('LinkedIn', 'http://linkedin.com/in/elyssonmr'),)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Comments config
DISQUS_SITENAME = 'elyssonmr'

# Analyctics
GOOGLE_ANALYTICS = 'UA-49815718-3'

# theme Configs
THEME = 'theme/blueidea'
DISPLAY_SEARCH_FORM = True
TWITTER_USERNAME = 'elyssonmr'
DISPLAY_CATEGORIES_ON_SUBMENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_CATEGORIES_ON_POSTINFO = True
DISPLAY_AUTHOR_ON_POSTINFO = True
