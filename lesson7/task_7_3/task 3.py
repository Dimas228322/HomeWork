#3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
#Написать скрипт, который собирает все шаблоны в одну папку templates:

#|--my_project
#...
#|--templates
#|   |--mainapp
#|   |  |--base.html
#|   |  |--index.html
#|   |--authapp
#|   |  |--base.html
#|   |  |--index.html

#Шаблон - это папка templates в исходной структуре папок. Ее уровень в структуре папок может быть любым.
#В папках mainapp, authapp и аналогичных могут быть и другие файлы, с другими раширениями, кроме тех что приведенны в примере.
#Папку templates надо создать внутри исходной директории, в примере - внутри my_project
#Исходные файлы и папки необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках (они играют роль пространств имён).
#Предусмотреть возможные исключительные ситуации;
from os.path import join
from shutil import copytree
from os import  walk
osnova = join(".", "my_project")
templates = join(osnova, "templates")
for papki, direct, allfiles in walk(osnova):
    if "templates" in direct:
        copytree(join(papki,"templates"), templates, dirs_exist_ok = True)



