import os
import unittest
from HTMLTestRunner import HTMLTestRunner
import time


def all_case():
    case_dir = os.path.join(os.getcwd(), "testcase")
    discover = unittest.defaultTestLoader.discover(case_dir, pattern="test*.py", top_level_dir=None)
    print(case_dir)
    print(discover)
    return discover


if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    # runner.run(all_case())
    all_case()
    # runner = unittest.TextTestRunner()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    report_path = r"\report"
    report_name = os.path.join(current_dir + r"\report", '{0}.html'.format(time.strftime('%Y%m%d-%H%M%S')))

    print(report_name)
    fp = open(report_name, "wb")

    # 使用HTMLTestRunner生成html报告，.py文件需要适配python3
    runner = HTMLTestRunner(stream=fp, title="报告生成", description="description")

    runner.run(all_case())
    fp.close()
    runner.run(all_case())
