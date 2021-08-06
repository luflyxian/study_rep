"""
用于获取http://www.gov.cn/zhengce/xxgk/index.htm的政策
修改数据库配置在open_mysql_db()函数中
"""
import requests
from lxml import etree
import json
from bs4 import BeautifulSoup
import os
import pymysql
import time
from datetime import datetime
import traceback
import random
count = 0
def get_request_text(url):
    response = requests.get(url=url, params=params, headers=headers)
    response.encoding = "utf-8"
    page_text = response.text
    return page_text
def get_xpath_data(page_text, data_dict):
    """
    通过xpath获得各项数据
    如:
    索 引 号:000014349/2020-00072
    主题分类: 科技、教育\科技
    发文机关: 国务院办公厅
    成文日期: 2020年07月23日
    标　　题: 国务院办公厅关于提升大众创业万众创新示范基地带动作用进一步促改革稳就业强动能的实施意见
    发文字号: 国办发〔2020〕26号
    发布日期: 2020年07月30日
    主 题 词: ""
    :param page_text: 页面的html文本信息
    :return:
    """
    tree = etree.HTML(page_text)
    td_xpath = tree.xpath('/html/body/div[6]/div[3]/table[1]/tbody/tr/td')
    if td_xpath == []:
        if tree.xpath('/html/body/div[5]/div[3]/table[1]/tbody/tr/td'):
            td_xpath = tree.xpath('/html/body/div[5]/div[3]/table[1]/tbody/tr/td')
        elif tree.xpath("/html/body/div[6]/div[4]/table[1]/tbody/tr/td"):
            td_xpath = tree.xpath('/html/body/div[6]/div[4]/table[1]/tbody/tr/td')

    td_content = td_xpath[0]
    top_content = td_content.xpath('./table[1]//tr')

    bottom_content = td_content.xpath('./table[2]//tr')

    syh = top_content[0].xpath('./td[2]/text()')
    # print(syh)
    data_dict["syh"] = " " if syh == [] else syh[0]

    zt_mc = top_content[0].xpath('./td[4]/text()')
    data_dict["zt_mc"] = " " if zt_mc == [] else zt_mc[0].replace("\\", "\\\\")
    # print(data_dict["zt_mc"])

    fwjg = top_content[1].xpath('./td[2]/text()')
    data_dict["fwjg"] = " " if fwjg == [] else fwjg[0].strip()

    cwrq = top_content[1].xpath('./td[4]/text()')
    data_dict["cwrq"] = " " if cwrq == [] else cwrq[0]

    bt = top_content[2].xpath('./td[2]/text()')
    # print(bt)
    data_dict["bt"] = " " if bt == [] else bt[0].replace("'", "\\\'").replace('"', "\\\"")

    fwzh = top_content[3].xpath('./td[2]/text()')
    data_dict["fwzh"] = " " if fwzh == [] else fwzh[0]

    fbrq = top_content[3].xpath('./td[4]/text()')
    data_dict["fbrq"] = " " if fbrq == [] else fbrq[0]

    # data_dict["syh"] = top_content[0].xpath('./td[2]/text()')  # 索 引 号:000014349/2020-00072
    # data_dict["zt_mc"] = top_content[0].xpath('./td[4]/text()')  # 主题分类: 科技、教育\科技
    # data_dict["fwjg"] = top_content[1].xpath('./td[2]/text()')  # 发文机关: 国务院办公厅
    # data_dict["cwrq"] = top_content[1].xpath('./td[4]/text()')  # 成文日期: 2020年07月23日
    # data_dict["bt"] = top_content[2].xpath('./td[2]/text()')  # 标　　题: 国务院办公厅关于提升大众创业万众创新示范基地带动作用进一步促改革稳就业强动能的实施意见
    # data_dict["fwzh"] = top_content[3].xpath('./td[2]/text()')  # 发文字号: 国办发〔2020〕26号
    # data_dict["fbrq"] = top_content[3].xpath('./td[4]/text()')  # 发布日期: 2020年07月30日
    ztc = bottom_content[0].xpath('./td/text()')
    data_dict["ztc"] = " " if ztc == [] else ztc[0]  # 主 题 词: ""
    # print(zt_mc)
    # print(fwjg)
    # print(cwrq)
    # print(bt)
    # print(fwzh)
    # print(fbrq)
    # print(ztc)
    # print(data_dict)
    full_text = tree.xpath('//*[@id="UCAP-CONTENT"]//text()')
    qwnr = "".join(full_text)  # 全文内容
    data_dict["qwnr"] = " " if qwnr == "" else qwnr.replace("'", "\\\'").replace('"', "\\\"")  # 全文内容


def get_bs4_tag(page_text):
    """
    使用bs4获得要创建本地HTML的对应标签
    :param page_text:页面的html文本信息
    :return:对应HTML标签
    """
    soup = BeautifulSoup(page_text, 'lxml')
    tag = soup.select("body > div.w1100 > div.wrap > table:nth-child(3) > tbody > tr > td:nth-child(1) > table")[0]
    return tag


def create_native_path(url):
    """
    创建存储HTML的本机路径,产生文件路径
    :param url: 指定的url
    :return: 一个元组  (文件路径,文件名称)
    """
    # 开始创建存储HTML的本机路径
    dir_path = "/".join(url.split("/")[2:-1])
    file_name = url.split("/")[-1]
    file_path = "./" + dir_path
    # print(file_path, file_name)
    return (file_path, file_name)


def create_html_file(file_path, file_name):
    """
    创建本地HTML文件并存储,文件路径不存在就新建路径
    :param file_path: 文件路径(不包括文件)
    :param file_name: 文件名称
    :return: 整个文件的相对路径
    """
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    with open(file_path + "/" + file_name, "w", encoding="utf-8") as fp:
        fp.write(html_template)
    return file_path + "/" + file_name


def open_mysql_db():
    # 打开数据库连接
    conn = pymysql.connect("192.168.1.2", "zhangchaoyin", "zhangchaoyin123456", "future_time")
    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()
    return conn, cursor


def select_mysql_db(conn, cursor, data_dict={}):
    # 先查是否有重复URL,来做到只插入新政策,不插入旧数据
    sql = f""" SELECT url FROM zc where url="{data_dict['url']}" """
    # 执行SQL语句
    cursor.execute(sql)
    # 获取记录元组
    results = cursor.fetchone()
    if not results:
        # SQL 查询语句
        if data_dict["zt_mc"] == "其他":
            sql = "SELECT zt2_id FROM zt2  WHERE zt1_mc='其他' and zt2_mc='其他'"
        else:
            sql = "SELECT zt2_id FROM zt2  WHERE zt1_mc='{}' and zt2_mc='{}'".format(*data_dict["zt_mc"].split("\\\\"))
            # print(sql)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取记录元组
            results = cursor.fetchone()  # (336,)
            data_dict["zt2_id"] = results[0]
        except:
            print("Error: unable to fetch data")

        return 1


def close_mysql_db(conn):
    conn.close()


def insert_mysql_db(conn, cursor, data_dict={}):
    # SQL 插入语句
    # # print(sql)
    sql = f"""INSERT INTO zc(syh,zt2_id,zt_mc,fwjg,cwrq,bt,fwzh,fbrq,ztc,qwnr,fj,zcly,url)
                         VALUES ("{data_dict['syh']}",{data_dict["zt2_id"]},"{data_dict['zt_mc']}","{data_dict['fwjg']}","{data_dict['cwrq']}","{data_dict['bt']}","{data_dict['fwzh']}","{data_dict['fbrq']}","{data_dict['ztc']}","{data_dict['qwnr']}","{data_dict['fj']}","{data_dict['zcly']}","{data_dict['url']}")"""

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        conn.commit()
        # print("插入成功!!!")
        # ---------------------------------------------------------
        if data_dict['fwjg'].strip():
            lsts_fwjg = [data_dict['fwjg'].strip()]
            if len(data_dict['fwjg'].strip().split(" ")) > 1:
                lsts_fwjg = data_dict['fwjg'].split(" ")
            elif len(data_dict['fwjg'].strip().split("、")) > 1:
                lsts_fwjg = data_dict['fwjg'].split("、")

            for fwjg in lsts_fwjg:

                sql = f"SELECT jg_id FROM jg  WHERE jg_mc = '{fwjg}' "  # 建议使用like,返回id以及名称
                try:
                    # print(sql)
                    # 执行SQL语句
                    cursor.execute(sql)
                    # 获取记录元组
                    jg_id = cursor.fetchone()  # (jg_id,)

                    if not jg_id:
                        insert_jg_sql = f"""INSERT INTO jg(jg_mc,jglx,gxdm,bz) values ("{fwjg}","国家部委",999999,"国家部委") """
                        # 执行inert_jg_sql
                        # 执行sql语句
                        cursor.execute(insert_jg_sql)
                        jg_id = [cursor.lastrowid]
                        # 提交到数据库执行
                        conn.commit()
                        # print("插入成功!!!")

                    sql = f"""SELECT zc_id FROM zc where URL = "{data_dict['url']}" """
                    cursor.execute(sql)
                    zc_id = cursor.fetchone()[0]
                    insert_jgzc_sql = f"""INSERT INTO jg_zc(zc_id,jg_id,jg_mc,jglx,dm) values ({zc_id},{jg_id[0]},"{fwjg}","国家部委",999999) """
                    # 执行sql语句
                    cursor.execute(insert_jgzc_sql)
                    # 提交到数据库执行
                    conn.commit()
                    # print("插入成功!!!")


                except:
                    with open("./国务院政策报错日志.log", "a", encoding="utf-8") as fp:
                        fp.write("*" * 20 + str(datetime.now()) + "*" * 20 + "\n" + traceback.format_exc())
                    print("插入机关表失败!!!!")

        # ----------------------------------------------------

        global count
        count += 1
        if count % 100 == 0:
            print(f"现在已经爬取{count}条数据")
    except:
        # 如果发生错误则回滚
        conn.rollback()
        print(f'{data_dict["url"]}' + "插入失败")


def operate_mysql_db(data_dict={}):
    conn, cursor = open_mysql_db()
    ret = select_mysql_db(conn, cursor, data_dict)
    if ret:
        insert_mysql_db(conn, cursor, data_dict)
        close_mysql_db(conn)
    else:
        print("无最新政策")
        close_mysql_db(conn)
        return 1


if __name__ == '__main__':
    start = time.time()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.49"
    }
    params = {
        "callback": "jQuery112409104460597805375_1599009229377",
        "page_index": "1",
        "page_size": "5512"
    }

    url = "http://xxgk.www.gov.cn/search-zhengce/"
    page_text = get_request_text(url)
    # 下面两行代码把页面数据转换成DICT类型
    page_text = page_text[page_text.find("{"):-2]
    page_dict = json.loads(page_text)
    flag = True
    conn, cursor = open_mysql_db()
    for class_dict in page_dict["data"]:
        # if class_dict['url'] == "http://www.gov.cn/zhengce/content/2008-03/28/content_4519.htm":
        #     flag = False
        # if flag:
        sql = f""" SELECT url FROM zc where url="{class_dict["url"]}" """
        # 执行SQL语句
        cursor.execute(sql)
        # 获取记录元组
        results = cursor.fetchone()
        if results:
            continue



        try:
            # print(class_dict)
            data_dict = {}
            data_dict["zcly"] = "中国人民共和国中央人民政府"

            data_dict['url'] = class_dict["url"]
            print(class_dict["url"])  # http://www.gov.cn/zhengce/content/2020-07/30/content_5531274.htm
            url = class_dict["url"]
            detail_page_text = get_request_text(url)
            get_xpath_data(detail_page_text, data_dict)
            content = get_bs4_tag(detail_page_text)
            html_template = f"""
                        <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <title>Title</title>
                    </head>
                    <body>
                    {str(content)}
                    </body>
                    </html>
            """
            file_path, file_name = create_native_path(url)
            data_dict["fj"] = create_html_file(file_path, file_name)
            ret = operate_mysql_db(data_dict)
            t = random.randint(3,5)
            time.sleep(t)
            # 查询数据库是否有当前的url,有则停止程序,所以在更新最新数据的时候,取消注解
            # if ret == 1:
            #     break


        except:
            print("报错了,请看日志!!!")
            with open("./国务院政策报错日志.log", "a", encoding="utf-8") as fp:
                fp.write("*" * 20 + str(datetime.now()) + "*" * 20 + "\n" + data_dict['url'] + "\n"  + traceback.format_exc())
    print(f"一共花费{time.time() - start}")

