# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def les05_easy_01():
    print('Напишите скрипт, создающий директории dir_1 - dir_9 в папке, \
из которой запущен данный скрипт. И второй скрипт, удаляющий эти папки.')
#выдает синтаксическую ошибку. ВРоде бы все перерыл и оно работало. Но сейчас не работает.
    main_start = True
    while main_start == True:
        try:
            choise = str(input('Выберите один из двух вариантов:\n\
1 - создать файлы\n\
2 - удалить файлы\n'))
            if choise == '1': make_dir()
            elif choise == '2': remove_dir()
            else:
                print('Good bye')
                main_start = False
        except Exception as e:
            print('Что-то пошло не так')
                         
      
        
def make_dir():
    import os
    print('Нажмите ввод для создания файлов')
    dir_path = [('dir_' + str(i + 1)) for i in range(9)]
    for i in dir_path:
        os.mkdir(i)

def remove_dir():
    import os
    print('Нажмите ввод для удаления файлов')
    dir_path = [('dir_' + str(i + 1)) for i in range(9)]
    for i in dir_path:
        os.rmdir(i)
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def les05_easy_02():
    import os
    print('Напишите скрипт, отображающий папки текущей директории.')
# надо написать, чтобы только папки отображал, а os.listdir показывает все содержимое.
# поэтому используем os.path()
    print('Папки в текущей директории: {arr}'.format(arr=[i for i in os.listdir(os.getcwd()) if os.path.isdir(i)]))
# еще вариант - с использованием filter
    dirs = list(filter(lambda x: os.path.isdir(x), os.listdir(os.getcwd())))
    print('Папки в текущей директории с использованием filter(): ', dirs)
    
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def les05_easy_03():
    print('Напишите скрипт, создающий копию файла, из которого запущен \
данный скрипт.')
    import os
    import shutil
    import sys
    try:
        file_copy = input('Введите имя копии файла без расширения для создания \
копии файла в той же директории: ')
        shutil.copy(sys.argv[0], os.getcwd()+'\\'+file_copy + '.py')
        print('Копия файла {} успешна создана в рабочей директории'.format(os.path.basename(sys.argv[0])))
        print('Нажмите ввод для продолжения')
        input()
    except Exception as e:
        print('Допущена ошибка')
        print('Нажмите ввод для продолжения')
        input()
