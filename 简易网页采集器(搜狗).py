import requests
import json
from lxml import etree
import os
# 简易网页采集器(搜狗)
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    url = 'http://www.sogou.com/web'
    keyword = input('enter a word: ')
    params = {
        'query': keyword
    }
    response = requests.get(url=url, headers=headers, params=params)
    page_text = response.text
    filename = keyword+'.html'
    with open(filename, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(filename, '保存成功')