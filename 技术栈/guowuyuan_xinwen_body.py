import requests
import pymysql
import urllib
from lxml import html
import re
import time
count = 0
def get_first_url(url_start, params, headers):
    response = requests.get(url=url_start, params=params, headers=headers)
    response.encoding = "utf-8"
    pages_text = response.text
    etree = html.etree
    tree = etree.HTML(pages_text)
    td_xpath = tree.xpath('//div[@class="fl list_t"]/a/@href')
    for i in td_xpath:
        url_one = "http://www.scio.gov.cn/xwfbh/gssxwfbh/xwfbh/jiangxi/"
        url = urllib.parse.urljoin(url_one, i)  # ---------------------------------------url
        # urllist.append(url_two)
        response = requests.get(url=url)
        response.encoding = "utf-8"
        pages_text = response.text
        tree = etree.HTML(pages_text)
        # xwzt = tree.xpath('//div[@class="tc A_title"]/text()')  # ----------------------新闻主题
        # text_two = tree.xpath('//div[@style="DISPLAY: inline"]/text()')
        # pattern = re.compile(r"(\d{4}-\d{1,2}-\d{1,2})")
        # sj = re.findall(pattern, text_two[0])  # ------------------------------------------时间
        # wybah = "京ICP备05070218号"  # ------------------------------------------------网页备案号
        # jgmc = "中华人民共和国中央人民政府"  # ------------------------------------------机关名称
        text_three = tree.xpath('//div[@class="p10 f14 lh30"]/p/text()')
        #print(url)
        nr = []
        for x in text_three:
            nr.append(x.replace(u'\u3000', u' ').replace(u'\xa0', u' '))  # ------------------------------------新闻内容
        # connect = pymysql.Connect(host='localhost', port=3306, user="root", passwd="mima123456", db="gwy_xinwen",
        #                           charset='utf8')
        # cursor = connect.cursor()
        # sql = r'INSERT INTO guowuyuan_xinwen_text(URL,XWZT,SJ,JGMC,NR,WYBAH)VALUES("' + str(url) + '","' + str(
        #     xwzt) + '","' + str(sj) + '","' + str(jgmc) + '","' + str(nr) + '","' + str(wybah) + '")'
        # cursor.execute(sql)
        # # sql = "truncate guowuyuan_xinwen_text"
        # # cursor.execute(sql)
        # connect.commit()
        # connect.close()
        # print("--------------------------------------------------------------------------------------------------------------")
        # print(nr)
    print(f"一共花费{time.time() - start}")


if __name__ == "__main__":
    start = time.time()
    url_start = "http://www.scio.gov.cn/xwfbh/gssxwfbh/xwfbh/jiangxi/index.htm"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.49"
    }
    params = {"sn": "a14062711010650606ss9p000000", "size": "0"}
    get_first_url(url_start, params, headers)
