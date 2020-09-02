# _*_ coding:utf-8 _*_

from appium import webdriver

import time
import unittest
from common.log import logger

from common.element_action import ElementAction
from config.config_reader import configReader


class MiPrint(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '9',
            'appPackage': 'com.mi.print',
            # 'appActivity': 'com.mi.print/.MainActivity',
            'appActivity': '.SplashActivity',
            # 'deviceName': '58a610e1',
            'deviceName': '37955909',
            'noReset': 'True'
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium
        self.driver.implicitly_wait(5)
        self.data = configReader('element_config.ini')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    """
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '9',
            'appPackage': 'com.mi.print',
            #'appActivity': 'com.mi.print/.MainActivity',
            'appActivity': '.SplashActivity',
            #'deviceName': '58a610e1',
            'deviceName': '37955909',
            'noReset': 'True'
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()
    

    def test_Func1(self):
        self.driver.find_element_by_id('com.mi.print:id/title_bar_return').click()
        self.driver.implicitly_wait(5)
        textChk = self.driver.find_element_by_id('com.mi.print:id/title_bar_title').text
        self.driver.find_element_by_id('com.mi.print:id/title_bar_return').click()

        time.sleep(1)
        self.assertEqual(textChk, "我的打印机")
        # pass

    def test_Func2(self):
        logger.info("进入我的打印机界面")
        myPrinter_id = self.data.getValue('home_page', 'myPrinter_id')
        myPrinter_title = self.data.getValue('myPrinter_page', 'myPrinter_title')
        myPrinter_title_id = self.data.getValue('myPrinter_page', 'myPrinter_title_id')
        print(
            'myPrinter_id = %s, myPrinter_title = %s, myPrinter_title_id = %s' % (myPrinter_id, myPrinter_title,
                                                                                  myPrinter_title_id))
        ElementAction(self.driver).find_element("id", myPrinter_id).click()
        #myPrinter_title_text = ElementAction(self.driver).find_element("id", myPrinter_title_id).text()
        myPrinter_title_text = ElementAction(self.driver).find_element("id", "com.mi.print:id/title_bar_title").text
        logger.info('myPrinter_title_text = %s' % myPrinter_title_text)
        ElementAction(self.driver).back()
        self.assertEqual(myPrinter_title, myPrinter_title_text)
        # pass
    """

    # def test_Func3(self):
    #     logger.info("进入文档打印")
    #     docPrint_id = self.data.getValue('home_page', 'docPrint_id')
    #     docPrint_page_title = self.data.getValue('docPrint_page', 'docPrint_page_title')
    #     docPrint_page_title_id = self.data.getValue('docPrint_page', 'docPrint_page_title_id')
    #     logger.info(
    #         'docPrint_id = %s, docPrint_page_title = %s, docPrint_page_title_id = %s' % (docPrint_id, docPrint_page_title,
    #                                                                               docPrint_page_title_id))
    #     ElementAction(self.driver).find_element("id", docPrint_id).click()
    #     docPrint_page_title_text = ElementAction(self.driver).find_element("id", docPrint_page_title_id).text
    #     logger.info('docPrint_page_title_text = %s' % docPrint_page_title_text)
    #     ElementAction(self.driver).back()
    #     self.assertEqual(docPrint_page_title, docPrint_page_title_text)

    # def test_Func4(self):
    #     logger.info("进入设置界面")
    #     setting_id = self.data.getValue('home_page', 'setting_id')
    #     setting_title = self.data.getValue('setting', 'setting_title')
    #     setting_title_id = self.data.getValue('setting', 'setting_title_id')
    #     ElementAction(self.driver).find_element("id", setting_id).click()
    #     setting_title_text = ElementAction(self.driver).find_element("id", setting_title_id).text
    #     ElementAction(self.driver).back()
    #     self.assertEqual(setting_title, setting_title_text)
    """
    def test_Func5(self):
        logger.info("进入照片打印界面")
        photoPrint_id = self.data.getValue('home_page', 'photoPrint_id')
        photo_size_class_name = self.data.getValue('photoPrint_page', 'photo_size_class_name')
        ElementAction(self.driver).find_element('id', photoPrint_id).click()
        test_text1 = ElementAction(self.driver).find_element("class_names", photo_size_class_name)[0].text
        test_text2 = ElementAction(self.driver).find_element("class_names", photo_size_class_name)[1].text
        logger.info("照片打印尺寸， %s, %s" % (test_text1, test_text2))

        ElementAction(self.driver).find_element("class_names", photo_size_class_name)[1].click()
        photo_select_title_id1 = self.data.getValue('photoPrint_page', 'photo_select_title_id1')
        photo_select_title_id2 = self.data.getValue('photoPrint_page', 'photo_select_title_id2')
        photo_select_title1 = self.data.getValue('photoPrint_page', 'photo_select_title1')
        photo_select_title2 = self.data.getValue('photoPrint_page', 'photo_select_title2')
        photo_select_title_text1 = ElementAction(self.driver).find_element("id", photo_select_title_id1).text
        photo_select_title_text2 = ElementAction(self.driver).find_element("id", photo_select_title_id2).text
        logger.info("照片选择页面标题为：%s, %s" % (photo_select_title_text1, photo_select_title_text2))

        chkResult = True
        if photo_select_title1 != photo_select_title_text1:
            chkResult = False
            logger.error("照片选择页面标题不正确，APP中为%s，实际应为%s" % (photo_select_title_text1, photo_select_title1))
        elif photo_select_title2 != photo_select_title_text2:
            chkResult = False
            logger.error("照片选择页面标题不正确，APP中为%s，实际应为%s" % (photo_select_title_text2, photo_select_title2))
        ElementAction(self.driver).back()
        self.assertEqual(chkResult, True)
    

    def test_Func6(self):

        logger.info("进入身份证打印界面")
        ID_id = self.data.getValue('home_page', 'ID_id')

        i = 1
        while i <= 3:
            try:
                logger.info("尝试第%i次点击身份证打印 ,id：%s，如有Error请忽略" % (i, ID_id))
                ElementAction(self.driver).find_element('id', ID_id).click()
                break
            except:
                i = i + 1
                ElementAction(self.driver).swipe_to_up()

        ID_page_title = self.data.getValue('ID_page', 'ID_page_title')
        ID_page_title_id = self.data.getValue('ID_page', 'ID_page_title_id')

        ID_page_title_text = ElementAction(self.driver).find_element("id", ID_page_title_id).text

        logger.info("身份证打印界面的标题为：%s" % ID_page_title_text)
        ElementAction(self.driver).back()
        self.assertEqual(ID_page_title, ID_page_title_text)
    """

    def test_Func7(self):
        u"""测试用例7"""
        logger.info("点击购买纸张")
        paper_id = self.data.getValue('home_page', 'paper_id')
        toast_title = self.data.getValue('toast', 'toast_title')
        # paper_id = self.data.getValue('home_page', 'paper_id')

        i = 1
        while i <= 3:
            try:
                logger.info("尝试第%i次点击身份证打印 ,id：%s，如有Error请忽略" % (i, paper_id))
                print("尝试第%i次点击身份证打印 ,id：%s，如有Error请忽略" % (i, paper_id))
                ElementAction(self.driver).find_element('id', paper_id).click()
                break
            except:
                i = i + 1
                ElementAction(self.driver).swipe_to_up()
        chkTag = True
        ele = ElementAction(self.driver).is_toast_exist(toast_title)
        if not ele:
            # chkTag = False
            logger.error("未找到toast：%s" % toast_title)
        else:
            toast_title = 'cuowushili'
            if toast_title != ele.text:
                chkTag = False
                logger.error("Toast标题错误：%s" % ele.text)

        self.assertEqual(chkTag, True)

        """
            控件在有些手机不能显示出来，需要滑动才能找到
            首先尝试点击控件，找不到后滑动屏幕
        

        i = 1
        while i <= 3:
            try:
                logger.info("尝试第%i次点击帮助中心,id：%s，如有Error请忽略" % (i, ink_id))
                ElementAction(self.driver).find_element('id', ink_id).click()
                break
            except:
                i = i + 1
                ElementAction(self.driver).swipe_to_up()

        ink_page_title = self.data.getValue('ink_page', 'ink_page_title')
        ink_page_title_id = self.data.getValue('ink_page', 'ink_page_title_id')

        # 页面加载时间过长
        time.sleep(20)
        ink_page_title_text = ElementAction(self.driver).find_element("id", ink_page_title_id).text

        logger.info("身份证打印界面的标题为：%s" % ink_page_title_text)
        ElementAction(self.driver).back()
        self.assertEqual(ink_page_title, ink_page_title_text)
        """
from HTMLTestRunner import  HTMLTestRunner
import os
if __name__ == '__main__':

    suit = unittest.TestSuite()
    suit.addTest(MiPrint("test_Func7"))
    current_dir = os.path.dirname(os.path.realpath(__file__))
    report_path = r"\report"
    report_name = current_dir + report_path + r"\report.html"
    print(report_name)
    fp = open(report_name, "wb")
    runner = HTMLTestRunner(stream=fp, title="报告生成", description="description", verbosity=2)

    runner.run(suit)
    fp.close()
