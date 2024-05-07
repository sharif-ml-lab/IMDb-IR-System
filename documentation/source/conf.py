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
import os
import sys

sys.path.insert(0, os.path.abspath("../../"))


# -- Project information -----------------------------------------------------

project = "IMDb-IR-System"
copyright = "2024, MIR Course team @ CE at Sharif University"
author = "AmirHossein Razlighi"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
]
autodoc_mock_imports = [
    "numpy",
    "beautifulsoup4",
    "pandas",
    "nltk",
    "scipy",
    "sklearn",
    "streamlit",
    "matplotlib",
    "seaborn",
    "fasttext",
    "networkx",
    "tqdm",
]

python_use_unqualified_type_names = True
autosummary_generate = True

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
}

templates_path = ["_templates"]
html_static_path = ["_static"]
source_suffix = ".rst"
main_doc = "index"
highlight_language = "python"
pygments_style = "sphinx"
add_module_names = False

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"

html_theme_options = {
    "show_toc_level": 2,
    "repository_url": "https://github.com/sharif-ml-lab/IMDb-IR-System",
    "use_repository_button": True,
    "navigation_with_keys": False,
    "logo": {
        "image_light": "IMDB_Logo.jpeg",
        "image_dark": "IMDB_Logo.jpeg",
    },
}

htmlhelp_basename = "imdb_ir_doc"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
