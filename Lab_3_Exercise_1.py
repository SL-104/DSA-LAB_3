x = input("please input list([1, 2, 3]): ")

# Remove square brackets and split by commas
z = [int(u.strip()) for u in x.strip('[]').split(',')]

# Filter odd numbers
o = [num for num in z if num % 2 != 0]

# Square the odd numbers
y = [a * a for a in o]

print(f"{x} == {y}")
