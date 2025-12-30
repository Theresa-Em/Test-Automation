import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

def test_broken_images(driver):
    # Write your code below this line
    try:
        driver.get("http://localhost:8081/")
        wait = WebDriverWait(driver, 10)
        broken_image_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Broken Images')))
        broken_image_link.click()
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'img')))
        images = driver.find_elements(By.TAG_NAME, 'img')
        print("\n")
        print("Inspecting images")
        try:
            for img in images:
                img_src = img.get_attribute("src")
                img_namge = img_src.split("/")[-1]
                if img.get_attribute("naturalWidth") == "0":
                    print('Image name: "' + img_namge + '". Image is broken.')
                else:
                    print('Image name: "' + img_namge + '". Image is not broken.')
        except Exception as e:
            print(e)
            pytest.fail("Failed to inspect images. Broken Image test failed.")
        print("")
        print("Broken Images test passed.")
    except Exception as e:
        print(e)
        pytest.fail("Broken Image test failed.")