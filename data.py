from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import sys

url = 'https://marketplace.atlassian.com/search?category=Time%20tracking&product=jira'
chrome_driver_path = 'C:/Users/Sun of sadi/PycharmProjects/Web_Crawler/chromedriver.exe'

chrome_options = Options()
chrome_options.add_argument('--headless')

webdriver = webdriver.Chrome(
    executable_path=chrome_driver_path, options=chrome_options
)

# default search query
search_query = "jira"

if (len(sys.argv) >= 2):
    search_query = sys.argv[1]
    print(search_query)

with webdriver as driver:
    # Set timeout time
    wait = WebDriverWait(driver, 10)

    # retrive url in headless browser
    driver.get(url)

    # find search box
    search = driver.find_element_by_class_name('Input__InputElement-sc-1o6bj35-0 bfCuIo')
    search.send_keys(search_query + Keys.RETURN)

    wait.until(presence_of_element_located((By.CLASS_NAME, 'hits')))
    # time.sleep(3)
    results = driver.find_elements_by_class_name('css-187scic-LargeHitContainer e13wqmfi0')

    for quote in results:
        quoteArr = quote.text.split('\n')
        print(quoteArr)
        print()

    # must close the driver after task finished
    driver.close()