thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "Electric": False,
    "colors": ["red", "white", "blue"]
}

print(thisDict)
print(thisDict["brand"])
print(len(thisDict))

#constructor
thisDict1 = dict(name = "John", age = 36, country = "Norway")
print(thisDict1)

x = thisDict["model"]
x2 = thisDict.get("model")
print(x2)

x3 = thisDict.keys()
print(x3)

#add items
thisDict["Type"] = "suv"
print(thisDict)

#Get values
x4 = thisDict.values()
print(x4)

#change value
thisDict["brand"] = "Toyota"
print(thisDict)

#Get items
x5 = thisDict.items()
print(x5)

for x in thisDict :
    print(x)

for x in thisDict :
    print(thisDict[x])

#nested dictionaries
myFanily = {
    "child1" : {
    "name" : "Emil",
    "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }
}
