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

#import math
#class Point:
#    """ Point class for representing and manipulating x,y coordinates. """
#    def __init__(self, initX, initY):
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
#
#    def distance(self, point2):
#        xdiff = point2.getX()-self.getX()
#        ydiff = point2.getY()-self.getY()
#
#        dist = math.sqrt(xdiff**2 + ydiff**2)
#        return dist
##p = Point(4,3)
#q = Point(0,0)
#print(p.distance(q))

#import math
#class Point:
#    """ Point class for representing and manipulating x,y coordinates. """
#
#    def __init__(self, initX, initY):
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
#
#    def distance(self, point2):
#        xdiff = point2.getX()-self.getX()
#        ydiff = point2.getY()-self.getY()
#        dist = math.sqrt(xdiff**2 + ydiff**2)
#        return dist
#
#    def __str__(self):
#        return "x = {}, y = {}".format(self.x, self.y)
#p = Point(7,6)
#print(p)

#class Cereal:
#    def __init__(self, name, brand, fiber):
#       self.name = name
#        self.brand = brand
#        self.fiber = fiber
#    def __str__(self):
#        return "{} cereal is produced by {} and has {} grams of fiber in every serving!".format(self.name, self.brand, self.fiber)
#c1 = Cereal("Corn Flakes","Kellogg's",2)
#c2 = Cereal("Honey Nut Cheerios","General Mills",3)

#class Point:
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
#
#    def __str__(self):
#        return "x = {}, y = {}".format(self.x, self.y)
#
#    def halfway(self, target):
#        mx = (self.x + target.x)/2
#        my = (self.y + target.y)/2
#        return Point(mx, my)
#
#p = Point(3,4)
#q = Point(5,12)
#mid = p.halfway(q)
# note that you would have exactly the same result if you instead wrote
# mid = q.halfway(p)
# because they are both Point objects, and the middle is the same no matter what
#print(mid)
#print(mid.getX())
#print(mid.getY())

#class Fruit():
#    def __init__(self, name, price):
#        self.name = name
#        self.price = price
#    def sort_priority(self):
#        return self.price
#L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
#for f in sorted(L, key=lambda x: x.price):
#    print(f.name)
#    
#print(sorted(L, key=Fruit.sort_priority))#
#
#for f in sorted(L, key=Fruit.sort_priority):
#    print(f.name)

#class Point:
#    """ Point class for representing and manipulating x,y coordinates. """
#
#    printed_rep = "*"
#
#    def __init__(self, initX, initY):
#
#        self.x = initX
#        self.y = initY
#
#    def graph(self):
#        rows = []
#        size = max(int(self.x), int(self.y)) + 2
#        for j in range(size-1) :
#            if (j+1) == int(self.y):
#                special_row = str((j+1) % 10) + (" "*(int(self.x) -1)) + self.printed_rep
#                rows.append(special_row)
#            else:
#                rows.append(str((j+1) % 10))
#        rows.reverse()  # put higher values of y first
#        x_axis = ""
#        for i in range(size):
#            x_axis += str(i % 10)
#        rows.append(x_axis)
#
#        return "\n".join(rows)
#p1 = Point(2, 3)
#p2 = Point(3, 12)
#rint(p1.graph())
#print()
#print(p2.graph())
