import os
import time

from appium import webdriver
from config.config_reader import configReader as cr
from common.log import logger


def appium_start():
    appium_data = cr('config.ini')
    desired_caps = appium_data.getSections('appium')
    appium_url = appium_data.getValue('appium_url', 'url')

    print('appium_url', appium_url)
    #print(type(desired_caps))
    for i in desired_caps:
        print('desired_caps', i, desired_caps[i])
    driver = webdriver.Remote(appium_url, desired_caps)  # 连接Appium
    driver.implicitly_wait(5)
    return driver


if __name__ == '__main__':
    driver = appium_start()
    time.sleep(3)
    driver.quit()
