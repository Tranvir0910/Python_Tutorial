
def sublists(my_list):
	# khai báo list tạm để lưu các list con
	tmp_lists = [[]]
	
	for i in range(len(my_list) + 1):
		for j in range(i):
			tmp_lists.append(my_list[j: i])
	tmp_lists.sort(key=len)
	return tmp_lists


l1 = [1, 4, 6]

for i in range(1, len(sublists(l1))):
	print(sublists(l1)[i], end = ', ')
