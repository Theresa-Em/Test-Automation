import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

parent_directory = "/usercode/automated-testing/files/"
uploaded_path = "/usercode/automated-testing/server/public/uploads/"

@pytest.mark.parametrize("test_case, file_name, expected_message", [
    ("Uploading valid file", "valid_file.txt", "File Uploaded!"),
    ("Uploading invalid file", "invalid_file.py", "Only text files are allowed for upload"),
    ("Uploading large file", "large_file.txt", "File size should not exceed 1MB"),
    ("Clicking upload button without choosing any file", "", "Please select a file to upload")
])
def test_file_upload(driver, test_case, file_name, expected_message):
    # Write your code below this line
    try:
        driver.get("http://localhost:8081/")
        wait = WebDriverWait(driver, 10)
        file_upload_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'File Upload')))
        file_upload_link.click()
        choose_file_button = wait.until(EC.element_to_be_clickable((By.ID, 'file-upload')))
        upload_botton = wait.until(EC.element_to_be_clickable((By.ID, 'file-submit')))
        print("\n")
        print(test_case)
        try:
            if test_case != "Clicking upload button without choosing any file":
                choose_file_button.send_keys(os.path.join(parent_directory, file_name))
            upload_botton.click()
            response = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3")))
            if test_case == "Uploading vaild file":
                response = driver.find_elements(By.TAG_NAME, 'h3')[0]
            else:
                if len(driver.find_elements(By.TAG_NAME, 'h3')) > 1:
                    response = driver.find_elements(By.TAG_NAME, 'h3')[1]
            response = response.text
            if response == expected_message:
                if test_case == "Uploading vaild file":
                    if os.path.exists(os.path.join(uploaded_path, file_name)):
                        print("Uploading vaild file test successful.")
                    else:
                        pytest.fail("Uploaded file test not found. File Upload test failed.")
                elif test_case == "Uploading invalid file":
                    print("Uploading invalid file test successful.")
                elif test_case == "Uploading large file":
                    print("Uploading large file test successful.")
                elif test_case == "Clicking upload button without choosing any file":
                    print("Clicking upload button without choosing any file test successful.")
            else:
                pytest.fail("Invalid response received. File Upload test failed.")
        except Exception as e:
            print(e)
            pytest.fail("Something went wrong. File Upload test failed.")
        print("")
        print("File Upload test passed.")
    except Exception as e:
        print(e)
        pytest.fail("File Upload test failed.")