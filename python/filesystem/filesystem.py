import os

## To open a new file for writing data in it, specify O_WRONLY as well as O_CREAT modes by inserting pipe (|)
#  operator. The os.open() function returns a file descriptor.

# Sr.No.	Os Module & Description
# 1	
# os.O_RDONLY

# Open for reading only

# 2	
# os.O_WRONLY

# Open for writing only

# 3	
# os.O_RDWR

# Open for reading and writing

# 4	
# os.O_NONBLOCK

# Do not block on open

# 5	
# os.O_APPEND

# Append on each write

# 6	
# os.O_CREAT

# Create file if it does not exist

# 7	
# os.O_TRUNC

# Truncate size to 0

# 8	
# os.O_EXCL

# Error if create and file exists

# f = os.open("service.dat", os.O_WRONLY | os.O_CREAT)

# data = "How To Change the World".encode('utf-8')
# print(data)

# os.write(f, data)
# os.close(f)



# # Read from file
# f = os.open("service.dat", os.O_RDONLY)
# data = os.read(f,20)
# print(data)

#create file
#open file
#write to file
import os

f = os.open("inventory.csv", os.O_WRONLY | os.O_CREAT | os.O_APPEND)
data = "Section".encode("UTF-8")
os.write(f, data)


#open file
#read from file

# f = os.open("inventory.csv", os.O_RDONLY)
# data = os.read(f, 100)

# print(data)

# os.close(f)


item2 = ["Hisense Tv", "Television", "Image", 300000, "Electical Appliance"]

item1 = [ "Fanta", "Orange Drink", "Image", 200, "Drinks"]

# data=bytearray(item2)
# file.write(data)
# file.close()

# file = open("service.txt", "a")
# # numbers=[10,20,30,40]
# data=bytearray(item1)
# file.write(data+"/n")
# file.close()

# f = open("service.txt", "rb")
# data = f.read()
# print(bytearray(data))

# from pickle import dumps, loads

# data = dumps(item1)

# print(data)

# data = loads(data)
# print(data)


import pickle 

# Create and Write to File
f = open("pickle_test.txt", "ab")
items = str(item1)
data = pickle.dump(items, f)
f.close()


# Read from file

r = open("pickle_test.txt", "rb")
d = pickle.load(r)
print(d)
r.close()
