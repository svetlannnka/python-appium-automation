from behave import given, when, then


@given('Skip welcome screen')
def skip_welcome(context):
    context.app.welcome_page.skip_welcome()


@when('Tap Search')
def click_search_icon(context):
    context.app.main_page.click_search_icon()


@when('Search for {search_query}')
def search_wiki(context, search_query):
    context.app.search_page.search_wiki(search_query)


@then('Verify {expected_result} is shown')
def verify_search_result(context, expected_result):
    context.app.search_page.verify_search_result(expected_result)