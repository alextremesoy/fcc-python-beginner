# 27-Jan-2022
# ----------------------

# -> Just plain text stored into a string

phrase = 'Im string created prev.'
concat_phrase = " \nAppending string!!"

# \n -> new line
# \" -> print simple 

print("Im a string!!\nThis \"is a new\" line.")
print('Im a string with simple columns')
print(phrase)
print(phrase + concat_phrase)

# Converted to lower case
print(phrase.lower())

# Converted to lower case
print(phrase.upper())

# Verifies that all the char are upper case 
# if not -> returns false or true
print(phrase.isupper())

# phrase converted to upper -> verifies the upper
# returns true
print(phrase.upper().isupper())

# len function
print(len(phrase))

# individual characters
# index starting -> 0
print(phrase[0])


# index fun -> where the character is located
print(phrase.index("created"))

# index function -> gives error if the word is not located
# Error ----------------------------------
# Traceback (most recent call last):
#   File "src/working_strings.py", line 43, in <module>
#     print(phrase.index("z"))
# ValueError: substring not found
print(phrase.index("z"))


# Replace function
# param1: word looking for -> param2: word to be replaced
print(phrase.replace("string", "cadena"))