# -*- coding: utf-8 -*-
'''
子线程: 自动运行&有返回值
'''

from threading import Thread
import time

#debug模式:
#debug=1:显示线程用时:    <线程xxx  用时xxx秒>
DEBUG=0

#有返回值的线程
class SubThread(Thread):
    def out(self):  
        return self.output 

    #返回值窃取函数
    def trace_func(self, func,*args,**kwargs):
        t=time.time()
        self.output = self.func(*args,**kwargs)
        if DEBUG==True: print('<线程'+self.func.__name__+'\t用时:'+str(round(time.time()-t,2))+'秒>')
    def __init__(self,func,args=(),daemon=True):
        self.func=func
        arg_list=[]
        arg_list.append(func)
        for index in args:
            arg_list.append(index)
        arg=tuple(arg_list)
        Thread.__init__(self,target=self.trace_func,args=arg,daemon=daemon)
        self.start()
        #输出:output初始化为0
        self.output=0

