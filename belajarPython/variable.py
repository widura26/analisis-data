#assign Multiple values
# x = y = z = 'Orange'
# print(x);
# print(y);
# print(z);

#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#separated by comma
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#separated by plus
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#Global Variables
x = 'awesome'
def myFunc():
    print('Python is', x)

myFunc()

#Global keyword
def myFunc2():
    global x
    x = 'fantastic'

myFunc2()
print("Python is", x)


