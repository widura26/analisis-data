#operasi logika atau boolean

#not or and xor

#not
print('===NOT===')

a = False
c = not a
print('data a =', a)
print('---------NOT')
print('data c =', c)

#or

print('===OR===')

a = False
b = False
c = a or b
print(a, 'OR',b, '=', c)
a = False
b = True
c = a or b
print(a, 'OR',b, '=', c)
a = True
b = False
c = a or b
print(a, 'OR',b, '=', c)
a = True
b = True
c = a or b
print(a, 'OR',b, '=', c)

print('===AND===')

a = False
b = False
c = a and b
print(a, 'AND',b, '=', c)
a = False
b = True
c = a and b
print(a, 'AND',b, '=', c)
a = True
b = False
c = a and b
print(a, 'AND',b, '=', c)
a = True
b = True
c = a and b
print(a, 'AND',b, '=', c)

print('===XOR===')

a = False
b = False
c = a ^ b
print(a, 'XOR',b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'XOR',b, '=', c)
a = True
b = False
c = a ^ b
print(a, 'XOR',b, '=', c)
a = True
b = True
c = a ^ b
print(a, 'XOR',b, '=', c)