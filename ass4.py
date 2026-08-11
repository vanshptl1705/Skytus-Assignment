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



# 11 Create a dictionary storing student names and marks.



# 12 Add a new key-value pair to an existing dictionary.



# 13 Delete a key-value pair from a dictionary.



# 14 Merge two dictionaries into one.



# 15 Check if a key exists in a dictionary.



# 16 Count word frequency in a given string using a dictionary.



# 17 Find the key with the maximum value in a dictionary.



# 18 Reverse keys and values in a dictionary.



# 19 Update the value for a specific key.



# 20 Convert a list of tuples into a dictionary.