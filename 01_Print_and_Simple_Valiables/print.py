# 1.
print(" ________________")
print("|                |")
print("|                |")
print("|                |")
print("|                |")
print("|                |")
print(" ________________")
print("\n")

# 2.
print(" ________________")
print("|    ______      |")
print("|   / @  @ \     |")
print("|   |   ^   |    |")
print("|   |   ==  |    |")
print("|    \_____/     |")
print(" ________________")
print("\n")

# 3.
print('*')
print('**')
print('***')
print('****')
print('*****')
print('******')
print('*******')
print('********')
print('*********')
print('**********')
print("\n")

# 4.
rectangle_height = 8
for i in range(rectangle_height):
    if i == 0 or i == rectangle_height-1:
        print(" ________________")
    else:
        print("|                |")

# 5.
triangle_height = 10
for i in range(triangle_height):
    print('*' * (i+1))

# 6.
my_string = "Hello World!"
print(my_string.upper())

# 7.
print(my_string.index("W"))

# 8.
print(len(my_string))

# 9.
print(my_string.replace("Hello", "Hey"))
