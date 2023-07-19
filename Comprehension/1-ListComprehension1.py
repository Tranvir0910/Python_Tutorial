# Hãy viết chương trình sử dụng kỹ thuật list comprehension để in ra màn hình 
# các số nguyên dương nhỏ hơn hoặc bằng n và chia hết cho 7. Với n là một số được nhập từ bàn phím.

n = int(input())

div7 = [ i for i in range(1, n+1) if i % 7 == 0 ] 

print(div7)