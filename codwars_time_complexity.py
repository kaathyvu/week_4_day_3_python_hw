# Codwars Problem #1 - Vowel Count
# https://www.codewars.com/kata/54ff3102c1bad923760001f3
# Old Solution - Quadratic because of the double for loop
# Runtime = 567ms
def get_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in sentence:
        for vowel in vowels:
            if letter == vowel:
                count+=1
    return count

# New Solution - Linear? Because we changed the list to a dict and accessing a dict is linear time
# Runtime = 478ms
def get_count(sentence):
    vowels = {
        "a":"",
        "e":"",
        "i":"",
        "o":"",
        "u":""
    }
    count = 0
    for letter in sentence:
        if letter in vowels:
            count+=1
    return count


# //////////////////////////////////////////////////////////////////////////////

# Codwars Problem #2 - Disemvowel Trolls
# https://www.codewars.com/kata/52fba66badcd10859f00097e
# Old solution - Quadratic because are iterating through both a string and list in a foor lop?
# Run time = 556ms
def disemvowel(string_):
    new_string = ""
    vowels = ["a", "e", "i", "o", "u"]
    for letter in string_:
        if letter.lower() not in vowels:
                new_string += letter
    return new_string

# New solution - Linear? Again because we changed the list to a dict and accessing a dict is linear time
# Runtime = 502ms
def disemvowel(string_):
    vowels = {
        "a":"",
        "e":"",
        "i":"",
        "o":"",
        "u":"",
        "A":"",
        "E":"",
        "I":"",
        "O":"",
        "U":"",
    }
    new_string = ""
    for letter in string_:
        if letter not in vowels:
            new_string += letter
    return new_string


# /////////////////////////////////////////////////////////////////////////////

# Codewars Problem #3 - Array.diff
# https://www.codewars.com/kata/523f5d21c841566fde000009
# Old solution - Quadratic? Because we have a while loop nested in a for loop?
# Runtime = 683ms
def array_diff(a, b):
    for num in b:
        while num in a:
            a.remove(num)
    return a

# New solution - Quadratic still I think - I couldn't figure out a way to make this
#     linear but I did try to decrease the time by changing the list to a set to rule out any duplicates. Not sure if it did much though
# Runtime = 511ms
def array_diff(a, b):
    c = [num for num in a if num not in set(b)]
    return c