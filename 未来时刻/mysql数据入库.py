import requests
from lxml import html
import time
import pymysql
import base64
import urllib

start = time.time()

url_start = "http://www.moe.gov.cn/was5/web/search?channelid=254874&chnlid=2147438998&page="+str(i) #当前总共有403页数据，从page=1开始
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.49"
}
response = requests.get(url=url_start, headers=headers)
response.encoding = "utf-8"
pages_text = response.text
etree = html.etree
tree = etree.HTML(pages_text)
keys = url_start
key = keys

zhuti = ''
faburiqi = ''
#----------------------------------------------------------------------------------------------------数据导入mysql
connect = pymysql.Connect(host='localhost', port=3306, user="root", passwd="mima123456",
                          db="guojiazhengce",
                          charset='utf8')  #数据库 库 表 账号密码及权限
cursor = connect.cursor()
sql = 'INSERT ignore INTO gjjybb(`Key`,`Zhuti`,`Faburiqi`,`Neirong`,`Banquansuoyou`,`Wzbsm`,`Ipbeianhao`,`Beianhao`)VALUES("' + str(key) + '","' + str(zhuti) + '","' + str(shijian) + '","' + str(neirong) + '","' + str(banquansouyou) + '","' + str(wangzhanbiaoshi) + '","' + str(icp) + '","' + str(jinggongwanganbei) + '")'
cursor.execute(sql)  # 数据入库
# sql = "truncate 表名称"
# cursor.execute(sql)  # 删除数据库表内数据格式和内容
connect.commit() #关闭数据库
connect.close()  # 关闭语句


print(f"一共花费{time.time() - start}") #查看运行时间




