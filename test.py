# -*- coding: utf-8 -*-
import re

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(20) # 隐性等待，最长等30秒
driver.get('https://telegra.ph/%E8%A0%A2%E6%B2%AB%E6%B2%AB%E6%A3%92%E7%90%83%E5%A5%B3%E5%AD%A91%E6%9C%882%E6%89%93%E8%B5%8F%E7%BE%A4%E8%B5%84%E6%BA%90-01-02')

img_pattern = re.compile(r'<img src="(.*?)"')
# 获取页面源代码
html_source = driver.page_source
img_url = re.findall(img_pattern, html_source)  # re.DOTALL忽略格式#匹配objURL的内容,大部分为objURL或URL

print(html_source)
print(len(img_url))
# 重点
# html = lxml.html.fromstring(html_source)
# 获取标签下所有文本
# items = html.xpath("//div[@id='y_prodsingle']//text()")
