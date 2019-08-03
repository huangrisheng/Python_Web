# -*- coding: utf-8 -*- 
"""
    @Time : 2019/8/1 上午10:10 
    @Author : 黄任添 
    @File : test5.py 
    @Software: PyCharm
    note:
        1. Samphore是用于控制进入数量的锁
        2. 在编写代码中,特别是文件操作,写一般只是单线程写,读可以允许多个
        3. 但是在编写网络爬虫的过程中,我们需要控制线程的允许数量
"""
import threading
import time


class HtmlSpider(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self) -> None:
        time.sleep(2)
        print(self.url)
        self.sem.release()  # 解锁,释放


class UrlSpider(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self) -> None:
        for i in range(20):
            self.sem.acquire()  # 上锁,控制
            htmlspider = HtmlSpider("http://www.baidu.com/{}".format(i), self.sem)
            htmlspider.start()


if __name__ == '__main__':
    sem = threading.Semaphore(3)  # 创建控制线程的数量
    url_producer = UrlSpider(sem)
    url_producer.start()
