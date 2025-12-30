import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

def test_javascript_alerts(driver):
    # Write your code below this line
    try:
        driver.get("http://localhost:8081/")
        wait = WebDriverWait(driver, 10)
        js_alerts_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'JavaScript Alerts')))
        js_alerts_link.click()
        js_alert_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Click for JS Alert"]')))
        js_confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Click for JS Confirm"]')))
        js_prompt_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Click for JS Prompt"]')))

        print("\n")
        print("Clicking alert button")
        try:
            js_alert_button.click()
            alert = Alert(driver)
            alert_text = alert.text
            if alert_text == "I am a JS Alert":
                print("Alert button textL " + alert_text)
            else:
                pytest.fail("Wrong alert button clicked. JavaScript Alerts test failed.")
            alert.accept()
            driver.switch_to.default_content()
            wait.until(EC.presence_of_element_located((By.ID, "result")))
            result = driver.find_element(By.ID, "result")
            if result.text == "You successfully clicked an alert":
                print(f'Alert button result: "{result.text}"')
            else:
                pytest.fail("Invalid alert button result. JavaScript Alerts test failed.")
            print("Alert button test passed.")
        except Exception as e:
            print(e)
            pytest.fail("Failed to click alert button. JavaScript Alerts test failed.")
        
        print("")
        print("Clicking confirm button")
        try:
            js_confirm_button.click()
            confirm = Alert(driver)
            confirm_text = confirm.text
            if confirm_text == "I am a JS Confirm":
                print("Confirm button text: " + confirm_text)
            else:
                pytest.fail("Wrong confirm button clicked. JavaScript Alerts test failed.")
            print("Accepting confirm button")
            confirm.accept()
            driver.switch_to.default_content()
            wait.until(EC.presence_of_element_located((By.ID, "result")))
            result = driver.find_element(By.ID, "result")
            if result.text == "You clicked: Ok":
                print(f'Confirm button acceptance result: "{result.text}"')
            else:
                pytest.fail("Invalid confirm button result while accepting. JavaScript Alerts test faild.")

            print("Dismissing confirm button")
            js_confirm_button.click()
            confirm = Alert(driver)
            confirm.dismiss()
            driver.switch_to.default_content()
            wait.until(EC.presence_of_element_located((By.ID, "result")))
            result = driver.find_element(By.ID, "result")
            if result.text == "You clicked: Cancel":
                print(f'Confirm button dismissal result: "{result.text}"')
            else:
                pytest.fail("Invalid confirm button result while dismissing. JavaScript Alerts test failed.")
            print("Confirm button test passed.")
        except Exception as e:
            print(e)
            pytest.fail("Failed to click confirm button. JavaScript Alerts test failed.")
        
        print("")
        print("Click prompt button")
        try:
            js_prompt_button.click()
            prompt = Alert(driver)
            prompt_text = prompt.text
            if prompt_text == "I am a JS prompt":
                print("Prompt button text: " + prompt_text)
            else:
                pytest.fail("Wrong prompt button clicked. JavaScript Alerts test failed.")
            print("Accepting prompt button with empty input field")
            prompt.accept()
            driver.switch_to.default_content()
            wait.until(EC.presence_of_element_located((By.ID, "result")))
            result = driver.find_element(By.ID, "result")
            if result.text.strip() == "You entered: ".strip():
                print(f'Prompt button acceptance result with empty input field: "{result.text}"')
            else:
                pytest.fail("Invalid prompt button result while accepting with empty input field. JavaScript Alerts test failed.")
            print("Accepting prompt button with non-empty input field.")
            js_prompt_button.click()
            prompt.send_keys("hello world")
            prompt.accept()
            driver.switch_to.default_content()
            wait.until(EC.presence_of_element_located((By.ID, "result")))
            result = driver.find_element(By.ID, "result")
            if result.text == "You entered: hello world":
                print(f'Prompt button acceptance result with non-empty input field: "{result.text}"')
            else:
                pytest.fail("Invalid prompt button result whilt accepting with non-empty input field. JavaScript Alerts test failed.")
            print("Dismissing prompt button with empty input field.")
            js_prompt_button.click()
            prompt = Alert(driver)
            prompt.dismiss()
            driver.switch_to.default_content()
            wait.until(EC.presence_of_element_located((By.ID, "result")))
            result = driver.find_element(By.ID, "result")
            if result.text == "You entered: null":
                print(f'Prompt button dismissal result with empty input field: "{result.text}"')
            else:
                pytest.fail("Invalid prompt button result while dismissing with empty input field. JavaScript Alerts failed.")
            print("Dismissing prompt button with non-empty input field")
            js_prompt_button.click()
            prompt = Alert(driver)
            prompt.send_keys("hello world")
            prompt.dismiss()
            driver.switch_to.default_content()
            wait.until(EC.presence_of_element_located((By.ID, "result")))
            result = driver.find_element(By.ID, "result")
            if result.text == "You entered: null":
                print(f'Prompt button dismissal with non-empty input field: "{result.text}"')
            else:
                pytest.fail("Invaild prompt button result while dismissing with non-empty input field. JavaScript Alerts test failed.")
            print("Prompt button test passed.")
        except Exception as e:
            print(e)
            pytest.fail("Failed to click prompt button. JavaScript Alerts test failed.")
        
        print("")
        print("JavaScript Alerts test passed.")
    except Exception as e:
        print(e)
        pytest.fail("JavaScript Alerts test failed.")
