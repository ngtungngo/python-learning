import datetime
import timeit



class ElapsedTime:
    def __init__(self, round_ndigits: int = 0):
        self._round_ndigits = round_ndigits
        self._start_time = timeit.default_timer()

    def __call__(self) -> float:
        return timeit.default_timer() - self._start_time

    def __str__(self) -> str:
        return str(datetime.timedelta(seconds=round(self(), self._round_ndigits)))



mlist = ['fifteen', 'we', 'percent', 'chart', 'swimming']
new_list = []

# Slow:
time = ElapsedTime()
time()
for item in mlist:
    new_list.append(item.capitalize())
print(f'>>> elapsed time (sec): {time()}')
print(f'Slow::new list: {new_list}')

# Faster:
time()
new_list = list(map(str.capitalize, mlist))
print(f'>>> elapsed time (sec): {time()}')
print(f'Faster::new list: {new_list}')



# String Concatenation vs join
#slow
time()
for item in mlist:
    new_list += item
print(f'>>>Concatenation: elapsed time (sec): {time()}')

#faster:
time()
new_list = "".join(mlist)
print(f'>>>join: elapsed time (sec): {time()}')
