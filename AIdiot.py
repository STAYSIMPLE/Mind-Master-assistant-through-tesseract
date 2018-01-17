# -*- coding: utf-8 -*-

#Ai ver.2.0 by Simpleson -A Junior PyLearner->(ง •_•)ง,

#ver1.0作者:Aitext from  by manoshape on Github
DEBUG=1
import urllib.request,_thread,urllib.parse
import webbrowser
from my_threading import SubThread
class Ai:
    #I/O func:
    def __init__(self,issue='',answer={}): # 起始函数
        self.issue = issue
        self.answer = answer
        self.ans_count ={}
        self.ans_detail={}#{site:{A:1,B:2,C:3,D:4}}
        self.webstr={}
    #tool func:
    def biggest(self,d={}):  #取最大值
        for j in d:
            m=j
            break
        for j in d:
            if d[j]>=d[m]:m=j
        return m

    #sub-process func:
    def search(self):           #要搜索的引擎
        #可以自己添加搜索接口  self.threhtml(网址) .
        _s={}
        _s['BaiDu_ZhiDao']  =SubThread( self.gethtml , ('https://zhidao.baidu.com/search?lm=0&rn=10&pn=0&fr=search&ie=gbk&word='+urllib.parse.quote(self.issue,encoding='gbk'),) )
        _s['Sogou_WenWen']  =SubThread( self.gethtml , ('http://wenwen.sogou.com/s/?w='+urllib.parse.quote(self.issue)+"&ch=ww.header.ssda",) )
        _s['Sina_Iask']     =SubThread( self.gethtml , ('https://iask.sina.com.cn/search?searchWord='+urllib.parse.quote(self.issue)+"&record=1",) )
        #360需要验证码,不予考虑#_s['360So_WenDa']   =SubThread( self.gethtml , ('https://wenda.so.com/search/?q='+urllib.parse.quote(self.issue),) )
        for i in _s:
            _s[i].join()
            self.webstr[i]=_s[i].out()


    def gethtml(self,url=''):
        #get:
        headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
        opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        date = opener.open(url).read()
        #Decode:
        if "zhidao.baidu.com" in url:
            str1=date.decode('gbk').encode('utf-8').decode('utf-8')
        else:
            str1=str(date,"utf-8")
        #Report:
        return str1

    def printans(self):#输出答案
        for i in self.answer:self.ans_count[i]=0
        for j in self.webstr:
            self.ans_detail[j]={}
            for i in self.answer:
                self.ans_detail[j][i]=self.webstr[j].count(self.answer[i])
                self.ans_count[i]=self.ans_count[i]+self.ans_detail[j][i]

        if self.issue.count('不')or self.issue.count('没有') or self.issue.count('从未'): 
            for i in self.ans_count:self.ans_count[i]=-self.ans_count[i]
        ans=self.biggest(self.ans_count)
        if DEBUG:self.printdebug(DEBUG)
        print(self.issue)
        print('---------------------------------')
        print(' 选项    出现次数  ')
        for j in self.answer:
            print(j+': '+self.answer[j]+'    '+str(self.ans_count[j]))
        print('---------------------------------')
        print('  推荐答案：' +ans+': '+ self.answer[ans])
        print('---------------------------------')
        return ans
    def printdebug(self,level=1):
        if level>1:
            str_dbg={}
            for j in self.webstr:
                str_dbg[j]=self.webstr[j]
                print(j+':')
                for i in range(1,127):
                    str_dbg[j]=str_dbg[j].replace(chr(i),'')
                print(str_dbg[j])
        if level>0:
            for i in self.ans_detail:
                print(i+':')
                print(self.ans_detail[i])
