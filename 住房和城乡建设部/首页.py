import requests
import pymysql
import urllib
from lxml import html
import time
import re
import base64
start = time.time()
url_start = "http://www.mohurd.gov.cn/wjfb/index_5.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.49"
}
params = {"sn": "a14062711010650606ss9p000000", "size": "0"}
response = requests.get(url=url_start, params=params, headers=headers)
response.encoding = "utf-8"
pages_text = response.text
etree = html.etree
tree = etree.HTML(pages_text)
td_xpath=tree.xpath('//td[@style="text-align:left;"]/a/@href')
for i in td_xpath:
    try:
        url_one = "http://www.scio.gov.cn/xwfbh/gssxwfbh/xwfbh/jiangxi/"
        url = urllib.parse.urljoin(url_one, i)  # ---------------------------------------url
        response = requests.get(url=url, params=params, headers=headers)
        response.encoding = "utf-8"
        pages_text = response.text
        etree = html.etree
        tree = etree.HTML(pages_text)
        biaoti1 = tree.xpath('//tr[@align="center"]/td/text()')
        biaoti3 = tree.xpath('//h2[@class="title"]/text()')
        biaoti4 = biaoti1 + biaoti3
        biaoti2 = []
        for x in biaoti4:
            biaoti2.append(x.replace(u'>', u'').replace(u' ', u'\n').replace(u'\n', u'').replace(u'\t', u''))
        biaoti = ''.join(biaoti2)

        nr1 = tree.xpath("//div[@class='union']/p/text()")
        nr2 = tree.xpath("//td[@style='text-align: center']/text()")
        nr = nr1 + nr2

        neirong = []
        for x in nr:
            neirong.append(x.replace(u'\u3000', u'').replace(u'\r', u'\n').replace(u'\xa0', u'').replace(u'\n', u''))

        nr12 = str(neirong).replace("年", "-").replace("月", "-").replace("日", "").replace("/", "-").strip()
        date3 = re.findall('\d{4}-\d{1,2}-\d{1,2}', str(nr12))
        shijian1=tree.xpath('//*[@class="tdleft"]/text()')
        shijian = str(shijian1).replace("年", "-").replace("月", "-").replace("日", "").replace("/", "-").strip()
        date2 = re.findall('\d{4}-\d{1,2}-\d{1,2}', str(shijian))
        date4 = ''.join(date2)
        time1 = date3[-1]
        # print(date3)

        # date5 = tree.xpath("//div[@class='info']/text()")
        # date6 = re.findall('\d{4}-\d{1,2}-\d{1,2}', str(date5))
        # date7 = ''.join(date6)
        # time = str(time1) + str(date7)
        # print(url)
        # print(time1)

        fujian1 = tree.xpath("//td[@width='730px']/a/@href")
        fujian=[]
        for i in fujian1:
            url_one = "http://www.mohurd.gov.cn/"
            fujian2 = urllib.parse.urljoin(url_one, i)
            fujian.append(fujian2.replace(u'\u3000', u''))
        chengbandanwei = "承办单位：住房和城乡建设部信息中心"
        dizhi = "地　　址：北京市海淀区三里河路9号"
        youxiang = "邮　　编：100835"
        wangzhanbiaoshima = "网站标识码：bm18000002"
        ipbeianhao = "备案编号：京ICP10036469号"
        banquansuoyou = "版权所有：中华人民共和国住房和城乡建设部"
        print(time1)
        print(biaoti)
        print(neirong)
        print(fujian)
    except:
        pass











# connect = pymysql.Connect(host='localhost', port=3306, user="root", passwd="mima123456",
#                           db="guojiazhengce",
#                           charset='utf8')
# cursor = connect.cursor()
# sql = 'INSERT ignore INTO gjzcb(`Key`,`Suoyinhao`,`Zhutifenlei`,`Fawenjiguan`,`Chengwenriqi`,`Biaoti`,`Fawenzihao`,`Faburiqi`,`Neirong`,`Wzbsm`,`Ipbeianhao`,`Beianhao`)VALUES("' + str(key) + '","' + str(
#     suoyinhao) + '","' + str(
#     zhutifenlei) + '","' + str(fawenjiguan) + '","' + str(chengwenriqi) + '","' + str(biaoti) + '","' + str(
#     fawenzihao) + '","' + str(faburiqi) + '","' + str(neirong) + '","' + str(
#     wangzhanbiaoshima) + '","' + str(ipbeianhao) + '","' + str(beianhao) + '")'
# cursor.execute(sql)
# connect.commit()
# connect.close()