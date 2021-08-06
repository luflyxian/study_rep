import requests
from lxml import html
import re
import time
import pymysql
import base64
import urllib
url_start = "https://www.miit.gov.cn/api-gateway/jpaas-publish-server/front/page/build/unit?webId=8d828e408d90447786ddbe128d495e9e&pageId=1b56e5adc362428299dfc3eb444fe23a&parseType=bulidstatic&pageType=column&tagId=%E5%8F%B3%E4%BE%A7%E5%86%85%E5%AE%B9&tplSetId=209741b2109044b5b7695700b2bec37e&paramJson=%7B%22pageNo%22%3A16%2C%22pageSize%22%3A%2224%22%7D"
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.49"
    }
params = {"sn": "a14062711010650606ss9p000000", "size": "0"}
response = requests.get(url=url_start, params=params, headers=headers)
response.encoding = "utf-8"
pages_text = response.text
etree = html.etree
tree = etree.HTML(pages_text)
#a=tree.xpath('//*[@id="右侧内容"]/div[1]/ul/li[1]/a//@href')
part = r'/zwgk/zcjd/art/2020/art_[A-Za-z0-9]*.html'
b = re.findall(part,pages_text)
# print(b)
for i in b:
    url_one = "https://www.miit.gov.cn"
    url = urllib.parse.urljoin(url_one, i)  # ---------------------------------------url
    response = requests.get(url=url, params=params, headers=headers)
    response.encoding = "utf-8"
    pages_text = response.text
    etree = html.etree
    tree = etree.HTML(pages_text)
    zhuti =  tree.xpath('//*[@class="ctitle"]/h1//text()')
    shijian = tree.xpath('//*[@id="con_time"]/text()')  # 时间
    neirong1 = tree.xpath('//*[@id="con_con"]/p//text()')
    neirong2 = tree.xpath('//*[@id="con_con"]//text()')
    neirong =neirong1+neirong2
    nr = []
    for x in neirong:
        nr.append(x.replace(u'\u3000', u' ').replace(u'\xa0', u' '))
    neirong = [x.strip() for x in nr if x.strip() != '']
    sj = []
    for x in shijian:
        sj.append(x.replace(u'\u3000', u' ').replace(u'\xa0', u' '))
    shijian = [x.strip() for x in sj if x.strip() != '']
    print(zhuti)
    print(shijian)
    print(neirong)
    # connect = pymysql.Connect(host='localhost', port=3306, user="root", passwd="1842505833", db="XCX",
    #                           charset='utf8')
    # cursor = connect.cursor()
    # sql = 'INSERT ignore INTO gongyexinxihuabu(zt,sj,`nr`)VALUES("' + str(zhuti) + '","' + str(shijian) + '","' + str(neirong) + '")'
    # cursor.execute(sql)
    # connect.commit()
    # connect.close()