# the following line reads the list from the input, do not modify it, please
old_list = [int(num) for num in input().split()]

binary_list = [int(num > 0) for num in old_list]  # your code here
print(binary_list)
