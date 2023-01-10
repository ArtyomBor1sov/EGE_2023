from fnmatch import fnmatch

for num in range(0, 10 ** 9, 3123):
    if fnmatch(str(num), '12*63?5?'):
        print(num)