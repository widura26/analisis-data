#tuples are used to store multiple items in a single variable
#tuple is an immutable data type, meaning the value of tuple cannot be changed after it has been assigned.

thisTuple = ("apple", "banana", "cherry", "grape", "watermelon", "mango", "orange")
print('items in index 2:5 ', thisTuple[2:5])
print('element in :4 ', thisTuple[:4])
print('element in 2: ', thisTuple[2:])

#to get tuple item, you can use index
print('item in index 0', thisTuple[0])
print('item in index -1', thisTuple[-1])

#range of negative indexes
print('elements from index -3 to -1', thisTuple[-3:-1])

#range of indexes
print(thisTuple[2:5])


#tuple length
print('length of tuples', len(thisTuple))

# tuple with one item
thisTuple = ("apple",) # you have to use comma
#not a tuple => thisTuple = ("apple")
print(thisTuple)

#tuple items - Data types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

tuple4 = ("abc", 34, True, 40, "male")
print(type(tuple4))

#the tuple() constructor
tup = tuple(("apple", "banana", "cherry"))
print(tup)

#check if item exists
if "apple" in thisTuple :
    print('Yes, there is apple in fruits tuple')
    
#change tuple values
x = ("durian", "apple", "kiwi")
y = list(x)
y[1] = "orange"
x = tuple(y)

print(x)

#add items
# 1. Add tuple to a tuple
why = ("apple", "banana", "ceherry")
y = ("orange",)
why += y
print(why)

