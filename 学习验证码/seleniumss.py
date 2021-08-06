from requests_html import  HTMLSession
from fake_useragent import UserAgent
ua = UserAgent()
session = HTMLSession()
from selenium import webdriver
import time,random
import base64
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()

driver.get('https://kyfw.12306.cn/otn/resources/login.html')

driver.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()
driver.find_element_by_xpath('//*[@id="J-userName"]').send_keys('15179506922')
driver.find_element_by_xpath('//*[@id="J-password"]').send_keys('as123456')
time.sleep(random.randint(1,2))

# js = 'scrollTo(0,500)'
# driver.execute_script(js)  #鼠标向下滑动

img = driver.find_element_by_xpath('//*[@id="J-loginImg"]')

img.screenshot('12306验证码.png')

with open('12306验证码.png','rb')as f:
    bese64_data = base64.b64encode(f.read()).decode()

headers = {
'AppCode':'29A08C825BE129FA140DA10229635E92',
'AppKey':'AKID9dfe09ad375ae1984ecdbd40df3a9382',
'AppSecret':'afcf06b1c6f9f86b0eb489dd5f934689',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

img_url = 'http://apigateway.jianjiaoshuju.com/api/v_1/yzmCrd.html'
data = {
    'v_pic':bese64_data,
    'v_type':'crd'
}
response = session.post(img_url,data=data,headers=headers).json()
print(response)
v_code = response['v_code']
for code in v_code.split('|'):
    x = int(code.split(',')[0])
    y = int(code.split(',')[1])
    ActionChains(driver).move_to_element_with_offset(img, x, y).click().perform()
time.sleep(random.randint(1,2))
driver.find_element_by_xpath('//*[@id="J-login"]').click()
time.sleep(random.randint(1,2))
div_size_obj = driver.find_element_by_xpath("//*[@class='nc-lang-cnt'][1]")

div_size = div_size_obj.size

button = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')

button_location = button.location

y = button_location['y']
# action = ActionChains(driver)
# action.click_and_hold(button).perform()
# action.move_by_offset(332,0)
# action.release().perform()

ActionChains(driver).click_and_hold(button).move_by_offset(y,0).perform()