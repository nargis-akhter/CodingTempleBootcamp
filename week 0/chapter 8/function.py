#functions require information to be passed in order for the task to be completed. we pass information into functions as arguments

#arguments go inside parentheses () after the function name

#functions need their arguments to work. missing arguments can result in errors

#a function can take as many arguments as needed to complete the task
 
#return sends values back so they can be stored and used in the program

#multiple return values are separated by a comma


#the execution of the code inside a function ends when a value is returned
#any additional lines of code after the return line will be ignored
def rect(d1, d2):
  area = 0
  return area
  #end of function execution
  area = d1 * d2 #not executed
  
  
#python allows function arguments to have default values
#if the function is called without the argument, the argument gets its default value
#the default value is used only if no other value has been passed as an argument when the function is called.
def greet(name="Guest"):
  print("Welcome", name)
greet() # Welcome Guest
greet("John") # Welcome John