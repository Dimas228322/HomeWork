# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх заданных списков.
# Функция должна вернуть список строк-шуток.
# Функция принимает 4 параметра: количество шуток и 3 списка со словами.
# В списках nouns, adverbs, adjectives не обязательно одинакое количество элементов. Они могут быть произвольной длины.
# Проверьте работу функции для количества шуток больше, чем длины списков слов и меньше
# Сделайте вызов функции как с позиционными аргументами, так и с именованными.
# Менять исходные списки nouns, adverbs, adjectives нельзя. Это «side effects»
# Документируйте код функции.

from random import randrange
howmore = input('Количество шуток:')
n = int(howmore)
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
def get_jokes(n,nouns, adverbs, adjectives):
    i = 0
    joke = []
    while i < n:
        random_slovo1 = randrange(len(nouns))
        random_slovo2 = randrange(len(adverbs))
        random_slovo3 = randrange(len(adjectives))
        a = nouns[random_slovo1]
        b = adverbs[random_slovo2]
        c = adjectives[random_slovo3]
        lst1 = a + ' ' + b + ' ' + c
        joke.append(lst1)
        i += 1
    print(joke)
get_jokes(n,nouns,adverbs,adjectives)
