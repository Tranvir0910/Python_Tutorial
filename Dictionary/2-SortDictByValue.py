list = [
       {"name": "Hung", "point": 10},
       {"name": "Giang", "point": 10},
       {"name": "Hieu", "point": 9}
       ]

'''
Hãy sử dụng hàm sorted() và hàm lambda để sắp xếp danh sách sinh viên theo điểm số tăng dần. 
Nếu điểm bằng nhau hãy ưu tiên sinh viên có tên xếp trước trong bảng chữ cái Alphabet.

Đầu ra mong muốn:
[{'name': 'Hieu', 'point': 9}, {'name': 'Giang', 'point': 10}, {'name': 'Hung', 'point': 10}]
'''

sorted_list= sorted( 
    list,
    # Tham số `key` trong hàm` sort () `được sử dụng để chỉ định một hàm 
    # sẽ được sử dụng để xác định thứ tự sắp xếp của các phần tử trong danh sách.
    # Đầu tiên là sắp xếp theo điểm trước ( x['point'] ) , sau đó là sắp xếp name ( x['name'] )
    key = lambda x : ( x["point"], x['name'] ),
    reverse = False
)

print(sorted_list)

