for row in range(6):

    for col in range(7):

        if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

size = int(input())

for i in range(size):
    for j in range(size - i):
        print(size - j - i, end=" ")
    print()

# 1 2 3 4 5 
# 2 2 3 4 5 
# 3 3 3 4 5 
# 4 4 4 4 5 
# 5 5 5 5 5 

for i in range(1, size + 1):
    for j in range(i - 1):
        print(i, end=" ")
    for j in range(i, size + 1):
        print(j, end=" ")
    print()

'''
1  
2  4  
3  6  9  
4  8  12  16  
5  10  15  20  25  
6  12  18  24  30  36  
7  14  21  28  35  42  49  
8  16  24  32  40  48  56  64 
'''
for i in range(1, 8 + 1):
    for j in range(1, i + 1):
        print(i * j, end="  ")
    print()
