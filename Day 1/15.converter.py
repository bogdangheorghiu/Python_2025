EUR = 4.97
USD = 4.87
HUF = 0.0012
PLN = 1.16

# amount  = int(input("Pleases instert your amount in RON\n"))

amount = 100
print(amount)
currency = ("Please insert de currency you want to convert to: (ER, USD, HUF, PLN)\n")
currency = currency.upper()

if currency != "EUR" and currency != "USD" and currency != "HUF" and currency != "PLN":
    currency = ("Please insert de currency you want to convert to: (ER, USD, HUF, PLN)\n")
    currency = currency.upper()


if currency =="EUR":
    print("Sum in EUR = ", amount / EUR)
elif currency =="USD":
    print("Sum in EUR = ", amount / USD)
elif currency =="HUF":
    print("Sum in EUR = ", amount / HUF)
elif currency =="PLN":
    print("Sum in EUR = ", amount / PLN)
 
