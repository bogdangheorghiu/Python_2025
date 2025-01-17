


lsit_a = [1, 2, 3, 4, 5, 6, 7, 8]
lsit_b = [4, 5, 6, 7, 8]


result_list = []

for i in range (len(lsit_b)):
    result_list.append(lsit_a(i) + lsit_b(i))


slice_of_lsit_a = lsit_a[len(lsit_b):]
print(slice_of_lsit_a)


result_list += slice_of_lsit_a


result_list.extend(slice_of_lsit_a)
print(result_list) 