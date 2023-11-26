myArr = [1,7,2,512,3]
left_pointer = myArr[0]

for i in range(1, len(myArr)):
    right_pointer = myArr[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer

print(left_pointer)