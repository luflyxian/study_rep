import time
import pymysql
from elasticsearch import Elasticsearch
from elasticsearch import helpers

ES = [
    'http://ip:9200'
]
es = Elasticsearch(ES, sniffer_timeout = 1000)

# 连接数据库
db = pymysql.connect("127.0.0.1", "root", "123456", "test", 3307)
cursor = db.cursor()
db.set_charset("utf8")
cursor.execute('SET NAMES utf8;')
cursor.execute('SET CHARACTER SET utf8;')
cursor.execute('SET character_set_connection=utf8;')

def getVal(str):
    if str is not None:
        return str
    else:
        return ""

def get_skin_list(page,size):
    start = (page-1)*size
    sql = "select * from res_resource order by id desc limit %s,%s"
    cursor.execute(sql, (start, size))
    data = cursor.fetchall()
    return data

def import_db(page,size):
    skin_list = get_skin_list(page,size)
    if not skin_list:
        return False
    actions = []
    for fields in skin_list:
        action = {
            "_index": "res",
            "_type": "sql",
            "_id": fields[0],
            "_source": {
                "id": fields[0],
                "status": int(fields[1]),
                "name": getVal(fields[2]),
                "mail": getVal(fields[3]),
                "direction": getVal(fields[4]),
                "field": getVal(fields[5]),
                "mail_source": getVal(fields[6]),
                "phone": getVal(fields[7]),
                "occupation": getVal(fields[8]),
                "company": getVal(fields[9]),
                "meeting_title": getVal(fields[10]),
                "country": getVal(fields[11]),
                "region": getVal(fields[12]),
                "links": getVal(fields[13]),
                "explain": getVal(fields[14]),
                "import_name": getVal(fields[15]),
                "import_time": int(fields[16]),
                "export_time": int(fields[17]),
                "export_name": getVal(fields[18]),
                "operation_time": int(fields[19]),
                "frequency": int(fields[20]),
                "disabled": int(fields[21]),
            }
        }
        actions.append(action)
        helpers.bulk(es, actions)
        print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+":成功上传-"+str(len(actions)))
    return True

if __name__ == '__main__':
    print(import_db(1, 10000))