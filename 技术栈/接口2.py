import pymysql
import os
import json
# from flask import Flask
#app = Flask(__name__)
# @app.route('/index1', methods=['GET'])
def getcontent():

    conn = pymysql.Connect(host='localhost', port=3306, user="root", passwd="mima123456", db="gwy_xinwen",
                           charset='utf8')
    cursor = conn.cursor()
    # sql = 'INSERT ignore INTO guowuyuan_xinwen_gis(`SDM`,`JGMC`,`ZCZT`,`SJ`,`URL`)VALUES("' + str(sdm) + '","' + str(
    #     jgmc) + '","' + str(zczt) + '","' + str(sj) + '","' + str(url_two) + '")'
    #sql='SELECT SDM,JGMC,ZCZT,SJ,URL FROM guowuyuan_xinwen_gis'
    sql='select * from guowuyuan_xinwen_gis order by URL desc limit 10'
    cursor.execute(sql)
    data = cursor.fetchall()

    #print(data)
    para = []
    for i in data:
        text = {'name': i[0], 'class': i[1], 'number': i[2], 'score': i[3], 'URL': i[4]}
        # text = {"省代码":i[0],"机关名称":i[1],"政策主题":i[2],"时间":i[3],"url":i[4],}
        print(text)
        para.append(text)
        # return json.dumps(para, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    getcontent()