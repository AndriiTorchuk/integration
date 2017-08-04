"""
Exercise 10: Class 
"""

# Create a class: Car
class Car:
    def start(self):
        return("started")
    def stop(self):
        return("stopped")
# Create a class: Mazda
class Mazda(Car):
    def __str__(self):
        return "this is mazdaaa"
    def brand(self):
        print("mazda")
        return("mazda")
    def somestuff(self):
        pass
        

mazda = Mazda()
print(mazda)
print(dir(mazda))

mazda.start()
mazda.stop()
mazda.brand()

print(mazda)
