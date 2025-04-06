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
"""Для наполнения listboxа элементами определяем список languages, затем этот список передаем в переменную типа Variable. Затем привязываем эту переменную к параметру listvariable у Listbox"""
"""Основные методы Listbox"""
"""Listbox имеет ряд методов для управления поведением элемента и его содержимым. Некоторые из них:"""
# curselection(): возвращает набор индексов выделенных элементов
# delete(first, last = None): удаляет элементы с индексами из диапазона [first, last]. Если второй параметр опущен, то удаляет только один элемент по индексу first
# get(first, last = None): возвращает кортеж, который содержит текст элементов с индексами из диапазона [first, last]. Если второй параметр опущен, возвращается только текст элемента с индексом first
# insert(index, element): вставляет элемент по определенному индексу
# size(): возвращает количество элементов
"""Для рассмотрения этих методов напишем небольшой скрипт по управлению данными:"""
## удаление выделенного элемента
#def delete():
#    selection = languages_listbox.curselection()
#    # мы можем получить удаляемый элемент по индексу
#    # selected_language = languages_listbox.get(selection[0])
#    languages_listbox.delete(selection[0])
#
## добавление нового элемента
#def add():
#    new_language = language_entry.get()
#    languages_listbox.insert(0, new_language)
#
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("300x250")
#root.columnconfigure(index=0, weight=4)
#root.columnconfigure(index=1, weight=1)
#root.rowconfigure(index=0, weight=1)
#root.rowconfigure(index=1, weight=3)
#root.rowconfigure(index=2, weight=1)
#
## текстовое поле и кнопка для добавления в список
#language_entry = ttk.Entry()
#language_entry.grid(column=0, row=0, padx=6, pady=6, sticky=EW)
#ttk.Button(text="Добавить", command=add).grid(column=1, row=0, padx=6, pady=6)
#
## создаем список
#languages_listbox = Listbox()
#languages_listbox.grid(row=1, column=0, columnspan=2, sticky=EW, padx=5, pady=5)
#
## добавляем в список начальные элементы
#languages_listbox.insert(END, "Python")
#languages_listbox.insert(END, "C#")
#
#ttk.Button(text="Удалить", command=delete).grid(row=2, column=1, padx=5, pady=5)
#
#root.mainloop()
"""Для манипулирования элемента списка здесь определенно две кнопки. Первая кнопка вызывает функцию add(), которая получает введенное в текстовое поле значение и добавляет его на первое место в списке с помощью метода insert()."""
"""Вторая кнопка по нажатию удаляет выделенный элемент. Для этого мы сначала получаем выделенные индексы через метод curselection(). Так как в нашем случае выделяется только один элемент, то получаем его индекс через выражение selection[0]. И этот индекс передаем в метод delete() для удаления."""
