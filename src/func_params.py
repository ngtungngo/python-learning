# BAD
def declare_defaults(p1=None, p2=None, p3=None):
  print([p1, p2, p3])
# GOOD


def positional_arguments(*args):
  print(args)
# GOOD


def key_word_arguments(**kwargs):
  print(kwargs)
  print(kwargs['p1'])


declare_defaults(p1=1, p2=2, p3=3)   # [1,2,3]
positional_arguments(1, 2, 3)          # [1,2,3]
key_word_arguments(p1=1, p2=2, p3=3)  # {'p1': 1, 'p2': 2, 'p3': 3}

