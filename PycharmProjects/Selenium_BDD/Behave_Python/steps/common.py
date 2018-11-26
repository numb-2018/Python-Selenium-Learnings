from behave import given, when, then
from Behave_Python.framework.webapp import webapp
from Behave_Python.framework.serviceapp import serviceapp


@given(u'I load the website')
def step_impl_load_website(context):
    webapp.load_website()


#@given(u'Launch the website')
#def step_impl_load_website(context):
    #serviceapp.load_website()


@when(u'I go to "{page}" page')
def step_impl_goto_page(context, page):
    webapp.goto_page(page)


@then(u'I see this component "{component}"')
def step_impl_verify_component(context, component):
    webapp.verify_component_exists(component)
