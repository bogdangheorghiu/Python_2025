



def most_frequent_value(numbers):
    if not numbers:
        return -1
    

frequencies_dict = {
    no : numbers.count(no)  for no in nummbers if no  % 2 == 0
}

max_freq = (frequencies_dict.values())

if max_freq