import requests
import urllib
from lxml import html
import base64
import time
def get_first_url(url_start, params, headers):
    response = requests.get(url=url_start, params=params, headers=headers)
    response.encoding = "utf-8"
    pages_text = response.text
    etree = html.etree
    tree = etree.HTML(pages_text)
    td_xpath = tree.xpath('//ul[@class="listTxt"]/li/h4/a/@href')
    for i in td_xpath:
        url_one = "http://www.scio.gov.cn/xwfbh/gssxwfbh/xwfbh/jiangxi/"
        url = urllib.parse.urljoin(url_one, i)  # ---------------------------------------url
        response = requests.get(url=url, params=params, headers=headers)
        response.encoding = "utf-8"
        pages_text = response.text
        etree = html.etree
        tree = etree.HTML(pages_text)
        neirong1 = tree.xpath("//p[@style='text-indent: 2em; font-family: 宋体; font-size: 12pt;']/text()")
        neirong2 = tree.xpath('//*[@id="UCAP-CONTENT"]/p/text()')
        neirong3=neirong1+neirong2
        neirong4 = []
        for x in neirong3:
            neirong4.append(x.replace(u'\u3000', u' ').replace(u'\xa0', u' '))
        neirong = [neirong5 + "\n" for neirong5 in neirong4]
        faburiqi1 = tree.xpath('//table[@style="width:660px;margin:0 auto;margin-top:12px;"]/tbody/tr[4]/td[4]/text()')
        faburiqi2 = tree.xpath('//table[@style="width:860px;margin:0 auto;margin-top:12px;"]/tbody/tr[4]/td[4]/text()')
        faburiqi3 = tree.xpath('//div[@class="pages-date"]/text()')
        faburiqi4 = faburiqi1 + faburiqi2 +faburiqi3
        faburiqi1 = [x.strip() for x in faburiqi4 if x.strip() != '']
        texts = str(faburiqi1)
        faburiqi = texts.replace("年", "-").replace("月", "-").replace("日", "").replace("/", "-").strip()
        biaoti1 = tree.xpath('//div[@class="article oneColumn pub_border"]/h1/text()')
        biaoti2 = tree.xpath('//table[@style="width:860px;margin:0 auto;margin-top:12px;"]/tbody/tr[3]/td[2]/text()')
        biaoti3 = tree.xpath('//table[@style="width:660px;margin:0 auto;margin-top:12px;"]/tbody/tr[3]/td[2]/text()')
        biaoti4 = biaoti3 + biaoti2 + biaoti1
        biaoti = [x.strip() for x in biaoti4 if x.strip() != '']
        suoyinhao1 = tree.xpath('/html/body/div[6]/div[3]/table[1]/tbody/tr/td/table[1]/tbody/tr[1]/td[1]/b/text()')
        suoyinhao2 = tree.xpath('/html/body/div[6]/div[3]/table[1]/tbody/tr/td/table[1]/tbody/tr[1]/td[2]/text()')
        suoyinhao = suoyinhao1+suoyinhao2
        zhutifenlei1 = tree.xpath('/html/body/div[6]/div[3]/table[1]/tbody/tr/td/table[1]/tbody/tr[1]/td[3]/b/text()')
        zhutifenlei2 = tree.xpath('/html/body/div[6]/div[3]/table[1]/tbody/tr/td/table[1]/tbody/tr[1]/td[4]/text()')
        zhutifenlei = zhutifenlei1+zhutifenlei2
        fawenjiguan1 = tree.xpath('/html/body/div[6]/div[3]/table[1]/tbody/tr/td/table[1]/tbody/tr[2]/td[1]/b/text()')
        fawenjiguan2 = tree.xpath('/html/body/div[6]/div[3]/table[1]/tbody/tr/td/table[1]/tbody/tr[2]/td[2]/text()')
        fawenjiguan = fawenjiguan1+fawenjiguan2
        chengwenriqi1 = tree.xpath('/html/body/div[6]/div[3]/table[1]/tbody/tr/td/table[1]/tbody/tr[2]/td[3]/b/text()')
        chengwenriqi2 = tree.xpath('/html/body/div[6]/div[3]/table[1]/tbody/tr/td/table[1]/tbody/tr[2]/td[4]/text()')
        chengwenriqi = chengwenriqi1+chengwenriqi2
        fawenzihao1 = tree.xpath('/html/body/div[6]/div[3]/table[1]/tbody/tr/td/table[1]/tbody/tr[4]/td[1]/b/text()')
        fawenzihao2 = tree.xpath('/html/body/div[6]/div[3]/table[1]/tbody/tr/td/table[1]/tbody/tr[4]/td[2]/text()')
        fawenzihao = fawenzihao1 +fawenzihao2
        wangzhanbiaoshima = '网站标识码bm01000001'
        ipbeianhao = '京ICP备05070218号'
        beianhao = '京公网安备11010202000001号'
        key = base64.b64encode(url.encode("utf8"))
        json = {
            "key":key,
            "suoyinhao":suoyinhao,
            "zhutifenlei":zhutifenlei,
            "fawenjiguan":fawenjiguan,
            "chengwenriqi":chengwenriqi,
            "biaoti":biaoti,
            "fawenzihao":fawenzihao,
            "faburiqi":faburiqi,
            "neirong":neirong,
            "wangzhanbiaoshima":wangzhanbiaoshima,
            "ipbeianhao":ipbeianhao,
            "beianhao":beianhao
        }
        print(json)

    print(f"一共花费{time.time() - start}")

if __name__ == "__main__":
    start = time.time()
    url_start = "http://sousuo.gov.cn/column/30469/13.htm"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.49"
    }
    params = {"sn": "a14062711010650606ss9p000000", "size": "0"}
    get_first_url(url_start, params, headers)

    # print(key)
    # print(suoyinhao)
    # print(zhutifenlei)
    # print(fawenjiguan)
    # print(chengwenriqi)
    # print(biaoti)
    # print(fawenzihao)
    # print(faburiqi)
    # print(neirong)
    # print(wangzhanbiaoshima)
    # print(ipbeianhao)
    # print(beianhao)