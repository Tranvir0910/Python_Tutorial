import math

'''
Số hoàn hảo là số nguyên dương mà tổng các ước số của nó lớn gấp 2 lần số đó.
Hoặc theo một cách định nghĩa khác, là số mà có tổng các ước của nó ngoại trừ 
chính nó bằng chính số đó. Chẳng hạn, 6 là số hoàn hảo do nó có các ước là 1, 2, 3 và 6, 
chúng có tổng là 12 và lớn bằng 2 lần của 6.

Hãy viết hàm perfect_number, nhận hai tham số a và b. 
Hàm perfect_number này có chức năng in ra tất cả các số hoàn hảo nằm trong đoạn [a,b] (chứa cả a và b). 
Hãy điền vào các dấu _ _ _ để hoàn thiện hàm này.

Sau khi có hàm này, hãy hoàn thiện đoạn chương trình sử dụng nó bằng cách 
truyền vào 2 số nguyên dương a, b nhập từ bàn phím.
'''

def check_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return n>1

def perfect(a,b):
    for i in range(1,33):
        if check_prime(i):
            tmp = 2**i - 1
            if check_prime(tmp):
                perfect = tmp*(2**(i-1))
                if perfect >= a and perfect <= b:
                    print(perfect, "is a perfect number")

a=int(input())
b=int(input())
perfect(a,b)

email = str(input())
print(email[0].lower())