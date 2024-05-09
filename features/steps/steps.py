import re

import requests
from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@given('the URL for environment "{env}" is "{url}"')
def step_the_URL_is(context, env, url):
    """
    Environment URL is stored in the context object
    """
    context.environment = url



@step('I verify the text "{expected_text}" is present')
def step_verify_text_present(context, expected_text):
    element = WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{expected_text}')]"))
    )

    assert element is not None, f"Text '{expected_text}' not found on the page"


@step("I enter the website")
def step_i_enter_the_website(context):
    context.driver = webdriver.Chrome()  # Initialize a Chrome WebDriver
    context.driver.get(context.environment)


@step("I navigate to the URL")
def step_i_navigate_to_the_url(context):
    response = requests.get(context.environment)
    context.csp_header = response.headers.get('Content-Security-Policy')


@step('I should see the CSP header')
def step_see_csp_header(context):
    assert context.csp_header is not None, "CSP header not found"
    print("CSP Header found:", context.csp_header)


@then("I should see the score is a number between 0 and 100")
def step_i_should_see_score(context):
    score_element = WebDriverWait(context.driver, 2).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Your score so far:')]"))
    )
    score_text = score_element.text
    score_match = re.search(r'\d+', score_text)
    assert "/" not in score_text, f"Score '{score_text}' is not a number"

    if score_match:
        score = int(score_match.group())
        assert 0 <= score <= 100, f"Score '{score}' is not between 0 and 100"
    else:
        raise ValueError("No numeric score found on the page")


@step('I click the "{button_name}" button')
def step_click_button(context, button_name):
    if button_name.lower() == 'start':
        button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f"span#pa_5c9126fe3b767_p15577f075e9-button__text"))
        )
        button.click()
    else:
        button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(), '{button_name}')]")))
        button.click()


@step('I should see the button "{button_name}" present')
def step_verify_button_present(context, button_name):
    """
    :type context: behave.runner.Context
    """
    button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//button[text()='{button_name}']"))
    )
    assert button is not None, f"Button '{button_name}' not found on the page"

