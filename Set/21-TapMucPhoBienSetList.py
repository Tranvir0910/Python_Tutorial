'''
Tập mục phổ biến
Cho tập hợp các mặt hàng mà Alice mua trong một siêu thị 
items={1,2,3,4,5,8,9,12,15,17,21,25,27,31,32,38,40,44,48,50}. 
Mỗi phần tử của tập tương ứng với mã mặt hàng trong cơ sở dữ liệu.

Alice được gọi là khách hàng điển hình, khi mặt hàng mà Alice mua trùng với trên 40%
các mặt hàng của trên 1 nửa số người dùng khác.

Hãy viết chương trình cho phép đọc vào n dòng từ bàn phím. 
Trong đó mỗi dòng ứng với 1 tập hợp các mặt hàng mà một người dùng mua, mỗi mặt hàng 
phân cách nhau bởi dấu khoảng trắng. 

Chương trình sau đó sẽ thực hiện việc so sánh để xem Alice có phải là một khách hàng điển
hình hay không, và trả ra kết quả: YES, nếu là người dùng điển hình và NO nếu không phải.

'''

items={1,2,3,4,5,8,9,12,15,17,21,25,27,31,32,38,40,44,48,50}
n=int(input())

customer = []
for i in range(n):   
  each_customer = set([int(x) for x in input().split()])
  customer.append(each_customer)

count_other = 0
for each_customer in customer:
  if len(items & each_customer) / len(items) > 0.4:
    count_other += 1

if count_other / n > 0.5:
  print("YES")
else:
  print("NO")
