# 3.
# current_year = 2022
# birth_year = input("In what year were you born (YYYY) ? ")
# age = current_year - int(birth_year)
# target_age = 120
# print(f"You're about {age} years old, in {target_age - age} years you'll be {target_age} years old.")

# 4.
target_age = 120
current_year = 2022
birth_year = input("In what year were you born (YYYY) ? ")

if len(birth_year) != 4 or not birth_year.isdigit():    # user didn't inserted a 4-digits positive number.
    print("Year should be 4-digits positive number (Example: 1989).")
    exit(1)
if int(birth_year) > current_year:                      # user inserted a year in the future
    print("Wow! you were born in the future.")
    exit(1)

age = current_year - int(birth_year)
if age >= target_age:                                   # user is older than the target age
    print(f"Nice! you're very old.")
    exit(1)

years_until_120 = target_age - age
print(f"You're about {age} years old, in {years_until_120} years you'll be {target_age} years old.")
