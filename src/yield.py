def odd_normal(my_iterable):
  odd_numbers = []
  for x in my_iterable:
    if x % 2 == 1:
      odd_numbers.append(x)

  return odd_numbers

# use yield
def odd(my_iterable):
  for x in my_iterable:
    if x % 2 == 1:
      yield x


my_generator = odd_normal([1, 2, 3, 4, 5, 6])
print(*my_generator)
print(list(my_generator))                          # [1,3,5]
print(len(list(my_generator)))                       # 3
[x for x in my_generator] == list(my_generator)  # True
