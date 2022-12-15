
# Practise for loop
#ask the user  a number like 2345
#calculate sum of digits ------>>>> 2+3+4+5


#Logic
#num ="2345"
#int(num[0])---->2
#int(num[1])-->>>3
#int(num[2])--->>4
#int(num[3])--->>5



# total=0
# num=input("enter the number: ")
# for i in range (0,len(num)):
    # total+=int(num[i])        #using(print(i))give the position of digits of numbers
#     print(i)
# print(total)      
 



# 2nd ,method to find the sum of digits of a given numbers

# def getSum(n):
#     sum=0
#     for digit in str(n):
#         sum+=int(digit)
#     return sum
# n=569
# print(getSum(n))
# for i in str(n):
#     print(n)

# 3rd method

#another method to find sum of the digits of a given numbers
# n1=int(input())
# x=n1    
# s=0
# while n1>=1:
#     s=s+n1%10
#     n1=n1//10
# print("Sum of the digits of ",x,"is",s)



#Sum of digits 
# a=2336
# x1=a
# sum=0
# while a>=1:
#     sum=sum+a%10
#     a=a//10
# print("sum of digits of",x1,"is ",sum)     



# (6th) # print the sum  of  1st 10 natural numbers  for loop:


# n= 1,2,3,4,5,6,7,8,9,10
# total=0
# for i in range (0,11):
#     total+=i
# print(total) 
# print(i)  

# for i in n:
#     print(i)


#python program to calculate
# sum of even numbers from 1 to  100:

#max=100
#total=0
#for i in range (1,max+1):
#     if(i%2==0):
#         print(i)
#         # print("{0}.format(num")       #this also will print even numberts b/w 1 to 100+1
#         total+=i
# print(total)        



# 7 qestion : print the sum of odd numbers  b/w 1 to 33+1

# max1=33
# total=0
# for i in range (1,max1+1):
#     if (i%2!=0):
#         print(i)
#         total+=i
# print(total)        


# ( 8 qestion no ):-->> write a program and print even numbers and odd numbers from 1 to 100:
max2=100
total=0
for i in range (1,max2+1):
    if i%2==0:
        print(i)
        
# to print odd numbers from 1 to 100:::>>>>       

a=100
total=0
for i in range (1,100+1):
    if (i%2!=0):
        print(i)
    











