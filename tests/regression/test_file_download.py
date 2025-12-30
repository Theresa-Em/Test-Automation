import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time
import os

downloaded_path = "/root/Downloads/"

if os.path.exists(downloaded_path):
    for filename in os.listdir(downloaded_path):
        file_path = os.path.join(downloaded_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

def wait_for_download(file_path, timeout=30):
    start_time = time.time()
    while not os.path.exists(file_path):
        if time.time() - start_time > timeout:
            return False
        time.sleep(0.5)
    return True

def test_file_download(driver):
    # Write your code below this line
    try:
        driver.get("http://localhost:8081/")
        wait = WebDriverWait(driver, 10)
        file_download_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'File Download')))
        file_download_link.click()
        file_links = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'a')))
        file_links = driver.find_elements(By.TAG_NAME, 'a')
        print("\n")
        try:
            for link in file_links:
                print("Downloading file: " + link.get_attribute("href").split("/")[4])
                link.click()
                if not wait_for_download('/root/Downloads/' + link.get_attribute("href").split("/")[4]):
                    pytest.fail("Timeout while downloading file. File Download test failed.")
                if os.path.exists(os.path.join(downloaded_path, link.get_attribute("href").split("/")[4])):
                    print("Download successful")
                    print("")
                else:
                    pytest.fail("Downloaded file not found. File Download test failed.")
        except Exception as e:
            print(e)
            pytest.fail("Something went wrong. File Download test failed.")
        print("File Download test passed.")
    except Exception as e:
        print(e)
        pytest.fail("File Download test failed.")