# -*- coding: UTF-8 -*-
import hashlib
import random
import requests
import time

s = requests.Session()
m = hashlib.md5()


class Dict:
	def __init__(self):
		self.headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
			'Referer': 'http://fanyi.youdao.com/',
			'contentType': 'application/x-www-form-urlencoded; charset=UTF-8'
		}
		self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom='
		self.base_config()

	def base_config(self):
		"""
		设置基本的参数，cookie
		"""
		s.get('http://fanyi.youdao.com/')

	def translate(self):
		i = '中华人民共和国'
		salf = str(int(time.time() * 1000) + random.randint(0, 9))
		n = 'fanyideskweb' + i + salf + "aNPG!!u6sesA>hBAW1@(-"
		m.update(n.encode('utf-8'))
		sign = m.hexdigest()
		data = {
			'i': i,
			'from': 'AUTO',
			'to': 'AUTO',
			'smartresult': 'dict',
			'client': 'fanyideskweb',
			'salt': salf,
			'sign': sign,
			'doctype': 'json',
			'version': "2.1",
			'keyfrom': "fanyi.web",
			# 'action': "FY_BY_DEFAULT",
			'action': "FY_BY_CLICKBUTTION",
			'typoResult': 'false'
		}
		resp = s.post(self.url, headers=self.headers, data=data)
		print(resp.text)
		return resp.json()


dic = Dict()
resp = dic.translate()
print(resp)
