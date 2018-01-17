# -*- coding: utf-8 -*-
"""
         ___     ___
      |_|   |___|   |_|
      | |___|   |___| |
        
             = =
         \_________/

me=Stay Simple
my=Live Young

"""
################################
"""
瞎玩系列:头脑王者辅助脚本
思路: 识别图像 ->爬关键字-> 统计词频
"""
import subprocess
import pytesseract
from PIL import Image
import time #用于 计时器
##local_series:
from my_threading import SubThread
import droid
from AIdiot import Ai
import random

#debug模式:保存截图与答案
DEBUG=False
DEBUG_i=1
#需要手动完成的初始化操作:
#请根据题目\手机型号不同,手动调节识别区域= =||
box_mi5={
     'Q':(120,600, 960,880 ),#问题
     'A':(280,1000,800,1100),#选项A
     'B':(280,1190,800,1270),#选项B
     'C':(280,1380,800,1460),#选项C
     'D':(280,1580,800,1650)}#选项D
box_mi5_learn={#审题版
     'Q':(120,440, 960,660 ),#问题
     'A':(280,910 ,800,970 ),#选项A
     'B':(280,1110,800,1170),#选项B
     'C':(280,1310,800,1380),#选项C
     'D':(280,1510,800,1570)}#选项D
box=box_mi5
boxQ={'Q':box['Q']} #确定问题列表{Q}
boxA=box            #确定选项列表{ABCD}
boxA.pop('Q')       

_Lang='chi_sim'

# pytesseract:CHANGE THIS IF TESSERACT IS NOT IN YOUR PATH, OR IS NAMED DIFFERENTLY
#pytesseract.tesseract_cmd = 'tesseract'


#计时器
t2=0
t1=time.clock()
def dt(n=3):
    global t1,t2
    t2=t1
    t1=time.clock()
    return round(t1-t2,n)

#提取文字的线程池
def im_to_str_thread(img,box={},cfg='-psm 7',join=True):
    imgs={}
    todo={}
    text={}
    for i in box:
        imgs[i]=img.crop(box[i])
        todo[i]=SubThread(func=pytesseract.image_to_string,args=(imgs[i],'chi_sim',0,cfg))
    if join:
        for j in todo:
            todo[j].join()
    #返回{SubThread},todo[j].out()即为识别结果.
    return todo

def box_click(box):
    (x1,y1,x2,y2)=box
    x=(x1+x2)/2+random.randint(-100,100)
    y=(y1+y2)/2+random.randint(-20,20)
    droid.swipe(x,y,x,y,0)
    #多线程:
    #[截屏1(usb)]-[问题提取(cpu)]- [问题检索(web)]- [答案查找(pycode)]
    #            \[截屏2(usb)]   -[答案提取(cpu) ]/
def main():
    input(str(dt())+":Enter for Q")
    dt()
    #[截屏1][问题提取
    img=droid.getscreen()
    print('==截图用时:'+str(dt())+'秒')
    threadQ=im_to_str_thread(img,boxQ,'-psm 6',join=0)
    #[截屏2]
    #input("Enter for A")
    threadS=SubThread(func=droid.getscreen)
    threadS.join()
    #问题提取]
    for i in threadQ:
        threadQ[i].join()
        Question=threadQ[i].out()
        Question=Question.replace(' ', '')
    print('==问题用时:'+str(dt())+'秒')
    #[答案提取
    img=threadS.out()

    threadA=im_to_str_thread(img,boxA,'-psm 7',join=0)

    #[问题检索
    ai=Ai(Question)
    threadAi=SubThread(func=ai.search)
    #问题检索]
    threadAi.join()
    #答案提取][答案查找
    Answer={}
    for i in threadA:
        threadA[i].join()
        Answer[i]=threadA[i].out()
        Answer[i]=Answer[i].replace(' ', '')
    print('==答案用时:'+str(dt())+'秒')
    #答案查找]
    ai.answer=Answer
    ans=ai.printans()  
    box_click(boxA[ans])
    print(boxA[ans])
    if DEBUG:
        global DEBUG_i
        time.sleep(0.7)
        img=droid.getscreen()
        img.save('capture'+str(DEBUG_i)+'.png')
        DEBUG_i+=1
    print('=================================')
if __name__ == '__main__':
    while True:
        main()
