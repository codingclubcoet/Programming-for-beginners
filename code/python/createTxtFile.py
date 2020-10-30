from os import system, name
from time import sleep
import os

#buat class baru
class newfile(object):
    def create(self,**namefile):
        try:
            print("Createing File Zone")
            self.namefile = str(input("Enter The File Name:"))
            f = open(self.namefile+".txt","x")
            f.close()
            print("----------------------------")
            print("| File Create Successfull |")
            print("----------------------------")
        except FileExistsError:
            print("File is Already Exists")
            y = str(input("Still Want To continue(y/n):"))
            if y == 'y':
                x = newfile()
                x.create()
    def read(self,**namefile):
        try:
            print("Reading File Zone")
            self.namefile = str(input("Enter The File Name:"))
            f = open(self.namefile+".txt","r")
            print(f.read())
            f.close()
        except FileNotFoundError:
            print("Oops! Sorry We Cannot Find Your File")
            new = str(input("Do You Want To Create A new File(y/n):"))
            if new == "y":
                name = str(input("Enter the File name:"))
                y = newfile(name)
                y.create()
    def append(self,**namefile):
        try:
            print("Appending File Zone")
            valid = True
            self.namefile = str(input("Enter The File Name:"))
            f = open(self.namefile+".txt","a")
            while valid:
                file = " "
                file += str(input("Put Some String:"))
                f.write(file)
                x = str(input("Do You Want To Continue(y/n):"))
                if x == "y":
                    pass
                else:
                    valid = False
            f.close()
        except FileNotFoundError:
            print("Oops! Sorry We Cannot Find Your File")
            new = str(input("Do You Want To Create A new File(y/n):"))
            if new == "y":
                name = str(input("Enter the File name:"))
                y = newfile(name)
                y.create()
    def over(self,**namefile):
        try:
            print("OverWriting File Zone")
            valid = True
            self.namefile = str(input("Enter The File Name:"))
            f = open(self.namefile+".txt", "w")
            while valid:
                file = str(input("Put Some String / Word:"))
                f.write(file)
                x = str(input("Do You Want To Continue(y/n):"))
                if x == "y":
                    pass
                else:
                    valid = False
            f.close()
        except FileNotFoundError:
            print("Oops! Sorry We Cannot Find Your File")
            new = str(input("Do You Want To Create A new File(y/n):"))
            if new == "y":
                name = str(input("Enter the File name:"))
                y = newfile(name)
                y.create()
    def delete(self):
        self.namefile = str(input("Enter The File Name:"))
        if os.path.exists(self.namefile+".txt"):
            os.remove(self.namefile+".txt")
            print("Delete Successfully")
        else:
            print("File Doesn't Exists")

#class baru
class switcher(newfile):
    def __init__(self,num):
        self.pick = num

    def number_method(self):
        """"Dispatch Method"""
        method = 'method'+str(self.pick)
        # Get the method form 'self'. Default to a Lambda
        thismethod = getattr(self, method, lambda : "Invalid Choose")
        # Call the method as we return it
        return thismethod()
    def method1(self):
        x = newfile()
        x.create()
    def method2(self):
        x = newfile()
        x.read()
    def method3(self):
        x = newfile()
        x.append()
    def method4(self):
        x = newfile()
        x.over()
    def method5(self):
        x = newfile()
        x.delete()

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

valid = True
while valid:
    print("1. Create A New File")
    print("2. Read A File")
    print("3. Append The File")
    print("4. OverWrite File")
    print("5. Delete A File")
    num = int(input("Enter The Number:"))
    file1 = switcher(num)
    file1.number_method()
    x = str(input("Do You Want To Continue The File(y/n):"))
    if x == 'y':
        sleep(2)
        clear()
    else:
        valid = False


