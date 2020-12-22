import time
import random
import json
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 请求地址
targetUrl = "https://www.google.com"
i = 0
# 代理服务器
ip_addresses = open('ip.txt', encoding='utf_8')
hrefs = ['https://tktxinuk.com/',
         'https://www.officialtktx.com/,http://officialtktx.com/',
         'https://tktxdirect.com/',
         'https://tktxink.com/',
         'http://www.realtktxuk.co.uk/,https://realtktxuk.co.uk/']
fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.headless = False


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server={}'.format("2001:470:1:518::c928:63a6:443"))


def agree_click(browser_input):
    agree_ele = browser_input.find_elements_by_css_selector('.bErdLd')
    if len(agree_ele) > 0:
        iframe = browser_input.find_element_by_css_selector('#cnsw > iframe')
        browser_input.switch_to.frame(iframe)
        browser_input.implicitly_wait(5)
        agree_btn = browser_input.find_elements_by_css_selector('#introAgreeButton')
        if len(agree_btn) > 0:
            agree_btn[0].click()
            time.sleep(random.uniform(0, 1))
            browser_input.switch_to.default_content()


not_found_list = []
for proxyMeta in ip_addresses:
    print(proxyMeta)
    is_clicked = False
    # proxyMeta = '127.0.0.1:1081'
    ip = proxyMeta.split(':')[0]
    webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
        "httpProxy": proxyMeta,
        "ftpProxy": proxyMeta,
        "sslProxy": proxyMeta,
        "proxyType": "MANUAL",

    }
    profile = webdriver.FirefoxProfile()
    profile.set_preference("permissions.default.image", 2)

    browser = webdriver.Firefox(options=fireFoxOptions, firefox_profile=profile)
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
        time.sleep(random.uniform(10, 250))
        #
        agree_click(browser)
        # click image ads
        image_ads_div = browser.find_elements_by_css_selector("#tvcap")
        image_ads_div_side = browser.find_elements_by_css_selector('.cu-container')
        if len(image_ads_div) > 0:
            image_ads_div = image_ads_div[0]
        if len(image_ads_div_side) > 0:
            image_ads_div = image_ads_div_side[0]
        image_ads = image_ads_div.find_elements_by_tag_name('a')
        for image_ad in image_ads:
            href = image_ad.get_attribute('href')
            if 'www.tktxdirect.com' in href or 'www.tktxinuk.com' in href or 'www.txtkink.com' in href:
                if 'vplaurlt' not in image_ad.get_attribute('id'):
                    continue
                action = ActionChains(browser)
                hover = action.move_to_element(image_ad)
                hover.perform()

                print('do hover')
                time.sleep(random.uniform(3, 6))
                print('click image id')
                # image_ad.click()
                hover.key_down(Keys.CONTROL).click().key_up(Keys.CONTROL)
                hover.perform()
                time.sleep(random.uniform(7, 20))
                print('going back')
                # browser.execute_script("window.history.go(-1)")

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
