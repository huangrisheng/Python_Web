# -*- coding: utf-8 -*- 
"""
    @Time : 2019/8/1 上午10:32 
    @Author : 黄任添 
    @File : test1.py 
    @Software: PyCharm
    note:
        1.通过queue的方式进行线程间同步
"""
# 线程间共享变量
import time
import threading

# 1. 生产者当生产出10个URL以后就等待,保证detail_url_list中最多只能有十个url
# 2. 当url_list为空的时候,消费者站厅
deta_url_lists = []
