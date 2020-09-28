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
ip_addresses = json.load(open('./ip.json', encoding='utf-8')).get('data')
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
        "ftpProxy": proxyMeta,
        "sslProxy": proxyMeta,
        "proxyType": "MANUAL",

    }

    # with webdriver.Firefox() as driver:
    # Open URL
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.headless = True
    try:
        with webdriver.Firefox(options=fireFoxOptions) as browser:
            browser.implicitly_wait(10)
            print('open google')
            browser.get(targetUrl)
            search_input_element = browser.find_element_by_css_selector('.gLFyf')
            time.sleep(random.uniform(2, 8))
            print('enter keyword')
            for letter in 'TKTX':
                search_input_element.send_keys(letter)
                time.sleep(random.uniform(0.2, 2))
            search_input_element.send_keys(Keys.ENTER)
            time.sleep(random.uniform(6, 20))
            print('find website')
            href = ['https://tattootktx.com/', 'https://tknumbing.com/'][random.randint(0, 1)]
            ad_element = browser.find_element_by_xpath('//data-pcu[@href="{}"]'.format(href))
            time.sleep(random.uniform(3, 10))
            print('go to website {}'.format(href))
            ad_element.click()
            time.sleep(random.uniform(10, 30))
            print('finished with {} with {}'.format(proxyMeta, href))
    except Exception as inst:
        print(type(inst))
        print(inst)
        print(browser.title)
        browser.quit()
