import time
import random
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

targetUrl = "https://www.amazon.com"
i = 0
ip_addresses = open('ip.txt', encoding='utf_8')
# ip_addresses = open('ip.txt', encoding='utf_8')
fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.headless = False
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server={}'.format("2001:470:1:518::c928:63a6:443"))


# proxyMeta = '127.0.0.1:1081'
for proxyMeta in ip_addresses[:20]:
    print(proxyMeta)
    is_clicked = False
    # proxyMeta = '127.0.0.1:7890'
    ip = proxyMeta.split(':')[0]
    title = 'Topical Anesthetic Tattoo Cream 10g for Tattoos Semi Permanent US 3-6 Working Days'
    webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
        "httpProxy": proxyMeta,
        "ftpProxy": proxyMeta,
        "sslProxy": proxyMeta,
        "proxyType": "MANUAL",

    }
    browser = webdriver.Firefox(options=fireFoxOptions)
    try:
        browser.implicitly_wait(10)
        print('open amazon')
        browser.get(targetUrl)
        search_input_element = browser.find_element_by_css_selector('#twotabsearchtextbox')
        time.sleep(random.uniform(2, 15))
        print('enter keyword')
        for letter in 'tktx':
            search_input_element.send_keys(letter)
            time.sleep(random.uniform(0.2, 3))
        search_input_element.send_keys(Keys.ENTER)
        time.sleep(random.uniform(4, 10))
        elements_instead = browser.find_elements_by_link_text('Search instead for tktx')
        if len(elements_instead) > 0:
            elements_instead[0].click()

        time.sleep(random.uniform(4, 10))
        for i in range(10):
            test_elements = browser.find_elements_by_link_text(title)
            if len(test_elements) > 0:
                test_elements[0].click()
                "finished"
                break
            else:
                next_element = browser.find_element_by_css_selector('.a-last > a:nth-child(1)')
                print("go to next page")
                next_element.click()
                time.sleep(random.uniform(5, 8))

        time.sleep(random.uniform(5, 10))
        browser.close()
        browser.quit()
        time.sleep(random.uniform(53, 126))
    except Exception as inst:
        print(inst)