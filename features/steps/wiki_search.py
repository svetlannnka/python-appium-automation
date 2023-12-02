from behave import given, when, then


@given('Click to Skip onboarding')
def click_skip_ob(context):
    context.app.ob_page.click_skip_ob()


@when('Click Search icon')
def click_search_icon(context):
    context.app.explore_page.click_search_icon()


@when('Search for {search_text}')
def input_search_text(context, search_text):
    context.app.search_page.input_search_text(search_text)


@then('Verify first result is {expected_text}')
def verify_search_result(context, expected_text):
    context.app.search_page.verify_search_result(expected_text)
