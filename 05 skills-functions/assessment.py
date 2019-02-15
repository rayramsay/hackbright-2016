# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5%


def total_cost(price, state, tax=.05):
    """Given price, state abbreviation, and sales tax (default 5%), returns
    total cost of item. CA tax is always 7%.

    For example::

        >>> total_cost(10,'MA')
        10.5
        >>> total_cost(10,'CA')
        10.7
        >>> total_cost(10,'PA',.07)
        10.7
    """

    if state == 'CA':
        tax = .07
    total_cost = price + price * tax
    return total_cost

# This took ~5 minutes

#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.


def is_berry(fruit):
    """Given a fruit as a string, returns a boolean re: fruit being in set of
    berries.

    For example::
        >>> is_berry('apple')
        False
        >>> is_berry('cherry')
        True
        >>> is_berry('blueberry')
        False
    """

    berries = set(['strawberry', 'cherry', 'blackberry'])
    return fruit in berries


def shipping_cost(fruit):
    """Given a fruit as a string, returns shipping cost.

    For example::
        >>> shipping_cost('apple')
        5
        >>> shipping_cost('cherry')
        0
        >>> shipping_cost('blueberry')
        5
    """

    if is_berry(fruit):
        return 0
    else:
        return 5

# Part Two: 1a and 1b took 15 minutes


def is_hometown(town):
    """ Takes town name as a string and returns a boolean re: it matching my
        hometown.

    For example::
        >>> is_hometown('Oakland')
        False
        >>> is_hometown('Pittsburgh')
        True
    """

    return town is 'Pittsburgh'


def full_name(first, last):
    """Takes first and last names as separate strings, returns as one string.

    For example::
        >>> full_name('Rachel', 'Ramsay')
        'Rachel Ramsay'
    """

    full = first + ' ' + last
    return full


def hometown_greeting(town, first, last):
    """Takes home town, first, and last names as separate strings, returns a
    greeting.

    For example::
        >>> hometown_greeting('Shelby','Norah','Smith')
        'Hi, Norah Smith, where are you from?'
        >>> hometown_greeting('Pittsburgh','Kara','Ramsay')
        "Hi, Kara Ramsay, we're from the same place!"
    """

    name = full_name(first, last)
    if is_hometown(town):
        greeting = "Hi, {}, we're from the same place!".format(name)
    else:
        greeting = "Hi, {}, where are you from?".format(name)
    return greeting

# Part Two: 2a, b, and c took 20 mintues

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addone with y = 5. Call again with y = 20. 

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.


def increment(x=1):
    """
    For example::
        >>> addfive = increment(5)
        >>> addfive(5)
        10
        >>> subfive = increment(-5)
        >>> subfive(5)
        0
    """
    def add(y):
        return x + y
    return add

# If I understand this correctly, ``increment()`` returns a function that adds
# ``x`` to whatever I pass to that function (i.e., ``y``).

addfive = increment(5)

# Is there an error in the instructions above; is ``addone`` meant to be
# ``addfive``?

addfive(5)

addfive(20)

# This took about 15 minutes to wrap my head around.


def append_number(number, lst):
    """Takes a number and a list of numbers; appends number to list; returns
    list.

    For example::
        >>> append_number(5, [1, 2, 3, 4])
        [1, 2, 3, 4, 5]
        >>> append_number(5, [])
        [5]
    """

    lst.append(number)
    return lst

    # Because lists can contain heterogenous types, does it matter if ``number``
    # is not actually a number? E.g., if I pass ``cat`` and end up with [1, 2,
    # 3, 4, 'cat'], it doesn't throw an error, but should I check number's type
    # regardless? Like this:

    # if type(number) == float or type(number) == int:

#####################################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GO RACHEL!"
    print
