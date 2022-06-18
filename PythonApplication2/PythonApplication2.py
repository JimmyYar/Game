Player = ""

import os

def clean(): os.system('cls' if os.name == 'nt' else 'clear')

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

     def show(self): return f"  {self.name}, {self.age} years, Balance: {self.balance}$, Work: {self.work}\n"

class Work:

    def __init__(self):
        start = 1
        while start != 0:
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
        Player.income = round(Player.income + Player.income / 10)

class Settings:
    def __init__(self):
        clean()
        start = 1
        while start != 0:
            print(f"1 - Recreate person\n2 - Edit person\n3 - Choose work\n4 - Close")
            try:
                choiceS = int(input())
                match choiceS:
                    case 1:
                        main()
                    case 2:
                        Settings.EditPerson()
                    case 3:
                        Settings.ChooseWork()
                    case 4:
                        break
            except:
                clean
                continue

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
        clean()

    def EditPerson():
        clean()
        age = 0
        name = input("Enter name: ")
        try:
            age = int(input("Enter age: "))
        except:
            pass
        Player.name = name
        Player.age = age
        clean()

    def ChooseWork():
        clean()
        try:
            choiceWork = int(input("1 - Programmist\n2 - Designer\n3 - Taxi\n"))
        except:
            clean()
            pass
        match choiceWork:
            case 1:
                Work.programmist()
            case 2:
                Work.designer()
            case 3:
                Work.taxi()
        clean()

def Save():
    save = open("save.txt", "w")
    save.write(f"{Player.name}*{Player.age}*{Player.balance}*{Player.work}*{Player.income}")
    save.close()

def Load():
    global Player
    Player = Person("", 0)
    try:
        load = open("save.txt", "r")
    except:
        clean()
        main()
    s = load.read()
    data = s.split("*")
    Player.name = str(data[0])
    Player.age = int(data[1])
    Player.balance = int(data[2])
    Player.work = str(data[3])
    Player.income = int(data[4])
    load.close()

def main():
    start = 1
    try:
        check = int(input("Load save? (0 | 1)\n"))
    except:
        clean()
        main()
    if check == 1:
        Load()
    elif check == 0:
        Settings.CreatePerson()
    else:
        clean()
        main()
    while start != 0:
        try:
            clean()
            print(Player.show())
            choiceM = int(input("1 - Work\n2 - Settings\n3 - Save\n4 - Load\n5 - Exit\n"))
        except:
            continue
        match choiceM:
            case 1:
                Work()
            case 2:
                Settings()
            case 3:
                Save()
            case 4:
                Load()
            case 5:
                Save()
                break

main()