# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'
key = list(test_dict.keys())[0]
k_max, v_max = key, test_dict.get(key)
k_min, v_min = key, test_dict.get(key)

for key, value in test_dict.items():
    if v_max < value:
        k_max, v_max = key, value
    if v_min > value:
        k_min, v_min = key, value

print(f"min: {k_min}")
print(f"max: {k_max}")
