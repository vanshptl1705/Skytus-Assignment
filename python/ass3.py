# 1 Take a string input and print its length.

z = "Hey Dear!!!"
print(z, "Total Length is", len(z))

# 2 Convert a sentence to lowercase.

z1 = ("LANGUAGE")
print(z1, "in Lower case is" ,z1.lower())

# 3  Replace spaces with underscores in a string.

z = "Hey Dear!!!"
print(z.replace(" " , "_"))

# 4 Extract the first and last character of a string.

z = "Hey Dear!!!"
print("First letter is" ,z[0], "& Second letter is", z[10])


# 5 Reverse a string using slicing.

z1 = "Hey Dear"
print("Reverse a string is" ,z1[::-1])

# 6 Count how many times a letter appears in a string.

z2 = "Heyyy everyone"
print(z2.count("y"))


# 7 Check if a word is present in a sentence.

z = "Hey Dear!!!"
w = "Hey"

if w in z:
    print(w, "Word is Present in" ,z)
else:
    print(w, "Word is not Present in" ,z)


# 8 Take name & age and print using f-string formatting.

n = input("Enter your Name:")
a = int(input("Enter your Age:"))
s = f"Username is {n} and Age is {a}"
print(s)

# 9 Remove extra spaces from the start and end of a string.

z3 = "   Hey Dear  !!!   "
print(z.strip())

# 10 Join a list of words into a single string with - between them.

w1 = ["Lets" , "Play" , "Games"]
w2 = "-".join(w1)
print(w2)

# 11 Create a list of your 5 favorite movies.

wo1 = ["Iron-man","Spider-man","Thor","Hulk","Captain-america"]
print(wo1)

# 12 Add a new movie to the list.

wo1 = ["Iron-man","Spider-man","Thor","Hulk","Captain-america"]
wo1.append("hawkeye")
print(wo1)

# 13 Remove the first movie from the list.

wo1.remove("Iron-man")
print(wo1)

# 14 Sort a list of numbers in ascending order.

wo1.sort()
print(wo1)

# 15 Reverse a list.

wo1.reverse()
print(wo1)

# 16 Find the largest number in a list.

w2 = [20 , 25 , 30, 11 , 12]
lar = max(w2)
print("largest number in a list", lar)

# 17 Merge two lists into one.

wo1 = ["Iron-man","Spider-man","Thor","Hulk","Captain-america"]
w2 = [20 , 25 , 30, 11 , 12]
w3 = wo1 + w2
print(w3)


# 18 Access the last element of a list without using index number.

w2 = [20 , 25 , 30, 11 , 12]
print("last element of a list", w2.pop())


# 19 Create a nested list and access a specific inner element.

w4 = [[1,2,3],[4,5,6],[7,8,9],[]]
print(w4[0][1])
print(w4[1][2])

# 20 Count how many times an element appears in a list.

w2 = [20 , 25 , 30, 11 , 12 , 20 , 32 , 20]
q = w2.count(20)
print(q, "element appears in a list")