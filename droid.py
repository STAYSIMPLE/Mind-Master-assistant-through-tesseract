# -*- coding: utf-8 -*-
"""
    
         ___     ___
        |   |___|   |
        |___|   |___|
        
             = =
    
    
-Stay Simple
=Live Young
2018/01/14 00:12 

"""
################################

"""
droid:对接ADB常用命令
ver 1.1:用subprocess.call替换os.system
ver 1.0:创建文档
"""
import subprocess
from PIL import Image
const_path = 'capture.png'#DO NOT CHANGE WHEN RUNNING
def swipe(xa,ya,xb,yb,t):
    #单指操作
    cmd = 'adb shell input swipe {x1} {y1} {x2} {y2} {duration}'.format(
        x1=xa,
        y1=ya,
        x2=xb,
        y2=yb,
        duration=t
    )
    subprocess.call(cmd,shell=1)
    return 0
i=0
j=1
def getscreen():
    #截屏返回
    global i
    global j
    subprocess.call('adb shell screencap -p /sdcard/'+const_path,shell=1)
    subprocess.call('adb pull /sdcard/'+const_path+' .',shell=1)
    if j==1:
        j=0
        i=i+1
    else:j=1
    return Image.open(const_path)#('capture'+str(i)+'.png')
    

def printscreen():
    #截屏'
    subprocess.call('adb shell screencap -p /sdcard/'+const_path,shell=1)
    subprocess.call('adb pull /sdcard/'+const_path+' .',shell=1)
