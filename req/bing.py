# -*- coding: UTF-8 -*-
import requests

s = requests.Session()


class Dict:
	def __init__(self):
		self.headers = {
			'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
			'content-type': "application/json; charset=UTF-8",
			# 'referer': "http://www.bing.com/translator/?mkt=zh-CN",  # 可有可没有
		}
		self.url = 'http://www.bing.com/translator/api/Translate/TranslateArray?from=zh-CHS&to=ko'
		# self.url = 'http://www.bing.com/translator/api/Translate/TranslateArray?from=ko&to=zh-CHS'
		self.base_config()

	def base_config(self):
		s.get('http://www.bing.com/translator/')

	def translate(self, line):
		payload = "[{\"id\":652829,\"text\":\"%s\"}]" % line
		try:
			resp = s.post(self.url, headers=self.headers, data=payload.encode('utf-8')).json()
			items = resp.get('items', [])
			if not items:
				return
			trans = items[0].get('text')
			return trans
		except Exception as e:
			print(e)
			return None


if __name__ == '__main__':
	dic = Dict()
	with open('./source/oral1600.zh', 'r') as f:
		with open('./result/oral1600-bing.ko', 'w') as f1:
			for i, line in enumerate(f.readlines()):
				# if i < 279:
				# 	continue
				if line == '\n':
					f1.write(line)
					continue
				print(str(i + 1), line)
				line = line.replace('\n', '').replace('\r', '').replace('"', '\'')
				t_line = dic.translate(line)
				while not t_line:
					t_line = dic.translate(line)
					print('again...')
				f1.write(t_line + '\n')
