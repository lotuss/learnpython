# coding=utf-8
#python类
class hello:
    #构造方法
    def __init__(self,name):
        self._name=name
    def sayhello(self):
        print("hello {0}".formatx(self._name))
#继承
class hi(hello):
    def __init__(self,name):
        hello.__init__(self,name)
    def sayhi(self):
        print("hi {0}".format(self._name))
h=hello("煞笔")
h.sayhello()

h1=hi("贱人")
h1.sayhi()