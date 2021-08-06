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
    shengdaima1 = tree.xpath('/html/body/div[2]/div/h4/text()') #省代码
    shidaima1=tree.xpath('/html/body/div[2]/div/ul/li/h5/text()')#市代码
    xiandaima1 = tree.xpath('/html/body/div[2]/div/ul/li/ul/li/text()')#县代码

    shengdaima = re.findall("(?<=')[\u4E00-\u9FA5A-Za-z0-9]+", str(shengdaima1))

    sdm1 = re.findall("\d+",str(shengdaima1))  # 输出结果为列表

    shidaima = re.findall("(?<=')[\u4E00-\u9FA5A-Za-z0-9]+", str(shidaima1))

    sdm2 = re.findall("\d+",str(shidaima1))  # 输出结果为列表


    xiandaima = re.findall("(?<=')[\u4E00-\u9FA5A-Za-z0-9]+", str(xiandaima1))

    xdm = re.findall("\d+",str(xiandaima1))  # 输出结果为列表

    connect = pymysql.Connect(host='localhost', port=3306, user="root", passwd="mima123456",
                              db="policy",
                              charset='utf8')
    cursor = connect.cursor()
    sql = 'INSERT ignore INTO area_code(`Province`,`Province_code`,`City`,`City_code`,`County`,`County_code`)VALUES' \
          '("' + str(shengdaima) + '","' + str(sdm1) + '","' + str(shidaima) + '","' + str(sdm2) + '","' +\
          str(xiandaima) + '","' + str(xdm) + '")'
    cursor.execute(sql)
    connect.commit()
    connect.close()

if __name__ == "__main__":
    start = time.time()#----------------------------------------------------------获取当前时间戳
    url = "http://www.ip33.com/area_code.html"#----------------------目标网址
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.49"
    } #-----------------------------------------------------------------------设置浏览器请求头，防止一来就被发现是爬虫
    params = {"sn": "a14062711010650606ss9p000000", "size": "0"}#---------------------------网页对应参数
    get_first_url(url,params,headers)