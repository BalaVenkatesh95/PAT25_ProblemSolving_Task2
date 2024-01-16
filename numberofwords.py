'''
Write a program to get total number of words present in a
String
'''
#Getting runtime data from user with help of input() method
input_data = input("Enter any Sentence or name")
#Split() - converts String into List
words = input_data.split()
no_of_words = len(words)
print("User provided Sentence is",input_data)
print("Total number of words is",no_of_words)