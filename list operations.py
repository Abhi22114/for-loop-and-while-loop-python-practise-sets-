
#listoperation.py

#1 ask the user the to take a list(which contain string input) ,and 
# assing them unique id (starting from zero) in the sequence they are
#registered suppose unique ID given to first student is 0 then 
# unique id of the next student will be next odd, value

# soltions:

#a=list(map(str,input("names: ").split(",")))
# for i in range(len(a)):
    # print(i**n,a[i])
a=['abhijeet','raja','jhon','motu']
for i in range(len(a)):
    print(i*3,a[i])
    print(a)

#2 two print odd odered code values in list(data at odd ordered position in the list):
# ex- [1,2,3,4,5]
# here : 1----->>0,2----->>>>1,3---->>>>2,4----->>>3,5---->>>>4rth position 
#odd-2,4
#even ordered-1,3,5

# solutions:

# a=list(map(int,input("list: ")))
# a=[1,2,3,4,5,6,6,89,60]
# print(a)
# t=0
# for i in a:
#     if i==0:
#         t+=1
# if t==0:
#     for i in range(len(a)):
#         if i%2!=0:
#             print(a[i],end=" ")
# else:
#     print("Invalid")



#3 take a list and print the absolute diffrence b/w the maximum and minimum of the square of ()**4

# #a=list(map(int,input("list: ")))
# a1=[9,2,7]
# print(max(a1)**3)
# print(min(a1)**3)
# print(abs(min(a1)**4-min(a1)**4))
# for i in a1:
#     print(a1)
 

  #4 ask teh user two take to list of integers and return the elements of list 1 excluding
  #  the common elements  in both lists

a1=[1,2,3,4]
a2=[9,5,6,2,4]
r=[]
for i in range (len(a1)):     #output -[1,3]
    if a1[i] in a2:
        continue
    else:
        r.append(a1[i])
print(r) 


#l  adding of to list
x=[1,2,3,4,5,6] 
y=[29.5,6,1,2]
list3=x+y
print(x+y)

#take a list of numbers or fruits  and print  the value in different line
# this is done with for loop
numbers1=[1,2,3,4,5,6]
for i in  numbers1:
    print(i)

# with help of while loop

fruits=['banana','apple','orange','kiwi']
i=0
while i<len(fruits):
    print(fruits[i])
    i+=1

   
    