from behave import given, when, then
from Behave_Python.pages.dashboard import dashboard


@then(u'Dashboard Status shows correct values for row "{row}"')
def step_impl_dashboard_status(context, row):
    print("\n****** Dashboard Status shows correct values for row ")
    dashboard.verify_status(row)


#@then(u'Clicking on Status Refresh should refresh status component')
@then(u'I scroll to element Paragraph_1')
def step_impl_status_refresh(context):
    dashboard.verify_refresh()


@then(u'verify_customer_info_page')
def step_impl_battery_status(context):
    dashboard.verify_customer_info()


@then(u'Clicking on Battery Refresh should refresh battery component')
def step_impl_battery_refresh(context):
    dashboard.verify_battery_refresh()


@then(u'Dashboard Detector Settings shows correct values for row "{row}"')
def step_impl_detector_settings(context, row):
    dashboard.veify_detector_setting(row)


@then(u'Dashboard GPS shows correct values for row "{row}"')
def step_impl_gps_settings(context, row):
    dashboard.verify_gps_setting(row)
