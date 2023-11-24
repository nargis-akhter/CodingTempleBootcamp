prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program." 

message = "" #We set up a variable message to store whatever value the user enters. We define message as an empty string

while message != 'quit':
    message = input(prompt)
    print(message)
