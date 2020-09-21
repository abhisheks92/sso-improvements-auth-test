from tests.model.selenium_helper import SeleniumHelper
import time

driver = SeleniumHelper()

FORM = "//form"

EMAIL = FORM + "/im-email/section/input"
PASSWORD = "//div/input[@id='passwordInput']"

SUBMIT = FORM + "/button"
SIGN_IN = FORM + "/div/div/span"

PROFILE_DROPDOWN = "//im-topbar/div/div/div/span"
LOGOUT = "//span[text()='Logout']"


def login(email, password):
    driver.find(FORM)
    driver.find(EMAIL).send_keys(email)
    driver.find(SUBMIT).click()
    time.sleep(3)
    driver.find(PASSWORD).send_keys(password)
    time.sleep(3)
    driver.find(SIGN_IN).click()
    time.sleep(3)


def logout():
    time.sleep(1.5)
    driver.find(PROFILE_DROPDOWN).click()
    time.sleep(1.5)
    driver.find(LOGOUT).click()
    driver.quit()

