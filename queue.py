# coding=utf-8
#队列的实现
class Queue():
    def __init__(qu,size):
        qu.queue=[]
        qu.size=size
        qu.head=-1
        qu.tail=-1
    def enQueue(qu,content):
        if qu.Full():
            print "队列已满"
        else:
            qu.queue.append(content)
            qu.tail=qu.tail+1
    def outQueue(qu):
        if qu.Empty():
            print "队列是空的"
        else:
            qu.head=qu.head+1
    def Full(qu):
        if qu.tail-qu.head+1==qu.size:
            return True
        else:
            return False
    def Empty(qu):
        if qu.head==qu.tail:
            return True
        else:
            return False
q=Queue(10)
q.Empty()
q.enQueue("1")
q.Empty()
q.outQueue()

