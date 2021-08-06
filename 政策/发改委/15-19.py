import requests
import pymysql
import urllib
from lxml import html
import time
import re
import base64
start = time.time()
url_start = "https://www.ndrc.gov.cn/xwdt/tzgg/index_19.html"
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
        neirong3 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div/p//text()')
        neirong4 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p//text()')
        neirong5 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div/p/span/text()')
        neirong6 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p/span/text()')
        neirong7 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/span/text()')
        neirong8 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div/p[1]/span/text()')
        neirong9 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div/span/text()')
        neirong10 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/div/span/text()')
        neirong11 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/p/text()')
        neirong12 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/span/text()')
        neirong13 = tree.xpath('/html/body/div[2]/div[2]/div[1]/text()')
        neirongs = neirong1 + neirong2+neirong3+neirong4+neirong5+neirong6+neirong7+neirong8+neirong9+neirong10+neirong11+neirong12+neirong13
        neirongss = []
        for x in neirongs:
            neirongss.append(x.replace(u'\u3000', u'').replace(u'\xa0', u'').replace(u'\n', u' ').replace(u'\r', u'').replace(u'\u2003', u'').replace(u'\t', u'').replace(u'      ', u''))

        # faburiqi1 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div[1]/text()')
        # faburiqi2 = tree.xpath('//table[@style="width:860px;margin:0 auto;margin-top:12px;"]/tbody/tr[4]/td[4]/text()')
        # faburiqi3 = tree.xpath('//div[@class="pages-date"]/text()')
        # faburiqi4 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[3]/div[1]/text()')
        # faburiqi5 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[11]/text()')
        # faburiqi6 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[8]/span/text()')
        # faburiqis = faburiqi1 + faburiqi2 + faburiqi3 +faburiqi4+faburiqi5+faburiqi6
        time4 = str(faburiqis).replace("年", "-").replace("月", "-").replace("日", "").replace("/", "-").strip()
        faburiqi= re.findall('\d{4}-\d{2}-\d{2}', str(time4))

        # biaoti1 = tree.xpath('/html/body/div[2]/div[2]/div[1]/h2/text()')
        # biaoti2 = tree.xpath('//table[@style="width:860px;margin:0 auto;margin-top:12px;"]/tbody/tr[3]/td[2]/text()')
        # biaoti3 = tree.xpath('//table[@style="width:660px;margin:0 auto;margin-top:12px;"]/tbody/tr[3]/td[2]/text()')
        # biaoti4 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/strong/span/font/text()')
        # biaoti5 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/p/strong/font/text()')
        # biaoti6 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p/b/font/text()')
        # # biaoti7 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p/font/text()')
        # biaoti8 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/p/b/font/text()')
        # biaotis = biaoti3 + biaoti2 + biaoti1+biaoti4+biaoti5+biaoti6+biaoti8
        # biaoti = [x.strip() for x in biaotis if x.strip() != '']


        fawenzihao1 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/span[3]/div/text()')
        fawenzihao2 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/span[2]/div/text()')
        fawenzihao3 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div/span[1]/div/text()')
        fawenzihao = fawenzihao1 +fawenzihao2+fawenzihao3

        fujian1 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[3]/div[2]/p/a/@href')
        fujian2 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[14]/a/@href')
        fujian3 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/p[7]/a/@href')
        fujian4 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[4]/a/@href')
        fujian5 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[9]/a/@href')
        fujian6 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[4]/a/@href')
        fujian7 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[12]/a/@href')
        fujian8 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[13]/a/@href')
        fujian9 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div/p[4]/a/@href')
        fujian10 = tree.xpath('/html/body/div[2]/div[2]/div/div[2]/div/div/p[3]/font/a/@href')
        fujian11 = tree.xpath('/html/body/div[2]/div[2]/div[1]/a[2]/@href')
        fujian12 = tree.xpath('/html/body/div[2]/div[2]/div[1]/a[3]/@href')
        fujian13 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[16]/a/@href')
        fujian14 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[3]/a/@href')
        fujian15 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[38]/a/@href')
        fujian16 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[3]/a/@href')
        fujian17 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[25]/a/@href')
        fujian18 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[6]/a/@href')
        fujian19 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[5]/a/@href')
        fujian20 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[7]/a/@href')
        fujian21 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[17]/a/@href')
        fujian22 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[32]/a/@href')
        fujian23 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/p[9]/a/@href')
        fujian24 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/p[8]/a/@href')
        fujian25 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[22]/a/@href')
        fujian26 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[23]/a/@href')
        fujian27 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[15]/a/@href')
        fujian28 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[9]/a/@href')
        fujian29 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/p[33]/a/@href')
        fujian30 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/p[34]/a/@href')
        fujian31 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/p[35]/a/@href')
        fujian32 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/p[36]/a/@href')
        fujian33 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/p[12]/a/@href')
        fujian34 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/p[13]/a/@href')

        fujian35 =tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[22]/a/@href')
        fujian36 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[9]/font/a/@href')
        fujian37 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[10]/font/a/@href')
        fujian38 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/p[4]/a/@href')
        fujian39 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[35]/a/@href')
        fujian40 =tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[28]/a/@href')
        fujian41 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[40]/a/@href')


        fujians = fujian1 + fujian2 + fujian3 + fujian4 + fujian5 +\
                  fujian8 + fujian7 + fujian6 + fujian9 + fujian10 + \
                  fujian12 + fujian11 + fujian13 + fujian14 + fujian15 +\
                  fujian16 + fujian17 + fujian18+fujian19+fujian20+fujian21+\
                  fujian22+fujian23+fujian24+fujian25+fujian26+fujian27+fujian28+\
                  fujian29+fujian30+fujian31+fujian32+fujian33+fujian34+fujian35+\
                  fujian36+fujian37+fujian38+fujian41+fujian40+fujian39

        fujianss = []
        for i in fujians:
            fujian0= urllib.parse.urljoin(url, i)
            fujianss.append(fujian0.replace(u'\u3000', u''))
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
        #
        neirong = ''.join(neirongss)
        print(url)  # url                   1
        # print(suoyinhao)#索引号              1
        # print(zhutifenlei)#主题分类           1
        # print(fawenjiguan)#发文机关            1
        # print(gongwenzhonglei)#公文种类           2
        # print(chengwenriqi)#成文日期          1
        print(biaoti)#标题                2
        print(faburiqi)#发布日期         2
        # # print(zhutici)#主题词             1
        # print(neirong)#全文内容         2
        # print(fujian)#fujian             2
        # print(zhengcelaiyuan)#政策来源            2
        # print(shenxiaorq)#生效日期      1
        # print(shixiaorq)#失效日期      1
        # print(jpgs) #图片链接                1
        print('\n')

        # connect = pymysql.Connect(host='localhost', port=3306, user="root", passwd="mima123456",
        #                           db="policy",
        #                           charset='utf8')
        # cursor = connect.cursor()
        # sql = 'INSERT ignore INTO fagaiwei(`urls`,`syh`,`ztfl`,`fwjg`,`gwzl`,`cwrq`,`bt`,`fbrq`,`ztc`,`nr`,`fj`,`zcly`,`shen_rq`,`shix_rq`,`jpg`)VALUES("' + str(
        #     url) + '","' + str(suoyinhao) + '","' + str(zhutifenlei) + '","' + str(fawenjiguan) + '","' + str(
        #     gongwenzhonglei) + '","' + str(chengwenriqi) + '","' \
        #       + str(biaoti) + '","' + str(faburiqi) + '","' + str(zhutici) + '","' + str(neirong) + '","' + str(
        #     fujian) + '","' + str(zhengcelaiyuan) + '","' + str(shenxiaorq) + '","' + str(shixiaorq) + '","' + str(
        #     jpgs) + '")'
        # cursor.execute(sql)
        # connect.commit()
        # connect.close()
        # print('正在运行')
    except:
        pass