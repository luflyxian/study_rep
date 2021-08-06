import requests
import time
import json

def get_first_url(url,data,headers):
    response = requests.post(url=url, data=data, headers=headers)
    # response.encoding = "utf-8"
    # pages_text = response.text
    print(response)

    #'‪C:\Users\未来时刻\Desktop\try.txt'
    print(f"一共花费{time.time() - start}")

if __name__ == "__main__":
    start = time.time()
    
    url = 'http://data.chineseafs.org/report/ajax/chart_info/60374d590ee9c30001b2d655/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.49"
    }
    data = {"page":"2","question_id":"6034d6979fc2a2d4e4f45d23","__xsrf":"2|140188cc|fd194ca5bba93eb13aab0bc8f000aa1a|1615795014"}
    get_first_url(url,data,headers)
