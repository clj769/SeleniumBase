# from behave import given, when, then
#
# @given('Open the Calculator App')
# def step_open_calculator_app(context):
#     context.sb.open("https://seleniumbase.io/apps/calculator")  # replace with the actual URL
#
# @when('Press C')
# def step_press_c(context):
#     context.sb.click("button#clear")  # replace with the actual selector
#
#
# @when('Press +')
# def step_press_plus(context):
#     context.sb.click('button#add')  # replace with the actual selector
#
# @when('Press -')
# def step_press_minus(context):
#     context.sb.click('button#subtract')  # replace with the actual selector
#
# @when('Press ×')
# def step_press_multiply(context):
#     context.sb.click('button#multiply')  # replace with the actual selector
#
# @when('Press ÷')
# def step_press_divide(context):
#     context.sb.click('button#divide')  # replace with the actual selector
#
# @when('Press =')
# def step_press_equals(context):
#     context.sb.click('button#equal')  # replace with the actual selector
#
# @when('Press .')
# def step_press_dot(context):
#     context.sb.click('button[id="."]')  # replace with the actual selector
#
# @when('Press {digit:d}')
# def step_press_digit(context, digit):
#     context.sb.click(f'selector_for_{digit}')  # replace with the actual selector
#
# @when('Press [{number}]')
# def step_press_number(context, number):
#     context.sb.click(f'selector_for_{number}')  # replace with the actual selector
#
# @when('Evaluate [{expression}]')
# def step_evaluate_expression(context, expression):
#     for char in expression:
#         context.sb.click(f'selector_for_{char}')  # replace with the actual selector
#
# @then('Verify output is "{output}"')
# def step_verify_output(context, output):
#     context.sb.assert_text(output, 'selector_for_output')  # replace with the actual selector
#
# @given('Save calculator screenshot to logs')
# def step_save_screenshot(context):
#     context.sb.save_screenshot("calculator.png")
