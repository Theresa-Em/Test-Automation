import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service('/usr/local/bin/chromedriver'), options=options)
    yield driver
    sleep(2)
    driver.quit()