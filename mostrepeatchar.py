'''
Program to find most repeated character in String
'''
input_data = input("Enter a String:")
# Converting string to lowercase for uniformity
original_string = input_data.lower()

#dictionary to store value of each character
char_frequency = {}

# Count the frequency of each character
for char in original_string:

#get() - fetches current value of character from dictionary and adds value by (+1)
#char_frequency[char] - makes reuqired update to dictionary
    char_frequency[char] = char_frequency.get(char, 0) + 1

#max() - finds maximum value present in iterable(Here dictionary is iterable)
#based on get() comparison is done based on value and key with maximum value is assigned to max_char
    max_char = max(char_frequency, key=char_frequency.get)
print("Most repeated Character in String:",max_char)

