# _*_ coding=utf-8 _*_

import configparser
import os


class configReader(configparser.ConfigParser):
    """
    读取配置文件
    """

    def __init__(self, filename):
        configparser.ConfigParser.__init__(self, defaults=None)
        config_path = os.path.dirname(os.path.realpath(__file__))
        config_file = os.path.join(config_path, filename)
        print("config_file, ", config_file)
        self.read(config_file, encoding="UTF-8")

    def getValue(self, section, option):
        return self.get(section, option)

    def getSections(self, sections):
        return dict(self.items(sections))

    """重写optionform，不要返回小写"""
    def optionxform(self, optionstr):
        return optionstr

if __name__ == '__main__':
    pass
    test_Config = configReader('element_config.ini')

    test_options1 = test_Config.getVaule('print_document', 'print_document_type1')
    test_options2 = test_Config.getVaule('print_document', 'print_document_type2')
    test_options3 = test_Config.getVaule('print_photo', 'photo_type1')
    print("test_options2, ", test_options2)
    print("test_options1, ", test_options1)
    print("test_options3, ", test_options3)
