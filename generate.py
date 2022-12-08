# -*- coding: utf-8 -*-
# @Time    : 2022/12/8 12:33
# @Author  : AI悦创
# @FileName: generate.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
import os
from urllib.parse import urljoin

TEMPLATE = '<VideoPlayer src="{url}" />'


def save(urls: list):
    html = """# SQL-MySQL-
SQL/MySQL 零基础从入门到精通
"""
    code = """```url
{}
```
"""
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(html)
        for url in urls:
            content = code.format(url)
            f.write(content + "\n")


def generate_path():
    BASE = "https://github.aiyc.top/SQL-MySQL-Easy-Learn/"
    target = ["mp4", ]
    result = []
    for root, _, filenames in os.walk("."):
        for name in filenames:
            suffix = name.split(".")[-1].lower()
            # print(suffix)
            if suffix not in target:
                continue
            url = urljoin(BASE, os.path.join(root, name))
            url = TEMPLATE.format(url=url)
            yield url

if __name__ == '__main__':
    r = generate_path()
    for i in r:
        print(i)