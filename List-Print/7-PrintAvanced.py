name1 = 'orange'
price1 = 150
unit1 = 2

name2 = 'grape'
price2 = 130
unit2 = 23

tprice = price1 + price2
discount = 15
fprice = tprice - discount

print("{:<14}{:<25}{:<5}{}".format("S.no", "Product", "Unit", "Price"))
print("{:<14}{:<25}{:<5}{}".format(0, name1, unit1, price1))
print("{:<14}{:<25}{:<5}{}".format(1, name2, unit2, price2))
print("{:<44}{}".format("Discount:", discount))
print("{:<44}{}".format("Total:", fprice))