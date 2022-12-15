#Practise for loop
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
 
# total=0
# num=int(input(6345))
# for i in range (0,4):
#     total=i
#     print (i)
# print(total)




# 2nd ,method to find the sum of digits of a given numbers

def getSum(n):
    sum=0
    for digit in str(n):
        sum+=int(digit)
    return sum
n=569
print(getSum(n))
for i in str(n):
    print(n)

    