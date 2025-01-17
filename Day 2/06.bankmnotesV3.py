


initial_amount = int(input("Insert your value"))
amount = initial_amount

bankotes = [100, 50, 20, 10, 5, 1]

for note in bankotes:
    value = amount // note
    print("Banknotes of", note, ":", value)
    print(f"Baknotes of {note} : {value}")
    amount = amount % note

print("Inintial amount", initial_amount)