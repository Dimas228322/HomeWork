# 4. Написать скрипт, который для заданной папки выводит статистику размеров файлов
#Техническое задание

#Директорию с файлами 'some_data' можно скачать из прикрепленных к уроку файлов.
#Результат формируется в виде словаря
#ключи — верхняя граница размера файла.
#значения — общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей (начинаем с 0)
#Границы диапазонов размеров считаем фиксированными данными - пусть будет кратна 10, как в примере.
#Программа должна легко модифицироваться под другие границы диапазонов.
#Программа должна легко модифицироваться под увеличение количества диапазонов. Т.е. если диапазонов станет 150 шутк - не надо будет переписывать всю программу.
from os.path import join
from os import walk, stat
directory_name = "task_7_4"
dir1 = join("..", directory_name)
somedata = join(dir1, '../some_data')
diapozon = [100,1000,10000,100000]
statistic_files = {key: 0 for key in diapozon}
for dirs, some_dirs, allfiles in walk(somedata):
    for file in allfiles:
        fullsize = stat(join(dirs, file)).st_size
        for i in statistic_files.keys():
            if fullsize < i:
                statistic_files[i] = statistic_files[i] + 1
print(statistic_files)

