#1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:

#|--my_project
#|   |--settings
#|   |--mainapp
#|   |--adminapp
#|   |--authapp

#Техническое задание

#Продумайте ситуацию, когда все или часть этих папок уже есть в директории.
#Выберите наиболее подходящую структуру данных для хранения имен папок так
#чтобы легко расширить количество создаваемых папок, например до 100 папок.
import os.path
from os import makedirs
from os.path import join
task7 = "task_1"
dir_name = "my_project"
all_dirs = ["settings", "mainapp", "adminapp", "authapp"]
addirs = join(".", task7, dir_name)
for i in all_dirs:
    dirs1 = join(".", task7, dir_name, i)
    if not os.path.exists(dirs1):
        makedirs(dirs1)
