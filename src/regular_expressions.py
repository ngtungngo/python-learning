import re

## findall
msg = "completely refer 12345 bright pick town 42 money market task finger 4711 television pine herself personal fish ability pound industry torn potatoes indeed easier happened shake biggest"
pattern = "\d+"

result = re.findall(pattern, msg)
print(f'findall::Output: {result}')


## search

text = "Content: hall dog kind pony frozen population mother continued captain spell furniture prepare student development draw pull children rice remember crowd stock identity blind he"
# checking if 'Content' is present at the beginning
match = re.search('\AContent', text)

print('Search: Found') if match else print('Search: Not found')


## split

text = "discuss sight 4711 tongue radio help current throw bright rear else 42 capital both north produce did done greatly shop been 7 tall jungle think floor major"
pattern = "\d+"

result = re.split(pattern, text)
print(f'split::result: {result}')

## sub

text="wear helpful floating additional fix constantly slept attempt breakfast teeth serious action comfortable with poet finish concerned continued those shore probably per bad add"
# replacing whitesspace characters with ';'
result = re.sub("\s", ";", text)
print(f'sub::result: {result}')

## subn

text="dinner fix ourselves fat army my particularly rhythm hospital selection perhaps wait citizen combine child eaten route club include worth zero people equipment bear"
pattern = "en"
result = re.subn(pattern, "EN", text)

print(f'subn::result: {result}')