# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'plenoptic tutorial, CSHL Vision Course, 2024'
copyright = '2024, Billy Broderick'
author = 'Billy Broderick'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_nb',
]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_favicon = '_static/plenoptic.ico'
html_theme_options = {
    "logo": {
        "alt_text": "Home",
        "image_light": "_static/plenoptic.svg",
        "image_dark": "_static/plenoptic_darkmode.svg",
    }
}
