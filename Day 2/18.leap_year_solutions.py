

start_date = 2001
stop_date = 2005

leap_year = []

print("*" * 5 + "Allowed years" + "*" * 5)
for year in range(start_date, stop_date +1):
    print(year)

print("*" * 5 + "*" * 5)


print("*" * 5 + "Allowed years" + "*" * 5)
for year in range(start_date, stop_date +1):
    if year % 4 == 0 or (year %4  == 0 and year % 100 != 0):
         print(year)
         leap_year.append(year)

print("*" * 5 + "*" * 5)