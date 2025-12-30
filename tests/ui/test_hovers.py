import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

def test_hovers(driver):
    # Write your code below this line
    try:
        driver.get("http://localhost:8081/")
        wait = WebDriverWait(driver, 10)
        hovers_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Hovers')))
        hovers_link.click()
        images = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'img')))
        print("\n")
        print("Hovering over images and getting image information")
        print("")
        try:
            images = driver.find_elements(By.TAG_NAME, 'img')
            actions = ActionChains(driver)
            counter = 1
            for img in images:
                actions.move_to_element(img).perform()
                name = img.find_element(By.XPATH, './following-sibling::div/h5')
                if name.text == "name: user" + str(counter):
                    print(name.text)
                else:
                    pytest.fail("Invalid image information. Hovers test failed.")
                counter += 1
        except Exception as e:
            print(e)
            pytest.fail("Failed to hover over images. Hovers test failed.")
        print("")
        print("Hovers test passed.")
    except Exception as e:
        print(e)
        pytest.fail("Hovers test failed.")