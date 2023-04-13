import requests
import json
from lxml import etree
import os

from hashlib import md5


class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php',
                          data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post(
            'http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


if __name__ == '__main__':
    session = requests.Session()
    headers = {
        # 请求头
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'  # 指定url
    page = session.get(url=url, headers=headers).text  # 获取网页原码
    tree = etree.HTML(page)  # 创建etree对象
    img_src = 'https://so.gushiwen.cn/' + tree.xpath('//*[@id="imgCode"]/@src')[0]  # 对网页进行xpath分析拿到验证码图片位置
    img = session.get(url=img_src, headers=headers).content  # 将图片以二进制形式保存
    with open('./a.jpg', 'wb')as fp:  # 写入文件夹
        fp.write(img)
    __VIEWSTATE = tree.xpath('//input[@id="__VIEWSTATE"]/@value')[0]
    __VIEWSTATEGENERATOR = tree.xpath(
    '//input[@id="__VIEWSTATEGENERATOR"]/@value')[0]
    # 使用超级鹰识别验证码
    chaojiying = Chaojiying_Client('zknbnbdnb', 'zknbnbdnb123.', '914930')
    im = (open('./a.jpg', 'rb').read())
    result = chaojiying.PostPic(im, 1902)['pic_str']
    print(result)
    # 登进去是post请求
    
    login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'  # post的url
    data = {
        '__VIEWSTATE': __VIEWSTATE,  # post的参数
        '__VIEWSTATEGENERATOR': __VIEWSTATE,              #?为什么要写这个动态数据，不解析无法获取，输入value都一样
        'from': 'http://so.gushiwen.cn/user/collect.aspx',
        'email': '19879830250',
        'pwd': '102030zk',
        'code': result,
        'denglu': '登录',
    }
    response = session.post(url=login_url, data=data,
                            headers=headers)  # 发起post请求模拟登陆
    page_text=response.text
    print(response.status_code)  # 看是不是200
    with open('gsw.html', 'w', encoding='utf-8')as fp:
        fp.write(page_text)
    

