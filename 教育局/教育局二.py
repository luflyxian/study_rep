import requests
from lxml import html
import time
import pymysql
import base64
import urllib

start = time.time()
for i in range(1,11):
    url_start = "http://www.moe.gov.cn/was5/web/search?channelid=254874&chnlid=2147438998&page="+str(i)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.49"
    }
    params = {"sn": "a14062711010650606ss9p000000", "size": "0"}
    response = requests.get(url=url_start, params=params, headers=headers)
    response.encoding = "utf-8"
    pages_text = response.text
    etree = html.etree
    tree = etree.HTML(pages_text)
    shijian = tree.xpath('/html/body/li[1]/span/text()')
    xd_url = tree.xpath('/html/body/li/a/@href')
    for i in xd_url:
        url_one = "http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/"
        url = urllib.parse.urljoin(url_one, i)
        response = requests.get(url=url, params=params, headers=headers)
        response.encoding = "utf-8"
        pages_text = response.text
        etree = html.etree
        tree = etree.HTML(pages_text)
        zhuti1= tree.xpath('//*[@id="moe-detail-box"]/h1/text()')
        zhuti2=tree.xpath('//*[@id="moe-detail-box"]/h2/text()')
        zhuti=zhuti1+zhuti2 #标题
        neirong1 = tree.xpath('//*[@id="moe-detail-box"]/div[2]//text()')#内容
        banquansouyou1=tree.xpath('/html/body/div[3]/div/div[2]/p[1]/text()')
        banquansouyou = []
        for x in banquansouyou1:
            banquansouyou.append(x.replace(u'\u3000', u' ').replace(u'\xa0', u' '))
        icp=tree.xpath('/html/body/div[3]/div/div[2]/p[2]/a[1]/text()')
        jinggongwanganbei=tree.xpath('//*[@id="moe_gonganbeian"]/text()')
        wangzhanbiaoshi=tree.xpath('/html/body/div[3]/div/div[2]/p[2]/span/text()')
        keys = base64.b64encode(url.encode("utf8"))
        key = str(keys, encoding="utf8")
        nr = []
        for x in neirong1:
            nr.append(x.replace(u'\u3000', u' ').replace(u'\xa0', u' '))
        neirong1 = [x.strip() for x in nr if x.strip() != '']
        neirong = [neirong5 + "\n" for neirong5 in neirong1]
        sj=[]
        for x in shijian:
            sj.append(x.replace(u'\u3000', u' ').replace(u'\xa0', u' '))
        shijian = [x.strip() for x in sj if x.strip() != '']
        # print(key)
        # print(zhuti)
        # print(shijian)
        # print(neirong)
        # print(banquansouyou)
        # print(wangzhanbiaoshi)
        # print(icp)
        # print(jinggongwanganbei)
        # connect = pymysql.Connect(host='localhost', port=3306, user="root", passwd="1842505833", db="XCX",
        #                           charset='utf8')
        # cursor = connect.cursor()
        # sql = 'INSERT ignore INTO jiaoyu(zt,sj,nr,bqsy,icp,jgwab,wzbs)VALUES("' + str(zhuti) + '","' + str(shijian) + '","' + str(neirong1) + '","' + str(banquansouyou) + '","' + str(icp) + '","' + str(jinggongwanganbei) + '","' + str(wangzhanbiaoshi) + '")'
        # cursor.execute(sql)
        # connect.commit()
        # connect.close()
print(f"一共花费{time.time() - start}")




