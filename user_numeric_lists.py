"""
Beth Harvey
01/26/2023
Data Analytics Fundamentals Project 3

The purpose of this ssection is to practice working with lists.

"""

# import some modules first - how many can you make use of?

import math
import statistics as stats

""" 
list1 is a (hypothetical) list of number of birds spotted in one hour
for several weeks

"""

list1 = [31, 52, 20, 42, 28, 40, 35, 22, 23, 47, 33, 29, 25, 54, 38, 43, 29, 35, 27, 39]

""" 
listx represents 10 integer times

"""

listx = list(range(10))

"""
listy represents the temperature of the water in the bird bath
during the listed times

"""

listy = [32, 34, 35, 36, 37, 37, 38, 38, 39, 39]

divider = "=============================================================="

print("List 1. List Statistics")

""" 
Calculate mean, median, mode, standard deviation, and variance
for list1

"""

print()
mean = stats.mean(list1)
median = stats.median(list1)
mode = stats.mode(list1)
st_dev = stats.stdev(list1)
variance = stats.variance(list1)

print(f"Bird Count Mean: {round(mean, 2)}")
print(f"Bird Count Median: {round(median, 2)}")
print(f"Bird Count Mode: {round(mode, 2)}")
print(f"Bird Count Standard Deviation: {round(st_dev, 2)}")
print(f"Bird Count Variance: {round(variance, 2)}")

print()
print(divider)
print()

print("Lists 2. Lists - Correlation and Prediction")

"""
Calculate the correlation, slope, and intercept of the best fit
line for listx and listy
Predict the y value for future time x = 15

"""

print()
correlationxy = stats.correlation(listx, listy)
slope, intercept = stats.linear_regression(listx, listy)
xfuture = 15
yfuture = slope * xfuture + intercept

print(f"Correlation between time and water temperature: {round(correlationxy, 2)}")
print(f"Slope of best-fit line for listx and listy: {round(slope, 2)}")
print(f"Intercept of best-fit line for listx and listy: {round(intercept, 2)}")
print(f"Predicted water temperature at future time 15: {round(yfuture, 2)}")

print()
print(divider)
print()

print("List 3. Lists = Using Python Built-in Functions")

"""
Calculate the min, max, length, sum, and average of list1
Create a set from list1, and sort list1 in both forward 
and reverse directions

"""
print()

count_min = min(list1)
count_max = max(list1)
count_length = len(list1)
count_sum = sum(list1)
count_avg = count_sum / count_length
count_set = set(list1)
count_sorted_for = sorted(list1)
count_sorted_back = sorted(list1, reverse=True)

print(f"Minimum Bird Count: {count_min}")
print(f"Maximum Bird Count: {count_max}")
print(f"Number of Counting Days: {count_length}")
print(f"Total Number of Birds Counted: {count_sum}")
print(f"Average Number of Birds per Count: {round(count_avg, 2)}")
print(f"Bird Count Set: {count_set}")
print(f"Bird Counts Sorted (Ascending): {count_sorted_for}")
print(f"Bird Counts Sorted (Descending): {count_sorted_back}")

print()
print(divider)
print()

print("List 4. List Methods")

"""
Create new short list and use list methods append, extend, 
insert, remove, count, sort (forward and reverse), copy, and
pop (first and last)

"""

print()

# Create short list lst
lst = [57, 29, 501, 5, 10, 64, 18]
print(f"Lst: {lst}")

# Append a new value
lst.append(2)
print(f"Appended lst: {lst}")

# Extend list with new list
lst.extend([39, 52, 99])
print(f"Extended lst: {lst}")

# Insert a value at index 5
lst.insert(11, 5)
print(f"lst With Insert: {lst}")

# Remove value 5 from list
lst.remove(5)
print(f"List Minus Value 5: {lst}")

# Count how many times 2 appears in lst
print(f"The value 2 appears {lst.count(2)} times in lst.")

# Sort lst
lst.sort()
print(f"lst Sorted in Ascending Order: {lst}")

# Sort lst reversed
lst.sort(reverse=True)
print(f"lst Sorted in Descending Order: {lst}")

# Create a copy of lst
lst_copy = lst.copy()
print(f"Copy of lst: {lst_copy}")

# Pop first item from list
first = lst.pop(0)
print(f"lst First Value Popped: {first}")

# Pop last item from list
last = lst.pop(-1)
print(f"lst Last Value Popped: {last}")

print()
print(divider)
print()

print("List 5. List Transformations - Using filter() and map()")

"""
Use filter and map functions on list1

"""

print()

list1_evens = list(filter(lambda x: x % 2 == 0, list1))
list1_cubes = list(map(lambda x: x**3, list1))
list1_vol = list(map(lambda x: x * x * x, list1))

print(f"The even temperatures from the list are: {list1_evens}")
print()
print(f"The cube of each temperature in the list are: {list1_cubes}")
print()
print(f"The volumes of cubes with sides equal to the values in list1 are {list1_vol}")

print()
print(divider)
print()

print("Lists 6. List Transformations - Using List Comprehension")

"""
Practice using list comprehensions

"""

print()

# Get only odd values from list1
getx = [x for x in list1 if x % 2 != 0]
print(f"The odd values from list1 are {getx}")

print()

# Triple each value in list1
getx3 = [x * 3 for x in list1]
print(f"Each value in list1 tripled is {getx3}")

print()

# Convert each temperature into Celsius
getx_cel = [round((x - 32) / (5 / 9), 2) for x in list1]
print(f"The list1 temperatures converted to Celsius are {getx_cel}")

print()
