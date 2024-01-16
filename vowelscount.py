'''
Program to find total number of vowels present and count of each individual vowels
in given String
'''
name = "Guvi Geeks Network Private Limited"

#used built-in count() method
a_count = name.count("a")
print("Total number of 'a' in String: ",a_count)
e_count = name.count("e")
print("Total number of 'e' in String: ",e_count)
i_count = name.count("i")
print("Total number of 'i' in String: ",i_count)
o_count = name.count("o")
print("Total number of 'o' in String: ",o_count)
u_count = name.count("u")
print("Total number of 'u' in String: ",u_count)
total_count = a_count+e_count+i_count+o_count+u_count
print("Total number of vowels present in String: ",total_count)