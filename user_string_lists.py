"""
Beth Harvey
01/27/2023
Data Analysis Fundamentals Project 3

The purpose of this section is to practice using lists of strings.

"""

# imports first
import random

# lists of bird species and characteristics

species = ["Cardinal", "Bluejay", "Bluebird", "Flicker", "Goldfinch"]

favorite_food = ["sunflower seeds", "peanuts", "mealworms", "suet", "thistle seeds"]

main_color = ["red", "blue", "blue", "gray", "yellow"]

size = ["medium", "large", "medium", "large", "small"]

main_egg_color = ["green", "blue", "blue", "white", "white"]

divider = "=============================================================="

print()
print("String Lists 1. Using Python Built-in Functions")

"""
Use len, set, and zip functions

"""

print()

# Use len function
print(f"The length of the bird species list is {len(species)}.")

# Use set function
print(f"The unique values in the main color list are {set(main_color)}.")

# Combine multiple lists with zip function
bird_tuples = zip(species, main_color, favorite_food)
print(f"Tuples of species, color, and favorite food: {list(bird_tuples)}")

print()
print(divider)
print()

print("String Lists 2. Random Choice")

print()

print(f"Random choice from favorite foods list: {random.choice(favorite_food)}")

randomized_sentence = (
    f"The {random.choice(species)} is a {random.choice(size)} bird,"
    f"and its eggs are {random.choice(main_egg_color)}...maybe!"
)

print()

print(randomized_sentence)

print()
print(divider)
print()

print("String Lists 3. Get Unique Words")
"""
Use open(), read(), split(), and len() to create a list of unique
words from a provided text

"""

print()

with open("text_hamlet.txt", "r") as file:
    text = file.read()
    list_words = text.split()
    unique_words = set(list_words)

unique_words_sorted = sorted(unique_words)
unique_word_count = len(unique_words_sorted)
print(f"Hamlet contains {unique_word_count} unique words!")

print()
