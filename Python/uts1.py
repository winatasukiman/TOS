#!/usr/bin/env python
import os
import sys

# if else elif == != >= <= > <

#1
age = 10
if age > 16 :
 print("You are old")
else :
 print("You are still young")

if age >= 10 :
 print("You are too young to drive")
elif age >= 16 :
 print("You are old")
else : 
 print ("You are not old")

#logical operator and or not

if((age>=1) and (age<=18)):
 print("You get a birthday")
elif (age == 10) or (age >= 65):
 print("You")

#2 For
print("\n")
for x in range(0,10):
 print(x, ' ')

print("\n")

list = ["Apple" , "Juice"]

for y in list:
 print(y)

for x in [2,4,6,8,10]:
 print(x)

#num_list = [[1,2,3],[10,20,30]]

#for x in range(0,3):
 #for y in range(0,3):
  #print(num_list[x,y])

#3 Define function
print("\n")
def addNumber(fNum,lNum):
 sumNum = fNum + lNum
 return sumNum

print(addNumber(1,2))
 
#4 Inputan
print("\n")
print("What is your name")
name = sys.stdin.readline()
print("Hello", name)

#5 string
print("\n")
string = "I'll catch you if you fall - the floor"
print(string[0:4])
print(string[-5:])
print(string[:-5])
print(string[:4], " be there ")

#print("%c is my %s letter and my number %d number is %.5f" %"X","Favorite",1,.14)

print("Kapital" , string.capitalize())
print(string.find("floor"))
print(string.replace("floor" , "ground"))

