#!/usr/bin/env python

from distutils.core import setup

setup(name='WebViewHandler',
      version='1.0',
      description='Logging handler that provides scrolling web view',
      author='John Fink',
      author_email='johnfink8@gmail.com',
      packages=['WebViewHandler', ],
      requires=['Jinja2', ],
      package_data={'WebViewHandler': ['templates/base.html']}
      )
