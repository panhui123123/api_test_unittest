# coding:utf-8
import requests
import urllib3
from base.base_log import Log
import json
from requests_toolbelt import MultipartEncoder
from pprint import pprint


# 封装http请求
class HttpRequest:
    # 为了以防万一，在访问url的时候选择忽略访问的警告信息
    def __init__(self):
        urllib3.disable_warnings()

    # 由于某些接口返回的是文本类型的数据（虽然这种接口很少），这里需要对接口返回的是否是json串进行一个简单的判断
    def is_json(self, my_json):
        try:
            json_object = json.loads(my_json)
        except ValueError as e:
            return False
        return True

    def http_request(self, method, url, data=None, headers=None):
        '''
        :param method: 方法，这个必传
        :param url: url，必传
        :param data: 默认为空
        :param headers: 默认为空
        :return:
        '''
        res = None
        # 如果method是get请求，这里只用传url就行
        if method.lower() == 'get':
            try:
                res = requests.get(url=url, params=data)
            except Exception as e:
                Log().error('get请求出错！{}'.format(e))
        # 如果是post请求，则进行判断，请求头为application/json则直接用json.dumps转化参数data的类型，如果请求头类型不是这个则用
        # MultipartEncoder处理
        elif method.lower() == 'post':
            try:
                headers = eval(headers)
                data = eval(data)
            except Exception as e:
                Log().error('转换headers、data出错{}'.format(e))
            try:
                if headers == {'Content-Type':'application/json'}:
                    res = requests.post(url=url, data=json.dumps(data), headers=headers)
                else:
                    data = MultipartEncoder(fields=data)
                    res = requests.post(url=url, data=data, headers={'Content-Type': data.content_type})
            except Exception as e:
                Log().error('post请求出错{}'.format(e))
        return res

    def get_http_request_response(self, res):
        # 如果返回的是json串那就返回json串，如果不是那就返回文本
        return res.json() if self.is_json(res.text) else res.text


if __name__ == '__main__':
    Request = HttpRequest()
    # a = Request.http_request(method='Post', url='http://139.224.2.208:8020/chest_api/get_high_lucky_reward',
    #                          data={
    #                                 'type': '1',
    #                                 'currency_type': '2',
    #                                 'uid': 'ce9089d4-f7f5-4e2c-8414-7690cddc4eeb',
    #                                 'sid': '72b987b5c7fb238d0c96764de33dc8c0',
    #                                 'platform': '1',
    #                                 'game_version': '1.0',
    #                                 'version': '5.1.13',
    #                                 'market': 'apple',
    #                                 'device_id': '2D72959A-2D04-4178-9AF2-B5E84C7C6830-46536-000007F98392DEB1',
    #                                 'snake_sign': 'QxzFbc6AEwTMeywZjrSP9v1qg8o='
    #                                 })
    b = Request.http_request(method='get', url='https://www.baidu.com')
    print(Request.get_http_request_response(b))



