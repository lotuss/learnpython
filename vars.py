# coding=utf-8
# from modle1 import add
# i=7
# j=9
# add(i,j)
# str = raw_input("请输入：");
# print "你输入的内容是: ", str
class Stack():
    def __init__(st,size):
        st.stack=[];
        st.size=size;
        st.top=-1;
    def push(st,content):
        if st.Full():
            print "Stack is Full!"
        else:
            st.stack.append(content)
            st.top==st.top+1
    def out(st):
        if st.Empty():
            print "Stack is Empty!"
        else:
           st.top== st.top-1
    def Full(st):
        if st.top==st.size:
            return True
        else:
            return False
    def Empty(st):
        if st.top==-1:
            return True
        else:
            return False
q=Stack(7)
q.Empty()
q.push("hello")
q.Empty()
q.out()
import time
ticks=time.time()
print "时间为",ticks
localtime=time.localtime(time.time())
print "当地时间为:",localtime
localtime=time.asctime(time.localtime(time.time()))
print"格式化时间为:",localtime
import calendar
cal=calendar.month(2016,3)
print "此日历为："
print cal
#可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1,2,3,4]);
    print "函数内取值:",mylist
    return
#调用changeme函数
mylist=[10,20,30];
changeme(mylist)
print "函数外取值：",mylist


