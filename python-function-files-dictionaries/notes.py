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