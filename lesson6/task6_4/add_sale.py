import sys
s = sys.argv[1]
sale = s
if sale.isdigit() == True:
    f = open("bakery.csv",'a',encoding='utf-8')
    f.write(sale)
    f.write("\n")
    f.close()
    print('Добавлено в список продаж')
else:
    sale.isdigit()  == False
    print('Некоректное значение')

