# _*_ coding: utf-8 _*_
#2013/4/1
#通过hook键盘和鼠标，记录搜索历史记录（hook鼠标还存在问题） 
#先只考虑用使用google chrome ，百度搜索的情况
#需要安装pyHook 和 pywin32
import pyHook,pythoncom
import sys
impor win32api
#全局变量，用来存放上次搜索结果
preRes = 'solo'

#搜索记录保存到文件
def Save(res):
    global  preRes
    if(res!=preRes):
try:
   f = open('.\searchLog.dat','a')
except IOError:
   print '记录文件不存在，创建中。。。'
   f = open('.\searchLog.dat','w')
f.write(res)
f.write('\n')
#和C语言一样，打开文件后一定记得关闭
f.close()
preRes = res
    return True

def OnKeyboardEvent(event):
    print "WindowName:",event.WindowName
    #ctrl+z 退出监控程序
    if event.Ascii == 26:
print 'exiting...'
        #停止监控循环
        win32api.PostQuitMessage()
#sys.exit(1)
    elif str(event.WindowName).startswith('百度搜索'):
name = event.WindowName
#从网页题目获得搜索结果
res = name[9:name.rfind(' - Google Chrome')]
Save(res)
print 'keyboard hook finished--'
    return True

def OnMouseEvent(event):
    if str(event.WindowName).startswith('百度搜索'):
name = event.WindowName
res = name[9:name.rfind(' - Google Chrome')]
Save(res)
    print 'mouse hook finished--'
    return True

#pyHook典型用法
#1 定义HookManager
#2将event与handle绑定
#3启动Hook  
#4开始循环获取消息
hm=pyHook.HookManager()
hm.KeyDown=OnKeyboardEvent
hm.MouseAll=OnMouseEvent
hm.HookKeyboard()
hm.HookMouse()
pythoncom.PumpMessages()
