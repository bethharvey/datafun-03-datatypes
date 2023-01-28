"""
Beth Harvey
01/27/2023
Data Analysis Fundamentals Project 3

The purpose of this section is to practice using tuples, sets,
dictionaries, and dictionary comprehensions

"""

divider = "=============================================================="

print()
print("Practicing with Tuples")
print()

# Tuples
monday_measurements = (15, 32, 45, 82, 65)
tuesday_measurements = (59, 10, 64, 15, 99)
wednesday_measurements = (45, 11, 32, 60, 82)

print(f"Monday Measurements: {monday_measurements}")
print(f"Tuesday Measurements: {tuesday_measurements}")
print(f"Wednesday Measurements: {wednesday_measurements}")

print()

# Slice tuples
mon_morning = monday_measurements[:3]
tue_afternoon = tuesday_measurements[3:]

print(f"Monday Morning Slice: {mon_morning}")
print(f"Tuesday Afternoon Slice: {tue_afternoon}")

print()

# Concatenate tuples
week_measurements = monday_measurements + tuesday_measurements + wednesday_measurements
print(f"Week's Measurements: {week_measurements}")

print()

# Tuple repetition
two_mon = monday_measurements * 2
print(f"Double Monday Measurements: {two_mon}")

print()

# Membership testing
wed_60 = 60 in wednesday_measurements
mon_27 = 27 in monday_measurements
print(f"60 is in Wednesday's Measurements: {wed_60}")
print(f"27 is in Monday's Measurements: {mon_27}")

print()

# Tuple Indexing
first_wed = wednesday_measurements[0]
last_wed = wednesday_measurements[-1]
print(f"The first measurement on Wednesday was {first_wed}.")
print(f"The last measurement on Wednesday was {last_wed}.")

# Unpacking tuples
first, second, third, fourth, fifth = monday_measurements
print(
    f"""
Monday First: {first}
Monday Second: {second}
Monday Third: {third}
Monday Fourth: {fourth}
Monday Fifth: {fifth}
"""
)

print()
print(divider)
print()

print("Practicing With Sets")

print()

set1 = {"purple", "blue", "green", "green", "red", "cyan", "red"}
set2 = {"pink", "blue", "orange", "red", "pink", "green"}
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

print()

union_set = set1 | set2
intersection_set = set1 & set2
print(f"The union of set 1 and set 2 is: {union_set}")
print(f"The intersection of set 1 and set 2 is: {intersection_set}")

print()
print(divider)
print()

print("Practicing With Dictionaries")

print()

with open("text_woodchuck.txt") as text:
    word_list = text.read().split()

word_counts_dict = {word: word_list.count(word) for word in word_list}
print(f"Word Counts in Woodchuck Text: {word_counts_dict}")

print()
