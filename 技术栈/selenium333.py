from requests_html import  HTMLSession
from fake_useragent import UserAgent
ua = UserAgent()
session = HTMLSession()
from selenium import webdriver  # 导入webdriver模块
from  PIL import Image
import base64


driver= webdriver.Chrome()

start_url = 'http://www.jianjiaoshuju.com/path/login.htm'

driver.maximize_window()

driver.get(start_url)
driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[1]/input').send_keys('18607005060')
driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[2]/input').send_keys('as123456')
#截图
driver.save_screenshot('首页.png')

img = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[3]/div/span/img')

location = img.location

size = img.size

left = location['x']+380
top = location['y']+120
right = left + size['width']
bot  = top +size['height']

photo = Image.open('首页.png')
img_obj = photo.crop((left,top,right,bot))
img_obj.save('验证码.png')
with open('验证码.png','rb')as f:
    bese64_data = base64.b64encode(f.read()).decode()

headers = {
'AppCode':'29A08C825BE129FA140DA10229635E92',
'AppKey':'AKID9dfe09ad375ae1984ecdbd40df3a9382',
'AppSecret':'afcf06b1c6f9f86b0eb489dd5f934689',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

img_url = 'http://apigateway.jianjiaoshuju.com/api/v_1/yzmCustomized.html'
data = {
    'v_pic':bese64_data,
    'pri_id':'ne'
}
json_data = session.post(img_url,data=data,headers=headers).json()
# print(json_data)
driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[3]/div/div/input').send_keys(json_data['v_code'])
driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[4]/button').click()
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[3]/a').click()