#Complete the square sum function so that it squares each number passed into it and then sums the results together.
#For example, for [1, 2, 2] it should return 9 because 1^2+2^2+2^2=9.

x = [3,3,3]

def sum_of_squares(x):
    """return sum(i**2 for i in x)"""

    return sum([i**2 for i in x])

    """for i in x:
        square_list += (i**2)
    return square_list"""

print(sum_of_squares(x))