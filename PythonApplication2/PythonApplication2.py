Player = ""
Stop = True

from datetime import datetime
from threading import Thread
import os
import time

clean = lambda: os.system('cls')

class Person:
     normal_name = "NoName"
     normal_age = 18
     
     def __init__(self, name, age):
         if "*" in name:
             self.name = self.normal_name
         elif name == "":
             self.name = self.normal_name
         else:
             self.name = name
         if 1 < age < 100:
             self.age = age
         else:
             self.age = self.normal_age
         self.balance = 0
         self.work = "none"
         self.income = 0
         self.dps = 0
         self.business = 0

     def show(self): return f"  {self.name}, {self.age} years, Balance: {self.balance}$, Work: {self.work}, Dps: {self.dps}$\n" # Person

class Work:

    def __init__(self):
        while True:
            try:
                clean()
                print(Player.show())
                choiceM = int(input(f"1 - Go work ({Player.income}$)\n2 - Upgrade work\n3 - Close\n"))
                match choiceM:
                    case 1:
                        self.go()
                    case 2:
                        self.up()
                    case 3:
                        break
            except:
                continue

    def programmist(): 
        Player.work = "programmist"
        Player.income = 100

    def designer(): 
        Player.work = "designer"
        Player.income = 200

    def taxi(): 
        Player.work = "taxi"
        Player.income = 300

    def go(self):
        Player.balance += Player.income

    def up(self):
        Player.income = round(Player.income + Player.income / 10) # Work

class Settings:
    def __init__(self):
        clean()
        while True:
            print(f"1 - Recreate person\n2 - Edit person\n3 - Choose work\n4 - Save\n5 - Load\n6 - Close")
            try:
                choiceS = int(input())
                match choiceS:
                    case 1:
                        Settings.CreatePerson()
                    case 2:
                        Settings.EditPerson()
                        break
                    case 3:
                        Settings.ChooseWork()
                        break
                    case 4:
                        Settings.Save()
                        break
                    case 5:
                        Settings.Load()
                        break
                    case 6:
                        break
                break
            except:
                clean()
                break

    def CreatePerson():
        global Player
        clean()
        age = 0
        name = input("Enter name: ")
        try:
            age = int(input("Enter age: "))
        except:
            pass
        Player = Person(name, age)

    def EditPerson():
        clean()
        age = 0
        name = input("Enter name: ")
        try:
            age = int(input("Enter age: "))
        except:
            pass
        if "*" in name:
            Player.name = "NoName"
        elif name == "":
            Player.name = "NoName"
        else:
            Player.name = name
        if 1 < age < 100:
            Player.age = age
        else:
            Player.age = 18

    def ChooseWork():
        clean()
        try:
            choiceWork = int(input("1 - Programmist\n2 - Designer\n3 - Taxi\n"))
        except:
            clean()
        match choiceWork:
            case 1:
                Work.programmist()
            case 2:
                Work.designer()
            case 3:
                Work.taxi()

    def Save():
        save = open("save.txt", "w")
        save.write(f"{Player.name}*{Player.age}*{Player.balance}*{Player.work}*{Player.income}*{Player.dps}*{Player.business}")
        save.close()
        code = open("code.txt", "w")
        x = Player.age + Player.balance + Player.income + Player.dps + Player.business
        code.write(f"{x:0x}")
        code.close()

    def Load():
        global Player
        Player = Person("", 0)
        try:
            load = open("save.txt", "r")
            code = open("code.txt", "r")
            x = code.read()
            s = load.read()
            data = s.split("*")
            check = int(data[1]) + int(data[2]) + int(data[4]) + int(data[5]) + int(data[6])
            if check == int(x, 16):
                Player.name = str(data[0])
                Player.age = int(data[1])
                Player.balance = int(data[2])
                Player.work = str(data[3])
                Player.income = int(data[4])
                Player.dps = int(data[5])
                Player.business = int(data[6])
                if Player.business == 1:
                    M.start()
                load.close()
                code.close()
            else:
                load.close()
                code.close()
                clean()
                print(" Error: Don't edit save, I know it!\n")
                return 0
        except:
            clean()
            print(" Error: Corrupted save :(\n")
            return 0 # Settings

def TimeNow():
    now = datetime.now()
    sec = int("{}".format(now.second))
    minut = int("{}".format(now.minute))
    chas = int("{}".format(now.hour))
    sec = sec + minut * 60 + chas * 3600
    return sec # TimeNow

class Business():
    def __init__(self):
        while True:
            try:
                clean()
                print(Player.show())
                choiceM = int(input(f"1 - Open\n2 - Buy cafe (10$/sec)\n3 - Buy shop (23$/sec)\n4 - Close\n"))
                match choiceM:
                    case 1:
                        if Player.business == 0:
                            M.start()
                            Player.business = 1
                    case 2:
                        self.Cafe()
                    case 3:
                        self.Shop()
                    case 4:
                        break
            except:
                continue
    
    def Cafe(self): Player.dps += 10

    def Shop(self): Player.dps += 23
    
    def open():
        if Player.business == 1:
            M.start()

    def inc():
        global Stop
        while Stop:
            Player.balance += Player.dps
            time.sleep(1) # Business

def Start():
    while True:
        try:
            check = int(input("Load save? (0 | 1)\n"))
        except:
            clean()
            continue
        if check == 1:
            if Settings.Load() == 0:
                continue
            else:
                Menu()
            return
        elif check == 0:
            Settings.CreatePerson()
            Menu()
            return
        else:
            clean()
            continue # Start

def Menu():
    global Stop
    while True:
        try:
            clean()
            print(Player.show())
            choiceM = int(input(f"1 - Work\n2 - Business\n3 - Settings\n4 - Exit\n"))
        except:
            continue
        match choiceM:
            case 1:
                Work()
            case 2:
                Business()
            case 3:
                Settings()
            case 4:
                Settings.Save()
                Stop = False
                break
            case 113:
                Player.name = "*CHEATER*"
                Player.age = 69
                Player.balance = 143
                Player.work = "*CHEATER*"
                Player.income = 666666
                Player.dps = 777777
                Player.business = 1
                Business.open() # Menu

Starting = Thread(target = Start)
M = Thread(target = Business.inc)
Starting.start()