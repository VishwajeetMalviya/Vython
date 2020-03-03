from array import *

arr = array('i',[11,22,30,33,40,44,50,55,60,66,77,88,99])
end=12
i=0

print("Enter element to be searched : ")
data = int(input())
if arr.__contains__(data):
    print("Item found on " + str(arr.index(data)) + " location.")
else:
    print("Item not found .")
