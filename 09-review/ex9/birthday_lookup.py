# For this exercise, we will keep track of when our friend’s birthdays are, 
# and be able to find that information based on their name. 
# Create a dictionary (in your file) of names and birthdays. 
# When you run your program it should ask the user to enter a name, and return the birthday of that person back to them. 
# The interaction should look something like this:

# >>> Welcome to the birthday dictionary. We know the birthdays of:
# Albert Einstein
# Benjamin Franklin
# Ada Lovelace
# >>> Who's birthday do you want to look up?
# Benjamin Franklin
# >>> Benjamin Franklin's birthday is 01/17/1706.

birthdays = {
    "Nasir": "02/02/1920",
    "Benjamin" : "17/01/1706",
    "Albert" : "13/04/1930"
}

while True:
    name = input("Who's birthday do you want to look up? ")

    if name in birthdays:
        dob = birthdays[name]
        print("{}'s birthday is {}".format(name, dob))
    else:
        dob = input("This name is not in my list. Do you know the person's birthday ? " )
        birthdays[name] = dob
