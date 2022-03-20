import os
import unittest
from HTMLTestRunnerNew import HTMLTestRunner


def run_all_case():
    # 当前脚本路径
    cur_path = os.path.dirname(os.path.realpath(__file__))
    # 测试用例路径
    case_path = os.path.join(cur_path, 'testcase')
    # 测试报告路径
    report_path = os.path.join(cur_path, 'report', 'report.html')
    # 测试用例匹配规则
    test_rule = 'test_*.py'
    # 使用discover方式收集
    discover = unittest.defaultTestLoader.discover(case_path, pattern=test_rule)
    # 运行
    fp = open(report_path, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        verbosity=2,
        title='测试报告',
        description='接口测试',
        tester='辉哥'
    )
    # 报告
    runner.run(discover)
    fp.close()


if __name__ == '__main__':
    run_all_case()