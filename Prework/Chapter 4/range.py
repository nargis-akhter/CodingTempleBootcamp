for value in range(1,5):
    print(value)
    
for value in range(1,21):
    print(value)
    
#Using range() to make a list of numbers
numbers = list(range(1,6))
print(numbers)

#numbers = list(range(1,100000001))
#print(numbers)


#Make a list of the first 10 square numbers
#In Python, two asterisks (**) represent exponents.

threes = []
for value in range(3,31):
    three = value*3
    threes.append(three)  
print(threes)

    
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

#^More concise code:
squares = []
for value in range(1,11):
    squares.append(value**2) 
print(squares)

#^Even more concise code which is one line:
squares = [value**2 for value in range(1, 11)]
print(squares)

cubes = []
for value in range(1,11):
    cube = value**3
    cubes.append(cube)
print(cubes)

cubes = [value**3 for value in range(1,11)]
print(cubes)



