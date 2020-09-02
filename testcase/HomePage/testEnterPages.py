from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from common.log import logger
import time
import unittest

from common.appium_start import appium_start
from common.element_action import ElementAction
from config.config_reader import configReader

"""
首页进入其他各个页面
"""


class EnterPages(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = appium_start()
        self.data = configReader('element_config.ini')

        docPrint_id = self.data.getValue('home_page', 'docPrint_id')
        ele = ElementAction(self.driver).find_element('id', docPrint_id)
        if not ElementAction(self.driver).check_element_isEnabled(ele):
            logger.error("打印机状态错误，不能执行EnterPages测试用例")
            exit()
        # self.log = logger

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_01enter_myPrinter(self):
        logger.info("进入我的打印机界面")
        myPrinter_id = self.data.getValue('home_page', 'myPrinter_id')
        myPrinter_title = self.data.getValue('myPrinter_page', 'myPrinter_title')
        myPrinter_title_id = self.data.getValue('myPrinter_page', 'myPrinter_title_id')
        logger.info(
            'myPrinter_id = %s, myPrinter_title = %s, myPrinter_title_id = %s' % (myPrinter_id, myPrinter_title,
                                                                                  myPrinter_title_id))
        ElementAction(self.driver).find_element("id", myPrinter_id).click()
        myPrinter_title_text = ElementAction(self.driver).find_element("id", myPrinter_title_id).text
        logger.info('myPrinter_title_text = %s' % myPrinter_title_text)
        ElementAction(self.driver).back()
        self.assertEqual(myPrinter_title, myPrinter_title_text)

    def test_02enter_setting(self):
        logger.info("进入设置界面")
        setting_id = self.data.getValue('home_page', 'setting_id')
        setting_title = self.data.getValue('setting', 'setting_title')
        setting_title_id = self.data.getValue('setting', 'setting_title_id')
        ElementAction(self.driver).find_element("id", setting_id).click()
        setting_title_text = ElementAction(self.driver).find_element("id", setting_title_id).text
        ElementAction(self.driver).back()
        self.assertEqual(setting_title, setting_title_text)

    def test_03enter_docPrint(self):
        """
               home_page:首页
               docPrint_id:文档打印id
               docPrint_page:文档打印通道选择页面
               docPrint_page_title：文档打印通道选择页面title
               docPrint_page_title_id：文档打印通道选择页面title的id
               docPrint_page_title_text：app中title的实际值
        """
        logger.info("进入文档打印")
        """
            读取element_config.ini中home_page一项，获取docPrint_id，docPrint_page，docPrint_page_title_id的值
        """
        docPrint_id = self.data.getValue('home_page', 'docPrint_id')
        docPrint_page_title = self.data.getValue('docPrint_page', 'docPrint_page_title')
        docPrint_page_title_id = self.data.getValue('docPrint_page', 'docPrint_page_title_id')
        logger.info(
            'docPrint_id = %s, docPrint_page_title = %s, docPrint_page_title_id = %s' % (
            docPrint_id, docPrint_page_title,
            docPrint_page_title_id))
        ElementAction(self.driver).find_element("id", docPrint_id).click()
        """ 
            获取APP中docPrint_page_title_text：app中title的实际值
        """
        docPrint_page_title_text = ElementAction(self.driver).find_element("id", docPrint_page_title_id).text
        logger.info('docPrint_page_title_text = %s' % docPrint_page_title_text)
        ElementAction(self.driver).back()

        """
            断言配置文件中的值与实际APP的值
        """
        self.assertEqual(docPrint_page_title, docPrint_page_title_text)

    def test_04enter_photoPrint(self):
        """
            photoPrint_id:首页照片入口id
            photoPrint_page：照片选择界面
            photo_size_class_name：照片尺寸选择的class name，对应6寸和A4
            photo_select_title_id1：照片选择界面的标题1的id
            photo_select_title_id2：照片选择界面的标题2的id
            photo_select_title1：照片选择界面的标题1的值
            photo_select_title2：照片选择界面的标题2的值
            photo_select_title_text1：读取APP中标题1的值
            photo_select_title_text2：读取APP中标题2的值

        :return:
        """
        logger.info("进入照片打印界面")
        photoPrint_id = self.data.getValue('home_page', 'photoPrint_id')
        photo_size_class_name = self.data.getValue('photoPrint_page', 'photo_size_class_name')
        ElementAction(self.driver).find_element('id', photoPrint_id).click()

        """
            class_names返回值为list，需要处理一下
        """
        test_text1 = ElementAction(self.driver).find_element("class_names", photo_size_class_name)[0].text
        test_text2 = ElementAction(self.driver).find_element("class_names", photo_size_class_name)[1].text
        logger.info("照片打印尺寸， %s, %s" % (test_text1, test_text2))

        """
            选择A4进入照片选择界面
        """
        ElementAction(self.driver).find_element("class_names", photo_size_class_name)[1].click()
        photo_select_title_id1 = self.data.getValue('photoPrint_page', 'photo_select_title_id1')
        photo_select_title_id2 = self.data.getValue('photoPrint_page', 'photo_select_title_id2')
        photo_select_title1 = self.data.getValue('photoPrint_page', 'photo_select_title1')
        photo_select_title2 = self.data.getValue('photoPrint_page', 'photo_select_title2')
        photo_select_title_text1 = ElementAction(self.driver).find_element("id", photo_select_title_id1).text
        photo_select_title_text2 = ElementAction(self.driver).find_element("id", photo_select_title_id2).text
        logger.info("照片选择页面标题为：%s, %s" % (photo_select_title_text1, photo_select_title_text2))

        """
            照片选择界面有两个title，可以对其中一个进行断言，下面判断了两个title，需要额外处理
        """
        chkResult = True
        if photo_select_title1 != photo_select_title_text1:
            chkResult = False
            logger.error("照片选择页面标题不正确，APP中为%s，实际应为%s" % (photo_select_title_text1, photo_select_title1))
        elif photo_select_title2 != photo_select_title_text2:
            chkResult = False
            logger.error("照片选择页面标题不正确，APP中为%s，实际应为%s" % (photo_select_title_text2, photo_select_title2))
        ElementAction(self.driver).back()
        self.assertEqual(chkResult, True)


    def test_05enter_scan(self):
        """
            scan_id:首页中扫描id
            scan_page_title：扫描界面的标题
            scan_page_title_id：扫描界面标题的id
            scan_page_title_text：读取的APP中扫描界面的标题
        :return:
        """
        logger.info("进入扫描界面")
        scan_id = self.data.getValue('home_page', 'scan_id')
        ElementAction(self.driver).find_element('id', scan_id).click()

        scan_page_title = self.data.getValue('scan_page', 'scan_page_title')
        scan_page_title_id = self.data.getValue('scan_page', 'scan_page_title_id')
        scan_page_title_text = ElementAction(self.driver).find_element("id", scan_page_title_id).text

        logger.info("扫描界面的标题为：%s" % scan_page_title_text)
        ElementAction(self.driver).back()
        self.assertEqual(scan_page_title, scan_page_title_text)




    def test_06enter_ID(self):
        """
            ID_id:首页身份证打印的id
            ID_page：身份证扫描界面
            ID_page_title：身份证扫描界面的标题
            ID_page_title_id：身份证扫描界面title的id
            ID_page_title_text：读取APP中的身份证扫描界面的标题
        :return:
        """
        logger.info("进入身份证打印界面")
        ID_id = self.data.getValue('home_page', 'ID_id')

        """
            控件在有些手机不能显示出来，需要滑动才能找到
            首先尝试点击控件，找不到后滑动屏幕
        """

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



    def test_07enter_visa(self):
        """
        credential_id:首页证件照id
        credential_page_title：证件照界面的标题
        credential_page_title_id：证件照界面的标题id
        credential_page_title_text：读取APP中证件照界面的标题
        :return:
        """
        logger.info("进入证件照打印界面")
        credential_id = self.data.getValue('home_page', 'credential_id')

        """
            控件在有些手机不能显示出来，需要滑动才能找到
            首先尝试点击控件，找不到后滑动屏幕
        """
        i = 1
        while i <= 3:
            try:
                logger.info("尝试第%i次点击证件照打印 ,id：%s，如有Error请忽略" % (i, credential_id))
                ElementAction(self.driver).find_element('id', credential_id).click()
                break
            except:
                i = i + 1
                ElementAction(self.driver).swipe_to_up()

        credential_page_title = self.data.getValue('credential_page', 'credential_page_title')
        credential_page_title_id = self.data.getValue('credential_page', 'credential_page_title_id')

        credential_page_title_text = ElementAction(self.driver).find_element("id", credential_page_title_id).text

        logger.info("身份证打印界面的标题为：%s" % credential_page_title_text)
        ElementAction(self.driver).back()
        self.assertEqual(credential_page_title, credential_page_title_text)


    def test_08enter_help(self):
        """
            FAQ_id:首页帮助中心id
            FAQ_page_title:FAQ界面标的题
            FAQ_page_title_id:FAQ界面标题的id
            FAQ_page_title_text:读取APP中FAQ界面的标题
        :return:
        """
        logger.info("进入FAQ界面")
        FAQ_id = self.data.getValue('home_page', 'FAQ_id')

        """
            控件在有些手机不能显示出来，需要滑动才能找到
            首先尝试点击控件，找不到后滑动屏幕
        """

        i = 1
        while i <= 3:
            try:
                logger.info("尝试第%i次点击帮助中心,id：%s，如有Error请忽略" % (i, FAQ_id))
                ElementAction(self.driver).find_element('id', FAQ_id).click()
                break
            except:
                i = i + 1
                ElementAction(self.driver).swipe_to_up()

        FAQ_page_title = self.data.getValue('FAQ_page', 'FAQ_page_title')
        FAQ_page_title_id = self.data.getValue('FAQ_page', 'FAQ_page_title_id')

        FAQ_page_title_text = ElementAction(self.driver).find_element("id", FAQ_page_title_id).text

        logger.info("身份证打印界面的标题为：%s" % FAQ_page_title_text)
        ElementAction(self.driver).back()
        self.assertEqual(FAQ_page_title, FAQ_page_title_text)


    def test_09enter_ink(self):
        """
            ink_id:首页购买墨水的id
            ink_page_title:墨水购买页面的标题
            ink_page_title_id：墨水购买页面标题的id
            ink_page_title_text：读取APP中墨水购买页面的标题
        :return:
        """
        logger.info("进入墨水购买界面")
        ink_id = self.data.getValue('home_page', 'ink_id')

        """
            控件在有些手机不能显示出来，需要滑动才能找到
            首先尝试点击控件，找不到后滑动屏幕
        """
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

        time.sleep(20)  # 页面加载时间过长,可以再调整
        ink_page_title_text = ElementAction(self.driver).find_element("id", ink_page_title_id).text

        logger.info("身份证打印界面的标题为：%s" % ink_page_title_text)
        ElementAction(self.driver).back()
        self.assertEqual(ink_page_title, ink_page_title_text)

    def test_10enter_paper(self):
        """
            paper_id：首页购买纸张的id
            is_toast_exist()：点击会弹出toast，需要根据toast的内容来定位toast
        :return:
        """
        logger.info("点击购买纸张")
        paper_id = self.data.getValue('home_page', 'paper_id')
        toast_title = self.data.getValue('toast', 'toast_title')

        """
            控件在有些手机不能显示出来，需要滑动才能找到
            首先尝试点击控件，找不到后滑动屏幕
        """
        i = 1
        while i <= 3:
            try:
                logger.info("尝试第%i次点击身份证打印 ,id：%s，如有Error请忽略" % (i, paper_id))
                ElementAction(self.driver).find_element('id', paper_id).click()
                break
            except:
                i = i + 1
                ElementAction(self.driver).swipe_to_up()
        chkTag = True
        ele = ElementAction(self.driver).is_toast_exist(toast_title)
        if not ele:
            chkTag = False
            logger.error("未找到toast：%s" % toast_title)
        else:
            if toast_title != ele.text:
                chkTag = False
                logger.error("Toast标题错误：%s" % ele.text)

        self.assertEqual(chkTag, True)

    def test_Home_Page_text(self):
        pass
