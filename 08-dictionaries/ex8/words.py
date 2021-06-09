# Write a program that reads a string and returns a 
# table of the letters of the alphabet in alphabetical order 
# which occur in the string together with the number of times 
# each letter occurs. Case should be ignored.
# 
#  A sample output of the program when the user enters the data 
# “ThiS is String with Upper and lower case Letters”, would look this this:

# a  2
# c  1
# d  1
# e  5
# g  1
# h  2
# i  4
# l  2
# n  2
# o  1
# p  2
# r  4
# s  5
# t  5
# u  1
# w  2

{'t' : 1, 'h' : 1, 's' : 1, 'i' : 2}


sentence = input("Enter the sentence ")
count = 0
count_dictionary = {}

for letter in sentence:
    letter = letter.lower()
    if letter.isalpha():
        if letter in count_dictionary:
            count_dictionary[letter] += 1
        else:
            count_dictionary[letter] = 1


        
for key in count_dictionary.keys():
    occurrence = count_dictionary[key]
    print("{} {}".format(key, occurrence))
