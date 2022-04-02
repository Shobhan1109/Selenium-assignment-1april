import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setUp():
    global driver, product
    product = input("Enter the product to be searched:")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()

def test_flip(setUp):
    driver.get("https://www.google.com/")
    time.sleep(1)
    driver.find_element_by_name("q").send_keys("flipkart")
    time.sleep(1)
    driver.find_element_by_name("btnK").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[7]/div/div[10]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a/h3").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
    time.sleep(1)
    driver.find_element_by_name("q").send_keys(product)
    time.sleep(1)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 2800)")
    time.sleep(2)
    driver.find_element_by_partial_link_text("APPLE iPhone 13 ((PRODUCT)RED, 256 GB)").click()
    time.sleep(5)