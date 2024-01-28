# 1. “Python+is+an+awesome+language”.
# Split the given string to get a list and join to get another string “Python is an awesome language”

data = "Python+is+an+awesome+language"
result = data.split("+")
print(result)

result2 = " ".join(result)
print(result2)






# 4. Write a program to check whether a string is anagram or not.
# An anagram of a string is another string that contains the same characters,
# only the order of characters can be different. For example, “silent” and “listen” are an anagram of each other.

first_word = input("Enter a word: ")
second_word = input("Eter another word: ")
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



