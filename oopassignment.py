#Assignment 1: Design Your Own Class! 🏗️
#Add attributes and methods to bring the class to life!
#Use constructors to initialize each object with unique values.
#Add an inheritance layer to explore polymorphism or encapsulation.

class bags:  #Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
    def __init__(self, color, size, material): #Use constructors to initialize each object with unique values.
        self.color = color
        self.size = size
        self.material = material

bag1=  bags ("Pink", "small","pleather") #Add attributes and methods to bring the class to life!
bag2=  bags ("Black", "large","leather")
bag3=  bags ("Blue", "medium","canvas")
print(bag2.size)

#Add an inheritance laye
class shoes(bags): #Create a subclass that inherits from the parent class.
     pass
shoes1=shoes("Balck",37,"Shinny material")
shoes2=shoes("Peach",36,"plastic")
shoes3=shoes("brown",38,"leather")

print(shoes3.material)

# explore encapsulation.
class bagsStock:
    def __init__(self):
        self.__bags= 15 #Private attribute

    def sell_bag(self):
        if self.__bags> 0:
            self.__bags-=1
            print(f"Bag sold!. The remaining stock is {self.__bags}")
        else:
            print("Order more bags!")
orders=bagsStock()
orders.sell_bag()


#Activity 2: Polymorphism Challenge! 🎭
#Create a program that includes animals or vehicles with the same action (like move()).
#However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

class horse:
    def move(self):
         return "Gallops"
    

class fish:
    def move(self):
         return "swims"
##Create instances of each class and call the move() method.
for animal in [horse(),fish()]:
    print(animal.move()) #This will call the move method of each animal class.


