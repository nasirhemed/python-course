def print_less_than_10(lst):
    """
    Given a list, print out the numbers that are less than 10
    [10, 20, 5, 100, 4, 9000, 999]
    """
    for number in lst:
        if number < 10:
            print(number)


print_less_than_10([10, 20, 5, 100, 4, 9000, 999])
