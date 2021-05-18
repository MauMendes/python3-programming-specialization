#1) seqmut-1-5: Could aliasing cause potential confusion in this problem?
#b = ['q', 'u', 'i']
#z = b
#b[1] = 'i'
#z.remove('i')
#print(z)
#A. yes

#2) seqmut-1-6: Could aliasing cause potential confusion in this problem?
#sent = "Holidays can be a fun time when you have good company!"
#phrase = sent
#phrase = phrase + " Holidays can also be fun on your own!"
#B. no

#3) seqmut-1-1: Which of these is a correct reference diagram following the execution of the following code?
#lst = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
#lst.remove('pluto')
#first_three = lst[:3]
#A. I.

#4) seqmut-1-7: Which of these is a correct reference diagram following the execution of the following code?
#x = ["dogs", "cats", "birds", "reptiles"]
#y = x
#x += ['fish', 'horses']
#y = y + ['sheep']
#D. IV.

#5) seqmut-1-8: Which of these is a correct reference diagram following the execution of the following code? 
# sent = "The mall has excellent sales right now."
#wrds = sent.split()
#wrds[1] = 'store'
#new_sent = " ".join(wrds)
#A. I.
