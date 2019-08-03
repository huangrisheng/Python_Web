# -*- coding: utf-8 -*- 
"""
    @Time : 2019/7/31 下午7:15 
    @Author : 黄任添 
    @File : test2.py
    @Software: PyCharm
    note:
        1.Thread线程的创建方式以及常见的属性和方法
    Thread相关知识:
        1. 创建线程 threading.Thread(target=函数名, args=参数列表(元组))
        2. 启动线程 start()
        3. 加入主线程(作用: 阻止主线程向下执行,) join()
        4. 守护线程 setDaemon()
        5. 判断线程的状态 is_alive(), 未启动为False,启动为True
        6. 设置线程名称 setName(name)
        7. 获取线程名称: getName()

    注意:
        对于IO操作而言,多线程和多进程的性能差别不大,
"""
import threading
import time


# 01. 创建线程的方式一
def get_detail_html(url):
    print("get detail html start")
    time.sleep(0.5)
    print("get detail html end")


def get_detail_url(url):
    print("get detail url start")
    time.sleep(1)
    print("get detail url end")


# 02. 创建线程的方式二
class Thread1(threading.Thread):
    def run(self) -> None:
        print("get detail html start")
        time.sleep(0.5)
        print("get detail html end")


class Thread2(threading.Thread):
    def run(self) -> None:
        print("get detail url start")
        time.sleep(1)
        print("get detail url end")


# 03. 创建多线程方式二, 扩展点
class Thread3(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self) -> None:
        print("{}真漂亮!".format(self.name))
        time.sleep(0.5)
        print("{}太帅了!".format(self.name))


if __name__ == '__main__':
    # 创建多线程方式一,启动线程的方式
    # thread1 = threading.Thread(target=get_detail_html, args=(1,))
    # thread2 = threading.Thread(target=get_detail_url, args=(2,))
    # 启动多线程
    # thread1.start()
    # thread2.start()
    # 加入主线程
    # thread1.join()
    # thread2.join()
    # print("Main Thread start...")

    # 创建多线程方式二,启动线程的方式
    thread1 = Thread1()
    thread2 = Thread2()
    print("线程二存活状态:", thread2.is_alive())
    thread1.setName("hello")
    thread1.setDaemon(True)
    thread2.setDaemon(True)
    thread1.start()
    thread2.start()
    # 加入主线程
    # thread1.join()
    # thread2.join()
    print("线程二存活状态:", thread2.is_alive())
    print("线程一的名称:", thread1.getName())
    print("Main Thread start...")

    print("*" * 30)
    thread3 = Thread3(name="佳琪")
    thread3.start()
