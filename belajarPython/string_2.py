# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)

# Strings are Arrays
a = " hello, world "
print("huruf yang beraada di index 1 : " + a[1])

for x in a:
    print(x)

print("Jumlah karakter pada kalimat hello word : ", len(a));

#check string in sentence
print("Hello" in a) #kata yang dicheck harus sama persis. (false)
print("hello" in a) #kata yang dicheck harus sama persis. (true)
# Jika di kalimat 'hello' dan dicheck 'Hello' maka outputnya akan false karena python memiliki case sensitive

if "hello" in a :
    print("Yes, 'free' is present")
    
print("hello" not in a)
print("free" not in a)

#slicing strings
print(a[0:3]) # index 3 not included

#slice from the start
print(a[:5]) #index 5 not included

#slice to the end
print(a[2:])

#negative indexing
print(a[-3:-2])

#upper case
print(a.upper())

#lower case
print(a.lower())

#remove whitespace (menghilangkan spasi)
print(a.strip())

#replace string (mengganti huruf)
print(a.replace('l', 'w'))

#split string
print(a.split(","))

#string concatenation
x = "Hello"
y = "World"
z = x + y
w = x + " " + y
print(w)
print(y)

#string format
age = 36
txt = "My name is Widura, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
myorder2 = "I want to pay {2} dollars for {0} pieces of item {1}"
print(myorder.format(quantity, itemno, price))
print(myorder2.format(quantity, itemno, price))

#escape character
txt2 = "We are the so-called \"Vikings\" from the north."
print(txt2)
