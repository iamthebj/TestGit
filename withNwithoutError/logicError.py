

alphabets ="abcdefghijklmnopqrstuvwxyz"
def calculation(text,alphabets):
    sample_list = []
    total_counter = 0
    for element in text:
        if element != " ":
            total_counter += 1
    total = total_counter

    for alphabet in alphabets:
        alphabet_counter = 0
        for element in text:
            if element == alphabet:
                alphabet_counter += 1
        tna = alphabet_counter
        percentage_counter = float((tna/total)*100)
        sample_list.append(percentage_counter)
    return sample_list

text = "sahib will be a very successful programmer one day."

x = calculation(text,alphabets)
print x

"""I was trying to make a python programmer which calculates the percentage of each character in a text. But When i print the list it displays an empty list
"""