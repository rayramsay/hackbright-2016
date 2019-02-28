''' TO DO: check out isalpha() and Further Study
'''

fileobj = open("twain.txt")

#Creates empty list and dictionary
wordlist = []
wordcount = {}
punctuation = ['.',',','?','--','!',"''"]

# Iterates through each line, stripping of whitespace 
# Splits on ' ' and converts to lowercase
for line in fileobj:
    line = line.rstrip().lower()
    words = line.split(" ")

# Iterates through list of each word in each line
# Iterate through our list of punctuation
# Passes each item in the list punctuation to method rstrip
# Adds cleaned word to wordlist
    for word in words:
        for punc in punctuation:
            word = word.rstrip(punc)
        wordlist.append(word)

# iterates through list
# if key is in dict, the value increments by 1
# if key is not in dict, adds key and value of 1 to dict
for word in wordlist:
    wordcount[word] = wordcount.get(word, 0) + 1

# .items makes list of tuples
# list is unpacked to vars key, value
# loops over tuples to print
for key, value in wordcount.items():
    print key, value

fileobj.close()
