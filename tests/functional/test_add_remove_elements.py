import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_remove_elements(driver):
    # Write your code below this line
    try:
        driver.get("http://localhost:8081/")
        wait = WebDriverWait(driver, 10)
        add_remove_elements_list = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Add/Remove Elements')))
        add_remove_elements_list.click()
        
        add_element_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Add Element"]')))
        print("\n")
        print("Adding element")

        try:
            add_element_button.click()
            delete_button = wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="Delete"]')))
            assert delete_button.is_displayed()
        except Exception as e:
            print(e)
            pytest.fail("Failed to add element. Add/Remove Elements test failed.")
        else:
            print("")
            print("Element added successfully.")

        print("")
        print("Deleteing element\n")
        try:
            delete_button = driver.find_elements(By.XPATH, '//button[text()="Delete"]')[0]
            delete_button.click()
            if len(driver.find_elements(By.XPATH, '//button[text()="Delete"]')) == 0:
                print("Element deleted successfully.")
            else:
                pytest.fail("Failed to delete element. Add/Remove Elements test failed.")
        except Exception as e:
            print(e)
            pytest.fail("Failed to delete element. Add/Remove Elements test failed.")
        
        print("")
        print("Adding multiple elements")
        try:
            for _ in range(10):
                add_element_button.click()
            delete_buttons = driver.find_elements(By.XPATH, '//button[text()="Delete"]')
            if len(delete_buttons) != 10:
                pytest.fail("Failed to add multiple elements. Add/Remove Elements test failed.")
            else:
                print("Multiple elements added successfully.")
        except Exception as e:
            print(e)
            pytest.fail("Failed to add multiple elements. Add/Remove Elements test failed.")
        
        print("")
        print("Deleting multiple elements")
        try:
            delete_buttons = driver.find_elements(By.XPATH, '//button[text()="Delete"]')
            for delete_button in delete_buttons:
                delete_button.click()
            delete_buttons = driver.find_elements(By.XPATH, '//button[text()="Delete"]')
            if len(delete_buttons) != 0:
                pytest.fail("Failed to delete multiple elements. Add/Remove Elements test failed.")
            else:
                print("Multiple elements deleted successfully.")
        except Exception as e:
            print(e)
            pytest.fail("Failed to delete multiple elements. Add/Remove Elements test failed.")
        
        print("")
        print("Add/Remove Elements test passed")   
    except Exception as e:
        print(e)
        pytest.fail("Add/Remove Elements test failed.")