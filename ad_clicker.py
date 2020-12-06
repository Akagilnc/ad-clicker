import time
import random
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# ????
targetUrl = "https://www.google.com"
i = 0
# ?????
ip_addresses = open('ip.txt', encoding='utf_8')
hrefs = ['https://tktxusshop.com/,http://www.tktxusshop.com/',
         'https://tknumb.com/',
         'https://tk-tx.com/']
fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.headless = True
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server={}'.format("2001:470:1:518::c928:63a6:443"))


def agree_click(browser_input):
    agree_ele = browser_input.find_elements_by_css_selector('.bErdLd')
    if len(agree_ele) > 0:
        iframe = browser_input.find_element_by_css_selector('#cnsw > iframe:nth-child(1)')
        browser_input.switch_to.frame(iframe)
        browser_input.implicitly_wait(1)
        agree_btn = browser_input.find_elements_by_css_selector('#introAgreeButton')
        if len(agree_btn) > 0:
            agree_btn[0].click()
            time.sleep(random.uniform(0, 1))
            browser_input.switch_to.default_content()


not_found_list = []
for proxyMeta in ip_addresses:
    print(proxyMeta)
    is_clicked = False
    # proxyMeta = '127.0.0.1:7890'
    ip = proxyMeta.split(':')[0]
    webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
        "httpProxy": proxyMeta,
        "ftpProxy": proxyMeta,
        "sslProxy": proxyMeta,
        "proxyType": "MANUAL",

    }
    browser = webdriver.Firefox(options=fireFoxOptions)
    try:
        browser.implicitly_wait(10)
        print('open google')
        browser.get(targetUrl)
        search_input_element = browser.find_element_by_css_selector('.gLFyf')
        agree_click(browser)
        time.sleep(random.uniform(2, 15))
        print('enter keyword')
        for letter in 'TKTX':
            search_input_element.send_keys(letter)
            time.sleep(random.uniform(0.2, 3))
        search_input_element.send_keys(Keys.ENTER)
        time.sleep(random.uniform(4, 40))
        #
        agree_click(browser)
        #
        for href in hrefs:
            is_page2 = False
            print('find website {}'.format(href))
            ad_elements = browser.find_elements_by_xpath('//a[@data-pcu="{}"]'.format(href))
            time.sleep(random.uniform(3, 20))
            if len(ad_elements) == 0:
                page2 = browser.find_element_by_css_selector('#pnnext')
                page2.click()
                print('go to page 2')
                is_page2 = True
                time.sleep(random.uniform(2, 20))
                ad_elements = browser.find_elements_by_xpath('//a[@data-pcu="{}"]'.format(href))
            print('go to website {}'.format(href))
            if len(ad_elements) == 0:
                print('not found')
                browser.back()
                continue
            ad_elements[0].click()
            i += 1
            is_clicked = True
            time.sleep(random.uniform(4, 16))
            browser.back()
            time.sleep(random.uniform(0, 1))
            if is_page2:
                browser.back()
            print('finished with {} with {}'.format(proxyMeta, href))

        time.sleep(2)

        if not is_clicked:
            not_found_list.append(proxyMeta + '\n')
            browser.set_window_size(1920, 1080)
            browser.save_screenshot("{}_not_found.png".format(ip))
        browser.close()
        time.sleep(random.uniform(15, 50))
    except Exception as inst:
        print(type(inst))
        print(inst)
        browser.set_window_size(1920, 1080)
        browser.save_screenshot("{}_screenshot.png".format(ip))
        browser.close()
        time.sleep(random.uniform(0, 1))
    finally:
        print('clicked {} times'.format(str(i)))
        browser.quit()

with open('not_found.txt', 'w', encoding='utf_8') as file:
    file.writelines(not_found_list)

