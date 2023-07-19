def reverse(my_list, start, end):
    copy_list = my_list[start : end + 1 : 1]
    copy_list.reverse()
    for i in range(len(copy_list)):
        my_list[start + i] = copy_list[i]
    return my_list

my_list = list(map(int, input().split(", ")))
start = int(input())
end = int(input())
print(reverse(my_list, start, end))
