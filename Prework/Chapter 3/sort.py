#The cars are now in alphabetical order, and we can never revert to the original order
#.sort() IN PLACE
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#You can also sort this list in reverse alphabetical order by passing the argument reverse=True to the sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

#The reverse() doesn’t sort backward alphabetically; it simply reverses the order of the list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

#sorted OUT OF PLACE
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
cars = sorted(cars)
print(cars)
cars = sorted(cars, reverse=True)
print(cars)
