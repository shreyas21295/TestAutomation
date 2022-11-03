from seleniumConfig import sel_init, get_obj_repository
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver = sel_init()
url = get_obj_repository()['URL']

username = get_obj_repository()['username']
password = get_obj_repository()['password']
login_button = get_obj_repository()['login_button']
inventory = get_obj_repository()['inventory']
login_error = get_obj_repository()['login_error']
hamburger_menu = get_obj_repository()['hamburger_menu_open']
hamburger_menu_close = get_obj_repository()['hamburger_menu_close']
logout_button = get_obj_repository()['logout_button']


def test_unsuccessful_login():
    driver.get(url)
    driver.find_element(By.ID, username).send_keys('standard_user')
    driver.find_element(By.ID, password).send_keys('sauce')
    driver.find_element(By.ID, login_button).click()
    assert WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, login_error)))


def test_successful_login():
    driver.get(url)
    driver.find_element(By.ID, username).send_keys('standard_user')
    driver.find_element(By.ID, password).send_keys('secret_sauce')
    driver.find_element(By.ID, login_button).click()
    assert WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, inventory)))


def test_successful_logout():
    driver.get(url)
    driver.find_element(By.ID, username).send_keys('standard_user')
    driver.find_element(By.ID, password).send_keys('secret_sauce')
    driver.find_element(By.ID, login_button).click()
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, inventory)))
    driver.find_element(By.ID, hamburger_menu).click()
    driver.implicitly_wait(5)
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, hamburger_menu_close)))
    driver.find_element(By.ID, logout_button).click()
    assert WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, username)))


