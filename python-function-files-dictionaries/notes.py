#### WEEK 1

##FILES
#h = open(filename, 'r')
#h = open(filename, 'w')
# contents = h.read()
# lines = h.readlines()
# print(contents)
#for lin in h:
#    print(lin.strip())
#h.close()

# number of characters
#fhandle = open('school_prompt2.txt', 'r')
#contents = fhandle.read()
#num_char = len(contents)
#print(num_char)
#fhandle.close()

# number of lines
#fhandle = open('travel_plans2.txt', 'r')
#lines = fhandle.readlines()
#num_lines = len(lines)
#print(num_lines)
#for line in lines:
#    print(line.strip())
#fhandle.close()

# Create a string called first_forty that is comprised of 
# the first 40 characters of emotion_words2.txt.
#fhandle = open('emotion_words2.txt', 'r')
#content = fhandle.read()
#first_forty  = content[:40]
#fhandle.close()

##Finding a file in 
#open('../myData/data2.txt','r')

## writing to a file
#filename = "squared_numbers.txt"
#outfile = open(filename, "w")
#for number in range(1, 13):
#    square = number * number
#    outfile.write(str(square) + "\n")
#outfile.close()
#infile = open(filename, "r")
#print(infile.read()[:11])
#infile.close()

## Using With - context management
#with open('mydata.txt', 'r') as md:
#    for line in md:
#        print(line)

## CSV FILES
#fileconnection = open("olympics.txt", 'r')
#lines = fileconnection.readlines()
#header = lines[0]
#field_names = header.strip().split(',')
#print(field_names)
#for row in lines[1:]:
#    vals = row.strip().split(',')
#    if vals[5] != "NA":
#        print("{}: {}; {}".format(
#                vals[0],
#                vals[4],
#                vals[5]))

## Writing CSV
#olympians = [("John Aalberg", 31, "Cross Country Skiing"),
#             ("Minna Maarit Aalto", 30, "Sailing"),
#             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
#             ("Wakako Abe", 18, "Cycling")]
#
#outfile = open("reduced_olympics.csv", "w")
# output the header row
#outfile.write('Name,Age,Sport')
#outfile.write('\n')
# output each of the rows:
#for olympian in olympians:
#    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
#    outfile.write(row_string)
#    outfile.write('\n')
#outfile.close()
# another way -if all data is string
#row_string = ','.join(olympian)

#### WEEK 2 - DICTIONARIES
#eng2esp = {}
#eng2esp['one'] = 'uno' #key is one, value is uno
#eng2esp['two'] = 'dos'
#print(eng2esp)

# Dictionary methods
# keys()
#inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
#for akey in inventory.keys():     # the order in which we get the keys is not defined
#    print("Got key", akey, "which maps to value", inventory[akey])
#ks = list(inventory.keys())
#print(ks)
# 'apples' in inventory
# get() - another method to get the value inventory.get('apples'), 
#places = {"Australia":2000, "Greece":2004, "China":2008, "England":2012}
#places["Brazil"] = 2016
#medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}
#events = list()
#for event in medal_events:
#    events.append(event)
#print(events)

# Aliasing and copying
#opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
#alias = opposites
#print(alias is opposites)
#alias['right'] = 'left'
#print(opposites['right'])

# Dictionary Accumation
#f = open('scarlet.txt', 'r')
#txt = f.read()
# now txt is one long string containing all the characters
#x = {} # start with an empty dictionary
#for c in txt:
#    if c not in x:
#        # we have not seen this character before, so initialize a counter for it
#        x[c] = 0
#    #whether we've seen it before or not, increment its counter
#    x[c] = x[c] + 1
#print("t: " + str(x['t']) + " occurrences")
#print("s: " + str(x['s']) + " occurrences")

#f = open('scarlet.txt', 'r')
#txt = f.read()
## now txt is one long string containing all the characters
#letter_counts = {} # start with an empty dictionary
#for c in txt:
#    if c not in letter_counts:
#        # we have not seen this character before, so initialize a counter for it
#        letter_counts[c] = 0
    #whether we've seen it before or not, increment its counter
#    letter_counts[c] = letter_counts[c] + 1
#for c in letter_counts.keys():
#    print(c + ": " + str(letter_counts[c]) + " occurrences")

#travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}
#total = 0
#for places in travel:
#    total += travel[places]

# Create a dictionary called d that keeps track of all the characters in the string placement and notes how many times each 
# character was seen. Then, find the key with the lowest value in this dictionary and assign that key to min_value.
#placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
#d = {}
#min_value = None
#min_value_key = None
#for char in placement:
#    if char not in d:
#        d[char] = 0
#    d[char]+= 1
#print(d)
#for keys in d.keys():
#    if min_value is None:
#        min_value = d[keys]
#        min_value_key = keys
#    else:
#        if d[keys]<min_value:
#            min_value = d[keys]
#            min_value_key = keys
#print( min_value_key )     
#min_value = min_value_key

#product = "iphone and android phones"
#lett_d = {}
#for char in product:
#    if char not in lett_d:
#        lett_d[char] = 0
#    lett_d[char] += 1
#print(lett_d)
#keys=list(lett_d.keys())
#max_value = keys[0]
#for key in lett_d.keys():
#    if lett_d[key]>lett_d[max_value]:
#        max_value = key

#### WEEK 3 - FUNCTIONS
#def name( parameters ):
#    statements
#def square(x):
#    y = x * x
#    return y
#global variable

## TUPLE PACKING
#practice = 'y', 'h', 'z', 'x' # by default it is a tuple
#lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]
#t_check = list()
#for item in lst_tups:
#    t_check.append(item[2])

#t uples-3-1: If you want a function to return two values, contained in variables x and y, which of the following methods will work?
#B. Include the statement "return [x, y]"
#C. Include the statement "return (x, y)"
#D. Include the statement "return x, y"
#def information(name, birth_year, fav_color, hometown):
#    return name, birth_year, fav_color, hometown

## TUPLE UNPACKING
#a = 1
#b = 2
#(a, b) = (b, a)
#print(a, b)

#authors = [('Paul', 'Resnick'), ('Brad', 'Miller'), ('Lauren', 'Murphy')]
#for first_name, last_name in authors:
#    print("first name:", first_name, "last name:", last_name)

#fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
#for n in range(len(fruits)):
#    print(n, fruits[n])

#If you remember, the .items() dictionary method produces a sequence of tuples. Keeping this in mind, we have provided you a dictionary called pokemon. 
# For every key value pair, append the key to the list p_names, and append the value to the list p_number. Do not use the .keys() or .values() methods.
#pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}
#p_names = list()
#p_number = list()
#tup = pokemon.items()
#print(tup)
#for item in tup:
#    (name, number) = item
#    p_number.append(number)
#    p_names.append(name)

#The .items() method produces a sequence of key-value pair tuples. With this in mind, write code to create a list of keys from the dictionary 
#track_medal_counts and assign the list to the variable name track_events. Do NOT use the .keys() method.
#track_medal_counts = {'shot put': 1, 'long jump': 3, '100 meters': 2, '400 meters': 2, '100 meter hurdles': 3, 'triple jump': 3, 'steeplechase': 2, '1500 meters': 1, '5K': 0, '10K': 0, 'marathon': 0, '200 meters': 0, '400 meter hurdles': 0, 'high jump': 1}
#tup = track_medal_counts.items()
#track_events = list()
#for item in tup:
#    (s, n) = item
#    track_events.append(s)

#### WEEK 4 - WHILE
#while {condition}:

#Write a while loop that is initialized at 0 and stops at 15. If the counter is an even number, append the counter to a list called eve_nums.
#i = 0
#eve_nums = list()
#while (15-i)>0:
#    eve_nums.append(i)
#    i+= 2

#Below, we’ve provided a for loop that sums all the elements of list1. Write code that accomplishes the same task, but instead uses a while loop. 
#Assign the accumulator variable to the name accum.
#list1 = [8, 3, 4, 5, 6, 7, 9]
#tot = 0
#for elem in list1:
#    tot = tot + elem
#
#accum = 0
#i = 0
#while i<len(list1):
#    accum += list1[i]
#    i+=1