# 1. Write a program to read a file and display its contents.

f = open("demo.txt", "r")
print(f.read())
f.close()

# 2. Write a program to count the number of lines in a file.

f = open("demo.txt", "r")
count=0

for line in f:
    count=count+1
    
print("Total", count, "number of lines in a file.")
f.close()   

# 3. Write a program to count how many times each word appears in a file.

f = open("demo.txt", "r")
text=f.read()
wo = text.lower().split()
words = "python"

count=0
for w in wo:
    if w == words:
        count=count+1
f.close()

print("Total" ,count, "times Python word appears in a file.") 

# 4. Write a program to write 5 user-entered sentences to a file.

f= open("wr.txt","w")

for i in range(1,6):
    sen=input(f"user-{i} please enter the sentence:")
    f.write(sen + "\n")
f.close()

# 5. Write a program to append a list of strings to an existing file.

l=list(input("Please enter words:").split())
f= open("wr.txt","a")

for i in l:
    f.write(i + "\n")
f.close()

# 6. Write a program to read a file and print only lines containing a specific word.

f = open("demo.txt", "r")
w="python"

for li in f:
    if w in li.lower():
        print(li)
f.close()

# 7. Write a program to replace a specific word in a file and save changes.

f=open("wr.txt","r")
change = f.read().lower()
f.close()
change=change.replace("python","Favourite Language Python")
f=open("wr.txt","w")
f.write(change)
f.close()

# 8. Write a program to merge the contents of two text files into a third file.

f=open("wr.txt","r")
a = f.read()
f.close()

e=open("demo.txt","r")
b = e.read()
e.close()

c=open("new.txt","w")
c.write(a + "\n" + b)
c.close()

# 9. Write a program to read a CSV file and display its content in a formatted way.

import csv
f=open("sample-quoted.csv","r")
d = csv.reader(f)
for data in d :
    print(data)
f.close()

# 10. Write a program to back up a file by copying its contents into another file.

f=open("demo.txt","r")
d=f.read()
f.close()

b=open("back.txt","w")
b.write(d)
b.close()

print("your demo.txt data are backup in file:back.txt.")