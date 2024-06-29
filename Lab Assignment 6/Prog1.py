# Write a program that takes a sentence as input and counts the 
# occurrences of each word. Use a dictionary to store the word counts 
# and then print out each word along with its count.
def word_count(str):
    counts=dict()
    words=str.split()
    for word in words:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1
    return counts
print(word_count('the quick brown fox jumps over the lazy dog.'))

