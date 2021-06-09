# Write a program called alice_words.py 
# that creates a text file named alice_words.txt containing
# an alphabetical listing of all the words, and the number 
# of times each occurs, in the text version of Alice’s Adventures in Wonderland. 


def get_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

def get_word_count(lines):
    word_count = {}
    for line in lines:
        words = line.split(" ")
        for word in words:
            if word.isalpha():
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    return word_count

def write_file(filename, word_count):
    with open(filename, 'w') as f:
        for key in word_count:
            f.write("{} {}\n".format(key, word_count[key]))


filename = "alice_in_wonderland.txt"
output_file = "words_from_alice_story.txt"
lines = get_lines(filename) # The lines from the story. List of strings
word_count = get_word_count(lines) # {"Alice": 300, "is" : 3000" }
write_file(output_file, word_count) #

