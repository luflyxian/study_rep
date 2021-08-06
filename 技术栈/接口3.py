# -*- coding: UTF-8 -*-
import pymysql
import os
import json
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
from flask import Flask,request

app = Flask(__name__)


@app.route('/index2', methods=['POST'])
def indextest():
    inputData = request.json.get('inputData')
    data1 = getcontent(inputData)
    return data1


def getcontent(inputData):
    conn = pymysql.Connect(host='localhost', port=3306, user="root", passwd="mima123456", db="gwy_xinwen",
                           charset='utf8')
    cursor = conn.cursor()
    sql="SELECT SDM,JGMC,ZCZT,SJ,URL FROM guowuyuan_xinwen_gis where SJ='%s'" % (inputData)
    cursor.execute(sql)
    data = cursor.fetchone()
    print(data)

    result = {'name': data[0], 'class': data[1], 'number': data[2], 'score': data[3], 'URL': data[4]}
    return json.dumps(result, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5590)
#
# {
#     "inputData":"['2011-04-01']"
# }