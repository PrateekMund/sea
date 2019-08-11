#coding:utf-8
#购物系统
"锁刀工作室版权所有"
            #导入数据
import time
import datetime
import random
import easygui
import sys
import time
import pygame
from pygame.locals import *

            #储存数据

m1 = 610                #价格
m2 = 600                #价格
m3 = 600                #价格
m4 = 550                #价格
m5 = 550                #价格
name = 0                #名字
day = int(datetime.datetime.now().weekday())          #日期
day += 1
day1 = int(datetime.datetime.now().weekday())       #备份日期
day1 += 1                                                             
text  = open('money.txt','r')
temp = text.read()
money = int(temp)
text.close()                            #钱数
signed_on_temp = random.randint(1,100)                #签到数
commodity = ['土黄色时尚风衣套装','黑色‘魔’风衣套装','白色‘魔’风衣套装','海军上校套装','时尚衣服']
commodity.append('退出')
#储存用户名和密码
class Name_word():
    def __init__(self,username,password_temp,password,username0,password_temp0,password0):
        self.username = username
        self.password_temp = password_temp
        self.password = password
        self.username0 = username0
        self.password_temp0 = password_temp0
        self.password0 = password0
    def login(self):
        while True:
            username1 = easygui.enterbox("\n\n请输入名称：")
            if username1 == username or username1 == username0:
                password_temp1 = easygui.passwordbox("请输入密码：")
                if username1 == username:
                    if password_temp1 == password_temp:
                        easygui.msgbox("\n\n登录成功！！！\n\n\n")
                        break
                    else:   
                        easygui.msgbox("密码和用户名不匹配！！！",ok_button = '重试')
                elif username1 == username0:
                    if password_temp1 == password_temp0:
                        easygui.msgbox("\n\n登录成功！！！\n\n\n")
                        break
                    else:
                        easygui.msgbox("密码和用户名不匹配！！！",ok_button = '重试')
            else:
               easygui.msgbox("密码和用户名不匹配！！！",ok_button = '重试')        
#创建BUY函数
def buy(photos_temp,msgnum):
    global money
    easygui.buttonbox(msg = msg,title = '衣服展示框',image = photos_temp + '.gif',choices = ('继续','继续'))
     #购物操作
    price = m1 * num
    easygui.msgbox("\n\n价格为：" + str(price) + "元")
    time.sleep(0.5)
    easygui.msgbox('您的余额为'   + str(money) + '元')
    if int(money) - int(price) >= 0:
        easygui.msgbox("您的余额足够")
        while True:
                        
            shop = easygui.boolbox("请问是否购买？")
            if shop:
                money -= price
                easygui.msgbox("余额还剩" + str(money) + "元\n\n")
                time.sleep(1.5)
                break
            elif not shop:
                print("正在退出.....")
                time.sleep(1.5)
                break
    else:
        easygui.msgbox("您的余额不够")
        print("自动退出中......")
        time.sleep(1.5)
        


            #提示用户注册账号
easygui.msgbox("你好，请先注册账号",'提示','继续')
easygui.msgbox("最多只能注册2个账号",'提示','继续')

            #注册账号
while True:
    username0 = 'yang'
    password_temp0 = 666
    password0 = 666
    username = easygui.enterbox("请输入名称：")
    password_temp = easygui.passwordbox("请输入密码：")
    password = easygui.passwordbox("验证密码：")
    if password_temp == password:
        easygui.msgbox("验证成功！！！\n\n\n")
        break
    else:
        easygui.msgbox("验证失败！！！\n\n\n",ok_button = '重试')
    

            #登录或注册账号

while True:
    login = easygui.ccbox("请选择要进行的操作：",'选择',('注册账号','登录'))
    #注册账号
    if login:
        while True:
            smell = 1
            username0 = easygui.enterbox("请输入名称：")
            password_temp0 = easygui.passwordbox("请输入密码：")
            password0 = easygui.passwordbox("验证密码：")
            if password_temp0 == password0:
                easygui.msgbox("验证成功！！！\n\n\n")
                break
            else:
                easygui.msgbox("验证失败！！！\n\n\n",ok_button = '重试')
            
    #进入登录程序
    elif not login:
        print("\n正在准备登录程序.......")

        fine = 10
        while fine < 100:    
            fine += 10
            print("已完成" + str(fine) + "%")
            time.sleep(1)
        if fine == 100:
            break

#判断是否登录成功
name_word = Name_word(username,password_temp,password,username0,password_temp0,password0)
name_word.login()
        
#欢迎用户并提示选择需要的操作
while True:
    easygui.msgbox("@" + username + "\n欢迎来到购物中心！！！\n\n",'欢迎','继续')
    answer = easygui.choicebox ('请选择您需要的操作','控制台',('购物','签到','抽奖','玩游戏得积分','退出'))
    #进入购物系统
    if answer == '购物':
                                  
        print("请选择要购买的商品：")
        print("1.土黄色时尚风衣套装")
        print("2.黑色‘魔’风衣套装")
        print("3.白色‘魔’风衣套装")
        print("4.海军上校套装")
        print("5.时尚衣服")
        print("6.退出")
        
        #提示用户购买商品
        while True:
            easygui.msgbox("@" + username + "请选择：（填序号）")
            name = int(easygui.enterbox(">>>"))
            num = int(easygui.enterbox("请输入购买数量>>>"))
            print("正在处理......")
            time.sleep(1.5)
                #传参系统
            if name == 1:
                buy('images\\衣服00',commodity[0],num)
            elif name == 2:
                buy('images\\衣服01',commodity[1],num)
            elif name == 3:
                buy('images\\衣服02',commodity[2],num)
            elif name == 4:
                buy('images\\衣服03',commodity[3],num)
            elif name == 5:
                buy('images\\衣服04',commodity[4],num)
            elif name == 6:
                break
            else:
                continue
                        #计算总价
                

                #签到系统

    elif answer == '签到':
        while True:
            easygui.msgbox('今天是星期' + str(day1),'日期','继续')
            day = int(day)
            day1 = int(day1)
            if day == day1:
                easygui.msgbox('您未签到','提示','继续')
                signed_on = easygui.boolbox('请问是否签到？')
                if signed_on:
                    money += signed_on_temp
                    easygui.msgbox('您现在有' + str(money) + '积分','积分','继续')
                    day -= 1
                    time.sleep(0.5)
                    break
                else:
                    print('自动退出中......')
                    time.sleep(1.5)
                    break
            else:
                easygui.msgbox('您今天签过到了，请明天再来！！！','提示','返回')
                print('自动退出中......')
                time.sleep(1.5)
                break
    #抽奖系统
    elif answer == '抽奖':
        while True:
            easygui.msgbox('该系统暂未开放！！！','提示','返回')
            break       
    #游戏系统
    elif answer == '玩游戏得积分':
        while True:
            easygui.msgbox('该系统暂未开放！！！','提示','返回')
            break
    #退出程序
    elif answer == '退出':
        break
    

#结束
easygui.msgbox('感谢您的使用，谢谢','感谢','退出')
text = open('money.txt','w')
money -= int(temp)
text.write(str(money))
text.close()
                             
    
    
    
