#3. Написать декоратор для логирования(вывод в консоль) типов позиционных аргументов функции:
#Если аргументов несколько - выводить данные о каждом через запятую.
#Все выводы должны быть внутри функции-обертки/задекорированной функции
#После того как вы «обернули»/«задекорировали» функцию убедитесь что и аргументы, и возвращаемое значение остались как у исходной функции.
#Т.е. вызов задекорированной функции ничем не отличается от вызова исходной функции, результат возвращается такой же, но добавляется печать в консоль.
def type_logger(func):
    def decor(*args, **kwargs):
        name = func.__name__
        result = func(*args, **kwargs)
        print(f'Call for: {name}')
        for arg1 in args:
            print(f'{arg1} : {type(arg1)}')
        for arg2 in kwargs:
            val = kwargs[arg2]
            print(f'{arg2} = {val} : {type(val)}')
        print(f'Rezult: {result} type: {type(result)}')
        return result
    return decor

@ type_logger
def calc_cube(x):
    return x ** 3

@type_logger
def render_input(*args, **kwargs):
    return 1 #2,2,2

calc_cube(2)
render_input(22, a=10, b='qwerty', c=False)