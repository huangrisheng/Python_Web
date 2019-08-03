# -*- coding: utf-8 -*- 
"""
    @Time : 2019/7/31 下午5:52 
    @Author : 黄任添 
    @File : TCP_http.py 
    @Software: PyCharm
    note:
        1.使用socket发送http请求
"""
import socket
from urllib.parse import urlparse


def get_url(url):
    url_path = urlparse(url)
    # print(url_path)
    host = url_path.netloc
    path = url_path.path
    # 创建socket对象
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 创建连接
    client.connect((host, 80))
    # 发送数据
    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
    # 接送数据
    data = b''
    while True:
        # 每次读取1k数据
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)


if __name__ == '__main__':
    url = "http://shop.projectsedu.com/goods/1/"
    get_url(url)
