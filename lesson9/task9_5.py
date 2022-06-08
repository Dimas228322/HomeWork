#5. Реализовать класс Stationery (канцелярская принадлежность).
#Техническое задание:

#атрибут title (название)
#метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
#создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
#в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
#Подумайте о том, имеет ли смысл при переопределении draw использовать draw базового класса.
#создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:
    def draw(*title):
        return ('Запуск отрисовки')


class Pen(Stationery):
    def draw(*title):
        return ('Пишу ручкой')
class Pencil(Stationery):
    def draw(*title):
        return ('Пишу карандашом')
class Handle(Stationery):
    def draw(*title):
        return ('Пишу маркером')

pen = Stationery.draw()
print(pen)
pen1 = Pen.draw()
print(pen1)
pen2 = Pencil.draw()
print(pen2)
pen3 = Handle.draw()
print(pen3)