import time
import random
import json
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
import get_daily_ip_addresses
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

get_daily_ip_addresses.get_ip_address()
# 请求地址
targetUrl = "https://www.google.com"

# 代理服务器
ip_addresses = json.load(open('./ip.json')).get('data')
for info in ip_addresses:
    proxyHost = info.get('ip')
    proxyPort = info.get('port')
    proxyMeta = "{}:{}".format(proxyHost, proxyPort)
    print(proxyMeta)
    # proxyMeta = "127.0.0.1:1081"
    # options = ChromeOptions()
    # options.add_argument('--proxy-server={}'.format(proxyMeta))
    webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
        "httpProxy": proxyMeta,
        # "sslProxy": proxyMeta,
        "proxyType": "MANUAL",

    }

    # with webdriver.Firefox() as driver:
    # Open URL
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.headless = True
    try:
        with webdriver.Firefox(options=fireFoxOptions) as browser:
            browser.implicitly_wait(5)
            print('open google')
            browser.get(targetUrl)
            search_input_element = browser.find_element_by_css_selector('.gLFyf')
            time.sleep(random.randint(1, 3))
            print('enter keyword')
            for letter in 'eyecolens':
                search_input_element.send_keys(letter)
                time.sleep(random.uniform(0.2, 1))
            search_input_element.send_keys(Keys.ENTER)
            time.sleep(random.uniform(1, 3))
            print('find website')
            ad_element = browser.find_element_by_xpath('//a[@href="http://eyecolens.com/"]')
            time.sleep(random.uniform(1, 4))
            print('go to website')
            ad_element.click()
            time.sleep(random.uniform(4, 10))
            print('finished with {}'.format(proxyMeta))
    except Exception as inst:
        print(type(inst))
        print(inst)
        browser.quit()
    finally:
        browser.quit()
