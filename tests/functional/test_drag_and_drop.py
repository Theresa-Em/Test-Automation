import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop

def test_drag_and_drop(driver):
    # Write your code below this line
    try:
        driver.get("http://localhost:8081/")
        wait = WebDriverWait(driver, 10)
        drag_and_drop_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Drag and Drop')))
        drag_and_drop_link.click()
        draggable_A = wait.until(EC.element_to_be_clickable((By.ID, 'column-a')))
        draggable_B = wait.until(EC.element_to_be_clickable((By.ID, 'column-b')))
        print("\n")
        print("Before drag and drop")
        print("")
        print("Text in first box: " + draggable_A.find_element(By.TAG_NAME, "header").text)
        print("Text in second box: " + draggable_B.find_element(By.TAG_NAME, "header").text)
        print("")
        print("Dragging and dropping first box over second box\n")
        try:
            drag_and_drop(driver, draggable_A, draggable_B)
            if draggable_A.find_element(By.TAG_NAME, "header").text != "B" or draggable_B.find_element(By.TAG_NAME, "header").text != "A":
                pytest.fail("Boxes not swapped after dragging. Drag and Drop test failed.")
            print("After drag and drop")
            print("")
            print("Text in first box: " + draggable_A.find_element(By.TAG_NAME, "header").text)
            print("Text in second box: " + draggable_B.find_element(By.TAG_NAME, "header").text)
            print("")
            print("Drag and Drop test passed.")
        except:
            pytest.fail("Something went wrong during drag and drop. Drag and Drop test failed.")
    except ElementNotInteractableException:
        print("One of the elements was not interactable.")
        pytest.fail("Drag and Drop test failed due to non-interactable element.")
    except NoSuchElementException:
        print("One of the elements was not found.")
        pytest.fail("Drag and Drop test failed due to missing element.")
    except TimeoutException:
        print("Operation timed out.")
        pytest.fail("Drag and Drop test failed due to timeout.")
    except Exception as e:
        print("An unexpected error occured:", e)
        pytest.fail("Drag and Drop test failed due to an unexpected error.")
