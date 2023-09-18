cars = ['audi', 'bmw', 'subaru']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
#if-else statements      
age = 16
if age >= 18:
    print("You are old enough to vote!")
else:
    print("Sorry too young to vote.")
    
#if-elif-else statements
#test more than two possible situations

age = 12
if age < 4: #If the test passes, an appropriate message is printed and Python skips the rest of the tests.
    print("Your admission cost is $0.")
    
elif age < 18: #Another if test, which runs only if the previous test failed
    print("Your admission cost is $5.")
else: #If both the if and elif tests fail, Python runs the code in the else block at
    print("Your admission cost is $10.")