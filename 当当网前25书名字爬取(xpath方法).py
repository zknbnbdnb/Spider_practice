import requests
import json
from lxml import etree
import os



# 当当网前25书名字爬取(xpath方法)

'''if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-1'
    page = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page)
    divlist = tree.xpath('//ul[@class="bang_list clearfix bang_list_mode"]/li/div[@class="name"]')
    fp = open('58.txt', 'a', encoding='utf-8')
    for div in divlist:
        title = div.xpath('./a/text()')[0]
        print(title)
        fp.write(title+'\n')
    print('over') '''