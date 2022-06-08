 #Реализовать класс Worker (работник).
#Техническое задание:

#определить атрибуты: name, surname, position (должность), income (доход)
#атрибут income должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, '{"wage": wage, "bonus": bonus}'
#При создании экземпляра параметры wage, bonus передаются как числа.
#создать класс Position (должность) на базе класса Worker. Это наследование.
#в классе Position реализовать методы получения полного имени сотрудника '(get_full_name)' и дохода с учётом премии '(get_total_income)'. Методы возвращают соответсвующие значения. Подумайте, корректно ли в классе наследнике напрямую обращаться к защищенному атрибуту income. Или нужен getter? Аргументируйте ответ.
#проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
class Positon(Worker):
    def get_full_name(self):
        rez = f"{self.name} {self.surname}"
        return f"Полное имя сотрудника: {rez}"
    def get_total_income(self):
        gettotalincome = self._income['wage'] + self._income['bonus']
        return f"Оклад + премия = {gettotalincome}"
losk1 = Positon('Дмитрий','Ян','Директор',2000, 1000)
print(losk1.get_full_name())
print(losk1.get_total_income())
losk2 = Positon('Лже','Дмитрий','Повар',100, 10)
print(losk2.get_full_name())
print(losk2.get_total_income())
losk3 = Positon('Леже','Бока','Лежебока',20, 100)
print(losk3.get_full_name())
print(losk3.get_total_income())


