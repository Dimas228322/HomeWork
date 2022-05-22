import sys
argv = sys.argv
with open('bakery.csv', mode='r', encoding='utf-8') as bak_read:
    cena = bak_read.read().strip().split('\n')
lenth = len(cena)
if argv[1].isdigit() is False:
    print('Неккоректное значение')
elif int(argv[1]) > lenth - 1:
    print('Неккоректное значение')
elif len(argv) == 3:
    print('\n'.join(cena[int(argv[1]):int(argv[2])]))
elif len(argv) == 2:
    print('\n'.join(cena[int(argv[1]):]))
else: print('\n'.join(cena[1:]))

