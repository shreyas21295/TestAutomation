from seleniumConfig import sel_init, get_obj_repository
from selenium.webdriver.common.by import By
driver = sel_init()
url = get_obj_repository()['URL']


def test_login_elements():
    driver.get(url)
    username = get_obj_repository()['username']
    password = get_obj_repository()['password']
    login_button = get_obj_repository()['login_button']

    assert driver.find_element(By.ID, username)
    assert driver.find_element(By.ID, password)
    assert driver.find_element(By.ID, login_button)


def test_title():
    assert "Swag Labs" in driver.title
