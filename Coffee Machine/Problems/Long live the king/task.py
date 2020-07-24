column_postion = int(input())
row_postion = int(input())
if column_postion in [1, 8]:
    if row_postion in [1, 8]:
        print(3)
    else:
        print(5)
elif row_postion in [1, 8]:
    print(5)
else:
    print(8)

