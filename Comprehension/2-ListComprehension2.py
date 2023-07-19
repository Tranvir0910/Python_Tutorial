# Hãy viết chương trình sử dụng kỹ thuật list comprehension để in ra màn hình 
# các số nguyên dương nhỏ hơn hoặc bằng n mà có chứa số 3 trong nó. Với n là một số được nhập từ bàn phím.

n = int(input())

three = [i for i in range(1, n+1) if '3' in str(i) ] 

print(three)

# Hãy viết chương trình sử dụng kỹ thuật list comprehension để in ra màn hình 
# các số lượng các dấu cách nằm trong một đoạn văn bản được nhập vào từ bàn phím.

string = input()

spaces = [i for i in string if i == ' ']

print(len(spaces))



sentence = input() 
result = [ i for i in sentence if i not in "aeiou"]
print("".join(result))


# Hãy viết chương trình sử dụng kỹ thuật list comprehension để in ra màn hình 
# các từ có độ dài nhỏ hơn 5 ký tự trong một câu được nhập vào từ bàn phím.

string=input()
result = [x for x in string.split() if len(x) < 5]
for i in result:
  print(i, end = " ")