import math
#Tip: use a list comprehension instead of map, reduce, and filter.
good = [math.factorial(n) for n in range(6) if n % 2 == 1]
print(good)


bad = list(map(math.factorial, filter(lambda n: n % 2 == 1, range(6))))
print(bad)
