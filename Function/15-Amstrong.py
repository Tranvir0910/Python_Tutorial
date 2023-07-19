# Cach tu lam
while True:
    n = int(input())

    # Dem so chu so cua n
    cnt = 0
    # Cac bien thay the de tinh
    tmp1 = n
    tmp2 = n
    while tmp1>0:
        cnt += 1;
        tmp1//=10
        
    sum = 0
    k = cnt
    while n>0:
        sum += (n%10)**k
        n//=10
    if sum == tmp2:
        print(tmp2,"is an Armstrong number")
        break

# Cach TEK4 lam
while (True):
  n = int(input())
  num = n
  s = 0
  k = len(str(n))
  while (num != 0):
    res = num % 10
    print(res)
    s = s + res ** k
    num = num // 10
  
  if s == n:
    print(n, "is an Armstrong number")
    break 

