import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_dynamic_controls(driver):
    # Write your code below this line
    try:
        driver.get("http://localhost:8081/")
        wait = WebDriverWait(driver, 10)
        dynamic_controls_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Dynamic Controls')))
        dynamic_controls_link.click()
        enable_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Enable"]')))
        print("\n")
        print("Enabling text input and performamce testing")
        try:
            enable_button.click()
            start_time = time.time()
            wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'input')))
            elapsed_time = time.time() - start_time
            print("Total time taken for enabling text input: {:.2f} seconds".format(elapsed_time))
        except Exception as e:
            print(e)
            pytest.fail("Something went wrong while enabling the text input. Dynamic Controls test failed.")
        
        print("")
        print("Disabling text input and performance testing")
        try:
            disable_button = driver.find_element(By.XPATH, '//button[text()="Disable"]')
            disable_button.click()
            start_time = time.time()
            wait.until_not(EC.element_to_be_clickable((By.TAG_NAME, 'input')))
            elapsed_time = time.time() - start_time
            print("Total time taken for disabling text input: {:.2f} seconds.".format(elapsed_time))
        except Exception as e:
            print(e)
            pytest.fail("Something went wrong while disabling the text input. Dynamic Controls test failed.")

        print("")
        print("Dynamic Controls test passed.")
    except Exception as e:
        print(e)
        pytest.fail("Dynamic Controls test failed.")