import time
import random
import json
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 请求地址
targetUrl = "https://www.google.com"

# 代理服务器
ip_addresses = json.load(open('./ip.json')).get('data')
for info in [ip_addresses[0]]:
    proxyHost = info.get('ip')
    proxyPort = info.get('port')
    proxyMeta = "{}:{}".format(proxyHost, proxyPort)
    print(proxyMeta)
    proxyMeta="127.0.0.1:1081"
    # options = ChromeOptions()
    # options.add_argument('--proxy-server={}'.format(proxyMeta))
    webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
        "httpProxy": proxyMeta,
        "sslProxy": proxyMeta,
        "proxyType": "MANUAL",

    }

    # with webdriver.Firefox() as driver:
        # Open URL
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)
    browser.get("https://www.google.com")
    search_input_element = browser.find_element_by_css_selector('.gLFyf')
    time.sleep(random.randint(1, 3))
    for letter in 'RIMOWA COVER':
        search_input_element.send_keys(letter)
        time.sleep(random.uniform(0.2, 1))
    search_input_element.send_keys(Keys.ENTER)
    time.sleep(random.randint(1, 3))
    ad_element = browser.find_element_by_partial_link_text('RIMOWA® Accessories - Shop the Online Store')
    time.sleep(random.randint(1, 4))
    ad_element.click()
    time.sleep(random.uniform(2, 8))



