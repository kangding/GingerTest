import os
import subprocess
import socket
import time

from appium import webdriver
from config.config_reader import configReader as cr
from common.log import logger


def start_appium(host, port):
    """
    启动appium服务
    :param host:
    :param port:
    :return:
    """
    errormessage = ""
    appium_server_url = ""
    # 指定bp端口号
    bootstrap_port = str(port + 1)
    try:
        if check_port(host, port):
            # 把在cmd弹窗输入的命令，直接写到这里
            cmd = 'start /b appium -a ' + host + ' -p ' + str(port) + ' -bp ' + str(bootstrap_port)
            # 去掉 “/b”，即可以打开cmd弹窗运行
            # cmd = 'start  appium -a ' + host+' -p '+str(port) +' -bp '+ str(bootstrap_port)
            # 打印输入的cmd命令，及时间
            print("%s at %s " % (cmd, time.ctime()))

            project_path = os.path.dirname(os.path.dirname(__file__))
            ss_path = project_path.split('common')[0] + '\\log'
            ss_name = os.path.join(ss_path, '{0}.log'.format('appium' + str(port) + time.strftime('%Y%m%d-%H%M%S')))

            p = subprocess.Popen(cmd, shell=True, stdout=open(ss_name, 'a'), stderr=subprocess.STDOUT)
            p.wait()

            appium_server_url = 'http://' + host + ':' + str(port) + '/wd/hub'
            print(appium_server_url)
    except Exception as msg:
        errormessage = str(msg)

    return appium_server_url, errormessage

def check_port(host, port):
    """
    检测appium端口是否被占用
    :param host:
    :param port:
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, int(port)))
        s.shutdown(2)
        print('port %s is used!' % port)
        return False
    except:
        print('port %s is available!' % port)
        return True


def connect_mobile():
    appium_data = cr('config.ini')
    desired_caps = appium_data.getSections('appium')
    appium_url = appium_data.getValue('appium_url', 'url')

    print('appium_url', appium_url)

    # print(type(desired_caps))
    for i in desired_caps:
        print('desired_caps', i, desired_caps[i])

    driver = webdriver.Remote(appium_url, desired_caps)  # 连接Appium
    driver.implicitly_wait(5)
    return driver


if __name__ == '__main__':
    host = "127.0.0.1"
    port = 4723
    start_appium('127.0.0.1', 4723)
    time.sleep(3)
    print("branch test")
