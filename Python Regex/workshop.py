# Python Regex Lesson

# Regular Expressions (regex) are a powerful tool for string pattern matching and manipulation. In Python, the "re" module provides function to work with regular expressions.

# Basic Syntax: Some common metacharacters & special characters we use in regular expressions:
'''
    ***** META CHARACTERS *****
    ".": Any character except a newline
    "^": Start of a string
    "$": End of a string
    "*": Zero or more occurrences of the previous character
    "+": One or more occurrences of the previous character
    "?": Zero or one occurrence of the previous character
    "[]": Set of characters
    "|": Either/or condition
    "{}: Specify the exact number of occurences of the preceding character
    "\": Escape special characters (or use a "r" string)
    
    ***** SPECIAL CHARACTERS *****
    "\d": Matches any digit (0-9)
    "\D": Matches non-digit
    "\w": Matches any word characters (a-z, A-Z, 0-9, _)
    "\W: Matches any non-word character
    "\s": Matches any whitespace character (spaces, tabs, newlines)
    "\S": Matches any non-whitespace character
'''
import re
# 1. Common Functions & Methods with Regex


# re.search(): Searches for a pattern and returns the first occurrence
#NOTE: Always use "r" or "raw" strings when creating a pattern with regex
result = re.search(r"\d+", "The 1st house number is 1234")
print(type(int(result.group())))

# re.findall(): Returns all matches in the string
results = re.findall(r"\d+", "The 1st house number is 1234")
print(results)

# re.sub(): Replaces a pattern with a new string\
sentence1 = "the goat will always be kobe bryant!"
text = re.sub(r"Kobe Bryant".lower(), "michael jordan", sentence1)
print(text)
print(f"Sentence 1: {sentence1}")

# re.split(): Splits the string by the occurrences of the pattern
sentence = "the        goat   will   always     be    kobe   bryant!"
parts = re.split(r'\s+',sentence)
print(parts)


# 2. Grouping and Capturing: You can use parentheses (), to group parts of a regex pattern and capture a match 123-45-6789
ssn_pattern = r"(\d{3})-(\d{2})-(\d{4})"
result = re.search(ssn_pattern, "My SSN is 123-45-6789.")
print(result.group())
print(result.group(1))
print(result.group(2))
print(result.group(3))


# Create a pattern for a full name with naming/capturing groups ("My name is Allan Ahmed")
full_name_pattern = r"(?P<first_name>[A-Z][a-z]+)\s(?P<last_name>[A-Z][A-Za-z]+)"
result = re.search(full_name_pattern, "My name is Allan McDonald.")
print(result.group())
print(result.group('first_name'))
print(result.group('last_name'))



# 3. In-Class exercise
# Matching a Valid Email Address
email_string = 'my email for coding temple is: allan_12@ct.com'
email_pattern = r'[a-zA-Z0-9_.]+@[a-zA-Z0-9]+.[a-zA-z0-9]+'
result = re.search(email_pattern, email_string)
print(result)