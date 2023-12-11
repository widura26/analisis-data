thisSet = {"apple", "banana", "cherry"}
print(thisSet)

#Duplicates not allowed
thisSet2 = {"apple", "banana", "cherry", "apple"} #jika ada elemen yang sama, maka elemen tersebut akan ditunjukkan salah satu.
print(thisSet2)

#the values True and 1 are considered the same value in sets, and are treated as duplicates :
thisSet3 = {"apple", "banana", "cherry", True, 1, 2}
print(thisSet3) #begitu juga dengan False dan 0. kedua nilai tersebut akan dianggap sama

#Get the Length of a set
print(len(thisSet))

#Set items - Data types => set items can be of any data type
#type() sets are defined as objects with the data type 'set'

#The set() constructor
thisSet4 = set(("apple", "banana", "cherry"))
print("constructor : ", thisSet4)

''' 
Access Set Items -> You cannot access items in a set by referring to an index or a key.
But you can loop through the set items using a for loop, or ask if a specified value is present
in a set, by using the in keyword
'''

thisSet5 = {"apple", "banana", "cherry"}
for x in thisSet5 :
    print(x)

#check if "banana" is present in the set
print("banana" in thisSet5)

#change items -> You cannot change it's items, but you can add new items.
#Add Items
thisSet6 = {"apple", "banana", "cherry"}
thisSet6.add("orange")
print(thisSet6)

#add elements from tropical iinto thisset6
tropical = {"pineapple", "mango", "papaya"}
thisSet6.update(tropical)
print(thisSet6)

#add any iterable
myList = ["kiwi", "orange"]
thisSet6.update(myList)
print(thisSet6)

#remove item
thisSet7 = {"Minji", "Hanni", "Haerin", "Danielle", "Hyein"}
thisSet7.remove("Minji")
print(thisSet7)

#you can use discard()
thisSet7.discard("Hanni")
print(thisSet7)

#you can also use pop() => thisSet7.pop() / but this method will remove a random item.
#the clear() method empties the set -> thisset.clear()
#the del keyword empties the set -> del thisset

#loop items
thisSet8 = {"apple", "banana", "cherry"}

for x in thisSet8 :
    print(x)

#Join thwo sets
set1 = {"apple", "banana", "cherry"}
set2 = {"pineapple", "kiwi", "orange"}

set3 = set1.union(set2)
print(set3)
set1.update(set2)
print(set1)

#keep only the duplicates
x = {1,2,3}
y = {4,5,1}

x.intersection_update(y)
print(x)

z = {1,2,3}
q = {4,5,1}
w = z.intersection(q)
print(w)

#keep all, but not the duplicates
x2 = {"apple", "banana", "cherry"}
y2 = {"google", "microsoft", "apple"}

x2.symmetric_difference(y2)
print(x2)
