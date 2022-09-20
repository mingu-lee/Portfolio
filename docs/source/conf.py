# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'PortFolio'
copyright = '2022, mingu-lee'
author = 'mingu-lee'
release = '1.0.0'

from recommonmark.parser import CommonMarkParser

source_suffix = ['.md', '.rst']
source_parsers = {
    '.md': CommonMarkParser,
}
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    'sphinx.ext.todo',
    'sphinx.ext.viewcode'
]

exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']

templates_path = ['_templates']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
#html_static_path = ['_static']
html_favicon='smile.ico'
