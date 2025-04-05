from tkinter import *
from tkinter import ttk

"""Виджет Listbox в tkinter представляет список объектов. Стоит отметить, что данный виджет присутствует только в пакете tkinter, а в пакете tkinter.ttk для него нет аналогов."""
"""Для настройки Listbox мы можем указать в его конструкторе следующие параметры:"""
# listvariable: список элементов, которые добавляются в Listbox
# bg: фоновый цвет
# bd: толщина границы вокруг элемента
# cursor: курсор при наведении на Listbox
# font: настройка шрифта
# fg: цвет текста
# highlightcolor: цвет элемента, когда он получает фокус
# highlightthickness: толщина границы элемента, когда он находится в фокусе
# relief: устанавливает стиль элемента по умолчанию имеет значение SUNKEN
# selectbackground: фоновый цвет для выделенного элемента
# selectmode: определяет, сколько элементов могут быть выделены. Может принимать следующие значения: BROWSE, SINGLE, MULTIPLE, EXTENDED. Например, если необходимо включить множественное выделение элементов, то можно использовать значения MULTIPLE или EXTENDED.
# height: высота элемента в строках. По умолчанию отображает 10 строк
# width: устанавливает ширину элемента в символах. По умолчанию ширина - 20 символов
# xscrollcommand: задает горизонтальную прокрутку
# yscrollcommand: устанавливает вертикальную прокрутку
"""Определим простой список:"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#languages = ["Python", "JavaScript", "C#", "Java"]
#languages_var = Variable(value=languages)
#
#languages_listbox = Listbox(listvariable=languages_var)
#
#languages_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)
#
#root.mainloop()
