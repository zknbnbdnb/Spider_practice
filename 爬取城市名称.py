import requests
import json
from lxml import etree
import os

# 爬取城市名称

'''if __name__ == '__main__':
    url = 'https://www.aqistudy.cn/historydata/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    page = response.text
    tree = etree.HTML(page)
    List1 = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    all_city=[]
    for li in List1:
        city = li.xpath('./a/text()')[0]
        all_city.append(city)
    print(all_city)
    print(len(all_city))'''