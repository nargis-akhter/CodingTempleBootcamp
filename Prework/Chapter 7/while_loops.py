#Counts from 1 to 5:

current_number = 1 #We start counting from 1 by setting the value of current_number to 1
while current_number <= 5: #The while loop is then set to keep running as long as the value of current_number is less than or equal to 5
    print(current_number) #The code inside the loop prints the value of current_number
    current_number += 1 #Then adds 1 to that value with current_number += 1
    #Remember to increment i, or else the loop will continue forever.
    
"""
Python repeats the loop as long as the condition current_number <= 5
is true. Because 1 is less than 5, Python prints 1 and then adds 1, mak-
ing the current number 2. Because 2 is less than 5, Python prints 2
and adds 1 again, making the current number 3, and so on
"""