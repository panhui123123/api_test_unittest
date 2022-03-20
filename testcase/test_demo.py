import unittest
from ddt import ddt, data

from base.base_assertion import Assertion
from base.base_doExcel import DoExcel
from pprint import pprint

test_data_path = DoExcel('demo.xlsx', 'webtest')
test_demo_data = test_data_path.read_data()


@ddt
class TestDemo(unittest.TestCase):
    @data(*test_demo_data)
    def test_demo(self, test_dict):
        my_assertion = Assertion(test_dict, test_data_path)
        res = my_assertion.send_request()
        my_assertion.assert_result(res)


if __name__ == '__main__':
    unittest.main(verbosity=0)