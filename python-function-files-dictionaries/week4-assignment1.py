#1) Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. 
# The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).
def sublist(input_lst):
    out_lst = list()
    number = 0
    i = 0
    print(input_lst)
    print(len(input_lst))
    length = len(input_lst)
    
    while i<length:
        number = input_lst[i]
        i+=1
        if number==5: break
        else : out_lst.append(number)
    print(out_lst)
    return out_lst

#2) Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element of the
#  list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.def check_nums(input_lst):
def check_nums(input_lst):
    out_lst = list()
    number = 0
    i = 0
    print(input_lst)
    print(len(input_lst))
    length = len(input_lst)
    while i<length:
        number = input_lst[i]
        i+=1
        if number==7: break
        else : out_lst.append(number)
    print(out_lst)
    return out_lst

#3) Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list.
# The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).
def sublist(in_lst):
    out_list = list()
    str = ""
    i = 0
    while str!="STOP":
        str = in_lst[i]
        i+=1
        if str=="STOP": break
        else: out_list.append(str)
    return out_list

#4) Write a function called stop_at_z that iterates through a list of strings. Using a while loop, append each string to a new list until the string that 
# appears is “z”. The function should return the new list.
def stop_at_z(in_lst):
    out_list = list()
    str = ""
    i = 0
    while str!="z":
        str = in_lst[i]
        i+=1
        if str=="z": break
        else: out_list.append(str)
    return out_list

#5) Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does the same thing, but using a while loop instead of a for loop. 
# Assign the accumulated total in the while loop code to the variable sum2. Once complete, sum2 should equal sum1.
lst = [65, 78, 21, 33]
lenght = len(lst)
i = 0
sum2 = 0
while i<lenght:
    sum2 += lst[i]
    i+=1

#6) Challenge: Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’. 
# What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are 
# returned. If “bye” is the 5th element, the first 4 are returned.) If you want to make this even more of a challenge, do this without slicing
def beginning(in_list):
    length = len(in_list)
    out_lst  = list()
    i = 0
    str = ""
    while i<length:
        str = in_list[i]
        i+=1
        if str=="bye" or i>10:
            break
        out_lst.append(str)
    return out_lst
