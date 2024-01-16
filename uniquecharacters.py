'''
Take a String and return number of unique characters in it
'''
input_data = input("Enter a String:")
#Set is built-in function which doesn't allow duplicates
unique_chars = set(input_data)
#As Set removed all duplicates, length clearly depicts unique characters in it
total_unique_chars  = len(unique_chars)
print("Provided String is",input_data)
print("Number of unique Characters:",total_unique_chars)