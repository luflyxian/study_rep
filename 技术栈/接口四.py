# import flask
# import time
# from flask import request,jsonfy,make_response
# from conf.setting import*
# from tools import MyConnect，OpRedis，md5_passwd
#
#
# server = flask.Flask(__name__)   #把当前文件当做一个服务
# @server.route("/login",["get,post"])  #定义当前接口的请求方式和路径
# mysql=MyConnect(host=XXX,port=XXX,user=XXX,passwd=XXX,db=XXX)
# myredis=OpRedis(host=XXX,port=XXX,password=XXX)
# def login():
#     username = request.values.get('username','')
#     passwd = request.values.get('pwd','')
# #values.get这种方式是XXX/login？username=888&pwd=1111的请求方式
# #request.json.get("username","")   请求方式必须是json的 比如{"username":"wjx"}
#     if username.strip() and passwd.strip():
#         passwd = md5_passwd(passwd)
#         sql='select id,username from user where username="%s" and password="%s"'%(username,passwd)
#         sql_res = mysql.select_sql(sql)
#         if sql_res:
#             sign_str = username+str(int(time.time()))
#             sign = md5_passwd(sgn_str)
#             myredis.insert_redis(username,sign)
#             return jsonfy({"msg":"登陆成功！！！","code":"10000"})
#             #下面是操作cookie的操作
#             # response = make_response('{"msg":"登录成功""sign":"%s","userName":"%s"}'%(sign,username))
#             # response.set_cookie(username,sign)#设置cookie
#             # return response
#         else:
#
#              return jsonfy({"msg":"登陆失败","code":"1009"})
#
#         else:
#
#             return jsonfy({"msg":"用户名和密码都不能为空"，"code":"1001"})