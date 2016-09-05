#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mario Wenzel'
SITENAME = 'Linke Entwickler*innen Leipzig'
SITESUBTITLE = 'Eine AG der Linken Leipzig'
SITEURL = ''
RELATIVE_URLS = True
THEME = "theme"

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
            ('Linke Leipzig', 'http://die-linke-in-leipzig.de/'),
        )

# Social widget
SOCIAL = (
            ('github', 'https://github.com/LinkeEntwicklerInnenLeipzig'),
         )

DEFAULT_PAGINATION = 5
DEFAULT_ORPHANS = 1

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
