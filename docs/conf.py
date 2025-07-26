# Configuration file for the Sphinx documentation builder

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Kraken Wallet'
copyright = '2025'
author = 'John Lee'

release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]

html_extra_path = ['_html']

extensions = [
    "myst_parser",
]

extensions = ['sphinx_sitemap']
html_baseurl = "https://krakenhelpusa.readthedocs.io/en/latest/"

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']

