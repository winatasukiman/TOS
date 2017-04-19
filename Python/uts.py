#!usr/bin/env python
import sys

#1 
print("\n")
print("hello")

#2
print("\n")
name = "Winata"
print("Isi dari Variabel Nama: ",name)

#3 
print("\n")
print("5 + 2 = ",5+2)

#4
print("\n")
quote = "\"always remember u are unique"
print(quote)
multi_line_quote=''' just like everyone else '''
print(multi_line_quote)

#5 print \n sebanyak 5
#print("\n" * 5)
#print("Enter sebanyak 5x"

#6 list
print("\n")
list = ["Juice","Tomatoes"]
print("First item of list",list[0])
list[0] = "Green Juice"#array ke 0 diganti 
print("First item of new list",list[0])
print(list[0:2])#print list <2

other_list = ["Wash Car","Pick Up Kids","Cash Check"]
to_do_list = [other_list , list ]
print(to_do_list)
print((to_do_list[0][0]))
list.append("Onion")#menambah isi dari list
list.insert(1,"Pickle")#insert index ke 1
list.remove("Pickle")#remove pickle
list.sort()
list.reverse()
del list[0]
print(list)

to_do_list2 = other_list + list
print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))

#7 Tuple
print("\n")
#tuple = (1,2,3,4,5)
#new_tuple = list(tuple)
#new_list = tuple(new_tuple)
#len(tuple) min(tuple) max(tuple)

villain = {"Fiddler" : "Isaac"}
print(villain['Fiddler'])#print isi fiddler
villain["Fiddler"] = "Gary" 
print(villain['Fiddler'])
print(villain.keys())
print(villain.values())

#8
print("\n")
def donuts(count):
  don= "Number of donuts: "
  if count < 10:
    don= don + count
  elif count >= 10:
    don= don + "many"
  return don

print(donuts(5))
#9
