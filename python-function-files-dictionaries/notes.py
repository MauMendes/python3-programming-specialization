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

#Random walking turtles
#import random
#import turtle
#def isInScreen(w, t):
#    if random.random() > 0.1:
#        return True
#    else:
#        return False
#t = turtle.Turtle()
#wn = turtle.Screen()
#t.shape('turtle')
#while isInScreen(wn, t):
#    coin = random.randrange(0, 2)
#    if coin == 0:              # heads
#        t.left(90)
#    else:                      # tails
#        t.right(90)
#    t.forward(50)
#wn.exitonclick()

#import random
#import turtle
#def isInScreen(w,t):
#    leftBound = - w.window_width() / 2
#    rightBound = w.window_width() / 2
#    topBound = w.window_height() / 2
#    bottomBound = -w.window_height() / 2
#    turtleX = t.xcor()
#    turtleY = t.ycor()
#    stillIn = True
#    if turtleX > rightBound or turtleX < leftBound:
#        stillIn = False
#    if turtleY > topBound or turtleY < bottomBound:
#        stillIn = False
#    return stillIn
#t = turtle.Turtle()
#wn = turtle.Screen()
#t.shape('turtle')
#while isInScreen(wn,t):
#    coin = random.randrange(0, 2)
#    if coin == 0:
#        t.left(90)
#    else:
#        t.right(90)
#    t.forward(50)
#wn.exitonclick()

## Advanced functions
#number default value, being optional
#def str_mult(str, number=3):
#    return str*number

## keyword parameters
#initial = 7
#def f(x, y = 3, z = initial):
#    print("x, y, z are:", x, y, z)
#f(2, z = 10)
#print("The scores {nm} got were: {s1},{s2},{s3}.".format(nm=name,s1=scores[0],s2=scores[1],s3=scores[2]))

#def multiply(str,mult_int=10):
#    return str*mult_int

## LAMBDA EXPRESSION
#def fname(arguments):
#    return expression
#fname = lambda arguments: expression
#print(lambda x: x-2)
#print(type(lambda x: x-2))
#print((lambda x: x-2)(6))
#(lambda x: -x)

## PROGRAMING STYLE
#use 4 spaces for indentation
#imports should go at the top of the file
#separate function definitions with two blank lines
#keep function definitions together
#keep top level statements, including function calls, together at the bottom of the program

#### WEEK 5 - SORTING BASICS

## method sorted
## or list.sort()
## optional parameters
#L2 = ["Cherry", "Apple", "Blueberry"]
#print(sorted(L2, reverse=True))
#lst = [3, 5, 1, 6, 7, 2, 9, -2, 5]
#lst_sorted = sorted(lst, reverse=True)

## optional key parameters
#L1 = [1, 7, 4, -2, 3]
#def absolute(x):
#    if x >= 0:
#        return x
#    else:
#        return -x
#
#L2 = sorted(L1, key=absolute)
#print(L2)
##or in reverse order
#print(sorted(L1, reverse=True, key=absolute))

# You will be sorting the following list by each element’s second letter, a to z. Create a function to use when sorting, 
# called second_let. It will take a string as input and return the second letter of that string. Then sort the list, create a 
# variable called sorted_by_second_let and assign the sorted list to it. Do not use lambda.
#ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
#def second_let(str):
#    return str[1]
#sorted_by_second_let  = sorted(ex_lst, key=second_let)
#print(sorted_by_second_let)

# Below, we have provided a list of strings called nums. Write a function called last_char that takes a string as input, and returns 
# only its last character. Use this function to sort the list nums by the last digit of each number, from highest to lowest, and save 
# this as a new list called nums_sorted.
#nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']
#def last_char(str):
#    return str[-1]
#nums_sorted = sorted(nums, reverse=True, key=last_char)
#print(nums_sorted)

#Once again, sort the list nums based on the last digit of each number from highest to lowest. However, now you should do so by 
# writing a lambda function. Save the new list as nums_sorted_lambda.
#nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']
#nums_sorted_lambda = sorted(nums, reverse=True, key=lambda ch:ch[-1])

#### ADVANCED SORTED W/ dictionaries
#Sort the following dictionary based on the keys so that they are sorted a to z. Assign the resulting value to the variable sorted_keys
#dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}
#sorted_keys = sorted(dictionary.keys())

#Sort the following dictionary’s keys based on the value from highest to lowest. Assign the resulting value to the variable sorted_values.
#dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}
#sorted_values = list()
#
# now loop through the sorted keys
#for k in sorted(dictionary, key=lambda k: dictionary[k], reverse=True):
#    print("{} Have {} Items".format(k, dictionary[k]))
#    sorted_values.append(k)