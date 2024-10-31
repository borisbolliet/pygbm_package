# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
nbsphinx_kernel_name = 'python3'

import sphinx_rtd_theme

# Path to the logo image relative to the `_static` directory
# html_static_path = ['_static']
# html_logo = "_static/logo.jpg"

# -- Project information -----------------------------------------------------

project = 'Company Package'
copyright = '2024, Boris Bolliet'
author = 'Boris Bolliet'

# The full version, including alpha/beta/rc tags
release = 'beta'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	'nbsphinx',
    'myst_parser',
    'sphinx.ext.autodoc',    # Autodoc extension for extracting docstrings
	'sphinx.ext.mathjax',
	'sphinx_rtd_theme',
    'sphinx_gallery.load_style',  # load CSS for gallery (needs SG >= 0.6)
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'tutorial_notebooks/tutorial*/*_empty.ipynb']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
master_doc = 'index'

highlight_language = 'python3'

nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg', 'pdf'}",
    "--InlineBackend.rc={'figure.dpi': 96}",
]
# pygments_style = 'sphinx'


# Disable section numbering
secnumber_suffix = ''  # No suffix means no section numbers
# numfig = False  # Disable figure/table numbering if you don't need them


exclude_patterns = [
    # 'material/tbd/notebook_camhpc_cosmo.ipynb',  # Exclude specific file
]


# Add your module's path to `sys.path`
import os
import sys
sys.path.insert(0, os.path.abspath('..'))  # Point to your project source code

# Get the current directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")
