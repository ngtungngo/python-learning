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
    ```
    ```
    git add src/first_programm.py
    ```
    ```
    git commit src -m "initial"
    ```
    ```
    git commit src src/first_programm.py -m "initial"
    ```
    ```
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