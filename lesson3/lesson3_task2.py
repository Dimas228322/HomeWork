#. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Количество передаваемых имен в функцию может быть любым. Считаем, что переданы будут только корректные строки.
# Обратите внимание, что функция принимает произвольное количество параметров.
# Вернуть словарь с ключами, отсортированными в алфавитном порядке.
# Выполнить вызов функции для списка имен и вывести на экран словарь.
# Вы можете вывести на экран «красиво» - как в примере на каждой строке одна буква и список, но это не обязательно.
humans = input('Напишите имя сотрудника: ')
names = {}
if humans in names:
    print('yeees')
