
"""
Define a function postalValidate(S) which first checks if S represents
a postal code (Canadian) which is valid:
    first, delete all spaces;
    the remainder must be of the form L#L#L# where L are letters
    (in either lower or upper case) and # are numbers.
    
If S is not a valid postal code, return the boolean False.
If S is valid, return a version of the same postal code in the nice format
L#L#L# where each L is capital.
Use the following methods to do this exercise:
str.replace(), str.isalpha(), str.isdigit(), and str.upper()
"""

def postalValidate(S):
    """ Return False if S is not a valid postal code.
    If S is valid, return it in the format L#L#L# where each L is capital.
    
    >>> postalValidate(' d3 L3 T3')
    >>> 'D3L3T3'
    """

    remove_spaces = S.replace(" ", "")
    if len(remove_spaces) != 6:
        return False

    for i in range(6):
        if i % 2 == 1:
            if not remove_spaces[i].isnumeric():
                return False
        else:
            if not remove_spaces[i].isalpha():
                return False

    return True
            
    
    # your code here


# Use these arguments to test your function.


postalCodes = ["H0H H0H", "d3 L3 T3", "V4L1d", "postal", "m 6 P 4 s 9   "]

for postalCode in postalCodes:
    print("The postal code {} is {}".format(postalCode, postalValidate(postalCode)))

