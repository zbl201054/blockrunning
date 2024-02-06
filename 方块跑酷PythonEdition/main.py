#方块跑酷python版
#功能还未完善敬请谅解！
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
ks=Actor("开始.png",(710,100))
project=Actor("project0.png",(440,250))
music_button=Actor("music-button.png",(100,320))
notice=Actor("公告.png",(710,250))
store=Actor("store.png",(440,400))
settings=Actor("sz.png",(50,200))
user_center=Actor("user-center.png",(710,350))
activity=Actor("hd.png",(80,400))
dz=Actor("dz.png",(440,350))
a=0
b=0
c=0
d=0
e=0
f=0
g=0
fh=Actor("fh.png")
fh1=0
cg=Actor("闯关模式.png",(600,250))
zy=Actor("自由模式.png",(200,250))
k=0
color=0
floor=Actor("black_block.png",(445,500))
project_1=Actor("project0.png",(100,200))
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
        ks.draw()
        project.draw()
        music_button.draw()
        notice.draw()
        store.draw()
        settings.draw()
        user_center.draw()
        activity.draw()
        dz.draw()
    if m=="游戏模式":
        fh.draw()
        cg.draw()
        zy.draw()
    if m=="公告":
        fh.draw()
    if m=="个人中心":
        fh.draw()
    if m=="商店":
        fh.draw()
    if m=="音乐":
        fh.draw()
    if m=="活动":
        fh.draw()
    if m=="设置":
        fh.draw()
    if m=="第一关":
        fh.draw()
        project_1.draw()
        floor.draw()
def new0():
    global m
    m = '加载'

def new1():
    global m
    m = '登录'
def new2():
    global m,q
    m="登录界面"
def new3():
    global m
    m="游戏模式"
def new4():
    global m
    m="公告"
def new5():
    global m
    m="个人中心"
def new6():
    global m
    m="商店"
def new7():
    global m
    m="音乐"
def new8():
    global m
    m="活动"
def new9():
    global m
    m="设置"
def new10():
    global m
    m="第一关"
def jd0():
    global i #全局变量
    if i < 6:
        i += 1
def dl0():
    global m
    m="主屏幕"

def update():
    global m, i,dl2,fh1,a,b,c,d,e,f,g,k,color
    f4=open("color.txt","w",encoding="utf-8")
    f4.write(str(color))
    f4.close()
    f5=open("color.txt","r",encoding="utf-8")
    color=int(f5.read())
    f5.close()
    if fh1==1:
        clock.schedule(dl0,1)
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
    if m=="主屏幕":
        fh1=0
        project.image="project"+str(color)+".png"
        if a==1:
            clock.schedule(new3,1)
        if b==1:
           clock.schedule(new4,1)
        if c==1:
            clock.schedule(new5,1)
        if d==1:
            clock.schedule(new6,1)
        if e==1:
            clock.schedule(new7,1)
        if f==1:
            clock.schedule(new8,1)
        if g==1:
            clock.schedule(new9,1)
    if m=="游戏模式":
        a=0
        if k==1:
            clock.schedule(new10,1)       
    if m=="公告":
        b=0
    if m=="个人中心":
        c=0
    if m=="商店":
        d=0
    if m=="音乐":
        e=0
    if m=="活动":
        f=0
    if m=="设置":
        g=0
    if m=="第一关":
        k=0
        project_1.image="project"+str(color)+"_1"+".png"
        #project.pos=(100,200)
        project_1.y+=5
        if project_1.y>=465:
            project_1.y-=5
def on_mouse_down(pos):
    global m,f0,f1,f2,f3,dl2,dl1,q,a,b,c,d,e,f,fh1,g,k
    if fh.collidepoint(pos):
        fh1=1
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
    if m=="主屏幕":
        if ks.collidepoint(pos):
            a=1
        if notice.collidepoint(pos):
            b=1
        if user_center.collidepoint(pos):
            c=1
        if store.collidepoint(pos):
            d=1
        if music_button.collidepoint(pos):
            e=1
        if activity.collidepoint(pos):
            f=1
        if settings.collidepoint(pos):
            g=1
    if m=="游戏模式":
        if zy.collidepoint(pos):
            k=1    
go()
