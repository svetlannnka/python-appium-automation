from behave import given, when, then


@given('Skip onboarding')
def skip_onboarding(context):
    context.app.onboarding_page.click_skip()


@when('Click on search icon')
def click_search(context):
    context.app.main_page.click_search()


@when('Search for Python (Programming language)')
def input_search_phrase(context):
    context.app.main_page.input_search_phrase()


@then('Verify search result shown for Python (Programming language)')
def verify_search_result(context):
    context.app.search_result_page.verify_search_result()

