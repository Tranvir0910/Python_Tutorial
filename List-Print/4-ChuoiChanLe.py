s = input()

#print(s[::2])
#print(s[1::2])

if s[::2] > s[1::2]:
    print("Even Bias!")
elif s[::2] < s[1::2]:
    print("Odd Bias!")
else:
    print("Balance String!")