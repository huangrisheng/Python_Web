# -*- coding: utf-8 -*- 
"""
    @Time : 2019/7/31 下午8:51 
    @Author : 黄任添 
    @File : test4.py 
    @Software: PyCharm
    note:
        1.Thread Condition线程锁二
        2.条件变量, 用于复杂的线程间同步
"""
from threading import Thread, Condition, RLock
import time


# 小爱同学和天猫精灵对话,方式一
# class Thread1(Thread):
#     def __init__(self, lock):
#         super().__init__(name='小爱同学')
#         self.lock = lock
#
#     def run(self) -> None:
#         self.lock.acquire()
#         print("{}: 在!".format(self.name))
#         self.lock.release()
#
#         self.lock.acquire()
#         print("{}: 好呀!".format(self.name))
#         self.lock.release()
#
#
# class Thread2(Thread):
#     def __init__(self, lock):
#         super().__init__(name='天猫精灵')
#         self.lock = lock
#
#     def run(self) -> None:
#         self.lock.acquire()
#         print("{}: 小爱同学!".format(self.name))
#         self.lock.release()
#         time.sleep(0.1)
#         self.lock.acquire()
#         print("{}: 我们来对故事吧!".format(self.name))
#         self.lock.release()
# 方式一,不成功,现象:先执行的线程先结束.但是实际情况不一定


# 小爱同学和天猫精灵对话,方式二, 新锁condition
class Thread1(Thread):
    def __init__(self, cond):
        super().__init__(name='小爱同学')
        self.cond = cond

    def run(self) -> None:
        # with self.cond: # 方式一:写一句
        self.cond.acquire()  # 方式二:写两句
        self.cond.wait()
        print("{}: 在!".format(self.name))
        self.cond.notify()

        self.cond.wait()
        print("{}: 好呀!".format(self.name))
        self.cond.notify()

        self.cond.wait()
        print("{} : 君住长江尾 ".format(self.name))
        self.cond.notify()

        self.cond.wait()
        print("{} : 共饮长江水 ".format(self.name))
        self.cond.notify()

        self.cond.wait()
        print("{} : 此恨何时已 ".format(self.name))
        self.cond.notify()

        self.cond.wait()
        print("{} : 定不负相思意 ".format(self.name))
        self.cond.release()


class Thread2(Thread):
    def __init__(self, cond):
        super().__init__(name='天猫精灵')
        self.cond = cond

    def run(self) -> None:
        with self.cond:
            print("{}: 小爱同学!".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}: 我们来对故事吧!".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 我住长江头 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 日日思君不见君 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 此水几时休 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 只愿君心似我心 ".format(self.name))
            self.cond.notify()

if __name__ == '__main__':
    # 方式一
    # lock = RLock()
    # thread1 = Thread1(lock)
    # thread2 = Thread2(lock)
    # thread2.start()
    # thread1.start()

    # 方式二
    cond = Condition()
    thread1 = Thread1(cond)
    thread2 = Thread2(cond)
    thread1.start()
    thread2.start()

    # 启动顺序很重要
    # 在调用with cond之后才能调用wait和notify方法
    # condition有两层锁,一把底层锁,会在线程滴啊用了wait方法的时候释放,上面的锁会在每一次调用wait的时候分配一把并入到cond
    # 等待队列中,等到notify方式的唤醒
