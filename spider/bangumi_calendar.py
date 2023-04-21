# -*- coding: utf-8 -*-
# 自用爬虫脚本，用于爬取https://bgm.tv/中当前季度的追番表，返回id
import os
import re
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(30)  # 隐性等待,确保网站加载完全

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}

url = 'https://bgm.tv/calendar'

# response = requests.get(url)
# print(response)  # 可以事先测试一下连接, 若返回结果为418，200为请求成功，418则是对方发现咱们是爬虫了,则需要修改header等内容

bangumi_id_pattern = re.compile(r'<a href="/subject/(.*?)" class="nav">.*?</a>')
data = []  # 存储爬到的所有数据

driver.get(url)
content = driver.page_source
bangumi_id = re.findall(bangumi_id_pattern, content)
data.append(bangumi_id)  # 将获取到的图片地址保存在之前定义的列表中
time.sleep(3)

# response = requests.get(url, headers=headers)  # 请求网站
# content = response.content
print(data)
