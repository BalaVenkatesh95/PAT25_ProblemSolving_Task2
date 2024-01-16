'''
Write a program that takes a string and returns a new string with all vowels removed
'''
#using built-in method input() to get string value during runtime
input_data = input("Enter name:")
print("String with vowels:",input_data)
vowels = "AEIOUaeiou"
result_string = ""
#Using for loop to iterate each character present in String
#Using Memebership Operators(in,not in) to validate presence of characters
for char in input_data[:]:
    if char not in vowels:
         result_string = result_string +char
print("String without Vowels:",result_string)