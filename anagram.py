'''
Take a String and return true if it is anagram of another string
else return false
'''
input_string_01 = input("Enter String 01:")
input_string_02 = input("Enter String 02:")

#Using lower() for case uniformity
string_01 = input_string_01.lower()
string_02 = input_string_02.lower()

#sorted() - sorts provided string alphabetically which helps for our comparison
#Operator(==) returns value in boolean
comparison_result = sorted(string_01)==sorted(string_02)
print("Provided String is anagram of another string: ",comparison_result)

#Sample Anagram -- Silent,Listen
