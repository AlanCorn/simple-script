# -*- coding: utf-8 -*-
# 自用爬虫脚本，用于批量下载telegra.ph图片，基于requests
import os
import re
import time
from tqdm import tqdm, trange

import requests

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
    response = requests.get(url, headers, timeout=60)  # 设置请求超时时间3-7秒
    content = response.content.decode('utf-8')  # 使用utf-8进行解码
    title = re.findall(title_pattern, content)
    img_url = re.findall(img_pattern, content)  # re.DOTALL忽略格式#匹配objURL的内容,大部分为objURL或URL
    data.append((title, url, img_url))  # 将获取到的图片地址保存在之前定义的列表中
    response.close()
    time.sleep(1)

# response = requests.get(url, headers=headers)  # 请求网站
# content = response.content

for page in data:
    title = page[0][0]
    index = 0  # index重置
    save_dir = "{}\\{}".format(root_dir, title)
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    for _, url in zip(tqdm(range(len(page[2])), desc='下载 {}'.format(title)), page[2]):
        full_url = base_img_url + url
        while True:
            try:
                response = requests.get(full_url, headers=headers)
                break
            except Exception as ero:
                print('\n下载出现异常{},已重新尝试下载'.format(full_url))
                print(ero)
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
