
 
EUR = 4.97
USD = 4.87
HUF = 0.0012
PLN = 1.16

amount = int(input("Pleases insert your amount in RON\n"))
print(amount)

currency = ("Please insert de currency you want to convert to: (ER, USD, HUF, PLN)\n")

print(currency)
if currency =="EUR":
    print("Suma in EUR = ", amount / EUR)
elif currency =="USD":
    print("Suma in EUR = ", amount / USD)
elif currency =="HUF":
    print("Suma in EUR = ", amount / HUF)
elif currency =="PLN":
    print("Suma in EUR = ", amount / PLN)