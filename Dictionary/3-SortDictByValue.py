my_dict = {}

# enter the number of items
n = int(input())
for i in range(1, n+1):
    # enter key
    key = input()
    value = int(input())
    my_dict[key] = value


sorted_dict = sorted(my_dict.items(), key = lambda x : x[1])

print(dict(sorted_dict))
