import re
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
    if env == "dev":
        context.environment["dev"] = url
    elif env == "test":
        context.environment["test"] = url


@step('I assume I am on the "{env}" Environment')
def step_assume_environment(context, env):
    context.env = env
    assert env in context.environment, f"Environment '{env}' not found"


@step('I verify the text "{expected_text}" is present')
def step_verify_text_present(context, expected_text):
    element = WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{expected_text}')]"))
    )

    assert element is not None, f"Text '{expected_text}' not found on the page"


@step("I enter the website")
def step_i_enter_the_website(context):
    context.driver = webdriver.Chrome()  # Initialize a Chrome WebDriver
    context.driver.get(context.environment[context.env])


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


@step('I navigate to the "{page_Name}" page')
def step_navigate_to_page(context, page_Name):
    if page_Name == "You Decide":
        go_to_you_decide_page(context)
        step_verify_text_present(context, "six academic experts")
    else:
        raise ValueError(f"Unknown page name: {page_Name}")


@step('I should see the button "{button_name}" with white text and black background')
def step_verify_button_colors(context, button_name):
    continue_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(), '{button_name}')]"))
    )

    text_color = continue_button.value_of_css_property("color")
    background_color = continue_button.value_of_css_property("background-color")

    assert text_color == "rgb(255, 255, 255)", f"Text color is not white: {text_color}"
    assert background_color == "rgb(0, 0, 0)", f"Background color is not black: {background_color}"


def go_to_you_decide_page(context):
    """
    The below elements: Text ID's weren't used as using  WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(), '{button_name}')]")))
    didnt work, no element ID was found each time ;(
    """
    WebDriverWait(context.driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="pa_5c9126fe3f4fb_p179d7b273e1-card__image-1"]'))
    ).click()
    WebDriverWait(context.driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="pa_5c9126fe434ba_p15564daa856-textButton"]'))
    ).click()
    WebDriverWait(context.driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="pa_5c9126fe47260_p15515116385-itemInner-1"]'))
    ).click()
    WebDriverWait(context.driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="pa_5c9126fe47260_p15515116385-save_button"]'))
    ).click()
    WebDriverWait(context.driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="pa_5c9126fe47260_p15583b88249-dismiss_button"]'))
    ).click()
    WebDriverWait(context.driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="pa_5c9126fe4b742_p15550a254a1-textButton"]'))
    ).click()
