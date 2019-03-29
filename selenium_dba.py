import bs4
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def get_search_results(searchString):

    base_url = 'https://www.dba.dk'

    browser = webdriver.Firefox(executable_path='/home/juanni420/anaconda3/lib/python3.7/geckodriver')
    browser.get(base_url)
    browser.implicitly_wait(3)

    searchField = browser.find_element_by_id("searchField")
    searchField.send_keys(searchString)
    searchField.send_keys(Keys.ENTER)

    sleep(3)

    oprettet = browser.find_element_by_xpath("//h4[contains(text(),'Oprettet')]")
    oprettet.click()

    sleep(3)

    last24h = browser.find_element_by_xpath("//span[contains(text(), 'Seneste 24 timer')]")
    last24h.click() 

    sleep(3)

    cph = browser.find_element_by_class_name("no-koebenhavn-og-omegn")
    cph.click()

    return browser.page_source



