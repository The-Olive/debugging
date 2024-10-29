# This code is a debugging assignment

# Making the document path and the content within
db = open("output.txt", "a")
a = "Hello"
b = "How do you do?"
db.write(a + ", " + "\n" + b)
db.close()

# Making the document readable by humans
db = open("output.txt", "r")
print(db.read())
db.close()