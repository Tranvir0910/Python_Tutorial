s=input()
n=int(input())

print(s[:-n-1:-1])
print(s[:n:1])

if s[:n:1] == s[:-n-1:-1]:
    print("Chuỗi vừa nhập là chuỗi giả Palindrome với",n)
else:
    print("Chuỗi vừa nhập KHONG là chuỗi giả Palindrome với",n)