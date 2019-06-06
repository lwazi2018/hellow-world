from behave import *
from selenium import webdriver

use_step_matcher('re')


@given('I am on the home page')
def step_impl(context):
    context.browser = webdriver.Chrome('/usr/local/bin/chromedriver.exec')
    context.browser.get('http://127.0.0.1:8000')


@then('I am on the register screen')
def step_impl(context):
    expected_url = '127.0.0.0:8000/register'
    assert context.browser.current_url == expected_url


@then('I am on the driver screen')
def step_impl(context):
    expected_url = 'http://127.0.0.1:8000/register/driver'
    assert context.browser.current_url == expected_url


@given('I can see login button from the home page')
def step_impl(context):
    context.browser = webdriver.Chrome('/usr/local/bin/chromedriver.exec')
    context.browser.get('http://127.0.0.1:8000')


@given('User want to update their profile')
def step_impl(context):
    expected_url1 = 'http://127.0.0.1:8000/dashboard/landing'
    print(context.browser.current_url)

    assert context.browser.current_url == expected_url1


@given('User wants to view their products')
def step_impl(context):
    expected_url = 'http://127.0.0.1:8000/dashboard/profile'
    print(context.browser.current_url)
    assert context.browser.current_url == expected_url


@given('I want to view my driving tips from my dashboard by clicking driving tips link')
def step_impl(context):
    expected_url = 'http://127.0.0.1:8000/dashboard/landing'
    print(context.browser.current_url)
    assert context.browser.current_url == expected_url
