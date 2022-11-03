from seleniumConfig import sel_init, get_obj_repository
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import random
driver = sel_init()
url = get_obj_repository()['URL']
username = get_obj_repository()['username']
password = get_obj_repository()['password']
login_button = get_obj_repository()['login_button']
inventory = get_obj_repository()['inventory']
inventory_item_name = get_obj_repository()['inventory_item_name']
product_detail_text = get_obj_repository()['product_detail_text']
back_to_products = get_obj_repository()['back_to_products']

names_of_products_expected = ['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Fleece Jacket',
                'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)']

names_of_products_actual = []


def test_get_items():
    driver.get(url)
    driver.find_element(By.ID, username).send_keys('standard_user')
    driver.find_element(By.ID, password).send_keys('secret_sauce')
    driver.find_element(By.ID, login_button).click()
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, inventory)))

    items = driver.find_elements(*(By.CLASS_NAME, inventory_item_name))
    for item in items:
        names_of_products_actual.append(item.text)

    assert names_of_products_actual == names_of_products_expected


def test_products_detail_page():
    # test whether product names are same on product detail page
    driver.get(url)
    driver.find_element(By.ID, username).send_keys('standard_user')
    driver.find_element(By.ID, password).send_keys('secret_sauce')
    driver.find_element(By.ID, login_button).click()
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, inventory)))
    items = driver.find_elements(*(By.CLASS_NAME, inventory_item_name))
    item_number = random.randint(0, 5)
    product_name = items[item_number].text

    items[item_number].click()
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, product_detail_text)))
    assert product_name in driver.find_element(By.CLASS_NAME, product_detail_text).text
    driver.find_element(By.ID, back_to_products).click()
    assert WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, inventory)))
