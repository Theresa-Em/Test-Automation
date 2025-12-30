import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def test_horizontal_slider(driver):
    # Write your code below this line
    try:
        driver.get("http://localhost:8081/")
        wait = WebDriverWait(driver, 10)
        horizontal_slider_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Horizontal Slider')))
        horizontal_slider_link.click()
        slider = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'input')))
        slider_value = wait.until(EC.presence_of_element_located((By.ID, 'range')))
        step_size = float(slider.get_attribute("step"))
        print("\n")
        print("Testing slider forward")
        try:
            value = 0
            for _ in range(10):
                slider.send_keys(Keys.ARROW_RIGHT)
                value += step_size
                print("Current slider value: " + slider_value.text)
                if float(slider_value.text) != value:
                    pytest.fail("Invalid slider value after moving forward. Horizontal Slider test failed.")
        except Exception as e:
            print(e)
            pytest.fail("Failed moving the slider forward. Horizontal Slider test failed.")
        
        print("")
        print("Testing slider backward")
        try:
            value = 5
            for _ in range(10):
                slider.send_keys(Keys.ARROW_LEFT)
                value -= step_size
                print("Current slider value: " + slider_value.text)
                if float(slider_value.text) != value:
                    pytest.fail("Invalid slider value after moving backward. Horizontal Slider test failed.")
        except Exception as e:
            print(e)
            pytest.fail("Failed moving the slider backward. Horizontal Slider test failed.")
        
        print("")
        print("Horizontal Slider test passed.")
    except Exception as e:
        print(e)
        pytest.fail("Horizontal Slider test failed.")
                