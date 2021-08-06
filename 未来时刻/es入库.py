#chinese_ministry_of_justice
import requests
from elasticsearch import Elasticsearch
import urllib
from lxml import html
import time
import json
import re
import base64
start = time.time()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.49"
}
url = "http://www.moj.gov.cn/pub/sfbgw/zwxxgk/fdzdgknr/fdzdgknrtzwj/202104/t20210402_351371.html"
ywgjc = ["political"]
zwgjc = ["政治"]       #文章中文和英文关键词

response = requests.get(url=url, headers=headers)
response.encoding = "utf-8"
pages_text = response.text
etree = html.etree
tree = etree.HTML(pages_text)

date1 = tree.xpath('//*[@id="xxgkzt_7"]/div/div[2]/p/text()')
date4 = '_'.join(date1)
date5 = str(date4).replace("年", "-").replace("月", "-").replace("日", "").replace("/", "-").strip()
date3 = re.findall('\d{4}-\d{2}-\d{2}', str(date5))
date6 = ''.join(date3)
timeArray = time.strptime(date6, "%Y-%m-%d") #数据转化
date7 = int(time.mktime(timeArray)) #  时间转换成时间戳
date=str(date7)
print(date)

keys = base64.b64encode(url.encode("utf8")) #主键加密 保护服务器
key = str(keys, encoding="utf8")#     -------------------------------------------------------------主键key
#
headline1 = tree.xpath('//*[@id="xxgkzt_7"]/div/div[2]/h1/text()')
headline2 = tree.xpath('/html/body/div/div[3]/div[1]/h1/text()[2]')
headlines = headline1+headline2#  --------------------------标题----headline
headline=''.join(headlines)
print(headline)

content1 = tree.xpath('//p[@align="justify"]//text()')
content2 = tree.xpath('//*[@id="xxgkzt_7"]/div/div/div/p/text()')
content3 = tree.xpath('/html/body/div/div[3]/div[2]/div[1]/div[1]/div/div/div/p/text()')
content4 = tree.xpath('/html/body/div/div[3]/div[2]/div[1]/div[1]/p/text()')
contents = content1 + content2 +content3 +content4   # 文章内容
#
content = []
for x in contents:
    content.append(x.replace(u'\u2002',u'').replace(u'\xa0', u'').replace(u'\u3000', u'').replace(u'\n', u'').replace(u'\r', u''))
print(content)
fujian = tree.xpath('//*[@style="display:none;"]/a/@href')  #时间

Website_ID = '网站标识码bm13000002' #------------------------------------------网站标识码--Website_ID
Internet_Content_Provider = 'ICP备案编号：京ICP备13016994号-2' #----------------ip备案号—-Internet Content Provider
Network_security_record_number = '京公网安备11010502035627号'#网络安全备案号---Network security record number
All_rights_reserved  = '版权所有：中华人民共和国司法部' #----------------------版权所有---All rights reserved
accessory = ''  #--------------------------------------------------------------附件--accessory

data1={

    #http://121.4.210.49:80/chinese_ministry_of_justice/_doc/
    #表名加时间
    "hash": "chinese_ministry_of_justice"+str(date),
    "range": key,#主键（加密且唯一）
    "index": "chinese_ministry_of_justice",#表名

    "headline":headline,#标题
    "datestamp":date,#时间
    "content": content,#内容
    "Website_ID":Website_ID,#网站标识码
    "Internet_Content_Provider":Internet_Content_Provider,#ip备案号
    "Network_security_record_number":Network_security_record_number,#网安备案号
    "All_rights_reserved":All_rights_reserved,#版权所有
    "accessory":[],#附件
    "key_words":ywgjc,
    "zh_hans_keyword":zwgjc,
    "The_media":{
        "jpg":[],
        "mp4":[],
        "mp3":[],
    }
}

data = str(data1).replace("'",'"')  #数据处理
es = Elasticsearch(hosts="http://121.4.210.49", port=80) #服务器地址
es.indices.create(index="chinese_ministry_of_justice", ignore=400)  #数据库地址
res = es.index(index="chinese_ministry_of_justice", doc_type="_doc", id=key, body=data) #数据入库
print(res)