#!/usr/bin/python
# -*- coding: UTF-8 -*-

from os import system, name
import itertools
import threading
import time
import sys
import datetime
from base64 import b64decode,b64encode
from datetime import date


expirydate = datetime.date(2022, 9, 24)
#expirydate = datetime.date(2022, 8, 30)
today=date.today()
green="\033[3;32m"
neon="\033[3;36m"
nc="\033[00m"
red="\033[3;31m"
purple="\033[3;34m"
yellow="\033[3;33m"
voilet="\033[3;35m"
def hero():

    def chalo():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']) :
                if done:
                    break
                sys.stdout.write('\rhacking in the Genting server for next colour--------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(10)
        done = True

    def chalo1():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rgetting the colour wait --------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(10)
        done = True

    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    def getSum(n):
        sum=0
        for digit in str(n):
            sum+= int(digit)
        return sum
    clear()
    y=1
    newperiod=period
    banner='figlet GentingMall|lolcat'
    numbers=[]
    while(y):
        clear()
        system(banner)
        print(f"{red}Contact me on telegram @IDFCMONEY")
        print(f"{yellow}Enter ",newperiod," Emerd Price :")
        current=input()
        current=int(current)
        chalo()
        print("\n---------Successfully hacked the server-----------")
        chalo1()
        print("\n---------Successfully got the colour -------------")
        print('\n')
        last2=str(current)[-2:]
        #samjha_maadarchod=lawde_time_pe_khel(last2)
        if(newperiod%2==0):
            sum=getSum(current)
            if(sum%2==0):
                print(newperiod+1," : 🔴, RED")
            else:
                print(newperiod+1,"  : 🟢, GREEN")
        else:
            sum=getSum(current)
            if(sum%2==0):
                print(newperiod+1,"   : 🔴, RED")
            else:
                print(newperiod+1,"   : 🟢, GREEN")
        newperiod+=1
        numbers.append(current)
        y=input("Do you want to play : Press 1 and 0 to exit \n")
        if(y==0):
            y=False
        if (len(numbers)>11):
            clear()
            system('figlet Thank you!!')
            print("Play on next specified time!!")
            print("-----------Current Time UP----------")
            sys.exit(" \n \n \n Contact on Telegram @IDFCMONEY")
            #print(numbers)
  



if(expirydate>today):
    now = datetime.datetime.now()
    First = now.replace(hour=13, minute=55, second=0, microsecond=0)
    Firstend = now.replace(hour=14, minute=35, second=0, microsecond=0)
    Second = now.replace(hour=16, minute=25, second=0, microsecond=0)
    Secondend = now.replace(hour=17, minute=35, second=0, microsecond=0)
    Third = now.replace(hour=15, minute=55, second=0, microsecond=0)
    Thirdend = now.replace(hour=16, minute=35, second=0, microsecond=0)
    Final = now.replace(hour=17, minute=55, second=0, microsecond=0)
    Finalend = now.replace(hour=18, minute=35, second=0, microsecond=0)

    if (now>Third and now<Thirdend):
            period=320
            hero()
    elif(now):
            period=340
            hero()
    elif(False):
            period=340
            hero()
    elif(False):
            period=360
            hero()
    else:
        banner='figlet GentingMall|lolcat'
        system(banner)
        print(f"{red}Hi!! Thanks for buying the hack")
        #print("Hi! thanks for trying our DEMO")
        print("----------Your play time-----------")
        #print("31st Aug 2021, 11:00 AM- 11:30 AM")
        #print("31st Aug 2021, 02:00 PM- 02:30 PM")
        print("23rd Sept 2021, 04:00 PM- 04:30 PM")
        #print("31st Aug 2021, 08:00 PM- 08:30 PM")
        print("Please play on the given time, and ")
        print("If you think it is an error contact")
        print(" admin on telegram @IDFCMONEY ")



else:
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    code="SKBhai"
    code1="LIFEISLOL"
    code2="SUCK"
    test="PROFIT"
    night="GENTING02"
    nextday="PLEASEW8"
    banner='figlet GentingMall|lolcat'
    rava=0
    now = datetime.datetime.now()
    Second = now.replace(hour=10, minute=55, second=0, microsecond=0)
    Secondend = now.replace(hour=14, minute=55, second=0, microsecond=0)
    Third = now.replace(hour=15, minute=30, second=0, microsecond=0)
    Thirdend = now.replace(hour=18, minute=34, second=0, microsecond=0)
    Final = now.replace(hour=18, minute=35, second=0, microsecond=0)
    Finalend = now.replace(hour=22, minute=35, second=0, microsecond=0)

    if(now>Second and now<Secondend):
            rava=290
    elif(now>Third and now<Thirdend):
            rava=350
    elif(now>Final and now<Finalend):
            rava=410
    system(banner)
    system(banner)
    print(f"{red}*---------*----------*-------------*----------*")
    print(f"{yellow}If The Above Text Is Not Visible Zoom Out")
    print("Your Screen")
    print(f"{green}To Know The Password --- Contact me")
    print(f"{green}on telegram ----@IDFCMONEY ")
    print(f"{voilet} Recharge Amount :        Total limit " )
    print(" 1.     5000 INR -------  1 Day (30 Games)")
    print(" 2.   10,000 INR -------  7 Days(2100 Games)")
    print(" 3.   50,000 INR -------  Month(6 Months)")
    print(f"{green}You Can Recharge And Activate Your Hack Directly")
    print("By Paying Here To Me To the Below Upi Id")
    print(f"{red}Upi-1: {green}  -----  {yellow}  N/A")
    print(f"{red}Upi-2: {green}  -----  {yellow}  N/A")
    print(f"{neon}*---------*----------*--------*---------*--------*")
    print(f"{green}Your custom hack can be made request from us.")
    print(f"{red}Beware of fraudsters!!!")
    while(True):
        print(f"{neon}*--------*--------*-------*---------*---------*")
        print("Hi, IDFC Here")
        print("If you send Payment to any other Person On Telegram ,")
        print(f"{purple}Then I'm Damn Sure That")
        print(f" IT IS A {red}SCAMMM")
        print(f"{purple}Don't Believe Any One Who Says ")
        print(f"I Have {yellow}Hack {purple}And Sends You Only ")
        print(f"{green}Fake {purple}ScreenShots Or Edited Ones")
        print(f"{red}After You Pay to The UPI ID above You Can Automatically")
        print(f"Activate Hack By Entering The Correct ")
        print(f"{green}(UTR) Or Upi Reference Number") 
        print(f"{neon}To Activate The Hack")
        print(f"If It Does'nt Open Contact Me On Telegram {yellow}@IDFCMONEY")
        print(f"{neon}*---------*----------*-------------*----------*")
        print(f"{green}This Update Contains")
        print(f"{neon}Automatic Recharge Updated")
        print(f"{purple}Colourful And User Friendly InterFace Updates")
        print(f"{green}And Much More..., Play And EnJoy Earning")
        print(f"{red}And A Warning Play The Amount Specified By Hack")
        print("If You Play More And Loss We Are Not Responsible")
        print(f"{neon}*---------*----------*-------------*----------*")
        print(f"{green}Things Under Maintenence")
        print(f"{yellow}Colour Combination And Emoji syncing")
        print(f"{green}Please Ignore Play Timings They Are Under Maintenence")
        print(f"{yellow}All These Will Be Updated In Upcomming Updates")
        print(f"{red}*---------*----------*-------------*----------*")
        
        
        print(f"{neon}Enter Your Password Or Upi Reference for Opening Hack ")
        bhai=input(": ")
        if(bhai==code or bhai==test or bhai==code1 or bhai==code2):
            clear()
            banner='figlet GentingMall|lolcat'
            print("You have bought hack for 1 day")
            print(f"{purple}---------------Your play time----------------")
            print("19th Jan 2021, 02:30 PM- 03:00 PM")
            print("19th Jan 2021, 05:30 PM- 06:00 PM")
            print("19th Jan 2021, 08:30 PM- 09:00 PM")
            print("Please play on the given time, and ")
            print(f"If you think it is an {red}error {yellow}contact {green}me ")
            print(f"{neon}On Telegram {red}@IDFCMONEY")
            print("wait.... starting....")
            time.sleep(10)
            period=rava
            hero()
            #print("Today Server is off Genting try tomorrow ")
            #rint(" of town, Tomorrow It will work as usual.")
            #print(" Thank You!!")
            #rint("To all the weekly members next week, cost will be  ")
            #print(" 4000 INR , because in this week 2 days off " )
            #print("Thank You!! ")
            sys.exit(" \n \n \n Contact on Telegram @IDFCMONEY")
        elif(bhai==nextday):
            clear()
            banner='figlet GentingMall|lolcat'
            system(banner)
            print("----------Your play time-----------")
            print("8th-14th Dec 2021, 02:30 PM- 03:00 PM")
            print("8th-14th Dec 2021, 06:00 PM- 06:30 PM")
            print("8th-14th Dec 2021, 08:30 PM- 09:00 PM")
            print("Please play on the given time, and ")
            print("If you think it is an error contact")
            print("wait.... starting....")
            time.sleep(20)
            period=rava
            hero()
            #period("Sorry too many people(>20) using hack in same time ")
            sys.exit(" \n \n \n Contact on Telegram @IDFCMONEY")
        elif(bhai==night):
            clear()
            banner='figlet GentingMall|lolcat'
            print("----------Your play time-----------")
            print("9th Dec 2021,  08:30 PM- 09:00 PM")
            print("10th Dec 2021, 08:30 PM- 09:00 PM")
            print("11th Dec 2021, 08:30 PM- 09:00 PM")
            print("Please play on the given time, and ")
            print("If you think it is an error contact")
            print("wait.... starting....")
            time.sleep(10)
            period=410
            hero()
            sys.exit(" \n \n \n Contact on Telegram @IDFCMONEY")
        else:
            clear()
            banner='figlet GentingMall|lolcat'
            system(banner)
            print("Incorrect Activation Code :")
     
