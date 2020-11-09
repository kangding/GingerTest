"""
element操作方法进行封装
"""

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.log import logger

import time


class ElementAction(object):
    def __init__(self, driver):
        self.driver = driver
        pass

    def find_element(self, element_type, element_value):
        ele = None
        try:
            if element_type == "id":
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_id(element_value))
                ele = self.driver.find_element_by_id(element_value)
            elif element_type == "xpath":
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath(element_value))
                ele = self.driver.find_element_by_xpath(element_value)
            elif element_type == "class_name":
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_class_name(element_value))
                ele = self.driver.find_element_by_class_name(element_value)
            elif element_type == "class_names":
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_class_name(element_value))
                ele = self.driver.find_elements_by_class_name(element_value)
        except Exception as e:
            logger.error("查找元素失败，元素类型：{}，元素属性:{}，失败原因：{}".format(element_type, element_value, e))
        else:
            return ele

    def check_element_isEnabled(self, element):
        """
        检查element是否为可点击状态
        :param element:<class 'appium.webdriver.webelement.WebElement'>
        :return:可点击状态返回True，不可点击返回False
        """
        i = 1
        chkTag = False
        print(type(element))
        while i <= 5:
            logger.info("第%i次查看%s是否enabled" % (i, element.id))
            if element.is_enabled():
                chkTag = True
                break
            time.sleep(2)
            i = i + 1
        return chkTag

    def is_toast_exist(self, text=None, timeout=15, poll_frequency=0.5):

        try:
            toast_loc = '//*[@text=\'{}\']'.format(text)
            ele = WebDriverWait(self.driver, timeout, poll_frequency).until(lambda driver: driver.find_element_by_xpath(toast_loc))
            return ele
        except:
            return False

    # 后退
    def back(self):
        self.driver.keyevent(4)

    # 退出
    def exit_driver(self):
        element = self.driver.quit()
        return element

    # 截图
    def get_screen(self, path):
        self.driver.get_screenshot_as_file(path)

    # 获取界面大小
    def get_size(self):
        size = self.driver.get_window_size()
        return size

    # 向上滑动屏幕
    def swipe_to_up(self):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)

    # 向下滑动屏幕
    def swipe_to_down(self):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 500)

    # 向左滑动屏幕
    def swipe_to_left(self):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, 500)

    # 向右滑动屏幕
    def swipe_to_right(self):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width * 4 / 5, height / 2, width / 5, height / 2, 500)

    # 长按元素
    def long_press(self, element):
        TouchAction(self.driver).long_press(element).perform()

    # 点击坐标
    def touch_tap(self, x, y, duration=50):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        a = (float(x) / width) * width
        x1 = int(a)
        b = (float(y) / height) * height
        y1 = int(b)
        self.driver.tap([(x1, y1), (x1, y1)], duration)

    def take_ss(self, name="screenshot"):
        """
        获取手机当前截图，并保存至电脑目录中
        :param name: 带入中文名称时需加u，例如 takse_ss(name=u"中文")
        :return:
        """

        project_path = os.path.dirname(os.path.dirname(__file__))
        day = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        ss_path = project_path.split('common')[0] + '\\screenshot\\' + day
        ss_name = os.path.join(ss_path, '{0}.png'.format(name + time.strftime('%Y%m%d-%H%M%S')))
        print(ss_path, ss_name)
        if not os.path.exists(ss_path):
            os.makedirs(ss_path)
        self.driver.get_screenshot_as_file(ss_name)