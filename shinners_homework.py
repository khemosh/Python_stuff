def get_word_count(file_name):
    handler = open(file_name)  # your file
    word_count_dict = {}  # your dictionary
    for line in handler:  # go through each line in the file
        words = line.split()  # split the line into a list of words
        for word in words:  # go through each word in the list
            if word not in word_count_dict:  # if the word is not in the your dictionary..
                word_count_dict[word] = 1  # put it there and give it a count value of 1
            else:   # if it is in the dictionary already..
                word_count_dict[word] += 1  # add one to its count value
    return word_count_dict


def get_word_count_first_line(file_name):
    handler = open(file_name).readline()  # get the first line of the file
    word_count = {}  # your dictionary
    for word in handler.split():  # split the line into words and go through each word
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count


def get_word_count2(file_name):
    handler = open(file_name)
    word_count_dict = {}
    for line in handler:
        words = line.split()
        for word in words:
            """get() is a built in python function for dictionaries that does
            the same thing as lines 7 to 10 above in one line of code.
            It says "if you dont find it give it a value of 0, but either way
            add 1 to its value".
            """
            word_count_dict[word] = word_count_dict.get(word, 0) + 1
    return word_count_dict

# print "Count from first line: \n", get_word_count_first_line('news.txt')
# print "Count of all words in file: \n", get_word_count2('news.txt')

dd = get_word_count2('news.txt')
for key in dd:
    print "key, value: ", key, dd[key]

print "list of tuples: ", dd.items()  # gives back tuples
print "list of keys: ", dd.keys()
print "list of values: ", dd.values()


bigword = 0
bigcount = 0

for word, count in dd.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print "Most common word is: ", bigword, "at", bigcount, "times"

stuff = dict()
print stuff.get('candy', -1)

