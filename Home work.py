# 1)-:Take two lists of criketers and print the output by removing the common name from the lists

l1=['ABD','Virat','MS Dhoni','Pandaya','Ashwin','Sachin']
l2=['Hitman','Rahul','Dhawan','Virat','Ashwin','Pandaya']
a=[]
for i in range(len(l1)):
    if l1[i] in l2:
        continue
    else:
        a.append(l1[i])
print(a)    


#2)-: To print odd numbers from 1 to 100:::>>>>       

a=100
total=0
for i in range (1,100+1):
    if (i%2!=0):
        print(i)
#3)-:To print even numbers from 1 to 100::::>>>>

b=100
total=0
for i in range(1,100+1):
    if i%2==0:
        print(i)

#4):- Take list of numbers and print the another list by removing the common numbers from the first list :::>>>>

n1=[12,2,3,45,78,9,67,31,0,8]
n2=[2,3,0,9,8,31,78,56,45]
r=[]
for i in range (len(n1)):
    if n1[i] in n2:
        continue
    else:
        r.append(n1[i])
print(r)

#5):- Take a list of actors and print the Unique Id of each present in the list such that the actor at the 
     # the first actor in the list have unique id 0 and next will have next even and so on::>>>

Actor1=['Sunny Deol','Mithun Chakravarti','Nana Patekar','Akshay kumar','Tiger Shrof']     
for i in range (len(Actor1)):
    print(i*4,Actor1[i])


#6):-your task is to take a list of prime numbers and print the abosolute minimum and maximum value of square()**3
#and also print the min()**5

Prime1=[2,3,5,7,11]
print(abs(max(Prime1)**3-(min(Prime1)**3)))
print(min(Prime1)**5)

#7) Your task is to take a list  and print the  even orderded values in the list(elements at the even palace  )
l3=[1,2,3,4,5,6,7]
t=0
for i in l3:
    if i==0:
        t+=1
if t==0:
    for i in range(len(l3)):
        if i%2==0:
            print(l3[i],end=' ')


# 8) your  task is to print the even natural numbers and their from 1 to 10

max =10
sum=0
for i in range(1,max+1):
    if i%2==0:
        print(i)
        sum+=i
print(sum)            


# 9) your task is to print the sum of digits given numbers 203045

x=203045
x1=x
s1=0
while x>=1:

    s1=s1+x%10
    x=x//10
print("sum of the digits of" ,x1, "is",s1)    
     
# your task is to take a number and print its sum using define sum:

t=12216848
def getSum(t):
    sum1=0
    for digits in  str(t):
        sum1+=int(digits)
    return sum1
print(getSum(t))        




