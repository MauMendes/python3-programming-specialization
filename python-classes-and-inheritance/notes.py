#### WEEK 1 - Classes and Instances
# Class inheritance
# Test Cases
#class Point:
#    """ Point class for representing and manipulating x,y coordinates"""
#    def __init__(self):
#        self.x = 0
#        self.y = 0
#
#    def getX(self):
#        return self.x
#pt1 = Point()
#pt2 = Point()
#pt1.x = 5
#pt1.y = 10
#print(pt1.getX())

#class Point:
#    """ Point class for representing and manipulating x,y coordinates"""
#    def __init__(self, initX=0, initY=0):
#        self.x = initX
#        self.y = initY
#    def getX(self):
#        return self.x
#    def getY(self):
#        return self.y
#
#pt = Point( 7, 6)
#print(pt.getX())
#print(pt.getY())

#class NumberSet:
#    def __init__(self, InitNum1, InitNum2):
#        self.num1 = InitNum1
#       self.num2 = InitNum2
 #       
#t = NumberSet(6,10)


#class Point:
#    """ Point class for representing and manipulating x,y coordinates. """
#
#    def __init__(self, initX, initY):
#
#        self.x = initX
#        self.y = initY
#
#    def getX(self):
#        return self.x
#
#    def getY(self):
#        return self.y
#
#    def distanceFromOrigin(self):
#        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

#p = Point(7,6)
#print(p.distanceFromOrigin())

#class Animal:
#    def __init__(self, init_arms, init_legs):
#        self.arms = init_arms
#        self.legs = init_legs
#    def limbs(self):
#        return self.arms + self.legs
#
#spider = Animal(4,4)
#pidlimbs = spider.limbs()

#cityNames =['Detroit', 'Ann Arbour', 'Pittsburgh', 'Mars', 'New York']
#populations = [680250,117070,304391,1683,8406000]
#states = ['MI','MI','PA','PA','NY']
#city_tuples = zip(cityNames, populations, states)
#print(str(city_tuples))

#class City:
#    def __init__(self, n, p, s):
#        self.name = n
#        self.population = p
#        self.state = s
#    def __str__(self):
#        return '{},{},(pop:{})'.format(self.name, self.state, self.population)

#cities =[]
#for city_tup in city_tuples:
#    n,p,s = city_tup;
#    city = City(n,p,s)
#    cities.append(city)
#    print(city)
#print(cities)

#all of that using list comprehesions
#cities = [City(n,p,s) for (n,p,s) in city_tuples]
#cities = [City(*t) for t in city_tuples]
#print(cities)