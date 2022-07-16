# 1.
numbers_list = [2, 7, 3, 99, 43, 12, 56, 17]
numbers_list.sort()
numbers_list.pop(0)
numbers_list.pop(len(numbers_list) - 1)
print(numbers_list)
print()

# 2.
numbers_list = []
max_list_len = 10
while len(numbers_list) < max_list_len:
    new_number = input(f"Enter number ({len(numbers_list)+1}/{max_list_len}): ")
    if new_number.isnumeric():
        numbers_list.append(float(new_number))
    else:
        print(f"{new_number} is not a positive number.")

numbers_list.sort()
numbers_list.pop(0)
numbers_list.pop(len(numbers_list) - 1)
print(numbers_list)
print()

# 3.
first_name_index = 0
last_name_index = 1
avengers = [("Steve", "Rogers"), ("Tony", "Stark"), ("Natasha", "Romanoff"), ("Bruce", "Banner"), ("Clint", "Barton")]
print(avengers[0][last_name_index])
print(avengers[1][last_name_index])
print(avengers[2][last_name_index])
print(avengers[3][last_name_index])
print(avengers[4][last_name_index])
print()

# 4.
for avenger in avengers:
    print(avenger[last_name_index])
print()

# 5.
avengers.append(("Tony", "Banner"))
avengers.append(("Tony", "Rogers"))
avengers.sort()
for avenger in avengers:
    print(f"{avenger[first_name_index]}, {avenger[last_name_index]}")
print()

# 6.
avengers.sort(key=lambda x: x[last_name_index])
for avenger in avengers:
    print(f"{avenger[first_name_index]}, {avenger[last_name_index]}")
