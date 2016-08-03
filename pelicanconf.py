#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Me'
SITENAME = 'EveBorn'
SITEURL = 'http://nigelzhf.github.io/'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'zh-cn'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', '#'),
          ('lastfm', '#'),
          ('github', 'https://github.com/nigelzhf'),)

DEFAULT_PAGINATION = 15

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# theme niu-x2 conf
THEME = "./theme/niu-x2"#/vagrant/PelicanBlog/theme/niu-x2

JINJA_EXTENSIONS = ['jinja2.ext.ExprStmtExtension',]
TEMPLATE_PAGES = {
    "404.html": "404.html",
}
NIUX2_CATEGORY_MAP = {
    "code": ("代码", "icon-code"),
    "note": ("笔记", ""),
}
NIUX2_HEADER_SECTIONS = [
     ("关于", "about", "/about.html", "icon-anchor"),
     ("存档", "archives", "/archives.html", "icon-archive"),
     ("标签", "tags", "/archives.html", "icon-tag"),
]

NIUX2_FOOTER_ICONS = [
     ("icon-envelope-alt", "my email address", "mailto: 992122833@qq.com"),
     ("icon-github-alt", "my github page", "https://github.com/nigelzhf"),
     ("icon-rss", "subscribe my blog via rss", "#"),
 ]
