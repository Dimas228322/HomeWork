# 1. Написать генератор нечётных чисел от 1 до n (включительно), без использования ключевого слова yield
# полностью истощить генератор.
# Формат вывода результата:
#
# Программа явно должна закончиться на StopIteration
#
#Техническое задание
#n - любое положительное число.
#Создание генератора сделайте внутри функции iterator_without_yield(n),
# примающей аргументом n любое положительное число и возвращающей генератор.
#
#Не путайте истощение генератора и печать его значений. Выполнение программы должно закончиться на исключении StopIteration.
# Истощение генератора - любым удобным для вас способом.
n = 15
def iterator_without_yield(n):
    return (i for i in range(1, n+1, 2))
gen1 = iterator_without_yield(n)
#print(gen1)
for i in gen1:
    print(i)
