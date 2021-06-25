#Define a class called Bike that accepts a string and a float as input, and assigns those inputs respectively to two instance variables, color and price. 
#Assign to the variable testOne an instance of Bike whose color is blue and whose price is 89.99. Assign to the variable testTwo an instance of Bike whose color is 
#purple and whose price is 25.0.
class Bike:
    def __init__(self, color, price):
        self.color = color
        self.price = price
        
testOne = Bike("blue", 89.99)
testTwo = Bike("purple", 25.0)

#Create a class called AppleBasket whose constructor accepts two inputs: a string representing a color, and a number representing a quantity of apples. 
#The constructor should initialize two instance variables: apple_color and apple_quantity. Write a class method called increase that increases 
#the quantity by 1 each time it is invoked. You should also write a __str__ method for this class that returns a string of the 
#format: "A basket of [quantity goes here] [color goes here] apples." e.g. "A basket of 4 red apples." or "A basket of 50 blue apples."
# (Writing some test code that creates instances and assigns values to variables may help you solve this problem!)
class AppleBasket:

    def __init__(self, color, quantity):
        self.apple_color = color
        self.apple_quantity = quantity

    def increase(self):
        self.apple_quantity += 1
        
    def __str__(self):
        return "A basket of {} {} apples.".format(self.apple_quantity, self.apple_color)
  
a1 = AppleBasket("red", 4)
a2 = AppleBasket("blue", 50)

print(a1)
print(a2)