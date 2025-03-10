from tkinter import *
from tkinter import ttk
"""Виджет Label представляет текстовую метку. Этот элемент позволяет выводить статический текст без возможности редактирования."""
"""Для создания элемента Label применяется конструктор, который принимает два параметра:"""
#Label(master, options)
"""Параметр master представляет ссылку на родительский контейнер, а параметр options представляет следующие именованные параметры"""
#anchor: устанавливает позиционирование текста
#background: фоновый цвет
#borderwidth: толщина границы метки
#cursor: курсор указателя мыши при наведении на метку
#font: шрифт текста
#foreground: цвет текста
#height: высота виджета
#image: ссылка на изображение, которое отображается на метке
#justify: устанавливает выравнивание текста. Значение LEFT выравнивает текст по левому краю, CENTER - по центру, RIGHT - по правому краю
#pading: отступы от границ вилжета до его текста
#relief: определяет тип границы, по умолчанию значение FLAT
#text: устанавливает текст метки
#textvariable: устанавливает привязку к элементу StringVar
#underline: указывает на номер символа в тексте метки, который подчеркивается. По умолчанию значение -1, то есть никакой символ не подчеркивается
#width: ширина виджета
#wraplength: при положительном значении строки текста будут переносится для вмещения в пространство виджета
"""Выведем в окне приложения простейший текст:"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#label = ttk.Label(text="Hello METANIT.COM")
#label.pack()
#
#root.mainloop()
"""Установка шрифта"""
"""Параметр font принимает определение шрифта в виде:"""
#font = ("имя шрифта", размер_шрифта)
"""Первое значение передает имя шрифта в кавычках, а второе - числовой размер шрифта. Например, установим шрифт Arial высотой в 14 единиц:"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#label = ttk.Label(text="Hello METANIT.COM", font=("Arial", 14))
#label.pack()
#
#root.mainloop()
"""Установка изображения"""
"""За установку изображения на метке отвечает параметр image. Самый простой способ определения изображения представляет создание объекта PhotoImage, в конструктор которого передается путь к изображению:"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#python_logo = PhotoImage(file="./python_logo.png")
#
#label = ttk.Label(image=python_logo)
#label.pack()
#
#root.mainloop()
"""В моем случае изображение представляет файл python_logo.png, которое находится в одной папке с файлом приложения и которое изображает логотип python"""
"""Если необходимо также отображать и текст, то для этого можно установить параметр compound, который определяет положение текста по отношению к изображению с помощью одного из следующих значений:"""
#top: изображение поверх текста
#bottom: изображение под текстом
#left: изображение слева от текста
#right: изображение справа от текста
#none: при наличии изображения отображается только изображение
#text: отображается только текст
#image: отображается только изображение
"""Например, отобразим картинку поверх текста:"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#python_logo = PhotoImage(file="./python_logo.png")
#
#label = ttk.Label(image=python_logo, text="Python",
#                  compound="top")
#label.pack()
#
#root.mainloop()
"""Стилизация"""
"""По умолчанию метка не имеет границы. Для установки толщины границы используется параметр borderwidth, при этом нам также надо установить тип границы с помощью параметра releaf, который может принимать значения: "flat", "raised", "sunken", "ridge", "solid" и "groove":"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#label = ttk.Label(text="Hello Tkinter", borderwidth=2,
#                  relief="ridge", padding=8)
#label.pack(expand=True)
#
#root.mainloop()
"""Установка цвета фона и текста:"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#label = ttk.Label(text="Hello Tkinter",
#                  background="#FFCDD2",
#                  foreground="#B71C1C", padding=8)
#label.pack(expand=True)
#
#root.mainloop()
