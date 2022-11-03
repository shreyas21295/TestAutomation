import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def sel_init():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    #chrome_options.add_argument("headless")
    chrome_options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver


def get_obj_repository():
    obj_rep = {}
    with open("../repository.csv") as rep:
        for line in csv.reader(rep):
            if "object" not in line[0]:
                obj_rep[line[0]] = line[1]

    return obj_rep
