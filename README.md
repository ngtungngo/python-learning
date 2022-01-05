# python-learning
## Git:
* Neue Order erstellen
```
mkdir src
```

* neue Datei mit der Name first_programm.py in Ordner src in visual studio code erstellen
* in git auf console:
    ```
    git add src
    git add src/first_programm.py
    git commit src -m "initial"
    git commit src src/first_programm.py -m "initial"
    git push
    ```
* Dateien abgleichen
    ```
    git pull
    ```
### Create Number with range
```
numbers = list(range(1,20,2))
print(numbers)
```

### Repeating the element multiple times
```
numbers = [3, 7, 12]
multi = numbers*5
```

### Using Conditions in Ternary Operator

```
consume = 25000
print("Hight") if consume > 50000 else print("Low")
```

## Regular Expressions
## findall
```
import re

msg = "completely refer 12345 bright pick town 42 money market task finger 4711 television pine herself personal fish ability pound industry torn potatoes indeed easier happened shake biggest"
pattern = "\d+"

result = re.findall(pattern, msg)
print(result)
```

## Search
```
text = "Content: hall dog kind pony frozen population mother continued captain spell furniture prepare student development draw pull children rice remember crowd stock identity blind he"
# checking if 'Content' is present at the beginning
match = re.search('\AContent', text)

print('Search: Found') if match else print('Search: Not found')

```

## split
```
text = "discuss sight 4711 tongue radio help current throw bright rear else 42 capital both north produce did done greatly shop been 7 tall jungle think floor major"
pattern = "\d+"

result = re.split(pattern, text)
print(f'split::result: {result}')
```

## sub
```
text="wear helpful floating additional fix constantly slept attempt breakfast teeth serious action comfortable with poet finish concerned continued those shore probably per bad add"
# replacing whitesspace characters with ';'
result = re.sub("\s", ";", text)
print(f'sub::result: {result}')
```

## subn
```
text="dinner fix ourselves fat army my particularly rhythm hospital selection perhaps wait citizen combine child eaten route club include worth zero people equipment bear"
pattern = "en"
result = re.subn(pattern, "EN", text)

print(f'subn::result: {result}')
```

## Simplify sequence check

1. Way:
```
if len(list_of_some_things) > 0:
    one_thing = chooose_thing(list_of_some_things)
```
2. Way:
```
if list_of_some_things:
    one_thing = chooose_thing(list_of_some_things)

```

## Use Any instead of Loop
1. Normal:
```
things = [1,3,4,5,9, 10, -3, -21]
flag = False
for num in things:
    if num < 0:
        flag = True
        break
```

2. Pythonic
```
things = [1,3,4,5,9, 10, -3, -21]
flag = any(things < 0 for num in things)
```

## Adding a Guard Clause
1. Normal:
```
def do_i_need_hat(self, hat):
    if isInstance(hat, Hat):
        weather_outside = getWeatherReport()
        if weather_outside.is_raining:
            print("Yes")
            return True
        else:
            return False
    else:
        return False
```

2. Better:
```
def do_i_need_hat(self, hat):
    if not isInstance(hat, Hat):
        return False
if isInstance(hat, Hat):
        weather_outside = getWeatherReport()
        if weather_outside.is_raining:
            print("Yes")
            return True
        else:
            return False
```