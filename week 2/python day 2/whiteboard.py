# Write a function that removes the spaces from the string, then return the resultant string.
# Your input will always be a string that only contains spaces, numbers, and letters.
# Examples:
# Input -> Output
# "8 j 8   mBliB8g  imjB8B8  jl  B" -> "8j8mBliB8gimjB8B8jlB"
# "8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd" -> "88Bifk8hB8BB8BBBB888chl8BhBfd"
# "8aaaaa dddd r     " -> "8aaaaaddddr"
# "                 " -> ""

#UPER

#Understand, Plan, Execute, Refactor

#Understand
#Use string.replace(" ", "") to remove space from string

#Plan
#Remove space from string, return string


def sol():
    word = "8 j 8   mBliB8g  imjB8B8  jl  B"
    print(word.replace(" ", ""))
sol()


def sol(word):
    word = word.replace(" ", "")
    return word
print(sol("Hi How are you?"))


def sol(word):
    return word.replace(" ", "")
print(sol("Hi How are you?"))
    
