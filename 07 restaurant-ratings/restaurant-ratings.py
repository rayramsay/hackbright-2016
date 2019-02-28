import random

def build_ratings(path):
    """Given a filepath, builds a dictionary of restaurants' ratings."""

    #Creates empty dictionary
    restaurant_ratings = {}

    #Opens file
    fileobj = open(path)

    # Iterates through each line
    # Strips whitespace to right and splits on ':'
    # Assigns key value pairs for dictionary

    for line in fileobj:
        line = line.rstrip().split(':')
        restaurant_ratings[line[0]] = line[1]
    
    # Closes file
    fileobj.close()

    return restaurant_ratings


def update_ratings(path):
    user_name = raw_input("Hi! What's your name? ")

    # Pseudo code:

    # make list of keys
    # based on the length of the list, generate a random number
    # use the random number as an index to select a key
    # use selected key from list to look up rating in dictionary



def sort_ratings(restaurant_ratings):
    """Given a dictionary of restaurants' ratings, prints them alphabetically."""

    # 1. "sorted(restaurant_ratings.items())" makes a list of tuples containing 
    # key-value pairs; the list is sorted alphabetically by key

    # 2. Each item in the list (i.e., a tuple containing a key-value pair) is
    # unpacked into the variables restaurant, rating

    # 3. Each item in the list (the unpacked variables) is iterated over.

    for restaurant, rating in sorted(restaurant_ratings.items()):
        print "{} is rated at {}.".format(restaurant,rating)


    # # Asks user if they want to rate a new restaurant
    # # If yes, prompts user to input a new restaurant and rating
    # # Adds to dictionary
    # # If no, skips if block

    # add_rest = raw_input("Do you want to add a new restaurant? (Y/N) ")
    # if add_rest == "Y" or add_rest == "y":
    #     new_restaurant = raw_input("Please enter restaurant name: ")
    #     new_rating = raw_input("Please enter your rating: ")

    #     restaurant_ratings[new_restaurant] = int(new_rating)

