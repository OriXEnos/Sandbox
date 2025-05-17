import random
import urllib.request
import math
import numpy
import time
import matplotlib.pyplot as plt 

"""
#การแสดงผล (Output)
print("Hello World")
print("Say Hi")



#ชนิดข้อมูลพื้นฐาน
#int,float,complex
#bool
#str
#NoneType (ไม่ระบุค่า)

#การสร้างตัวแปร Variable

#เขียนแบบที่ 1
name = "Ori-XEnos"
age = 10
grade = 3.99
status = True

#เขียนแบบที่ 2
name_1,age_1,grade_1,status = "Ake-Ori",10,5.55,True

#แก้ไขข้อมูล
age = 20
grade = 4.00

#แสดงข้อมูล (Output)
print(name)
print(age)
print(grade)
print(status)

#แสดงข้อมูล (Output)
print("ชื่อนักเรียน = ",name_1)
print("อายุ = ",age_1,"ปี")
print(grade)
print(status)

#แสดงชนิดข้อมูล
print(type(name))
print(type(age))
print(type(grade))
print(type(status))



#รับข้อมูลจากผู้ใช้ (Input)
name_2 = input("Input Your Name : ")
print("Your Name = ",name_2)

#การแปลงชนิดข้อมูล (Casting)
name = input("Please , Input your Name : ")
year = input("Pleae Input your Years : ")

print("Your Name = ",name)
print("Brith Year = ",year)
print("How old are you = ",2568-int(year))

print(type(name))
print(type(year))



#ตัวดำเนินการทางคณิตศาสตร์
number1 = 5 
number2 = 2
print("Number 1 = ",number1)
print("Number 2 = ",number2)

#คำนวณ
print("=================")
print("ผลบวก = ",number1+number2)
print("ผลลบ = " ,number1-number2)
print("ผลคูณ = ",number1*number2)
print("ยกกำลัง = ",number1**number2)
print("ผลหาร = ",number1/number2)
print("ผลหารไม่เอาจุดทศนิยม",number1//number2)
print("เศษ = ",number1%number2)

#ตัวดำเนินการ Compound Assignment
# +=
# -=
# *=
# /=
# %=
# **=
# //=

x,y=10,2
print("x = ",x)
print("y = ",y)

x+=y
print("result = ",x)

#ตัวดำเนินการ เปรียบเทียบ
# ==
# !=
# >
# <
# >=
# <=

x,y = 100,50
print(x==y)



#คำสั่งเงื่อนไข (if..else)
#input
score = int(input("Please Input your score : "))
print("Your score = ",score)

#process
if score >= 50:
    print("Pass")
else:
    print("Not Pass")



#Ternary operator เขียน if..else ลดรูป

number = int(input("Please ,Input your number : "))
print("Your number is : ",number)
print("Even") if number%2==0 else print("Odd")

#ตัวดำเนินการตรรกศาสตร์ ใช้ and,or,not 
#ยกตัวอย่าง

username = input("Input your username : ")
password = input("Input your password : ")

if username=="admin" or password=="1234":
    print("Login Successful")
else:
    print("Data Not Correct !!!")


#โปรแกรมตัดเกรด
score = int(input("Input your score : "))
print("Your socre is : ",score)
grade = None

if score>=80 and score<=100:    #80-100
    grade = "A"
elif score>=70 and score<=79:   #70-79
    grade = "B"
elif score >= 0 and score<=69:  #0-69
    grade = "F"
else:
    grade = "N (Invalid)"

#Nested-if
username = input("Input your Username")
password = input("Input your Password")

if username=="member" and password=="1234":
    print("Login Successful !!!")
    service = input("Input your number service(1-2) :")
    if service=="1":
        print("Withdraw money")
    elif service=="2":
        print("Deposit money")
    else :
        print("Service number Not correct")
else:
    print("Don't found Account")



#Match..Statement (รองรับ หลากหลายประเภทชนิดข้อมูล) #แตกต่างจาก switch..case
service = input("Input service number (1-3) : ")       

match service:
    case "1": print("Withdraw")
    case "2": print("Deposit")
    case "3": print("Remaining balance")
    case " ": print("Service number not correct")

#While..loop
counter = 5
while counter<10:
    counter+=1
    print(counter)

print("Ending Programming")



#For...loop
#รูปแบบการเขียน for i in range(start, end, step):
#ใช้งานกับ Iterable Objects (วัตถุที่วนซ้ำได้) เช่น List, Tuple, Set, String
#ใช้ range() เพื่อกำหนดช่วง (Start, End, Step)

for counter in range(10,0,-1): #10-1
    print(counter)



#Break / Continue
for counter in range(1,11):
    if counter%2==0:
        continue
    print(counter)

print("Ending Program")



#แสดง แม่สูตรคูณ
number = int(input("Input Multiplication number >>> "))

for i in range(1,13):
    print(number,"x",i, " = ",number*i) 

#หาผลรวมของตัวเลข 5 จำนวน
total = 0
for i in range(1,6):
    number = int(input("ลำดับที่ "+str(i)+" :"))
    total += number
print(" ผลรวม = ",total)

#หาผลรวมของตัวเลขไม่จำกัดจำนวน

while True:
    number = int(input("ป้อนตัวเลข : "))
    if number<=0:
        break
print("Ending Program")


#Nested Loop
for i in range(2):
    print("รอบที่ ",i)
    for j in range(3):
        print(j)

#แม่สูตรคูณแบบกำหนดช่วง
start = int(input("แม่สูตรคูณเริ่มต้น : "))
end = int(input("แม่สูตรคูณสุดท้าย : "))

for number in range(start, end+1):#2-5
    print("สูตรคูณแม่",number)
    print("-----------------")
    for i in range(1,13):#1-12
        print(number,"x",i," = ",number*i)


#เจาะลึกการใช้ String

# สอง ข้อความมาเชื่อมกัน
fname = "Ori"
lname = "XEnos"

fullname=fname+lname+" Studio "
print(fullname)

# แสดงผลเป็น ข้อความ "   ยาวๆ"
#address=
#ที่อยู่ 123
#หมู่ 4
#ซอย 5/6
#จังหวัด อุดรธานี
#12345

print(address)

#แทรกตัวแปร ไปใน string
year = 2540
message = f"เกิดเมื่อปี พ.ศ. {year}"
print(message)

#Format String
salary = 18000
data = f"เงินเดือนของผม = {salary:.2f}"
print(data)

#แสดงตัวอักษร ผ่าน For..loop
text = "Hello"
for i in text:
    print(i)

print(len(text))
print(text[-5:-1])

#Function จัดการ string
#=======================================
#upper() แปลงอักษร เป็น พิมพ์ใหญ่
#lower() แปลงอักษร เป็น พิมพ์เล็ก
#startswith(string) ตัวอักษร ตัวแรกใน string
#endswith(string) ตัวอักษร ตัวสุดท้ายใน string
#find(string) ค้นหา ตัวอักษร ใน string
#count(string) นับตัวอักษร ใน string
#replace(old, string) แทนที่ ตัวอักษร string
#strip() ลบช่องว่าง ซ้าย และ ขวา ออก
#format() จัดรูปแบบ string
#=======================================

name = "OriXEnos"
print(name.upper())

fname = "Ori"
print(name.lower())

lname = "XEnos"
print(lname.startswith("XE"))       #return ค่าเป็น bool

month=input("Input month : ")

if month.endswith("คม"):
    print("This's month 31 days")
elif month.endswith("ยน"):
    print("This's month 30 days")

find_text = "Hello Python"
print(find_text.find("Python"))     #ถ้าค้นเจอ ค่าเป็น + , ค้นไม่เจอ ค่าเป็น - 

print(find_text.count("o"))         #ให้นับว่า ตัว o มีกี่ตัว

text_year = "Year of month : 2567"
update = text_year.replace("2567","2568")
print(update)

text_format = "ฉันชื่อ {0} - อายุ {1} - ปี {2}".format("เอก",30,2568)       #format แทรกข้อมูลลงไปใน string ตามลำดับ
print(text_format)



#ชนิดข้อมูล (Data Type)
#1.ชนิดข้อมูลพื้นฐาน (Primitive Data Type) , ข้อจำกัด เก็บค่า 1 ค่า = 1 ตัวแปร,
#,เช่น score1 = 100

#2. ชนิดข้อมูลแบบอ้างอิง
#List [] เก็บข้อมูล แบบลำดับ ,ข้อมูลซ้ำได้ , แก้ไขได้
#Tuple เก็บข้อมูล แบบลำดับ , ข้อมูลซ้ำได้ , แก้ไขไม่ได้
#Set เก็บข้อมูล ไม่มีลำดับ , ข้อมูลซ้ำไม่ได้
#Dictionary เก็บข้อมูลแบบ key , value 

#List 

#การสร้าง List[]
pet = []                            #แบบที่ 1 ไม่กำหนดข้อมูล
pet = ["Dog","Cat"]                 #แบบที่ 2 กำหนดข้อมูล
list_var = list(("Dog","Cat"))      #แบบที่ 3

#จำนวนสมาชิกใน List
score = [100,90,80]
len(score)

#เชื่อมข้อมูลใน List
score1 = [100,90,80]
score2 = [50,30,45]

new_score = score1+score2
print(new_score)

#กำหนดช่วง
#1.[index : ]
#2.[:end+1]         ก่อนสุดท้าย
#3.[index : end+1]

#การเข้าถึง List ด้วย for..loop
for i in score1[0:1]:
    print(i)

#การแก้ไขข้อมูล
score3 = [100,69,24,54]
score3[2] = 44
print(score3[0:3])


#Function จัดการ List
#append(element)            เพิ่มข้อมูล 1 จำนวน (ต่อท้าย)
#extend([element])          เพิ่มสมาชิกใหม่หลายรายการ (ต่อท้าย)
#insert(index,element)      แทรกสมาชิก ลงไปตาม index ที่กำหนด
#clear()                    ลบสมาชิกทั้งหมดออกจาก list

colors=["แดง","เขียว","น้ำเงิน","ดำ","ขาว"]
colors.append("น้ำตาล")
colors.extend(["ส้ม","เหลือง","ควย"])
colors.insert(1,"เทา")
colors.sort()                            #เรียงจาก น้อย ไป มาก
colors.reverse()                         #เรียง แบบ ย้อนกลับ
#colors.remove("น้ำเงิน")                   #ลบเฉพาะ น้ำเงิน
#colors.clear()                          #ลบทุกตัว
print(colors)

#Tuple ()
#ใช้เก็บข้อมูล ซ้ำกันได้
#สมาชิกใน Tuple , เก็บข้อมูลเหมือน หรือ ต่างกันได้
#ไม่สามารถแก้ไข ข้อมูลได้

product=("กางเกง",150.0,10)
name,price,stock = product   #เก็บข้อมูลตัวแปร ผ่าน Tuple
#print(product[0])
#print(product[1])
#print(product[2])
print(name)
print(price)
print(stock)
for item in product:
    print(item)
print(type(product))
print(len(product))

#การเชื่อม Tuple , 2 ข้อมูลเชื่อมเข้าด้วยกัน
colors1=("แดง","เขียว","น้ำเงิน")
colors2=tuple(("ดำ","ขาว"))

fullcolors=colors1+colors2
colors=("แดง","เขียว","น้ำเงิน","ดำ","ขาว")
print(colors[0:3])
print(fullcolors*2)
print(type(fullcolors))
print(len(fullcolors))



#Sets {}
#เก็บข้อมูล ต่างกัน หรือ เหมือนกัน
#ค่าไม่ซ้ำกัน
#ไม่มีเลข index กำกับข้อมูล
#ไม่สามารถแก้ไขค่า



#เข้าถึงสมาชิก set โดยใช้ for..loop


#function จัดการ set
#add()                  เพิ่มสมาชิกใหม่ 1 รายการ
#update(())             เพิ่มสมาชิกหลายรายการ
#discard()              ลบสมาชิก ที่ต้องการ ระบุ

#กรณีที่ มี set มากกว่า 1 set
#union()                    รวมสมาชิก ใน set A และ Set B เข้าด้วยกัน
#intersection()             สมาชิกใน set A และ set B ที่มีร่วมกัน
#difference()               สมาชิกอยู่ใน set A แต่ไม่มีอยู่ใน set B

#Set
animals = {"Dog","Cat","Lion","Bat","Rat","Tiger",True,1234}        #ไม่มี Index , หรือ ลำดับเรียงข้อมูล
pets = set(("Dog","Cat","Rabbit","Ant"))                            #เขียนแบบที่ 2
print(type(animals))
print(len(animals))

#ค้นหาข้อมูลใน set , ใช้ in
print("Brid" in animals)                #Return ออกมาเป็น Bool

#function จัดการ set
animals.add("Duck")                     #เพิ่ม 1 รายการ
animals.update(("Pig","Chicken"))       #เพิ่ม หลายรายการ
print(animals)
print(pets)

data = animals.union(pets)
print(data)
data = animals.intersection(pets)
print(data)
data = animals.difference(pets)
print(data)


#Dictionary {}
#key,value
#ใช้ key เป็น index เข้าถึง value
#ค่า key ต้องไม่ซ้ำกัน

colors={
    "red":"แดง",
    "green":"เขียว",
    "blue":"น้ำเงิน"
}
confirm = {
    True:"ตกลง",
    False:"ยกเลิก"
}
print(colors["red"])
print(colors["green"])

#แก้ไข , เพิ่มข้อมูล
colors["yellow"] = "สีเหลือง" #เพิ่ม
colors["blue"] = "คราม"     #แก้ไข



print(len(colors))
print(colors)
print(confirm[True])

"""
#Function จัดการ Dictionary
#keys()     keys ทั้งหมดใน Dictionary
#values()   values ทั้งหมดใน Dictionary
#get(key)   ดึงข้อมูล Dictionary ตาม key ที่ระบุ
#items()    ดึงข้อมูล key,value ทั้งหมด

colors_1 = {
    "red":"แดง",
    "green":"เขียว",
    "blue":"น้ำเงิน"
}
print(colors_1.keys())                  #รูปแบบเหมือน list
print(colors_1.values())                #รูปแบบเหมือน list
print(colors_1.items())                 #ดึงออกมา รูปแบบเหมือน tuple

for key,value in colors_1.items():
    print(key," = ",value)

#การลบ ข้อมูล Dictionary
colors_1.pop("blue")                #ลบข้อมูล โดยอ้าง key
print(colors_1)
colors_1.clear()                    #ลบข้อมูลทั้งหมด
print(colors_1)

#การเพิ่ม,แก้ไขข้อมูล ข้อมูล Dictionary
colors_1.update({"yellow":"เหลือง"})         #เพิ่ม
print(colors_1)

colors_1.update({"red":"แดงเข้ม"})           #แก้ไข
print(colors_1)

maincolor = colors_1.copy()                  #copy
print(maincolor)

#ตัวดำเนินการเอกลักษณ์ (identity Operator)
#ตัวดำเนินการ is และ is not จะตรวจสอบที่ ตำแหน่งหน่วยความจำ (Memory Address)
#is → ใช้ตรวจสอบว่า สองตัวแปรอ้างอิงถึงวัตถุเดียวกัน (Same Object) เหมือนกัน หรือไม่
#is not → ใช้ตรวจสอบว่า สองตัวแปรไม่ได้อ้างอิงถึงวัตถุเดียวกัน (Different Object)

colorsA = ["สีแดง","สีเขียว","สีน้ำเงิน"]
colorsB = ["สีแดง","สีเขียว","สีน้ำเงิน"]
data = colorsA

print(id(colorsA))                  #id() ตรวจสอบ ตำแหน่งหน่วยความจำ
print(id(colorsB))                  #id() ตรวจสอบ ตำแหน่งหน่วยความจำ

print(colorsA is colorsB)           #value เหมือนกัน , แต่ หน่วยความจำ ต่างกัน
                                    #คืนค่า ออกมาเป็น bool
print(colorsA is data)              #อยู่ใน ตำแหน่งหน่วยความจำ เดียวกัน , เหมือน data
print(colorsA is not colorsB)       

data[0] = "สีขาว"                    #แก้ไขข้อมูล , แต่ หน่วยความจำ ยังเท่าเดิม
print(id(colorsA))
print(id(data))

#ตัวดำเนินการสมาชิก (Membership operator)
colors_2 = ["สีแดง","สีเขียว","สีน้ำเงิน"]
print("สีแดง" in colors_2)                       #in , "สีแดง" อยู่ในกลุ่ม colors_2 ไหม
print("สีดำ" not in colors_2)                    #not in , สีแดง ไม่ได้อยู่ในกลุ่ม colors_2 ใช่ไหม