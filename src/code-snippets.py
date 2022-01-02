# Return Multiple
import time
import sys
def Test():
    return 100, 200, 300


print("####### Return Multiple >>>>>")
print(Test())  # (100, 200, 300)
# Get in list form
print(list(Test()))  # [100, 200, 300]
print("<<<<< Return Multiple #####")

########################################
#  In-Place Swapping
# Default Way
print("####### In-Place Swapping >>>>>")
print("Default Way >>>>>")
var1 = 90
var2 = 80
temp = var1
var1 = var2
var2 = temp
print(var1, var2)  # 80 90
print("<<<<< Default Way")

# In-Place way
print("In-Place way >>>>>")
var1 = 90
var2 = 80
[var2, var1] = [var1, var2]
print(var1, var2)  # 80 90
print("<<<<< In-Place way")


print("Reversing >>>>>")
# Reversing
mylist = [1, 2, 4, 6, 7]
# Way 1
mylist.reverse()
print(mylist)  # [7, 6, 4, 2, 1]
# Way 2
mylist = mylist[::-1]
print(mylist)  # [7, 6, 4, 2, 1]
print("<<<<< Reversing")


print("Save Memory with Generator >>>>>")
# Save Memory with Generator
# List way
mylst = [x for x in range(1000)]
print(sum(mylst))  # 499500
print(sys.getsizeof(mylst), 'Bytes')  # 9024 Bytes
# Generator way
mylst = (x for x in range(1000))
print(sum(mylst))  # 499500
print(sys.getsizeof(mylst), 'Bytes') # 120 Bytes
print("<<<<< Save Memory with Generator")


print("Slicing the String >>>>>")
# Slicing the String
#example 1 slice by spaces
data = "Welcome to the world of Programming"
sliced = data.split()
print(sliced)

sliced = data.split("the")
print(sliced)
print("<<<<< Slicing the String")

# Prefixes Search
print("Prefixes Search >>>>>")
data1 = "www.medium.com"
data2 = "google.com"
if data1.startswith("www"):
    print("Found!")
else:
    print("Not Found")


if data2.endswith(".com"):
    print("Yes")
else:
    print("No")
    
print("<<<<< Prefixes Search")



# Wait your program
print("Wait your program >>>>>")

def fun():
    print("Program is sleep!")
    time.sleep(5)
    print("Program is wake up!")
fun()

print("<<<<< Wait your program")


# Concatinate list
print("Concatinate list >>>>>")
list1 = [100, 200, 300]
list2 = [400, 500, 600]
print(list1+list2)
print("<<<<< Concatinate list")


# Check List is Empty
print("Check List is Empty >>>>>")
mylist = []
if not mylist:
    print("Yes")
if len(mylist) == 0:
    print("Yes Empty")
print("<<<<< Check List is Empty")


# Do nothing in Python
print("Do nothing in Python >>>>>")


def fun():
    pass


if 5 > 3:
    pass
else:
    pass
for x in range(1, 4):
    pass
print("<<<<< Do nothing in Python")
