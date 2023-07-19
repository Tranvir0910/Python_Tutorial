num = int(input("Number of rows: "))


#`Đối với i trong phạm vi (num):` là một vòng lặp lặp đi lặp lại `num` lần.Trên mỗi lần lặp, biến vòng lặp `I`
# nhận giá trị từ 0 đến `num-1`.Vòng lặp này được sử dụng để kiểm soát số lượng hàng trong mẫu in bởi mã.
for i in range(num):
    # Dòng mã này là in không gian trước các ngôi sao trong mỗi hàng của mẫu.Số lượng
    # khoảng trắng được in được xác định bởi giá trị của `num - i - 1`, trong đó` i` là số hàng hiện tại.
    # Khi `i` tăng, số lượng không gian được in giảm, dẫn đến một mẫu giống như kim tự tháp.
    for j in range(num - i - 1):
        print(end = " ")
    for j in range(i+1):
        print("*", end=" ")
    print()
