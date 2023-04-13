import requests
import json
from lxml import etree
import os

# 豆瓣电影

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    url = 'https://movie.douban.com/j/chart/top_list'
    params = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',  # 从库中第几部电影开始取
        'limit': '20',  # 从库取多少个
    }
    response = requests.get(url=url, params=params, headers=headers)
    listObj = response.json()
    fp = open('./douban.json', 'w', encoding='utf-8')
    json.dump(listObj, fp=fp, ensure_ascii=False, indent=4)
    print('over')
