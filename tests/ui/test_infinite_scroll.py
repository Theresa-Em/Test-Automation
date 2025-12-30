import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def test_infinite_scroll(driver):
    # Write your code below this line
    try:
        driver.get("http://localhost:8081/")
        wait = WebDriverWait(driver, 10)
        infinite_scroll_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Infinite Scroll')))
        infinite_scroll_link.click()
        scrollTexts = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'jscroll-added')))
        print("\n")
        print("Verifying initial load of contents")
        try:
            scrollTexts = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'jscroll-added')))
            #print(len(scrollTexts))
            if len(scrollTexts) == 2:
                print("Initial load of contents verified. Page load successful.")
            else:
                pytest.fail("Initial load of contents not as expected. Infinite Scroll test failed.")
        except Exception as e:
            print(e)
            pytest.fail("Something went wrong while testing initial load of contents. Infinite Scroll test failed.")
        
        print("")
        print("Verifying infinite scroll")
        try:
            for _ in range(5):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(3)
            scrollTexts = driver.find_elements(By.CLASS_NAME, 'jscroll-added')
            if len(scrollTexts) == 7:
                print("Infinite scroll working as expected.")
            else:
                pytest.fail("Infinite scroll not working as expected. Infinite Scroll test failed.")
        except Exception as e:
            print(e)
            pytest.fail("Something went wrong while testing infinite scroll. Infinite Scroll test failed.")

        print("")
        print("Infinite Scroll test passed.")
    except Exception as e:
        print(e)
        pytest.fail("Infinite Scroll test failed.")
