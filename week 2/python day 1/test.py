#Make a function that receive age, and return what they drink

#UPER

#Understand, Plan, Execute, Refactor

#Understand
#Input: An age object. This will be an integer!
#Output: String: The drink in which the person is able to order/drink
#If they are 14 or younger, they drink "toddy"
#If they are 14-18, they drink "coke"
#18-21: They drink "beer"
#21+: They drink "whiskey"

#Plan
#Make sure the age is integer
#Conditional statement: If age < 14: return 'drink toddy'
#Elifs to chain together my conditionals so we don't have to recheck elif age < 18: return 'drink coke'

#Execute:
def solutions(age):
    age = int(age)
    if age < 14:
        return 'drink toddy'
    elif age < 18:
        return 'drink coke'
    elif age < 21:
        return 'drink beer'
    else:
        return 'drink whiskey'
    
print(solutions(14))