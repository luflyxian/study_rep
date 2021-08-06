import requests
import pymysql
import urllib
from lxml import html
import time
import re
import base64
start = time.time()
url_start = "https://www.ndrc.gov.cn/xwdt/tzgg/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.49",
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
}
params = {"sn": "a14062711010650606ss9p000000", "size": "0"}
response = requests.get(url=url_start, params=params, headers=headers)
response.encoding = "utf-8"
pages_text = response.text
etree = html.etree
tree = etree.HTML(pages_text)
td_xpath = tree.xpath('/html/body/div[2]/div[2]/ul/li/a/@href')
biaoti1 = tree.xpath('/html/body/div[2]/div[2]/ul/li/a/text()')
faburiqi1 = tree.xpath('/html/body/div[2]/div[2]/ul/li/span/text()')
for i,biaoti,faburiqis in zip(td_xpath,biaoti1,faburiqi1):
    try:
        url_one = "https://www.ndrc.gov.cn/xwdt/tzgg/"
        url = urllib.parse.urljoin(url_one, i)  # ---------------------------------------url
        response = requests.get(url=url, params=params, headers=headers)
        response.encoding = "utf-8"
        pages_text = response.text
        etree = html.etree
        tree = etree.HTML(pages_text)

        neirong1 = tree.xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div/span/text()")
        neirong2 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div/span/text()')
        neirong3 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div/p/text()')
        neirong4 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p/text()')
        neirong5 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div/p/span/text()')
        neirongs = neirong1 + neirong2+neirong3+neirong4+neirong5

        neirongss = []
        for x in neirongs:
            neirongss.append(x.replace(u'\u3000', u' ').replace(u'\xa0', u' ').replace(u'\n', u' ').replace(u'\r', u' ').replace(u'\u2003', u' '))

        time4 = str(faburiqis).replace("年", "-").replace("月", "-").replace("日", "").replace("/", "-").strip()
        faburiqi= re.findall('\d{4}-\d{2}-\d{2}', str(time4))

        # biaoti1 = tree.xpath('/html/body/div[2]/div[2]/div[1]/h2/text()')
        # biaoti2 = tree.xpath('//table[@style="width:860px;margin:0 auto;margin-top:12px;"]/tbody/tr[3]/td[2]/text()')
        # biaoti3 = tree.xpath('//table[@style="width:660px;margin:0 auto;margin-top:12px;"]/tbody/tr[3]/td[2]/text()')
        # biaoti4 = biaoti3 + biaoti2 + biaoti1
        # biaoti = [x.strip() for x in biaoti4 if x.strip() != '']


        fawenzihao1 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/span[3]/div/text()')
        fawenzihao2 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/span[2]/div/text()')
        fawenzihao3 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div/span[1]/div/text()')
        fawenzihao = fawenzihao1 +fawenzihao2+fawenzihao3

        fujians = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[3]/div[2]/p/a/@href')
        fujianss = []
        for i in fujians:
            fujian0= urllib.parse.urljoin(url, i)
            fujianss.append(fujian0.replace(u'\u3000', u''))
        # print(fawenzihao)

        if len(fujianss)!= 0:
            fujian = set(fujianss)
            jpg1 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div/p[8]/img/@src')
            jpg2 = tree.xpath('/html/body/div[2]/div[2]/div/div/p/span/img/@src')
            jpgss = jpg1 + jpg2
            jpgs = []
            for x in jpgss:
                jpgs0 = urllib.parse.urljoin(url, x)
                jpgs.append(jpgs0.replace(u'\u2002', u'').replace(u'\xa0', u'').replace(u'\u200b', u'').replace(u'\n', u'').replace(u'\r', u'').replace(u'\t', u''))

            suoyinhao=[]
            zhutifenlei = []
            chengwenriqi = []
            gongwenzhonglei = '通知通告'
            fwzh = []
            zhutici=[]
            fawenjiguan='中华人民共和国国家发展和改革委员会'
            zhengcelaiyuan='国家发展和改革委员会'
            shenxiaorq=[]
            shixiaorq=[]

            neirong = ''.join(neirongss)
            connect = pymysql.Connect(host='192.168.31.210', port=1433, user="root", passwd="mima123456",
                                      db="policy",
                                      charset='utf8')
            cursor = connect.cursor()
            sql = 'INSERT ignore INTO fagaiwei(`urls`,`syh`,`ztfl`,`fwjg`,`gwzl`,`cwrq`,`bt`,`fbrq`,`ztc`,`nr`,`fj`,`zcly`,`shen_rq`,`shix_rq`,`jpg`)VALUES("' + str(url) + '","' + str(suoyinhao) + '","' + str(zhutifenlei) + '","' + str(fawenjiguan) + '","' + str(gongwenzhonglei) + '","' + str(chengwenriqi) + '","' \
                  + str(biaoti) + '","' + str(faburiqi) + '","' + str(zhutici) + '","' + str(neirong) + '","' + str(
                fujian) + '","' + str(zhengcelaiyuan) + '","' + str(shenxiaorq) + '","' + str(shixiaorq) + '","' + str(jpgs) + '")'
            cursor.execute(sql)
            # sql = "truncate fagaiwei"
            # cursor.execute(sql)
            connect.commit()
            connect.close()
        else:
            pass
    except:
        pass
