# Nửa trái và nửa phải của một chuỗi là các chuỗi con có kích thước bằng một 
# nửa chuỗi mẹ (lấy phần nguyên) và tương ứng nằm ở bên trái, phải của chuỗi mẹ.

# Nếu độ dài một chuỗi là chẵn thì ta dễ dàng chia thành nửa trái và nửa phải,
# nhưng độ dài chuỗi là lẻ thì ta chia thành hai nửa sao cho phần tử ở chính giữa 
# không được chọn (tức là không thuộc nửa trái cũng chẳng thuộc nửa phải). Điểm ở giữa 
# không thuộc nửa nào này được gọi là điểm trụ của chuỗi. 

# Ta gọi

# Một chuỗi được gọi là đối xứng (Symmetrical string) nếu cả hai nửa của chuỗi đều giống nhau.
# Một chuỗi được gọi là chuỗi lệch trái (Left Bias) nếu nửa trái của chuỗi lớn hơn nửa phải
# Một chuỗi được gọi là chuỗi lệch phải (Right Bias) nếu nửa phải của chuỗi lớn hơn nửa trái.

string = input()

left = len(string) // 2

if len(string) % 2 == 1:
  print("The central point of the string is " + string[left] + ".")
  right = left + 1
else:
  print("There is no central point.")
  right = left
  
if string[:left] == string[right:]:
  print("Symmertical String!")
elif string[:left] > string[right:]:
  print("Left Bias!")
else:
  print("Right Bias!")
