import requests
import pymysql
import urllib
from lxml import html
import re
import time

def get_first_url(url,params,headers):
    response = requests.get(url=url, params=params, headers=headers)
    response.encoding = "utf-8"
    pages_text = response.text
    etree = html.etree
    tree = etree.HTML(pages_text)
    td_xpath = tree.xpath('//ul[@class="listTxt"]/li/h4/a/@href')
    ztc = tree.xpath('//ul[@class="listTxt"]/li/h4/a/text()')  # ----------------------主题词
    for i in td_xpath:
        response = requests.get(url=i)
        response.encoding = "utf-8"
        pages_text = response.text
        tree = etree.HTML(pages_text)
        syh = tree.xpath(r'//div[@class="wrap"]/table/tbody/tr/td/table/tbody/tr[1]/td[2]/text()')  # ----------------------索引号
        ztfl = tree.xpath('//div[@class="wrap"]/table/tbody/tr/td/table/tbody/tr[1]/td[4]/text()')
        fwjg = tree.xpath(r'//div[@class="wrap"]/table/tbody/tr/td/table/tbody/tr[2]/td[2]/text()')
        cwrq = tree.xpath(r'//div[@class="wrap"]/table/tbody/tr/td/table/tbody/tr[2]/td[4]/text()')
        bt = tree.xpath(r'//div[@class="wrap"]/table/tbody/tr/td/table/tbody/tr[3]/td[2]/text()')
        fwzh = tree.xpath(r'//div[@class="wrap"]/table/tbody/tr/td/table/tbody/tr[4]/td[2]/text()')
        fbrq = tree.xpath(r'//div[@class="wrap"]/table/tbody/tr/td/table/tbody/tr[4]/td[4]/text()')
        #print(ztfl)
        connect = pymysql.Connect(host='localhost', port=3306, user="root", passwd="mima123456", db="zyrmzf",
                                  charset='utf8')
        cursor = connect.cursor()
        # sql = r'INSERT ignore INTO zyrmzf_zhengce(`ZTC`,`URL`,`SYH`,`ZTFL`,`FWJG`,`CWRQ`,`BT`,`FWZH`,`FBRQ`)VALUES("' + str(
        #     ztc) + '","' + str(i) + '","' + str(syh) + '","' + str(ztfl) + '","' + str(fwjg) + '","' + str(cwrq) + '","' + str(bt) + '","' + str(fwzh) + '","' + str(fbrq) + '")'
        # cursor.execute(sql)
        sql = "truncate zyrmzf_zhengce"
        cursor.execute(sql)
        connect.commit()
        connect.close()
    print(f"一共花费{time.time() - start}")#-----------------------------获取当前时间戳，减去上次时间戳，获取所用时间


if __name__ == "__main__":
    start = time.time()#----------------------------------------------------------获取当前时间戳
    url = "http://sousuo.gov.cn/column/30469/0.htm"#----------------------目标网址
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.49"
    } #-----------------------------------------------------------------------设置浏览器请求头，防止一来就被发现是爬虫
    params = {"sn": "a14062711010650606ss9p000000", "size": "0"}#---------------------------网页对应参数
    get_first_url(url,params,headers)#-------------------------------------------------运行get_first_url函数



#//div[@class="wrap"]/table/tbody/tr/td/table/tbody/tr[1]/td[2]/text() 索引号3
#//div[@class="wrap"]/table/tbody/tr/td/table/tbody/tr[1]/td[4]/text() 主题分类4
#//div[@class="wrap"]/table/tbody/tr/td/table/tbody/tr[2]/td[2]/text() 发文机关5
#//div[@class="wrap"]/table/tbody/tr/td/table/tbody/tr[2]/td[4]/text() 发文日期6
#//div[@class="wrap"]/table/tbody/tr/td/table/tbody/tr[3]/td[2]/text() 标题7
#//div[@class="wrap"]/table/tbody/tr/td/table/tbody/tr[4]/td[2]/text() 发文字号8
#//div[@class="wrap"]/table/tbody/tr/td/table/tbody/tr[4]/td[4]/text() 发布日期9