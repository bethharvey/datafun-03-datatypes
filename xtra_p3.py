"""
Beth Harvey
01/27/2023
Data Analysis Fundamentals Project 3

Optional bonus. See course site for details.

>>> len(longwordset1)
415

>>> len(longwordset2)
197

>>> len(longwords)
13
"""

import doctest

# read from Hamlet text and get a list of words

with open("text_hamlet.txt", "r") as f1:
    text = f1.read()
    wordlist1 = text.split()

# read from Julius Caesar and get a list of words

with open("text_juliuscaesar.txt", "r") as f2:
    text = f2.read()
    wordlist2 = text.split()

# Remove duplicates by creating a sorted set for each word list
wordset1 = set(wordlist1)
wordset2 = set(wordlist2)


# initialize a variable maxlen = 10
maxlen = 10

# use a list comprension to get a list of words longer than 10
longwordset1 = set([word for word in wordset1 if len(word) > 10])
longwordset2 = set([word for word in wordset2 if len(word) > 10])

# find the intersection of the two sets
longwords = longwordset1 & longwordset2

# print the length of the sets and the list
print()
print(f'Number of words in Hamlet with over 10 letters: {len(longwordset1)}')
print(f'Number of words in Julius Caesar with over 10 letters: {len(longwordset2)}')
print(f'Number of 10+ letter words in Hamlet and Julius Caesar: {len(longwords)}')
print()
print(f"Unique 10+ letter words in Hamlet and Julius Caesar: {sorted(longwords)}")
print()

# check your work
print("TESTING...if nothing prints before the testing is done, you passed!")
doctest.testmod()
print("TESTING DONE")
