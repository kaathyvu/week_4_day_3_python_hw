# Codwars Problem #1 - Vowel Count
# https://www.codewars.com/kata/54ff3102c1bad923760001f3
# Old Solution - Quadratic because of the double for loop
# Runtime = 567ms
def get_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in sentence: # linear
        for vowel in vowels: # linear -- nested linear = quadratic
            if letter == vowel: # constant
                count+=1 # constant
    return count

# New Solution - Linear? Because we changed the list to a dict and accessing a dict is constant time
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
    for letter in sentence: # linear time
        if letter in vowels: # constant time
            count+=1 # constant time
    return count




# //////////////////////////////////////////////////////////////////////////////

# Codwars Problem #2 - Disemvowel Trolls
# https://www.codewars.com/kata/52fba66badcd10859f00097e
# Old solution - Quadratic because are iterating through both a string and list in a foor lop?
# Run time = 556ms
def disemvowel(string_):
    new_string = ""
    vowels = ["a", "e", "i", "o", "u"]
    for letter in string_: # linear time
        if letter.lower() not in vowels: # linear time -- nested linear = quadratic
                new_string += letter # constant
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
    for letter in string_: # linear time
        if letter not in vowels: # constant time
            new_string += letter # constant time
    return new_string




# /////////////////////////////////////////////////////////////////////////////

# Codewars Problem #3 - Counting Duplicates
# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
# Old solution - Quadratic time
# Runtime = 718ms
def duplicate_count(text):
    lower_text = text.lower()
    new_list = [letter for letter in lower_text if lower_text.count(letter) > 1]
    # for loop = linear time
    # .count() = linear time but nested within for loop = quadratic time?
    return len(set(new_list)) # linear time

# New solution - Linear Time
# Runtime = 556ms
def duplicate_count(text):
    single_dict = {}
    dupe_dict = {}
    lower_text = text.lower() # linear time
    for letter in lower_text: # linear time
        if letter not in single_dict: # constant time
            single_dict[letter] = 1 # constant time
        else:
            dupe_dict[letter] = single_dict[letter] + 1 # constant time
    return len(dupe_dict) # linear time
        
