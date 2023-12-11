a = 2000
b = 200

if b > a :
    print("b is greater than a")
elif a == b :
    print("a and b are equal")
else :
    print("a is greater than b")

#shorthand if
if a > b : print("a is greater than b .")
print("A") if a > b else print("B")
print("A") if a > b else print("=") if a == b else print("B")

#and

a = 200
b = 33
c = 500
if a > b and c > a :
    print('Both condition are true')

#or
if a > b or a > c :
    print("at least one of the conditions is true")

#not
if not a > b :
    print('hei')    
