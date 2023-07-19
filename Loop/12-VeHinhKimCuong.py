'''
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
* * * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
'''

size=int(input())

for i in range(1, size + 1):
  print(" " * (size - i + 1), end = "")
  for j in range(i):
    print("*", end = " ")
  print()

for i in range(size + 1):
  print("*", end = " ")
print()

for i in range(size, 0, -1):
  print(" " * (size - i + 1), end = "")
  for j in range(i, 0, -1):
    print("*", end = " ")
  print()