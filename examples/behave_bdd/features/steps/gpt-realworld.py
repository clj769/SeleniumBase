from behave import given, when, then

@given('Open "{url}"')
def step_open_url(context, url):
    context.sb.open(url)

@given('Clear Session Storage')
def step_clear_session_storage(context):
    context.sb.execute_script("window.sessionStorage.clear();")

@when('Type "{text}" into "{selector}"')
def step_type_into(context, text, selector):
    context.sb.type(selector, text)

@when('Do MFA "{mfa_code}" into "{selector}"')
def step_do_mfa_into(context, mfa_code, selector):
    context.sb.type(selector, mfa_code)

@then('Assert exact text "{text}" in "{selector}"')
def step_assert_exact_text_in(context, text, selector):
    context.sb.assert_exact_text(text, selector)

@then('Highlight "{selector}"')
def step_highlight(context, selector):
    context.sb.highlight(selector)

@then('Click "{selector}"')
def step_click(context, selector):
    context.sb.click(selector)

@then('Save screenshot to logs')
def step_save_screenshot_to_logs(context):
    context.sb.save_screenshot('screenshot.png', folder="logs")

@then('Assert element "{selector}"')
def step_assert_element(context, selector):
    context.sb.assert_element(selector)

@then('Assert text "{text}"')
def step_assert_text(context, text):
    context.sb.assert_text(text)
