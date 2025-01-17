

# definition of a list

collection = [1, 2 , 3, 4,]
print(collection, type (collection))


for i in collection:
    print(i)


    for i in collection:
        print("i=", i)


## Indexing a value from a list
print("Position 0 =", collection[0])
print("Position 1 =", collection[1])

# Counting values

print ("len=", len(collection))

## definition of a tuple
# collection = (1, 2 , 3, 4)
print(collection, type (collection))


## Indexing (READ) a value from a tuple
print("Position 0 =", collection[0])
print("Position 1 =", collection[1])


## Updating values a list

collection [2] = 3333
print(collection)

# tuple is immutable


# collection = "hello"
print(collection)



## Add at the end. Cannot append to a tuple.

collection.append(678)
print(collection)


#Erase  the last element on the list
collection.pop()
print(collection)

# Insert a specific index.
collection.insert(0, "blue")
print(collection)
collection.pop(0)
print(collection)