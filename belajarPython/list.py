myList = ["apple", "banana", "cherry", "kiwi", "melon", "orange", "mango"]
print(myList)

#length
print('length from list : ', len(myList))

#type
print('type : ', type(myList))

#the list() constructor
thisList = list(("apple", "banana", "cherry"))
print(thisList)

#access items
print('index the first item is : ', myList[1])

#negative indexing
print('element thaat index -1 is : ', myList[-1])

#range of indexes
print('elements that range 2 to 4 are:', myList[2:5])
print(myList[:4])
print(myList[2:])

#range of negative indexes
print('elements that range -4 to -1 are:', myList[-4:-1])

#check if item exists
if "apple" in myList :
    print("Yes, ada")

#change item value
myList[5] = 'grape'
print('original : ', myList)

#change a Range of Item values
myList[1:2] = ['blueberry','dragonfruit']
print('change : ', myList)

#insert items
myList.insert(0, 'watermelon')
print(myList)

#append items (add an item to the end of the list)
myList.append("salak")
print(myList)

#extend list
newjeans = ["Minji", "Hanni", "Danielle", "Haerin", "Hyein"]
lesserafim = ["Sakura", "Chaewon", "Yunjin", "Kazuha", "Eunchae"]
newjeans.extend(lesserafim)
print(newjeans)

#Add any iterable
jus2 = ("Jaebeom", "Yugyeom")
newjeans.extend(jus2)
print(newjeans)

#remove list items
#remove specified item
newjeans.remove("Yugyeom")
print(newjeans)

#remove specified index
newjeans.pop(1) #jika tidak ada index yang spesifik, maka function pop akan menghapus item yang terakhir
print(newjeans)

#del newjeans[0] # jika tidak ada index yang spesifik, maka keyword del akan menghapus secara keseluruhan
# print(newjeans) 

# newjeans.clear()
# print(newjeans)

#loop throught a list
names = ['widura', 'hasta', 'sasangka']
for x in names :
    print(x)

#loop through the index numbers
for i in range(len(names)) :
    print(names[i])

#using a while loop
index = 0
while i < len(names) :
    print(names[i])
    i = i + 1

#looping using list compehension
[print(x) for x in names]

#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []
for x in fruits :
    if "a" in x :
        newList.append(x)
print('newList ', newList)

#sort list alphanumerically
fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruits.sort()
print('fruits', fruits)

#sort descendiong
fruits.sort(reverse = True)
print('fruits', fruits)

# customize sort function
def myFunc(n) :
    return abs(n - 50)

numberList = [100,50,65,82,2]
numberList.sort(key = myFunc)
print(numberList)

#Case Insensitive Sort
nameList = ["Widura","Hasta","Sasangka"]
nameList.sort(key = str.lower)
print('insensitive', nameList)

#sensitive sort
# nameList.sort(key = str.lower)
# print(nameList)

#reverse order
buah = ["banana", "Orange", "Kiwi", "cherry"]
buah.reverse()
print(buah)

#copy a list
li = ["apple", "banana", "cherry"]
liCopy = li.copy()
#another way : use list(). for example, liCopy = list(li)
print(liCopy)

#join two lists
list1 = ["a", "b", "c"]
list2 = [1,2,3]

list3 = list1 + list2
print(list3)

#another way to join two lists
for x in list2 :
    list1.append(x)

print(list1)

#another way again
list1.extend(list2)
print(list1)



