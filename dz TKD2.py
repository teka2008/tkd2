tuple1 = (1, 2, 3, 4, 7)
tuple2 = (4, 6, 7, 3)
tuple3 = (6, 7, 8, 9)

num1 = set(tuple1)
num2 = set(tuple2)
num3 = set(tuple3)
elements_num = num1 & num2 & num3
elements_num = tuple(elements_num)

print(elements_num)





tuple4 = (4, 5, 6, 9)
tuple5 = (8, 3, 6, 4)
tuple6 = (3, 4, 1, 6)

num4 = set(tuple4)
num5 = set(tuple5)
num6 = set(tuple6)
unick_elements1 = num4 - num5 - num6

unick_elements2 = num5 - num4 - num6

unick_elements3 = num6 - num4 - num5

print("первый список", unick_elements1)
print("втрой список", unick_elements2)
print("третий список", unick_elements3)





tuple7 = (9, 5, 1, 3, 6 )
tuple8 = (2, 5, 3, 3, 8, )
tuple9 = (9, 5, 7, 3, 4, )

elements_num2 = [tuple7[i] for i in range(min(len(tuple7), len(tuple8),len(tuple9)))
    if tuple7[i] == tuple8[i] == tuple9[i]]

print(elements_num2)



















