'''
Take a String and return True if it is a Palindrome and False if not
'''
#Getting runtime data from user with help of input() method
input_name = input("Enter your word:")
print("Provided String is",input_name)
reversed_name = ""
for char in input_name:
    reversed_name = char+reversed_name
print("reversed string is",reversed_name)
#Using Boolean operator(==), as result need to be in form of true/false
palindrome_result = input_name==reversed_name
print("Provided String is a Palindrome(True/False) - ",palindrome_result)

#Example Palindrome to enter:kayak,peep,civic,radar,mom





