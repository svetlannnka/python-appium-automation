from behave import given, when, then


@given('Click to skip onboarding')
def skip_onboarding(context):
    context.app.welcome_page.skip_onboarding()


@when('Click search icon')
def click_search(context):
    context.app.main_page.click_search()


@when('Search for {search_phrase}')
def search_on_wiki(context, search_phrase):
    context.app.search_page.search_on_wiki(search_phrase)


@then('Verify search results shown for {expected_result}')
def verify_search_result(context, expected_result):
    context.app.search_page.verify_search_result(expected_result)
