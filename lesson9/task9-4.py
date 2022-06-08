#Реализуйте класс Car (машина).
#Техническое задание:

#атрибуты: speed, color, name, 'is_police': (булево). speed - текущая скорость машины. Внимательно по отношению выбора атрибут класса/экземпляра.
#методы: go, stop, turn(direction), которые должны сообщать(выводить на экран), что машина поехала, остановилась, повернула (куда). turn(direction)
#- метод, принимающий параметр: направление поворота.
#Сами определите как вызов этих методов меняет скорость машины. На ваше усмотрение.
#опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar
#добавьте в базовый класс Car метод show_speed, который должен показывать текущую скорость автомобиля
#для классов TownCar и WorkCar переопределите метод 'show_speed'. При значении скорости машины свыше 60 (TownCar) и 40 (WorkCar)
#должно выводиться сообщение о превышении скорости.
#Ограничения на скорость - очевидно данные. Где их нужно хранить?
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self,speed,color,name):
        self.time = 10
        self.break_dvig = -9
        self.speedometr = 0
        self.color = color
        self.name = name
        self.maxspeed = speed
        self.pazgon = self.maxspeed / 10.0
        self.how = None

    def go(self):
        print(f"{self.name} поехал(а)")
        self.how = 1
    def stop(self):
        print(f"{self.name} остановилась")
        self.how = 0
    def turn(self,direction):
            print(f"{self.name} Повернул(а) {direction}")
    def show_speed(self):
        if self.how == 1:
            rez = ""
            for time in range(self.time):
                speedometr = self.speedometr + time * self.pazgon
                rez += f"{speedometr:.0f} "
            self.speedometr = speedometr
            print(rez)
        elif self.how == 0:
            rez = ""
            time = 0
            while True:
                time += 1
                speedometer = self.speedometr + time * self.break_dvig
                if speedometer <= 0:
                    self.speedometr = 0
                    break
                if speedometer is not None and time >= speedometer:
                    break
                rez += f"{speedometer:.0f} "
                self.speedometr = speedometer
            print(rez)
            self.how == None
        print(f"Текущая скорость {self.name} = {self.speedometr}")
class TownCar(Car):
    def __init__(self,speed,color,name):
        super().__init__(speed,color,name)
    def show_speed(self):
        limit = 60
        if self.how == 1:
            rez = ""
            for time in range(self.time):
                speedometr = self.speedometr + time * self.pazgon
                rez += f"{speedometr:.0f} "
            self.speedometr = speedometr
            print(rez)
            if self.speedometr > limit:
                howmany = self.speedometr - limit
                print(f"Превышение скорости на {howmany}")
        elif self.how == 0:
            rez = ""
            time = 0
            while True:
                time += 1
                speedometer = self.speedometr + time * self.break_dvig
                if speedometer <= 0:
                    self.speedometr = 0
                    break
                if speedometer is not None and time >= speedometer:
                    break
                rez += f"{speedometer:.0f} "
                self.speedometr = speedometer
            print(rez)
            self.how == None
        print(f"Текущая скорость {self.name} = {self.speedometr}")

class SportCar(Car):
    pass

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        limit = 40
        if self.how == 1:
            rez = ""
            for time in range(self.time):
                speedometr = self.speedometr + time * self.pazgon
                rez += f"{speedometr:.0f} "
            self.speedometr = speedometr
            print(rez)
            if self.speedometr > limit:
                howmany = self.speedometr - limit
                print(f"Превышение скорости на {howmany}")
        elif self.how == 0:
            rez = ""
            time = 0
            while True:
                time += 1
                speedometer = self.speedometr + time * self.break_dvig
                if speedometer <= 0:
                    self.speedometr = 0
                    break
                if speedometer is not None and time >= speedometer:
                    break
                rez += f"{speedometer:.0f} "
                self.speedometr = speedometer
            print(rez)
            self.how == None
        print(f"Текущая скорость {self.name} = {self.speedometr}")

class PoliceCar(Car):
    pass


Auto = Car(100,'Чёрная','Honda')
Auto.go()
Auto.show_speed()
Auto.stop()
Auto.show_speed()
Auto.turn('Налево')
Auto.turn('Направо')
Sport = SportCar(200,'black','Toyta')
Sport.go()
Sport.show_speed()
Sport.stop()
Sport.show_speed()
Town = TownCar(90,'Red','Bus')
Town.go()
Town.show_speed()
Town.stop()
Town.show_speed()
Work = WorkCar(80,'red','MAZ')
Work.go()
Work.show_speed()
Work.stop()
Work.show_speed()
# Что-то я тут намутил жоска, вроде работает как надо, но кода слишком много который повторяется или из-за того что я show_speed слишком рассписал
# Можно ведь было просто написать типо print 'Текущая скорость "автомобиль"'


