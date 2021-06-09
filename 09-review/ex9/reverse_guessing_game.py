print("Think of a number between 0 and 100, I will try to guess")
minimum = 0
maximum = 100
while True:
    guess = int((minimum + maximum) / 2)
    print("I have guessed ", guess)
    user_response = input("Am I right? (YES, HIGH, LOW): ")

    if user_response == "HIGH":
        maximum = guess
    elif user_response == "LOW":
        minimum = guess
    elif user_response == "YES":
        print("I (computer) have won")
        break
    else:
        print("Enter a valid value")
