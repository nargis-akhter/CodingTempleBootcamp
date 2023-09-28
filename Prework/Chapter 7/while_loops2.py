prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program." 

active = True
while active: """ We set the variable active to True u so the program starts in an active
state. Doing so makes the while statement simpler because no comparison is
made in the while statement itself; the logic is taken care of in other parts of
the program. As long as the active variable remains True, the loop will con-
tinue running """
message = input(prompt)
    
if message == 'quit':
    active = False
else:
    print(message)
    