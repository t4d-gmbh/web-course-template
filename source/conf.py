from datetime import date
from setuptools_scm import get_version

# -- Configuration parameter -------------------------------------------------
# ----------------------------------------------------------------------------
repository_owner = "t4d-gmbh"
repository_name = "web-course-template"
repository_branch = "main"
# -- optionally adat these
repository_url = f"https://github.com/{repository_owner}/{repository_name}"
page_url = f"https://{repository_owner}.github.io/{repository_name}"
# -- set the logo
course_logo = {
    "image_light": "_static/T4D_logo_bw.svg",
    "image_dark": "_static/T4D_logo_wb.svg",
    "link": f"{page_url}/index.html",
    "alt-text": "T4D GmbH",
    "favicon": "_static/T4D_logo_bw.svg",
}
# -- name your project
project = 'Web Course Template'
# -- provide authorship info
author = 'Jonas Liechti - https://github.com/j-i-l'
# -- optionally adapt copyright
copyright = f'{date.today().year}, {repository_owner}'
# -- should the duscussion link be shown?
show_discussion_link = True
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

# ###
# Versioning - get it from the git tag
# ###
version: str = get_version(root='..')
release = version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx_favicon",
    "sphinx_design",
    "sphinx_tabs.tabs",
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_css_files = ['custom.css',]

html_context = {
    "default_mode": "light",
}

discuss_icon = {
            "name": "GitHub Discussion",
            "url": f"{repository_url}/discussions",
            "icon": "fa-regular fa-comments",
            "type": "fontawesome",
        }
pages_icon = {
            "name": "Pages",
            "url": f"{page_url}/index.html",
            "icon": "fa-solid fa-book",
            "type": "fontawesome",
        }
slides_icon = {
            "name": "Slides",
            "url": f"{page_url}/slides/index.html",
            "icon": "fa-solid fa-person-chalkboard",
            "type": "fontawesome",
        }

icon_links_pages = [slides_icon]
icon_links_slides = [pages_icon]
if show_discussion_link:
    icon_links_pages.insert(0, discuss_icon)
    icon_links_slides.insert(0, discuss_icon)


html_theme_options = {
    "repository_url": repository_url,
    "repository_branch": repository_branch,
    "path_to_docs": "source/",
    "use_edit_page_button": True,
    "use_repository_button": True,
    "toc_title": "Content",
    "use_sidenotes": True,
    "logo": {
        "text": course_logo.get('alt-text', 'logo'),
        "image_light": course_logo.get('image_light', None),
        "image_dark": course_logo.get('image_dark', None),
        "link": course_logo.get('link', page_url),
        },
    "show_toc_level": 2,  # Show the table of contents up to level 2
    "navigation_with_keys": True,  # Enable keyboard navigation
    "collapse_navigation": False,  # Do not collapse the navigation
    # "sidebar_width": "250px",  # Set the width of the sidebar
    "icon_links": icon_links_pages,
}

favicons = [
    course_logo.get('favicon', None)
]

myst_enable_extensions = [
    "colon_fence",
]
suppress_warnings = [
    "myst.header", # suppress warnings of the kind "WARNING: Non-consecutive header level increase; H1 to H3"
]

# ###
# Custom jinja parser to enable jinja templating
# ###
def rstjinja(app, docname, source):
    """
    Render source file with jinja first
    """
    print(f"{docname=}")
    # only apply to 'html' builder
    if app.builder.format == 'html':
        src = source[0]
        rendered = app.builder.templates.render_string(
            src, app.config.html_context
        )
        source[0] = rendered

def include_rstjinja(app, docname, parent_docname, source):
    return rstjinja(app=app, docname=docname, source=source)

def setup(app):
    builds = app.config.html_context.get('build', 'pages')
    # setting `slide` and `page` context
    app.config.html_context['page'] = True
    app.config.html_context['slide'] = False
    if builds == 'slides':
        app.config.html_context['slide'] = True
        app.config.html_context['page'] = False
        # ###
        # we do some config adaptations for the slides
        # ###
        # simpler sidebar
        app.config.html_sidebars = {
            "**": [
                # "navbar-logo.html",
                "icon-links.html",
                # "search-button-field.html",
                "sbt-sidebar-nav.html"
                ]
        }
        # only show discuss and pages icons in sidebar
        app.config.html_theme_options['icon_links'] = icon_links_slides
        # adding the new styling
        app.config.html_css_files.append('slides.css')
    app.connect("source-read", rstjinja)
    app.connect("include-read", include_rstjinja)
