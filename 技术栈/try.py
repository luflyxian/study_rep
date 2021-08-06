import requests
from lxml import html
import time
import base64

def get_first_url(url,params,headers):
    response = requests.get(url=url, params=params, headers=headers)
    response.encoding = "utf-8"
    pages_text = response.text
    etree = html.etree
    tree = etree.HTML(pages_text)
    zhuti1 = tree.xpath('//div[@class="article oneColumn pub_border"]/h1/text()')#标题
    shijian1 = tree.xpath('//div[@class="pages-date"]/text()')#时间
    neirong=tree.xpath("//p[@style='text-indent: 2em; font-family: 宋体; font-size: 12pt;']/text()")
    faburiqi1 = tree.xpath('//table[@style="width:660px;margin:0 auto;margin-top:12px;"]/tbody/tr[4]/td[4]/text()')
    faburiqi2 = tree.xpath('//table[@style="width:860px;margin:0 auto;margin-top:12px;"]/tbody/tr[4]/td[4]/text()')
    faburiqi3 = tree.xpath('//div[@class="pages-date"]/text()')
    faburiqi4 = faburiqi1 + faburiqi2 + faburiqi3
    faburiqi = [x.strip() for x in faburiqi4 if x.strip() != '']
    zhuti1 = tree.xpath('//div[@class="article oneColumn pub_border"]/h1/text()')
    zhuti2 = tree.xpath('//table[@style="width:860px;margin:0 auto;margin-top:12px;"]/tbody/tr[3]/td[2]/text()')
    zhuti3 = tree.xpath('//table[@style="width:660px;margin:0 auto;margin-top:12px;"]/tbody/tr[3]/td[2]/text()')
    zhuti4 = zhuti3 + zhuti2 + zhuti1
    zhuti = [x.strip() for x in zhuti4 if x.strip() != '']
    suoyinhao1 = tree.xpath('/html/body/div[6]/div[3]/table[1]/tbody/tr/td/table[1]/tbody/tr[1]/td[1]/b/text()')
    suoyinhao2 = tree.xpath('/html/body/div[6]/div[3]/table[1]/tbody/tr/td/table[1]/tbody/tr[1]/td[2]/text()')
    suoyinhao = suoyinhao1 + suoyinhao2
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
    print(suoyinhao)  # 索引号
    print(zhutifenlei)  # 主题分类
    print(fawenjiguan)  # 发文机关
    print(chengwenriqi)  # 成文日期
    print(zhuti)  # 主题
    print(fawenzihao)  # 发文字号
    print(faburiqi)  # 发布日期
    for line in neirong:
        a=line + '\n'
        print(a)


    print(f"一共花费{time.time() - start}")

if __name__ == "__main__":
    start = time.time()


    url = 'http://www.gov.cn/zhengce/2021-02/26/content_5588966.htm'


    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.49"
    }
    params = {"sn": "a14062711010650606ss9p000000", "size": "0"}
    get_first_url(url,params,headers)

sql = "truncate one"
cursor.execute(sql)




