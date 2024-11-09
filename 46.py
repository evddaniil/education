l = input('буква ')
n = int(input('номер '))

if l in ('a', 'c', 'e', 'g'): 
    col = 'белая'
else:
    col = 'чёрная'

if (col == 'белая' and n % 2 == 0) or (col == 'чёрная' and n % 2 != 0):
    color = 'белая'
else:
    color = 'чёрная'

print(color)