# Thực hiện tạo các ma trận trong Python

m = 3
n = 4
val = [0] * m
for j in range (m):
    val[j] = [0] * n
print(val)

# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# Truy cập vào các phần tử trong ma trận

val = [[10,101,90,95], [11,102,85,100], [12,103,90,95]]
print(val[2])
print(val[0][1])

# OUT
# [12, 103, 90, 95]
# 101

# Thực hiện một số phép toán với ma trận trong Python bằng cách sử dụng tập hợp kiểu danh sách
# Thực hiện phép cộng ma trận
X = [[12,7,3],
     [4 ,5,6],
     [7 ,8,9]]

Y = [[5,8,1],
     [6,7,3],
     [4,5,9]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

#Duyệt qua từng hàng
for i in range(len(X)):
   #Duyệt qua từng cột
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)

# Thực hiện phép nhân ma trận
#Ma trận 3x3
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

#Ma trận 3x4
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

#Ma trận 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

#Duyệt qua hàng của X
for i in range(len(X)):
   #Duyệt qua cột của Y
   for j in range(len(Y[0])):
       #Duyệt qua các hàng của Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)

#Tìm ma trận chuyển vị
X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

#Duyệt qua các hàng
for i in range(len(X)):
   #Duyệt qua các cột
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)

