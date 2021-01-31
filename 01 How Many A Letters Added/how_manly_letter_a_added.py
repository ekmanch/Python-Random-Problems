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

total_a = 0
word_iter = iter(enumerate(range(0, len(word))))

def StrToList(string):
    list1 = []
    list1[:0] = string
    return list1

word_list = StrToList(word)
print(word_list)
# Manage beginning of word
if word[0] != 'a':
    total_a += 2
elif word[0] == 'a' and word[1] != 'a':
    total_a += 1
else:
    total_a += 0

# Manage end of word
if word[-1] != 'a':
    total_a += 2
elif word[-1] == 'a' and word[-2] != 'a':
    total_a += 1
else:
    total_a += 0

# Manage middle of word
for i, letters in word_iter:
    print("index: ", i)
    # if both current and next letter is non-A, then add 2
    if (word[i] != 'a') and (word[i+1] != 'a'):
        total_a += 2
    # if next letter is A but next-next letter is non-A, then add 1
    elif (word[i+1] == 'a') and (word[i+2] != 'a'):
        total_a += 1
        next(word_iter)
        if (i+3 >= len(word)):
            break
    elif (word[i+1] == 'a') and (word[i+2] == 'a'):
        total_a += 0
        for j in range(2):
            next(word_iter)
        if (i+4 >= len(word)):
            break
    else:
        pass

    if (i+3 >= len(word)):
        break

print("The number of A's added are: ", total_a)
