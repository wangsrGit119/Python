   **`__init__和self以及__name__=="__main__"演示代码`**
 ---
- 概念
     1. `__init__`: 本例用于class对象的初始化构造参数
     2. `self` 代表当前对象
     3. `__name__=="__main__"` 当另一个引用他的模块执行时 他后面的代码不会被执行  也就是属于自己的当前的模块执行体
 - 代码
 
  > responseClass.py
 ```python
    from  httpTest import result
    
    
    class Response(object):
        def __init__(self, code, data, message):
            self.code = code
            self.data = data
            self.message = message
    
        def tostring(self):
                print(self.code, self.data, self.message)
    
    
    if result == "error":
        print("error http request")
    else:
        re = Response(result["code"], result["data"], result["msg"])
        re.tostring()

```
  > httpTest.py

 ```python
    import requests
    import json
    
    
    def get(url):
        res = requests.get(url)
        stringres = res.text
        obj = json.loads(stringres)
        if isinstance(obj, object):
            if obj["code"] == 200:
                return obj
            else:
                return "error"
    
    
    url = "http://192.168.99.34:8002/quartz/getSysInfo"
    result = get(url)
    if __name__ == "__main__":
        print("result ", result)  # 当前的执行结果在另一个模块调用时是不会执行的

```
