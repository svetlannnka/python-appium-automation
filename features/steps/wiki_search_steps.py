from behave import when, then


@when('Click Skip')
def click_skip(context):
    context.app.onboarding_page.click_skip()


@when('Click Search Wikipedia')
def click_search_wiki(context):
    context.app.main_page.click_search_wiki()


@when('Input search query: {text}')
def input_search_query(context, text):
    context.app.search_page.input_search_query(text)


@then('Verify {expected_text} result is shown')
def verify_search_results(context, expected_text):
    context.app.search_page.verify_search_results(expected_text)
