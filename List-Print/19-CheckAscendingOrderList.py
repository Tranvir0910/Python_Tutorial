# Write a code that takes a list as a parameter and prints True if the list is 
# sorted in ascending order and False  otherwise. 
# Please do not sort the list, just check it.
# For example,
# Input: 1, 2, 3, 4
# Output: True

def ascendingCheck(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return 0
    return 1

t1 = tuple(map(int, input().split(', ')))
if ascendingCheck(t1):
    print("True")
else:
    print("False")
    
