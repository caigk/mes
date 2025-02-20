# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


####################################################################################################

import sys, os
from datetime import datetime

# http://www.sphinx-doc.org/en/stable/extdev/logging.html
# from sphinx.util import logging
import logging

logger = logging.getLogger(__name__)

# try:
#     import sphinx_rtd_theme
# except:
#     logger.warning('Failed to import sphinx_rtd_theme')
#     pass

####################################################################################################

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# for directory in ,:

PythonicGcodeMachine_path = os.path.abspath(os.path.join(__file__, *[".."] * 2))
sys.path.insert(0, PythonicGcodeMachine_path)

####################################################################################################

exec(
    compile(
        open(os.path.join(PythonicGcodeMachine_path, "setup_data.py")).read(),
        "setup_data.py",
        "exec",
    )
)


# -- Project information -----------------------------------------------------

project = setup_dict["name"]
copyright = "2024, caigk"
author = setup_dict["author"]


release = setup_dict["version"]
# The short X.Y version.
version = ".".join(release.split(".")[:2])


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    # 'sphinx.ext.pngmath',
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    #"sphinx.ext.viewcode",
    #"sphinxcontrib.getthecode",
    "sphinx_sitemap",
    "myst_parser",
    "sphinx.ext.githubpages",
    "sphinx_new_tab_link",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "zh"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

source_suffix = {
    ".rst": "restructuredtext",
    #'.txt': 'markdown',
    ".md": "markdown",
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'PythonicGcodeMachine'
html_theme = "PythonicGcodeMachineRtd"
# html_theme = 'sphinx_rtd_theme'
html_theme_path = ["themes"]

html_baseurl = setup_dict["url"]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

####################################################################################################
#
# sphinx-sitemap
# https://github.com/jdillard/sphinx-sitemap
#

site_url = setup_dict["url"]  # could use setup_dict
