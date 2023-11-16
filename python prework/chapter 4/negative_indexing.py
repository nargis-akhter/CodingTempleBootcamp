#Python supports "indexing from the end", called negative indexing. This means the last value of a sequence has an index of -1.

animals =["cat", "dog", "bird", "cow"]
print(animals[-1]) # Last element
print(animals[-2]) # Second last element
print(animals[-3:]) # Last 3 elements
print(animals[-3:-1])

#This is tricky because you have to remember that -1 is exclusive when the last value when slicing:
print(c[1:-1])
but inclusive when not slicing!
print(c[-1])