# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")
print(f"Modified String 1: {user_string.lower()}") # lowercase string
print(f"Modified String 2: {user_string.upper()}") # capitalises string
print(f"Modified String 3: {user_string.strip()}") # removes whitespace 
print(f"Modified String 4: {user_string.replace('a', '@')}") # replaces all letters of a with @
print(f"Modified String 5: {user_string.capitalize()}") # makes first letter of string capitalised
print(f"Modified String 6: {user_string[::-1]}") # reverses the string
print(f"Modified String 7: {user_string.title()}") # formats string as a title (captilises first letter of each word)
print(f"Modified String 8: {len(user_string)}") # returns the legnth of the string
print(f"Modified String 9: {user_string.find('a')}") # returns the index of the position of the letter a (first instance)
print(f"Modified String 10: {user_string.count('a')}") # returns the number of times "a" appears in the string
print(f"Modified String 11: {user_string.startswith('Hello')}") # checks whether the string starts with "hello"
print(f"Modified String 12: {user_string.endswith('!')}") # checks whethere the string ends with "!"
print(f"Modified String 13: {user_string.isalnum()}") # checks whether all characters in the string are alphaneumeric
print(f"Modified String 14: {user_string.isalpha()}") # checks whether all characters in the string are in the alphabet
print(f"Modified String 15: {user_string.isdigit()}") # checks whether all characters in the string are numbers



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!