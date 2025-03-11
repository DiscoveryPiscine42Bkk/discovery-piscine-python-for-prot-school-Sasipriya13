original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = [x + 2 if x > 5 else x for x in original_array]
new_array = list(set(new_array))
print("Original array:", original_array)
print("New array (with 2 added to values greater than 5, duplicates removed):", new_array)