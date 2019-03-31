import bs4
import operator
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def get_search_results(searchString):

    base_url = 'https://www.dba.dk'

    browser = webdriver.Firefox()
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

def get_data(page_source):
    soup = bs4.BeautifulSoup(page_source, 'html.parser')
    event_cells = soup.find_all('tr', {'class': 'dbaListing'})
    
    entries_arr = []
    for e in event_cells:
        description = e.select('td div a')[1].text
        price = float(e.select('td a')[6].text.strip()[:-3].strip())
        img_url = e.select('td div a div')[0]['data-original']
        details_url = e.select('td div a')[1]['href']
        combined = (description,price,img_url,details_url)
        entries_arr.append(combined)

    entries_arr.sort(key = operator.itemgetter(1))

    def mapfunc(el):
        return "<td>" + str(el) + "</td>"

    html = """<table>
        <tr>
            <th>Description</th>
            <th>Price</th>
            <th>Image url</th>
            <th>Details url</th>
        </tr>"""
    for tup in entries_arr:
        html += "<tr>"
        x = list(map(mapfunc, tup))
        for el in x:
            html += el
        html += "</tr>"
    return html
    

