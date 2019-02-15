def add(num1, num2):
    """ Return the sum """

    answer = num1 + num2
    return answer

def subtract(num1, num2):
    """ Return the difference """

    answer = num1 - num2
    return answer

def multiply(num1, num2):
    """ Return the result of multiplication """

    answer = num1 * num2
    return answer

def divide(num1, num2):
    """ Return the result of division """

    answer = float(num1)/float(num2)
    # only one of these needs to be a float; an int divided by a float is a float
    return answer

def square(num1):
    """ Return the square """

    answer = num1 * num1
    return answer

def cube(num1):
    """ Return the cube """

    answer = num1 ** 3
    return answer

def power(num1, num2):
    """ Return the num1 ^ num2 power """

    answer = num1 ** num2
    return answer

def mod(num1, num2):
    """ Return the modulous or remainder """

    answer = num1 % num2
    return answer
