import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_multiple_windows(driver):
    # Write your code below this line
    try:
        driver.get("http://localhost:8081/")
        wait = WebDriverWait(driver, 10)
        multiple_windows_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Multiple Windows')))
        multiple_windows_link.click()
        click_here_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Click Here')))
        print("\n")
        print("Opening multiple windows\n")
        openedWindows = 1
        try:
            parent_tab = driver.window_handles[0]
            for i in range(3):
                click_here_link.click()
                openedWindows += 1
                assert len(driver.window_handles) == openedWindows, "New window was not opened successfully."
                driver.switch_to.window(driver.window_handles[i+1])
                if "New Window" not in driver.title:
                    pytest.fail("Required window not opened. Multiple Windows test failed.")
                window_text = driver.find_element(By.TAG_NAME, "h3")
                if window_text.text != "New Window":
                    pytest.fail("Required content not found in new window. Multiple Windows test failed.")
                driver.switch_to.window(parent_tab)
        except Exception as e:
            print(e)
            pytest.fail("Opening a new window failed. Multiple Windows test failed.")
        print("Multiple Windows test passed.")
    except Exception as e:
        print(e)
        pytest.fail("Multiple Windows test failed.")