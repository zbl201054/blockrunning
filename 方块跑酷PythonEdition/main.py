import time
from pgzrun import *
HEIGHT = 500
WIDTH = 890
bg = Actor("bg.jpg")
tm = Actor("radishstudio.png",(445,250))
bj = Actor("bj.png",(480,480))
jd = Actor("jd1.png",(445,350))
fk = Actor("fk.png",(440,250))
jz = Actor("jz.png",(445,320))
dl = Actor("dl.png",(450,320))
zc=Actor("注册.png",(360,320))
fk1=Actor("fk1.png")
m = '开始'
i = 1
#f0=open("用户名.txt","r",encoding="utf-8")
#f1=open("password.txt","r",encoding="utf-8")
#f2=open("用户名.txt","w",encoding="utf-8")
#f3=open("password.txt","w",encoding="utf-8")
dl1 = Actor("dl.png",(450,320))
dl2=""
q=""
bbh=Actor("版本.png",(800,30))
def draw():
    global m
    screen.clear()
    bg.draw()
    if (m == '开始'):
        tm.draw()
        bj.draw()
    if (m == '加载'):
        jd.draw()
        fk.draw()
        jz.draw()
    if (m == '登录'):
        fk.draw()
        dl.draw()
    if m=="登录界面":
        fk.draw()
        zc.draw()
        dl1.draw()
    if m=="主屏幕":
        fk1.draw()
        bbh.draw()

def new0():
    global m
    m = '加载'

def new1():
    global m
    m = '登录'
def new2():
    global m,q
    m="登录界面"
def jd0():
    global i #全局变量
    if i < 6:
        i += 1
def dl0():
    global m
    m="主屏幕"
def update():
    global m, i,dl2
    if (m == '开始'):
        clock.schedule(new0,3.0)
    if (m == '加载'):
        jd.image = ('jd' + str(i))
        clock.schedule(jd0,1.0)
        clock.schedule(new1,3.0)
    if m=="登录":
        if q=="dljm":
            clock.schedule(new2,1)
    if m=="登录界面":
        if dl2=="成功":
            clock.schedule(dl0,1)

def on_mouse_down(pos):
    global m,f0,f1,f2,f3,dl2,dl1,q
    if m=="登录":
        q="dljm"
    if m=="登录界面":
        if dl1.collidepoint(pos):
            f0=open("用户名.txt","r",encoding="utf-8")
            f1=open("password.txt","r",encoding="utf-8")
            print("Hello,"+f0.read())
            password=input("请输入密码：")
            if password==f1.read():
                print("密码正确")
                f0.close()
                f1.close()
                dl2="成功"
            else:
                print("密码错误")
                dl2="错误"
        elif zc.collidepoint(pos):
            f2=open("用户名.txt","w",encoding="utf-8")
            f3=open("password.txt","w",encoding="utf-8")
            yhm=input("请输入你的用户名：")
            f2.write(yhm)
            password1=input("请输入你的密码：")
            f3.write(password1)
            m="登录界面"
            f2.close()
            f3.close()

go()
