#1. Распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
#Техническое задание
#Не использовать библиотеки для парсинга. Только работа со строками.
#Создать список кортежей вида: '(<remote_addr>, <request_type>, <requested_resource>)'. Именно список кортежей.
#Код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
#Формат вывода результата:
#   ('141.138.90.60', 'GET', '/downloads/product_2'),
#   ('141.138.90.60', 'HEAD', '/downloads/product_2'),
#  ('173.255.199.22', 'GET', '/downloads/product_1'),
allnames = []
def repars1(allnames):
    file_1 = open('nginx_logs.txt','r',encoding='utf-8')
    content = file_1.readlines()
    for i in content:
        fullnames = i.split(' ')
        remote_addr = fullnames[0]
        n1 = fullnames[5].split('"')
        request_type = n1[1]
        requested_resource = fullnames[6]
        list1 = remote_addr,request_type,requested_resource
        allnames.append(list1)
    yield allnames
gen1 = repars1(allnames)
for i1 in gen1:
    print(i1)




