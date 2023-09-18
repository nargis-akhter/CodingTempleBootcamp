

#If a conditional test evaluates to True, Python executes the code following the if statement. 
# If the test evaluates to False, Python ignores the code following the if statement.

car = 'bmw'
print(car == 'bmw')
print(car == 'audi')

#If case doesn’t matter and instead you just want to test the value of a variable, you can convert the variable’s value to lowercase before doing the comparison
car = 'Audi'
print(car.lower() == 'audi')
