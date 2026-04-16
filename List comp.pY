fruit = list(input("Enter a few fruits: ").split())
lst = map(lambda x: x[0].upper() + x[1:].lower(), fruit)
fruit = list(lst)
print(fruit)