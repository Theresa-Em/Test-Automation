import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("test_case, username, password, expected_message", [
    ("Valid credentials test", "admin", "admin", "You logged into a secure area!"),
    ("Invalid credentials test", "admin1", "admin1", "Invalid username or password!"),
    ("Empty credentials test", "", "", "Username or password field is empty!")
])
def test_form_authentication(driver, test_case, username, password, expected_message):
    # Write your code below this line
    try:
        driver.get("http://localhost:8081/")
        wait = WebDriverWait(driver, 10)
        form_authentication_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Form Authentication')))
        form_authentication_link.click()
        username_field = wait.until(EC.element_to_be_clickable((By.ID, "username")))
        password_field = wait.until(EC.element_to_be_clickable((By.ID, "password")))
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
        print("\n")
        print(test_case)
        try:
            if test_case != "Testing empty credentials":
                username_field.clear()
                username_field.send_keys(username)
                password_field.clear()
                password_field.send_keys(password)
            else:
                username_field.clear()
                password_field.clear()
            login_button.click()
            response_parent = wait.until(EC.element_to_be_clickable((By.ID, 'flash')))
            response_parent = response_parent.text.strip()
            response_child = driver.find_elements(By.TAG_NAME, "a")[0]
            response_child = response_child.text.strip()
            response = response_parent.replace(response_child, "").strip()
            if test_case == "Testing valid credentials":
                if response == expected_message:
                    logout_link = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'a')))
                    logout_link.click()
                    if driver.current_url != "http://localhost:8081/login":
                        pytest.fail("Logout was not successful. Form Authentication test failed.")
                    else:
                        print(testcase + " successful")
                else:
                    pytest.fail("Login with valid credentials failed. Form Authentication test failed.")
            else:
                if response == expected_message:
                    print(test_case + " successful")
                else:
                    pytest.fail("Invalid response received. Form Authentication test failed.")
        except Exception as e:
            print(e)
            pytest.fail("Something went wrong. Form Authentication test failed.")
        print("")
        print("Form Authentication test passed.")
    except Exception as e:
        print(e)
        pytest.fail("Form Authentication test failed.")