import mymodule

mymodule.greeting("Jonathan")
a = mymodule.person1["age"]
print(a)

# built-in modules
import platform
x = platform.system()
print(x)

#using the dir() function
x = dir(platform)
print(x)

#import from module
from mymodule import person1
print(person1['name'])