

initial_amount = int(input("Insert your value"))


amount = initial_amount

tens = amount //10
print("Banknote of ten", tens)

amount = amount %10
fives = amount // 5

print("Banknote of five", fives)
