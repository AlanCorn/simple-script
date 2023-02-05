# -*- coding: utf-8 -*-
# 自用爬虫脚本，用于批量下载telegra.ph图片，基于selenium
import os
import re
import time
from tqdm import tqdm, trange

import requests
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(30)  # 隐性等待,确保网站加载完全

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}

url_list = [
    'https://telegra.ph/xxxxx'
]

# response = requests.get(url)
# print(response)  # 可以事先测试一下连接, 若返回结果为418，200为请求成功，418则是对方发现咱们是爬虫了,则需要修改header等内容

title_pattern = re.compile(r'<title>(.*?)<\/title>')
img_pattern = re.compile(r'<img src="(.*?)"')
base_img_url = "https://telegra.ph"  # 图片url补全
root_dir = r"D:\xxx\xxx"  # 保存路径,不要带上最后的斜杠
data = []  # 存储爬到的所有数据

for _, url in zip(tqdm(range(len(url_list)), desc='正在爬取链接列表中的内容'), url_list):
    driver.get(url)
    content = driver.page_source
    title = re.findall(title_pattern, content)
    img_url = re.findall(img_pattern, content)  # re.DOTALL忽略格式#匹配objURL的内容,大部分为objURL或URL
    data.append((title, url, img_url))  # 将获取到的图片地址保存在之前定义的列表中
    time.sleep(3)

# response = requests.get(url, headers=headers)  # 请求网站
# content = response.content

for page in data:
    title = page[0][0]
    index = 0  # index重置
    save_dir = "{}\\{}".format(root_dir, title)
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    for _, url in zip(tqdm(range(len(page[2])), desc='正在下载 {}'.format(title)), page[2]):
        full_url = url  # selenium 直接爬出了全地址,所以无需补全
        while True:
            try:
                response = requests.get(full_url, headers=headers)
                break
            except Exception as ero:
                pass
                # print('\n下载出现异常{},已重新尝试下载'.format(full_url))
                # print(ero)
        content = response.content
        save_file_path = ''
        if url[-3:] == 'jpg':
            save_file_path = r'{0}\{1}-{2}.jpg'.format(save_dir, index, title)
        elif url[-4:] == 'jpeg':
            save_file_path = r'{0}\{1}-{2}.jpeg'.format(save_dir, index, title)
        elif url[-3:] == 'png':
            save_file_path = r'{0}\{1}-{2}.png'.format(save_dir, index, title)
        else:
            continue
        with open(save_file_path, 'wb') as f:
            f.write(content)
        response.close()
        time.sleep(1)
        index += 1
driver.quit()
