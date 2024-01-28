# 1. “Python+is+an+awesome+language”.
# Split the given string to get a list and join to get another string “Python is an awesome language”

data = "Python+is+an+awesome+language"
result = data.split("+")
print(result)

result2 = " ".join(result)
print(result2)







# 2. Write a Python program to create a dictionary from a string. Track the count of the
# letters from the string.
# Input = “broadway”
# Output = {“b”: 1, “r”: 1, “o”: 1, “a”: 2, “d”: 1, “w”: 1, “y”: 1}











# 3. Write a Python program to combine two dictionaries by adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# output: {'a': 400, 'b': 400, 'd': 400, 'c': 300}









# 4. Write a program to check whether a string is anagram or not.
# An anagram of a string is another string that contains the same characters,
# only the order of characters can be different. For example, “silent” and “listen” are an anagram of each other.

first_word = input("Enter a word: ")
second_word = input("Enter another word: ")
if sorted(first_word) == sorted(second_word):
    print("It is an anagram.")
else:
    print("It is not an anagram.")







# 5. Check whether a number is palindrome or not. Palindrome numbers are those which remain same even on reversing.
# Examples – 111, 131, 222, 212 etc.
# Input: 121 => The number is palindrome
# Input: 321 => The number is not palindrome

num1 = str(input("Enter a number: "))
if num1 == num1[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")



