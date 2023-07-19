test_list = [(6, 24, 12), (60, 12, 6), (12, 18, 21)]

k = int(input())

my_list = []

for i in test_list:
  count = 0
  for j in range(3):
    if i[j] % k != 0:
      count += 1
      break
  if count == 0:
    my_list.append(i)

print(my_list)