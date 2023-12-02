#built-in data types
#Text type : str
#Numeric Types : int, float, complex
#sequence types : list, tuple, range
#Mapping Type : dict
#set types : set, frozenset
#boolean Type : bool
#Binary types : bytes, bytearray, memoryview
#none type : NoneType

# Getting the Data Type
x = 5
print(type(x));

#setting the data type

#string
a = "Hello World"
#int
b = 20
#float
c = 20.5
#complex, merepresentasikan angka kompleks, kompleks terdiri dari bagian real dan bagian imajiner (aljabar)
d = 1j
#list
e = ["apple", "banana", "cherry"]
#tuple, struktur data yang digunakan untuk menyimpan kumpulan elemen yang berbeda. (bersifat immutable / tidak dapat diubah)
f = ("apple", 1, 3.14)
#range, merepresentasikan deret angka secara berurutan. digunakan ketika melakukan iterasi. range(start, stop, step)
g = range(6)
#dict / dictionary
h = {"name": "John", "age": 36}
#set
i = {1, 2, 3, 4, 5}
#frozenset
j = frozenset({"apple", "banana", "cherry"})
#bool
k = True
#bytes
l = b'hello world'
#bytearray
m = bytearray(5)
#memoryview
n = memoryview(bytes(5))
#Nonetype
o = None

print(type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h), type(i), type(j), type(k), type(l), type(m), type(n), type(o))
