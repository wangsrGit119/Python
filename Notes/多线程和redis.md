#### **多线程和 redis相关代码**

 ---
 
 - 代码
 ```
 import redis
import threading

r = redis.Redis(host='192.168.99.243', port=6379, db=0, password='cebon')
exitFlag = 0


def redis_operation():
    # r.set("pyTestKey", 10000000000000)
    # r.delete("test")
    print(r.decr("pyTestKey", 1))


class myThread(threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print("Starting " + self.name)
        print_time(self.name, self.counter, "pyTestKey")
        print("Exiting " + self.name)


def print_time(thread_name, counter, key):
    print(thread_name)
    print(r.incr(key, 1))


if __name__ == '__main__':
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)
    # 开启线程
    thread1.start()
    thread2.start()

 
 ```
