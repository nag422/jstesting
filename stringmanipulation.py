a = "Helloo"
# print(a.capitalize())
# print(a.upper())
# print(a.lower())
# print(a.casefold()) #is nothing but lower()
# for i,k in enumerate(a):
#     print(k.center(i+20)) # i is an index
#     print(k.center(i+20), "wow")
# print(a.count("o"))
arr = []
for i in a:
    arr.append({i:a.count(i)})
# fin = list(map(lambda key: key, arr[0].keys()))
# print(fin)
# get_data = lambda x: [i for i in arr if i[0] == x]
# print(lambda x: [i for i in arr if i[0] == x])
# print(arr)

# arr remove duplicates
# finarr = []
# for i,k in enumerate(arr):
#     dt = k.items()
#     for j in dt:
#         if(j[1] == 2):
#             finarr.insert((finarr.__len__() - 1),j[1]) #insert is the index of insert

#     # print(list(dt), k, i)
#     # print("value", arr[i][list(dt)])
# print(finarr)


# text = "The best things in life are free!"
# if "things" in text:
#     print("yes")


# b = "Hello, World!" #slicing dont change the original value
# print(b[2:7]) # string slice from the beginning
# print(b[:-1]) # string slice from the last

# astr = "Hello, World! "
# print(astr.strip())
# print(astr.replace(" ",""))

# quantity = 3
# itemno = 567
# price = 49.95
# my_order = "I want {} and good {} super salos"
# print(my_order.format(quantity, itemno, price))


# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)


#This example erases one character (backspace):
# txt = "Hell\bo \bWorld!"
# print(txt) 


txt = "My name is Ståle"

# x = txt.encode()

# print(x)

# print(txt.encode(encoding="ascii",errors="backslashreplace"))
# print(txt.encode(encoding="ascii",errors="replace"))
# print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

# print(txt.endswith("e"))

# txt = "H\te\tl\tl\to"
# print(txt.expandtabs(12)) # tabs with seperator



# txt = "Hello, welcome to my world."

# x = txt.find("welcome") # returns -1 if not found else starting of index
# txt.find("e", 5, 10) # search in particular index places
# print(x)


# txt = "Hello, welcome to my world."
# x = txt.index("my") #apply catch error else it throws the error.
# print(x) #returns the index of start

# txt = "Company12"
# txt1 = "Company"
# txt2 = "12345"
# x = txt.isalnum()
# print(x)

# print(txt1.isalpha())
# print(txt.isascii())
# print(txt2.isdecimal())


# a = "\u0030" #unicode for 0
# b = "\u0047" #unicode for G

# print(a.isdecimal())
# print(b.isdecimal())


# txt = "50800"

# x = txt.isdigit() # digit without float

# print(x)


# txt = "Demo"

# x = txt.isidentifier()

# print(x)

# a = "MyFolder"
# b = "Demo002"
# c = "2bring"
# d = "my demo"

# print(a.isidentifier())
# print(b.isidentifier())
# print(c.isidentifier())
# print(d.isidentifier())



# txt = "hello world!"
# x = txt.islower() # checks weather all chars are lower
# print(x)

# txt = "23545"
# print(txt.isnumeric()) # returns false if -ve and float numbers


# txt = "Hello! Are you #1?"
# print(txt.isprintable()) #checks is printable or not for pdf print etc.


# txt = "Hello!\nAre you #1?" 
# print(txt) #checks is printable or not for pdf print etc.


# txt = "     "
# x = txt.isspace() # return true if all are space chars
# print(x)

# txt = "Hello, And Welcome To My World!"
# x = txt.istitle() # returns true if all firstletter of each word.
# print(x)

# txt = "THIS IS NOW!"
# x = txt.isupper()
# print(x)


# a = "Hello World!"
# b = "hello 123"
# c = "MY NAME IS PETER"

# print(a.isupper())
# print(b.isupper())
# print(c.isupper())

# myTuple = ("John", "Peter", "Vicky")
# x = "  ".join(myTuple)
# print(x)


# myDict = {"name": "John", "country":"Norway", "faminity":"Male"}
# mySeperator = "TEST"

# x = mySeperator.join(myDict)
# print(x)


# txt = "banana"

# x = txt.ljust(12) # banana             is my favorite fruit.

# print(x, "is my favorite fruit.")

# x = txt.ljust(20, "O") # bananaOOOOOOOOOOOOOO
# print(x)

# x = txt.lstrip() # left space strips only

# txt = ",,,,,ssaaww.....banana"
# x = txt.lstrip(",.asw") # removes the leading chars.
# print(x)



# txt = "Hello Sam!"
# mytable = str.maketrans("S","P")
# print(txt.translate(mytable))


# txt = "I could eat bananas all every days bananas day"
# x = txt.partition("bananas")
# print(x)


# txt = "I could eat bananas all day"
# x = txt.partition("apples")
# print(x)

# txt = "I bananas like bananas"
# # x = txt.replace("bananas", "apples") # replace all
# # x = txt.replace("one", "three", 2) # how many occurrences have to replace
# # print(x)
# print(txt.rfind("bananas")) # find last occurence. -1 for no match.

# txt = "apple, banana, cherry, cherry, cherry, cherry"
# # setting the maxsplit parameter to 1, will return a list with 2 elements!
# x = txt.rsplit(", ", 1) #op ['apple, banana, cherry, cherry, cherry', 'cherry']


# txt = "Thank you for the music\nWelcome to the jungle"
# x = txt.splitlines()
# print(x) # ['Thank you for the music', 'Welcome to the jungle']

# x = txt.splitlines(True) #['Thank you for the music\n', 'Welcome to the jungle']
# print(x)
# # startswith()

# txt = "Hello My Name Is PETER"

# print(txt.swapcase())

# txt = "Welcome to my world"
# print(txt.title())
# txt = "hello b2b2b2 and 3g3g3g"
# x = txt.title()

# print(x) # Hello B2B2B2 And 3G3G3G

# txt = "50"
# print(txt.zfill(3)) # adds 0's 050


# print(bool(-1)) # 0, False, None result is false

# print(bool([])) # empty array returns False

# x = 200.00
# y = 200

# print(isinstance(x,float)) # True

# print(isinstance(y,int)) # True

# x = 30
# x &= 10
# print(x)

# x = 5

# x |= 7

# print(x)


# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:8]) # 8 th postion not included upto 8 it works.
# print(thislist[:4])

# # back traversal
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1]) # ['orange', 'kiwi', 'melon']


# change the range of elms

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:4] = ["blackcurrant", "watermelon"] # pass substitues as per no of ilocs other wise the elems will be disappers #['apple', 'blackcurrant', 'watermelon', 'kiwi', 'mango']
# print(thislist) 

# # in one place with 2 substitues

# thislist = ["apple", "banana", "cherry"]

# thislist[1:2] = ["blackcurrant", "watermelon"] #['apple', 'blackcurrant', 'watermelon', 'kiwi', 'mango']
 

# thislist = ["apple", "banana", "cherry"]

# thislist.insert(len(thislist), "watermelon")

# print(thislist)
# thislist.extend(["john","fair"])
# print(thislist)

# # can extend with dicts or arrays with any iterables
# thistuple = ("kiwi", "orange")


# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# thislists = ["apple", "banana", "cherry"]
# del thislists
# del thislist[0]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1) # remove which item index starts from 0;
# print(thislist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)
# print(*range(10)) #0 1 2 3 4 5 6 7 8 9
newlist = [x for x in fruits if x!= 'banana']
print(newlist)
a=[1,2]
b=[*a] #shallow copy
b[0]=5
print(a)
print(b)

newlist = [x if x!= 'banana' else 'orange' for x in fruits] #if else comes then condition adds first or after the for loop
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = ["1", "3", "2", "4", "5"]
thislist.sort()
print(thislist)

thislist.sort(reverse=True)
print(thislist)


def CustomSortFun(n):
    return abs(n-50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key=CustomSortFun)
print(thislist)

print([100, 50, 65, 82, 23]*2) # repeats the list
print([{"hi":"he"}]*2) # repeats the list

print([100, 50, 65, 82, 23]+[2])

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)
thislist.reverse()
print("reversed list", thislist)

newlist = thislist.copy() #shallow copy
newlist[0]="Sing is king"
print(newlist)
print(thislist)

mylist = list(thislist) # shllow copy
print(mylist)

customlist = [1,3,546,3]
mylist = list(customlist)
mylist[0]=3434
print(mylist)
print(customlist)


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = [*list2, *list1]
print(len(list3))


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(apple, *rest, cherry) = fruits
print(apple)
print(rest)
print(cherry)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(8)
print(x)

thisset = {"banana", "apple", "orange"}
thisset.add("Jaguar")
thisset.update({"banana","mango"})
for i in thisset:
    print(i)
thisset.discard("banana")
print(thisset)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
# set3= set1.union(set2)
set1.intersection_update(set2)
print(set1)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
v = x.symmetric_difference(y)
print(z)
convertedtedlist = list(v)
sortedlist = convertedtedlist.sort()
print(convertedtedlist)

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

print(x.issuperset(y))


thisdict = dict(name="John", age=36, country="Norway")
print(thisdict["name"])

if "name" in thisdict:
    print("yes name is here")
