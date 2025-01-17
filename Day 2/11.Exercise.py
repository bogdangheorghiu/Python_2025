a = [3, 7, 1, 9, 2, 4, 5, 12]
odd = []
even = []


a_list = [3, 7, 1, 9, 2, 4, 5, 12]



for i in a_list:
    print(i)
    if i % 2 == 0 :
       even.append(i)
    else:
        odd.append(i)

print(odd)
print(even)