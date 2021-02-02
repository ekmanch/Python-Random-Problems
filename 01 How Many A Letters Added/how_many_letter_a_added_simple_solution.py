##################################
# How Many Letter A's Added
##################################

# Create a program that figures out the number of letter A that is added to words given below.
#
# There should be 2 A's between each letter, including before and after the word.
# If there already is 1 A's between two letters, only 1 A should be added.
# If there already are 2 A's between two letters, no additional A's should be added.
#
# Assume that words are at least 2 letters long.
# Assume that all letters are lower case.
# Assume that no word contains more than 2 consecutive A's.
# Examples:
#
# me = aamaaeaa = 6 A's added
#
# hey = aahaaeaayaa = 8 A's added
#
# man = aamaanaa = 5 A's added
#
# naan = aanaanaa = 4 A's added

word = input("Give the word that should be calculated:\n")

# Create a list from a string
def StrToList(string):
    list1 = []
    list1[:0] = string
    return list1

# Print the string as list - makes it easier to read in cmd prompt
print(StrToList(word))

# Equation to quickly calculate the number of A's to add to the word
total_a_added = 2*(len(word)+1) - 3*word.count('a')

print("Number of A's added: ", total_a_added)