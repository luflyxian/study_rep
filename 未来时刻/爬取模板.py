import requests    #数据获取
import pymysql  #数据库接口调用
import urllib  #链接拼接
from lxml import etree
# from lxml import html  #数据清洗
import time #记录时间
import re #数据清洗
start = time.time()
for i in range(5):#0 1 2 3 4
    url_start = "http://sousuo.gov.cn/column/30469/"+str(i)+".htm"  #当前总共有66页数据，从0.htm开始

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.49"
    } #请求头

    params = {"sn": "a14062711010650606ss9p000000", "size": "0"}  #请求参数

    response = requests.get(url=url_start, params=params, headers=headers)#给对应网址发送get请求
    response.encoding = "utf-8"
    pages_text = response.text #文本数据
    # print(pages_text)
    # etree = html.etree
    tree = etree.HTML(pages_text)#数据格式化



    td_xpath = tree.xpath('//ul[@class="listTxt"]/li/h4/a/@href') #数据定位 #文章链接
    biaoti1 = tree.xpath('/html/body/div[2]/div/div[2]/div[2]/ul/li/h4/a/text()')#文章标题
    faburiqi1 = tree.xpath('/html/body/div[2]/div/div[2]/div[2]/ul/li/h4/span/text()')#发布时间


    for i, biaoti, faburiqis in zip(td_xpath, biaoti1, faburiqi1):

        url_one = "http://www.scio.gov.cn/xwfbh/gssxwfbh/xwfbh/jiangxi/"
        url = urllib.parse.urljoin(url_one, i)  # ---------------------------------------#拼接出相对统一的url

        response = requests.get(url=url, params=params, headers=headers)
        response.encoding = "utf-8"
        pages_text = response.text
        # etree = html.etree
        tree = etree.HTML(pages_text)

        neirong1 = tree.xpath("//*[@id='UCAP-CONTENT']/p/text()")#文章内容格式1

        neirong2 = tree.xpath('//*[@id="UCAP-CONTENT"]/p//text()')#文章内容格式2

        neirong3 = neirong1 + neirong2  #全部文章内容
        neirong = []
        for x in neirong3:
            neirong.append(x.replace(u'\u3000', u'').replace(u'\xa0', u'').replace(u'\r', u'').replace(u'\n', u'').replace(u'\u2003', u'').replace(u'\t', u''))
          #去除文章内的换行\n \r \u3000等特殊字符
        time4 = str(faburiqis).replace("年", "-").replace("月", "-").replace("日", "").replace("/", "-").replace(".", "-").strip()  #发文时间 例如2021年1月5日
        faburiqi= re.findall('\d{4}-\d{2}-\d{2}', str(time4)) # 格式化时间 2020-01-05
        #
        suoyinhao1 = tree.xpath('/html/body/div[6]/div[3]/table[1]/tbody/tr/td/table[1]/tbody/tr[1]/td[1]/b/text()')#索引号格式1
        suoyinhao2 = tree.xpath('/html/body/div[6]/div[3]/table[1]/tbody/tr/td/table[1]/tbody/tr[1]/td[2]/text()')#索引号格式2
        suoyinhao = suoyinhao1 + suoyinhao2 #全部索引号

        zhutifenlei1 = tree.xpath('/html/body/div[6]/div[3]/table[1]/tbody/tr/td/table[1]/tbody/tr[1]/td[3]/b/text()')
        zhutifenlei2 = tree.xpath('/html/body/div[6]/div[3]/table[1]/tbody/tr/td/table[1]/tbody/tr[1]/td[4]/text()')
        zhutifenlei = zhutifenlei1 + zhutifenlei2
        fawenjiguan1 = tree.xpath('/html/body/div[6]/div[3]/table[1]/tbody/tr/td/table[1]/tbody/tr[2]/td[1]/b/text()')
        fawenjiguan2 = tree.xpath('/html/body/div[6]/div[3]/table[1]/tbody/tr/td/table[1]/tbody/tr[2]/td[2]/text()')
        fawenjiguan = fawenjiguan1 + fawenjiguan2
        chengwenriqi1 = tree.xpath('/html/body/div[6]/div[3]/table[1]/tbody/tr/td/table[1]/tbody/tr[2]/td[3]/b/text()')
        chengwenriqi2 = tree.xpath('/html/body/div[6]/div[3]/table[1]/tbody/tr/td/table[1]/tbody/tr[2]/td[4]/text()')
        chengwenriqi = chengwenriqi1 + chengwenriqi2
        fawenzihao1 = tree.xpath('/html/body/div[6]/div[3]/table[1]/tbody/tr/td/table[1]/tbody/tr[4]/td[1]/b/text()')
        fawenzihao2 = tree.xpath('/html/body/div[6]/div[3]/table[1]/tbody/tr/td/table[1]/tbody/tr[4]/td[2]/text()')
        fawenzihao = fawenzihao1 + fawenzihao2

        jpg1 = tree.xpath('//*[@id="UCAP-CONTENT"]/p/img/@src') #图片格式1
        jpg2 = tree.xpath('/html/body/div[2]/div[2]/div/div/p/span/img/@src') #图片格式2
        jpgss = jpg1 + jpg2 #全部图片格式
        jpgs = []
        for x in jpgss:
            jpgs0 = urllib.parse.urljoin(url, x)
            jpgs.append(jpgs0.replace(u'\u2002', u'').replace(u'\xa0', u'').replace(u'\u200b', u'').replace(u'\n', u'').replace(u'\r', u'').replace(u'\t', u''))


        # zhutifenlei = []
        # chengwenriqi = []
        gongwenzhonglei = '通知通告'
        # fwzh = []
        zhutici=[]
        # fawenjiguan='国务院办公厅'
        zhengcelaiyuan='中国政府网'
        shenxiaorq=[]
        shixiaorq=[]
        fujian = []
        # neirong = ''.join(neirongss)

        print(url)  # url                   1
        print(suoyinhao)#索引号              1
        print(zhutifenlei)#主题分类           1
        print(fawenjiguan)#发文机关            1
        print(gongwenzhonglei)#公文种类                  1
        print(chengwenriqi)#成文日期          1
        print(biaoti)#标题                 1
        print(faburiqi)#发布日期          1
        print(zhutici)#主题词             1
        print(neirong)#全文内容           1
        print(fujian)#fujian             1
        print(zhengcelaiyuan)#政策来源            1
        print(shenxiaorq)#生效日期      1
        print(shixiaorq)#失效日期      1
        print(jpgs) #图片链接                1
        print('\n')

#         print('正在运行1')
#         print('正在运行2')
# print(f"一共花费{time.time() - start}")