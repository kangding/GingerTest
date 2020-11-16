from common.log import logger
import time
import unittest

from common.appium_start import connect_mobile
from common.element_action import ElementAction
from config.config_reader import configReader


class printDoc(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = connect_mobile()
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

    def test_0001enter_docPrint(self):
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

    def test_0002choose_doc(self):
        """"""
        logger.info("选择一个文档")
        """
            读取element_config.ini中home_page一项，获取docPrint_id，docPrint_page，docPrint_page_title_id的值
        """
        # resource id
        otherDoc_id = self.data.getValue('docPrint_page', 'otherDoc_id')
        otherDoc_text = self.data.getValue('docPrint_page', 'otherDoc_text')

        i = 0

        for ele in ElementAction(self.driver).find_element("ids", otherDoc_id):
            if ElementAction(self.driver).find_element("ids", otherDoc_id)[i].text == otherDoc_text:
                ElementAction(self.driver).find_element("ids", otherDoc_id)[i].click()

                break
            else:
                i += 1

        logger.info('enter into 其他文档')
