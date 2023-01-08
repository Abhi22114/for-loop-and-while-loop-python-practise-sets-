# take a example of list or set  assign the valves in varriable and
#  print the valve in sequences
# l--->>[123,abhi,9918,my_password]
# x,y,z,a=l
# print all the charecters in a separated line

example=[123,"abhi",9918,"my_password"]
x,y,z,a=example
print(x)
print(y)
print(z)
print(a)

# 2  Define a variable  inside and outside a varriable and print it inside  a function

x1= " python is easy to  learn "

def myfunc():
  x1=" is very handsome "
  print("Raja" + x1)
myfunc()    
print("Raja Says"+x1)


# 3.print your father's name using end parameters
first_name="Ravindra "
last_name="Chaudhur"
print("My Father's name is",first_name,last_name,end=" ")


# 3.question:--->
# print the following as a output
#  "My name " is abhijeet
#  My name is    abhijeet
#  My name is abhijeet //
# My name is abhijeet n\\
# My name is abhijeet \\
#  Abhijeet kumar in new line 

print("\"My name\" is abhijeet")
print("My name is\tabhijeet")
print("My name is abhijeet",end=" // ")
print("My name is abhijeet n\\\\")
print("My name is abhijeet",end=" \\\\")
print("Abhijeet\nKumar")







