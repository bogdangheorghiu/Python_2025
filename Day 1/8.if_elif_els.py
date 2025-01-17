

age = 105

if age < 18:
    print("minor")
else:
    if age < 30:
        print ("young adult")
    else:
        if age < 50:
            print("mature")
        else:
            if age < 80:
                print("wise")
            else:
                print("legacy")



# Version 2
# mutual condition

if age < 18:
    print("minor")
elif age  < 30:
    print ("young adult")
elif age < 50:
    print("mature")
elif age < 80:
    print("wise")
else:
    print("legacy")

    
if age >= 18 and age < 38:
    print("minor")

if age  < 30:
    print ("young adult")

if age < 50:
    print("mature")

if age < 80:
    print("wise")

else:
    print("legacy")
