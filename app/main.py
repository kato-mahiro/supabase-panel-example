import panel as pn
from pages.login import create_login_page

pn.extension()

template = pn.template.FastListTemplate(
    title='My Application',
    sidebar=[],
    main=[create_login_page()]
)

template.servable()