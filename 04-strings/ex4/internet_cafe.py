# Here is a program that calculates how much the user should pay 
# for the hours he spent in the internet cafe

# If the user is a member then a discount is applied
# We want to make sure that the user types in the right choices
# If we ask hours spent, he should give us a number and nothing else
# If we ask if he is a member, he should answer yes or no and nothing else
hours_spent = input("How many hours did you spend? ")
hours_spent = int(hours_spent)

is_member = input("Are you a member? ")

if is_member == "yes":
    total = 2 * hours_spent
    tax_rate = total * 1.1

else:
    total = 5 * hours_spent
    tax_rate = total * 1.2

print("You total is ", tax_rate)

