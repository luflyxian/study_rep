import requests
import pymysql
import urllib
from lxml import html
import time
import re
import json
import base64
start = time.time()
url_start = "https://www.ndrc.gov.cn/xwdt/tzgg/index_10.html"
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
        neirong6 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p/span/text()')
        neirong7 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/span/text()')
        neirong8 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div/p[1]/span/text()')
        neirong9 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div/span/text()')
        neirong10 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/div/span/text()')
        neirong11 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/p/text()')
        neirong12 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/span/text()')

        neirongs = neirong1 + neirong2+neirong3+neirong4+neirong5+neirong6+neirong7+neirong8+neirong9+neirong10+neirong11+neirong12
        neirongss = []
        for x in neirongs:
            neirongss.append(x.replace(u'\u3000', u' ').replace(u'\xa0', u' ').replace(u'\n', u' ').replace(u'\r', u' ').replace(u'\u2003', u' '))


        time4 = str(faburiqis).replace("年", "-").replace("月", "-").replace("日", "").replace("/", "-").strip()
        faburiqi= re.findall('\d{4}-\d{2}-\d{2}', str(time4))



        fawenzihao1 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/span[3]/div/text()')
        fawenzihao2 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/span[2]/div/text()')
        fawenzihao3 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div/span[1]/div/text()')
        fawenzihao = fawenzihao1 +fawenzihao2+fawenzihao3

        fujian1 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[3]/div[2]/p/a/@href')
        fujian2 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[32]/a/@href')
        fujian3 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/p[9]/a/@href')
        fujian4 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/p[23]/a/@href')
        fujian5 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/p[6]/a/@href')
        fujian6 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/p[8]/a/@href')
        fujian7 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/p[9]/a/@href')
        fujian8 = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div/p[9]/span/a/@href')


        fujians = fujian1+fujian2+fujian3+fujian4+fujian6+fujian7+fujian8+fujian5
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
        neirong = ''.join(neirongss)
        # print(url)  # url                   1
        # print(suoyinhao)#索引号              1
        # print(zhutifenlei)#主题分类           1
        # print(fawenjiguan)#发文机关            1
        # print(gongwenzhonglei)#公文种类           2
        # print(chengwenriqi)#成文日期          1
        print(biaoti)#标题                2
        # print(faburiqi)#发布日期         2
        # # print(zhutici)#主题词             1
        print(neirong)#全文内容         2
        # print(fujian)#fujian             2
        # print(zhengcelaiyuan)#政策来源            2
        # print(shenxiaorq)#生效日期      1
        # print(shixiaorq)#失效日期      1
        # print(jpgs) #图片链接                1
        # print('\n')

        url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=6h6mCoTbfk2ZOvLuZdtj35vP&client_secret=BN6MzD4kuznF2uf9ApSY6lG5xAM7jdbb'
        r1 = requests.post(url=url).text
        jsonobj = json.loads(r1)
        access_token = jsonobj['access_token']
        headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36',
            'Content-Type': 'application/json'
        }

        post_data = {
            "title": biaoti,
            "content": neirong

        }
        data = json.dumps(post_data).encode('GBK')
        url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/topic?charset=UTF-8&access_token=24.3899c67e784a0d47fa417aa60cdb1760.2592000.1628738331.282335-24537711'

        r = requests.post(url=url, headers=headers, data=data).text

        jsonobj = json.loads(r)
        leixing = jsonobj['item']['lv1_tag_list'][0]['tag']

        print(leixing)
        print('\n')

        # connect = pymysql.Connect(host='localhost', port=3306, user="root", passwd="mima123456",
        #                           db="policy",
        #                           charset='utf8')
        # cursor = connect.cursor()
        # sql = 'INSERT ignore INTO fagaiwei(`urls`,`syh`,`ztfl`,`fwjg`,`gwzl`,`cwrq`,`bt`,`fbrq`,`ztc`,`nr`,`fj`,`zcly`,`shen_rq`,`shix_rq`,`jpg`)VALUES("' + str(url) + '","' + str(suoyinhao) + '","' + str(zhutifenlei) + '","' + str(fawenjiguan) + '","' + str(gongwenzhonglei) + '","' + str(chengwenriqi) + '","' \
        #       + str(biaoti) + '","' + str(faburiqi) + '","' + str(zhutici) + '","' + str(neirong) + '","' + str(
        #     fujian) + '","' + str(zhengcelaiyuan) + '","' + str(shenxiaorq) + '","' + str(shixiaorq) + '","' + str(jpgs) + '")'
        # cursor.execute(sql)
        # connect.commit()
        # connect.close()
        # print('正在运行')
    except:
        pass