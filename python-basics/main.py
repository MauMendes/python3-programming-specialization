#### WEEK 1

### Values and Data Types
#a = 100
#b = 3.14
#c = 'Hello World'
#print(type(a))
#print(type(b))
#print(type(c))

### Operators and Operands
#print(100+200) #Addition
#print(100-200) #Subtraction
#print(2*2) #Multiplication
#print(10/3) #Division
#print(10//3) #Remeinder
#print(10%3) #Modular
#print(4**2) #Exponentiation

## Precedence
# 1. Parentheses
# 2. Multiplication & Division
# 3. Addition and Subtraction

### Functions Calls
#input (arguments)
#output (return value)

### Type Conversion Functions
#print(3.14, int(3.14))
#print(3.9999, int(3.9999))
#print("2345", int("2345"))
#print(17, int(17))
#print(int("23"))
#rint(float("123.45"))
#print(type(float("123.45")))
#print(str(123.45))
#print(type(str(123.45)))

### Variables - Useful for storing values of expressions and use later on
#message = "What's up, Doc?"
#n = 17 
#pi = 3.141559
#print(message)
#print(n)
#print(pi)
 
### Python Keywords
# and, as, assert, break, class, continue, def, del, elif, else, except, exec, finally, for, from, global
# if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
# True, False, None 

### Statements and Expressions
# Assignment Statement (pi=3.14)
# Assignment Statement of an expression ( value = 3.14 + 1)
# Python sequencially evaluate expressions, creating sub expressions

### Updating Variables
#x +=3 same as x = x + 3 
#y -=1 same as y = y - 1

### Turtle Graphics
#import turtle
#wn = turtle.Screen()
#alex = turtle.Turtle()
#alex.forward(150)
#alex.left(90)
#alex.forward(75)

### Repetition with a For Loop
#for _ in range(3):
#    print(_)

### Importing Modules
#import random
#from random import randrange, random
#prob = random()
#print(prob)

#diceThrow = randrange(1,7)
#print(diceThrow)

# Syntax, Runtime, and Semantic Errors
# print("hello"
# Syntax Error
# Runtime - 3/0 - Trying to divide by zero, ilegal operation
# Semantic Error - Software work, but not as intented 

#Write code to draw a regular pentagon (a five-sided figure with all sides the same length).
#import turtle
#wn = turtle.Screen()
#jazz = turtle.Turtle()
#for i in range(5):
#   jazz.forward(100) #Assuming the side of a pentagon is 100 units
#   jazz.left(72) #Turning the turtle by 72 degree

# Write a program that uses the turtle module to draw something. It doesnt have to be complicated, 
# but draw something different than we have done in the past. (Hint: if you are drawing something complicated, 
# it could get tedious to watch it draw over and over. Try setting .speed(10) for the turtle to draw fast, or .speed(0) 
# for it to draw super fast with no animation.)
#import turtle
#wn = turtle.Screen()
#jazz = turtle.Turtle()
#for i in range(5):
#   jazz.forward(100) #Assuming the side of a pentagon is 100 units
#   jazz.left(72) #Turning the turtle by 72 degree
#   jazz.speed(i)


#### WEEK 2
### Strings
### List
### Turple
#s = "Hello World"
#mylist = [1, "mauricio", 34, "Male"]
#tuples are immutable
#tuples = (1, "mauricio", 34, "Male")

#print(type(s))  #print type
#print(s[0])     #print first letter, or fist item of the string
#print(s[len(s)-1])  #print last character of the string
#print(s[6:]) #usage of the slice operator. print from the 6th character until end 

#print(tuples[2:]) #Note starts to print from item 2
#print(tuples[:2]) #Note not printing the item 2
#print(tuples[:-1]) #Note it is not going to print the last element

#print(type(mylist))
#print(type(tuples))

#create tuples empty or one item
#tuples = ()
#tuples = (100,)
#print(type(tuples))
#print(len(tuples))

### Concatenation
#print([1,2]+[3,4])
#fruit = ['apple', 'banana', 'kiwi']
#print(fruit + [1, 2, 3])
#print(fruit*2)  #prints twice the list, duplicating 

### Count method
#a = "I have had an apple on my desk before!"
#print(a.count("e"))
#print(a.count("ha"))

### Index method
#print(a.index("desk"))

### Split method
#song = "We are the champions"
#print(song.split())
#print(song.split("the"))

### Join method
#words = ["red", "blue", "green"]
#glue = ";"
#print(glue.join(words))
#print(" ".join(words))
#print("".join(words))

### Iteration
#for name in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
#    print("Hi", name, "Please come to my party on Saturday!")

### The Accumulator
#nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#accum = 0
#for w in nums:
#    accum = accum + w
#print(accum)

# Create a list, [0, 1, 2, .... 52]
#numbers = list(range(0,53))

#### WEEK 3
### Boolean Expressions
#print(True)
#print(type(True))
#print(type(False))
#print(5 == 5)
#print(5 == 6)
#x != y               # x is not equal to y
#x > y                # x is greater than y
#x < y                # x is less than y
#x >= y               # x is greater than or equal to y
#x <= y               # x is less than or equal to y

### Logical Operators ( and, not, in)
#x = 5
#print(x>0 and x<10)
#n = 25
#print(n%2 == 0 or n%3 == 0)
#print( not False )

### Precedence of Operators
#Level       Category        Operators
#7(high)     exponent        **
#6           multiplication  *,/,//,%
#5           addition        +,-
#4           relational      ==,!=,<=,>=,>,<
#3           logical         not
#2           logical         and
#1(low)      logical         or

### Conditional Execution
#if BOOLEAN EXPRESSION:
#    STATEMENTS_1        # executed if condition evaluates to True
#else:
#    STATEMENTS_2        # executed if condition evaluates to False

### Conditional Execution
#if x < y:
#    print("x is less than y")
#elif x > y:
#    print("x is greater than y")
#else:
#   print("x and y must be equal")

#str1 = "Today you are you! That is truer than true! There is no one alive who is you-er than you!"
#if "false" in str1:
#    output = "False. You aren’t you?"
#elif "true" in str1:
#    output = "True! You are you!"
#else:
#   output = "Neither true nor false!"

#percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
#resps = list()
#for percent in percent_rain:
#    if percent>90:
#        resps.append("Bring an umbrella.")
#    elif percent>80:
#        resps.append("Good for the flowers?")
#    elif percent>50:
#        resps.append("Watch out for clouds!")
#    else:
#        resps.append("Nice day!")
#print(resps)

#words = ["water", "chair", "pen", "basket", "hi", "car"]
#num_words = 0
#for word in words:
#    if(len(word)>3):
#        num_words += 1

#Challenge For each word in words, add ‘d’ to the end of the word if the word ends in “e” to make it past tense. Otherwise, add ‘ed’ to make it past tense. 
# Save these past tense words to a list called past_tense.
#words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
#past_tense = list()
#for word in words:
#    if word[-1]=='e':
#        past_tense.append(word+"d")
#    else:
#        past_tense.append(word+"ed")
#print(past_tense)