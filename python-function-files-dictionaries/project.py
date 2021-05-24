#1) We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet. 
# We have also words that express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.
# Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. You will create a csv file, 
# which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), 
# Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, you upload the csv file 
# to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.

# To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes 
# characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)
#punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
#def strip_punctuation(str):
#    print(str)
#    for char in punctuation_chars:
#        print(char)
#        str = str.replace(char, "")
#    return str

#2) Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, 
# a string which represents one or more sentences, and calculates how many words in the string are considered positive words. 
# Use the list, positive_words to determine what words will count as positive. The function should return a positive integer - 
# how many occurrences there are of positive words in the text. Note that all of the words in positive_words are lower cased, 
# so youll need to convert all the words in the input string to lower case as well.
# punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
#def strip_punctuation(str):
#    for char in punctuation_chars:
#       str = str.replace(char, "")
#    return str
# list of positive words to use
#positive_words = []
#with open("positive_words.txt") as pos_f:
#    for lin in pos_f:
#        if lin[0] != ';' and lin[0] != '\n':
#            positive_words.append(lin.strip())
#print(positive_words)
#
#def get_pos(str):
#    counter = 0
#    tmp = strip_punctuation(str)
#    #print(tmp)
#    words = tmp.split()
#    print(words)
#    for word in words:
#        if word.lower() in positive_words:
#            counter += 1
#    return counter

#3) Next, copy in your strip_punctuation function and define a function called get_neg which takes one parameter, a string 
# which represents one or more sentences, and calculates how many words in the string are considered negative words. Use the list, 
# negative_words to determine what words will count as negative. The function should return a positive integer - how many occurrences
#  there are of negative words in the text. Note that all of the words in negative_words are lower cased, so you'll need to convert 
# all the words in the input string to lower case as well.
#punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
#def strip_punctuation(str):
#    for char in punctuation_chars:
#        str = str.replace(char, "")
#    return str
#
#negative_words = []
#with open("negative_words.txt") as pos_f:
#    for lin in pos_f:
#       if lin[0] != ';' and lin[0] != '\n':
#            negative_words.append(lin.strip())
#           
#def get_neg (str):
#    counter = 0
#    tmp = strip_punctuation(str)
#    words = tmp.split()
#    for word in words:
#        if word.lower() in negative_words:
#            counter += 1
#    return counter

#4) Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv which has the fake generated 
# twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet). Your task is to 
# build a sentiment classifier, which will detect how positive or negative each tweet is. Copy the code from the code windows above, 
# and put that in the top of this code window. Now, you will write code to create a csv file called resulting_data.csv, which contains 
# the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score 
# (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. 
# The file should have those headers in that order. Remember that there is another component to this project. You will upload the csv 
# file to Excel or Google Sheets and produce a graph of the Net Score vs Number of Retweets. Check Coursera for that portion of the 
# assignment, if you're accessing this textbook from Coursera.
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(str):
    for char in punctuation_chars:
        str = str.replace(char, "")
    return str

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
def get_pos(str):
    counter = 0
    tmp = strip_punctuation(str)
    words = tmp.split()
    for word in words:
        if word.lower() in positive_words:
            counter += 1
    return counter

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())  
def get_neg (str):
    counter = 0
    tmp = strip_punctuation(str)
    words = tmp.split()
    for word in words:
        if word.lower() in negative_words:
            counter += 1
    return counter

info = list()
with open("project_twitter_data.csv") as pos_f:
    for lin in pos_f:
        tweet = lin.strip().split(',')
        if tweet[0] == 'tweet_text':
            continue # skip first line
        clean_line = strip_punctuation(tweet[0])
        pos_score = get_pos(clean_line)
        neg_score = get_neg(clean_line)
        info.append( (int(tweet[1]), int(tweet[2]), pos_score, neg_score, pos_score+neg_score  ) )
#print(info)    

outfile = open("resulting_data.csv", "w")
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')
for item in info:
    row_string = '{},{},{},{},{}'.format(item[0], item[1], item[2], item[3], item[4])
    #print(row_string)
    outfile.write(row_string)
    outfile.write('\n')  
outfile.close()
        