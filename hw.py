book = {
    "English" : 200,
    "Math" : 150,
    "Physics" : 250,
    "Chemistry" : 240,
    "Biology" : 260
}
print(book)
print()

#Task(a)
book["Physics"] = 200
print(book)
print()

#Task(b)
book["History"] = 300
book["Economics"] = 270
print()

#Task(c)
print("Which text book do you need?")
print("1)Eglish \n2)Math\n3)Physics\n4)Chemistry\n5)Biology")
choice = input("Please type in the subject name : ")
print("Price of " + choice + " textbook is " + str(book[choice]) + " Euro")
print()

#Task(d)
for key in book.keys():
    print(str(key) + " : " + str(book[key]))
print()