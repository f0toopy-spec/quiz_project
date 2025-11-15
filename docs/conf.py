import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'Quiz System'
copyright = '2024, Quiz Developer'
author = 'Quiz Developer'

release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

autodoc_member_order = 'groupwise'
napoleon_google_docstring = True
napoleon_include_init_with_doc = True
