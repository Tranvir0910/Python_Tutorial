"""
\n	Xuống dòng mới.
\\	Dấu gạch chéo.
\'	Dấu nháy đơn.
\"	Dấu nháy kép.
\b	Xóa ký tự.
\f	Sang trang mới.
\r	Giá trị trả về.
\t	Khoảng trắng tab.
\v	Khoảng trắng tab dọc.
\ooo	Ký tự với giá trị hệ cơ số bát phân (cơ số 8).
\xHH	Ký tự với giá trị hệ cơ số thập lục phân (cơ số 16). 
"""
print("D:\\folder1\\folder2")               # D:\folder1\folder2
print("Javascript\rProgramming")            # Programming
print("Python\vProgramming")                # Python
                                            # Programming

print("Python\vProgramming") 


string = "{:{fill}{align}{width}}"
print(string.format('python', fill='*', align='^', width=9))
num = "{:{align}{width}.{precision}f}"
print(num.format(392.989, align='<', width=8, precision=1))

print("--------------------")
print("{:20}Python".format("Python"))
print("{:>20}".format("Python"))
print("{:^20}".format("Python"))
'''

'd'

Số nguyên có dấu

print('%d' %(-100))

>>> -100

'i'

Số nguyên có dấu

print('%i' %(-100))

>>> -100

'o'

Giá trị dạng bát phân (octan)

print('%o' %(20))

>>> 24

'u'

Giống với ký tự 'd'.

print('%u' %(-100))

>>> -100

'x'

Giá trị hệ 16 có dấu (viết thường)

print("%5x"% (47))

>>> 2f

'X'

Giá trị hệ 16 có dấu (viết hoa)

print("%5.4X"% (47))

>>> 002F

'e'

Định dạng số mũ cho số thực dấu chấm động (viết thường)

print("%9.2e"% (312.087))

>>> 3.12e+02

'E'

Định dạng số mũ cho số thực dấu chấm động (viết hoa)

print("%9.2E"% (312.087))

>>> 3.12E+02

'f'

Định dạng số thực dạng thập phân

print('%f' %(100.21))

>>> 100.210000

'F'

Định dạng số thực dạng thập phân

print('%F' %(100.21))

>>> 100.210000

'g'

Định dạng số thực dấu chấm động. Sử dụng định dạng số mũ viết thường nếu số mũ nhỏ hơn -4 hoặc nhỏ hơn độ chính xác

print('%g' %(3e9))

>>> 3e+09

'G'

Định dạng số thực dấu chấm động. Sử dụng định dạng số mũ viết hoa nếu số mũ nhỏ hơn -4 hoặc nhỏ hơn độ chính xác

print('%G' %(3e9))

>>> 3E+09

'c'

Một ký tự (nhận vào một giá trị số nguyên hoặc một ký tự)

print('%c' %('a'))

>>> a

'r'

Chuỗi ký tự (chuyển đổi từ bất kỳ đối tượng Python nào bằng hàm repr()

print('%r' %('Python'))

>>> 'Python'

's'

Chuỗi ký tự (chuyển đổi từ bất kỳ đối tượng Python nào bằng hàm str()

print('%s' %('Python'))

>>> Python

'a'

Chuỗi ký tự (chuyển đổi từ bất kỳ đối tượng Python nào bằng hàm ascii()

print('%a' %('Python cơ bản'))

>>> 'Python c\u01a1 b\u1ea3n'

'%'

Không có tham số nào được chuyển đổi, trả về kết quả là ký tự dấu phần trăm '%'

print('%')

>>> %

'''