import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

def test_forgot_password(driver):
    # Write your code below this line
    MESSAGES = {
        "empty_email_alert": "Please enter your email address",
        "new_password_alert": "Your new password is: admin",
        "invalid_email_alert": "Invalid email format"
                }
    try:
        driver.get("http://localhost:8081/")
        wait = WebDriverWait(driver, 10)
        forgot_password_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Forgot Password')))
        forgot_password_link.click()
        retrieve_password_button = wait.until(EC.element_to_be_clickable((By.ID, "form_submit")))
        print("\n")
        print("Retrieving password with empty input failed")
        try:
            retrieve_password_button.click()
            alert = Alert(driver)
            alert_text = alert.text
            if alert_text == MESSAGES["empty_email_alert"]:
                print(f'Response message: "{alert_text}"')
            else:
                pytest.fail("Expected alert box and text not found. Forgot Password test failed.") 
            alert.accept()
            driver.switch_to.default_content()
            print("Retrieving password with empty input field test passed.")
        except Exception as e:
            print(e)
            pytest.fail("Failed to retrieve password with empty input field. Forgot Password test failed.")

        print("")
        print("Retrieving password with non-empty input field (valid email)")
        try:
            input_box = wait.until(EC.presence_of_element_located((By.ID, 'email')))
            input_box.clear()
            assert input_box.get_attribute('value') == '', "Email input field is not empty"
            input_box.send_keys('example@example.com')
            retrieve_password_button.click()
            alert = Alert(driver)
            alert_text = alert.text
            if alert_text == MESSAGES["new_password_alert"]:
                print(f'Response message: "{alert_text}"')
            else:
                pytest.fail("Expected alert box and text not found. Forgot Password test failed.")
            alert.accept()
            driver.switch_to.default_content()
            print("Retrieving password with non-empty input field (valid email) test passed.")
        except Exception as e:
            print(e)
            pytest.fail("Failed to retrieve password wtih non-empty input field (valid email). Forgot Password test failed.")

        print("")
        print("Retrieving password with non-empty input field (invalid email)")
        try:
            input_box = wait.until(EC.presence_of_element_located((By.ID, 'email')))
            input_box.clear()
            input_box.send_keys('example@exmaple')
            retrieve_password_button.click()
            alert = Alert(driver)
            alert_text = alert.text
            if alert_text == MESSAGES["invalid_email_alert"]:
                print(f'Response message: "{alert_text}"')
            else:
                pytest.fail("Expected alert box and text not found. Forgot Password test failed.")
            alert.accept()
            driver.switch_to.default_content()
            print("Retrieving password with non-empty input field (invalid email) test passed.")
        except Exception as e:
            print(e)
            pytest.fail("Failed to retrieve password with non-empty input field (invalid email). Forgot Password test failed.")
        print("")
        print("Forgot Password test passed.")
    except Exception as e:
        print(e)
        pytest.fail("Forgot Password test failed.")

