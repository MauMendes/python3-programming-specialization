#The function mySum is supposed to return the sum of a list of numbers (and 0 if that list is empty), but it has one or more errors in it.
#Use this space to write test cases to determine what errors there are. You will be using this information to answer the next set of multiple choice questions.
assert mySum(0)
mlist=[1]
assert mySum(mlist) == 1
mlist=[1, 2]
assert mySum(mlist) == 3

#answer: A. an empty list, C. a list with more than one item

#test-4-2: Are there any other cases, that we can determine based on the current structure of the function, that also fail for the mySum function?
#B. No


#The class Student is supposed to accept two arguments in its constructor:
#        A name string
#        An optional integer representing the number of years the student has been at Michigan (default:1)
#Every student has three instance variables:
#        self.name (set to the name provided)
#        self.years_UM (set to the number of years the student has been at Michigan)
#        self.knowledge (initialized to 0)
#There are three methods:
#        .study() should increase self.knowledge by 1 and return None
#        .getKnowledge() should return the value of self.knowledge
#        .year_at_umich() should return the value of self.years_UM
#There are one or more errors in the class. Use this space to write test cases to determine what errors there are. You will be using this information to answer the next set of multiple choice questions.
#a1 = Student("Mauricio")
#print("Name: {}".format(a1.name))
#print("years_UM: {}".format(a1.years_UM))
#print("knowledge: {}".format(a1.knowledge))
#
#print(a1.study())
#print("knowledge: {}".format(a1.knowledge))
#print("getKnowledge: {}".format(a1.getKnowledge()))git 
#print("year_at_umich: {}".format(a1.year_at_umich()))

#ANSWERS: C. the attributes/instance variables are not correctly assigned in the constructor D. the method study does not increase self.knowledge

#test-4-4: Are there any other cases, that we can determine based on the current structure of the class, that also fail for the Student class?
#A. Yes
# Correct! There is an issue with the getKnowledge method because it returns None when self.knowledge is 0, even though it returns the correct value when self.knowledge is non-zero.