import requests
from lxml import html
import time
import pymysql
import base64
import urllib

start = time.time()
for i in range(1,22):
    url_start = "http://www.moe.gov.cn/jyb_xwfb/s271/index_"+str(i)+".html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.49"
    }
    params = {"sn": "a14062711010650606ss9p000000", "size": "0"}
    response = requests.get(url=url_start, params=params, headers=headers)
    response.encoding = "utf-8"
    pages_text = response.text
    etree = html.etree
    tree = etree.HTML(pages_text)
    td_xpath = tree.xpath('//*[@id="list"]/li//@href')
    # print(url_start)
    # print(td_xpath)
    for i in td_xpath:
        url_one = "http://www.moe.gov.cn/jyb_xwfb/s271/"
        url = urllib.parse.urljoin(url_one, i)  # ---------------------------------------url
        response = requests.get(url=url, params=params, headers=headers)
        response.encoding = "utf-8"
        pages_text = response.text
        etree = html.etree
        tree = etree.HTML(pages_text)
        zhuti1 = tree.xpath('//*[@id="moe-detail-box"]/h1/text()')
        zhuti2 = tree.xpath('//*[@id="moe-detail-box"]/h2/text()')
        zhuti=zhuti1+zhuti2
        shijian=tree.xpath('//*[@id="moe-detail-box"]/div[1]/text()')
        # neirong1 = tree.xpath('//*[@id="moe-detail-box"]/div[2]//text()')
        neirong1 = tree.xpath('//*[@id="moe-detail-box"]/p/text()')
        neirong2 = tree.xpath('//*[@id="moe-detail-box"]/div[2]//text()')
        neirong = neirong1 + neirong2
        banquansuoyou=tree.xpath('/html/body/div[3]/div/div[2]/p[1]/text()')
        icp=tree.xpath('/html/body/div[3]/div/div[2]/p[2]/a[1]/text()')
        jinggongwanganbei=tree.xpath('//*[@id="moe_gonganbeian"]/text()')
        wangzhanbiaoshi=tree.xpath('/html/body/div[3]/div/div[2]/p[2]/span/text()')
        sj = []
        for x in shijian:
            sj.append(x.replace(u'\u3000', u' ').replace(u'\xa0', u' '))
        shijian = [x.strip() for x in sj if x.strip() != '']
        nr = []
        for x in neirong:
            nr.append(x.replace(u'\u3000', u' ').replace(u'\xa0', u' '))
        neirong = [x.strip() for x in nr if x.strip() != '']
        bqsy = []
        for x in banquansuoyou:
            bqsy.append(x.replace(u'\u3000', u' ').replace(u'\xa0', u' '))
        banquansuoyou = [x.strip() for x in bqsy if x.strip() != '']

        print(zhuti)
        print(shijian)
        print(neirong)
        print(banquansuoyou)
        print(icp)
        print(jinggongwanganbei)
        print(wangzhanbiaoshi)
        # connect = pymysql.Connect(host='localhost', port=3306, user="root", passwd="1842505833", db="XCX",charset='utf8')
        # cursor = connect.cursor()
        # sql = 'INSERT ignore INTO jiaoyuzhengce(zt,sj,nr,bqsy,icp,jgwab,wzbs)VALUES("' + str(zhuti) + '","' + str(shijian) + '","' + str(neirong) + '","' + str(banquansuoyou) + '","' + str(icp) + '","' + str(jinggongwanganbei) + '","' + str(wangzhanbiaoshi) + '")'
        # cursor.execute(sql)
        # connect.commit()
        # connect.close()

