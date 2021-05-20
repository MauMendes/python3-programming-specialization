#1) The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. 
# Find the total number of characters in the file and save to the variable num.
#handle = open('travel_plans.txt','r')
#content = handle.read()
#num = len(content)
#print(num)
#handle.close()


#2) We have provided a file called emotion_words.txt that contains lines of words that describe emotions. 
# Find the total number of words in the file and assign this value to the variable num_words.
#num_words = 0
#with open('emotion_words.txt', 'r') as md:
#    for line in md:
#        clean_line = line.strip()
#        print(clean_line)
#        words = clean_line.split()
#        print(words)
#        num_words += len(words)

#3) Assign to the variable num_lines the number of lines in the file school_prompt.txt.
#num_lines  = 0
#with open('school_prompt.txt', 'r') as md:
#   for line in md:
#       num_lines += 1

#4) Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars
#beginning_chars = ""
#with open('school_prompt.txt', 'r') as md:
#    content = md.read()
#    beginning_chars = content[:30]

#5) Using the file school_prompt.txt, assign the third word of every line to a list called three.
#three = list()
#with open('school_prompt.txt', 'r') as md:
#    for line in md.readlines():
#        line_list = line.split()
#        three.append(line_list[2])
#print(three)

#6) Create a list called emotions that contains the first word of every line in emotion_words.txt.
#emotions = list()
#with open('emotion_words.txt', 'r') as md:
#    for line in md.readlines():
#        line_list = line.split()
#        emotions.append(line_list[0])
#print(emotions)

#7) Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars. 
# with open('travel_plans.txt', 'r') as md:
#    content = md.read()
#    first_chars = content[:33]

#8) Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
#p_words = list()
#with open('school_prompt.txt', 'r') as md:
#    for line in md.readlines():
#        line_list = line.split()
#        for word in line_list:
#            if('p' in word):
#                p_words.append(word)
#print(p_words)