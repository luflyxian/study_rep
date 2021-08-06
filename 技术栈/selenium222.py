#pip install requests-html
#pip install selenium
from selenium import webdriver  # 导入webdriver模块

driver= webdriver.Chrome()

start_url = 'https://mail.163.com/'

driver.get(start_url)

el = driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(el)
driver.find_element_by_name('email').send_keys('a1282477979')
driver.find_element_by_name('password').send_keys('as123456')
driver.find_element_by_id('dologin').click()

# print(driver.get_cookies())
cookie_dict = {cook['name']:cook['value'] for cook in driver.get_cookies()}
# print(cookie_dict)

from requests_html import  HTMLSession
from fake_useragent import UserAgent
ua = UserAgent()
session = HTMLSession()
headers = {
    'referer':'https://mail.163.com/js6/main.jsp?sid=CAiQCTllGjJreEAmzIllADruXfECEvub&df=mail163_letter',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}
next_url = 'https://mail.163.com/js6/main.jsp?sid=XDDyprvSFyxRMUbJMfSSvIpsMTSqpzmR&df=mail163_letter#module=welcome.WelcomeModule%7C%7B%7D'
response = session.get(next_url, cookies=cookie_dict, headers=headers)
print(response.content.decode())