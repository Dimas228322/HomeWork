# Дан список строк. Выполнить обработку списка (смотри текст задания) и сформировать на его основе строку
#Техническое задание:

#Список может содержать произвольное кол-во элементов. Все его элементы - строки.

#1. Создать новый список и наполнить его элементами по схеме
#2. Обособить каждое целое число (исходного списка) кавычками
#   (добавить элемент списка: строку-кавычку до и после элемента списка, являющегося числом)
# 3. дополнить это число нулём до двух целочисленных разрядов
# 4. Например исходный список: ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов'].
# Тогда новый список: ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов'].
# Новый список вывести на экран
# 5. После окончательного формирования нового списка - сделать на его основе строку, соединив все элементы
# Для примера выше: 'в "05" часов "17" минут температура воздуха была "+05" градусов'
# 6. Вывести строку на экран.
list1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list2 = ['в', '5', 'часов', '5', 'минут', '5', 'секунд', 'температура', 'воздуха', 'была', '-5', 'градусов']
list3 = ['в', '19', 'часов', '18', 'минут', '03', 'секунд', 'температура', 'воздуха', 'была', '+50', 'градусов Цельсия']
skobka = '"'
white_list = []
for_list = []
for slova in list1:#1#2#3 Все списки работают
    if str.isdigit(slova) == True or str.isdigit(slova[1:]):
        white_list.append(skobka)
        white_list.append(slova)
        white_list.append(skobka)
    else: white_list.append(slova)
for black_list in white_list:
    if str.isdigit(black_list) == True:
        a = black_list.zfill(2)
        for_list.append(a)
    elif str.isdigit(black_list[1:]):
        b = black_list.zfill(3)
        for_list.append(b)
    else: for_list.append(black_list)
print(for_list)
#print(" ".join(for_list))
lastlist = ''
i = 0
while i < len(for_list):
    if for_list[i] == '"':
        lastlist += for_list[i] + for_list[i+1] + for_list[i+2] + ' '
        i += 2
    else: lastlist += for_list[i] + ' '
    i += 1
print(lastlist)
#Самое сложное задание пока что из всех














