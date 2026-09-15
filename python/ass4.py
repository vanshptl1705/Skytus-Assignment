# 1 Create a tuple with 5 numbers.

t1 = (5 , 10 , 15 , 20 , 25)
print(t1)

# 2 Access the third element in a tuple.

t1 = (5 , 10 , 15 , 20 , 25)
print(t1[2])

# 3 Unpack a tuple into separate variables.

name = ("riddhesh","parth","pratham","sujal","meet")
(gandevi , *bilimora, chikhli) = name
print(gandevi)
print(bilimora)
print(chikhli)

# 4 Create a set of 5 fruits.

fruits = {"banana" , "apple" , "kiwi" , "orange" , "cherry"}
print(fruits)

# 5 Add a new fruit to the set.

fruits = {"banana" , "apple" , "kiwi" , "orange" , "cherry"}
fruits.add("strawberry")
print(fruits)

# 6 Remove an element from a set.

fruits = {"banana" , "apple" , "kiwi" , "orange" , "cherry"}
fruits.remove("apple")
print(fruits)

# 7 Find union of two sets.

fruits = {"banana" , "apple" , "kiwi" , "orange" , "cherry"}
fruits2 = {"banana" , "apple", "watermelon" , "strawberry"}
fr = fruits | fruits2
print(fr)

# 8 Find intersection of two sets.

fruits = {"banana" , "apple" , "kiwi" , "orange" , "cherry"}
fruits2 = {"banana" , "apple", "watermelon" , "strawberry"}
fr = fruits & fruits2
print(fr)

# 9 Check if one set is subset of another.

fruits = {"banana" , "apple" , "kiwi" , "orange" , "cherry"}
fruits2 = {"banana" , "apple", "watermelon" , "strawberry"}
fr = fruits - fruits2
print(fr)

# 10 Convert a list with duplicate values into a set to remove duplicates.

l1 = [1,2,3,4,5,6,1,2,3]
s1 = set(l1)
print(s1)

# 11 Create a dictionary storing student names and marks.

dic = {
    "riddhesh" : 36,
    "parth" : 46,
    "pratham" : 56 
}

print(dic)  

# 12 Add a new key-value pair to an existing dictionary.

dic.update({"shrey" : 45})
print(dic)

# 13 Delete a key-value pair from a dictionary.

dic.pop("parth")
print(dic)

# 14 Merge two dictionaries into one.

dic = {
    "riddhesh" : 36,
    "parth" : 46,
    "pratham" : 56 
}
dic2 = {"student1" : 65,
        "student2" : 54}
dic.update(dic2)
print(dic)

# 15 Check if a key exists in a dictionary.

dic = {
    "riddhesh" : 36,
    "parth" : 46,
    "pratham" : 56 
}

if "riddhesh" in dic:
    print("key is exists in dictionary")
else:
    print("key is not exists in dictionary")

# 16 Count word frequency in a given string using a dictionary.

words = "dog cat dog cat dog cat rabbit rabbit"
w1 = words.split()
co = {}

for word in w1:
    if word in co:
        co[word]=co[word]+1
    else:
        co[word]=1
print(co)

# 17 Find the key with the maximum value in a dictionary.

dic = {
    "riddhesh" : 36,
    "parth" : 46,
    "pratham" : 56 
}
k = list(dic.keys())
v = list(dic.values())

print("key with the maximum value in a dictionary is", k[v.index(max(v))])

# 18 Reverse keys and values in a dictionary.

dic = {
    "riddhesh" : 36,
    "parth" : 46,
    "pratham" : 56 
}
newDic = {}

for r in dic:
    newDic[dic[r]] = r

print(newDic)
    

# 19 Update the value for a specific key.

dic = {
    "riddhesh" : 36,
    "parth" : 46,
    "pratham" : 56 
}
dic["parth"] = 70
print(dic)

# 20 Convert a list of tuples into a dictionary.

tup = (("a" , "red"),("b","blue"),("c","black"))
d = dict(tup)
print(d)