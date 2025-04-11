from tkinter import *
from tkinter import ttk

"""
Выделение строк таблицы
"""
"""
Для работы с выделенными строками в Treeview определен ряд методов:
* selection(): возвращает идентификаторы выделенных строк в виде кортежа
* selection_add(items): выделяет строки с идентификаторами, которые
    передаются в качестве параметра
* selection_remove(items): снимает выделение строк с идентификаторами,
    которые передаются в качестве параметра
* selection_set(items): снимает выделение с ранее выделенных строк и
    выделяет строки с идентификаторами, которые передаются в качестве
    параметра
    
Обработка события выделения
Для обработки выделения строк у Treeview применяется событие
<<TreeviewSelect>>
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
## определяем данные для отображения
#people = [("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com")]
#
#label = ttk.Label()
#label.pack(anchor=N, fill=X)
## определяем столбцы
#columns = ("name", "age", "email")
#tree = ttk.Treeview(columns=columns, show="headings")
#tree.pack(expand=1, fill=BOTH)
#
## определяем заголовки
#tree.heading("name", text="Имя", anchor=W)
#tree.heading("age", text="Возраст", anchor=W)
#tree.heading("email", text="Email", anchor=W)
#
#tree.column("#1", stretch=NO, width=70)
#tree.column("#2", stretch=NO, width=60)
#tree.column("#3", stretch=NO, width=100)
#
## добавляем данные
#for person in people:
#    tree.insert("", END, values=person)
#
#def item_selected(event):
#    selected_people = ""
#    for selected_item in tree.selection():
#        item = tree.item(selected_item)
#        person = item["values"]
#        selected_people = f"{selected_people}{person}\n"
#    label["text"] = selected_people
#
#tree.bind("<<TreeviewSelect>>", item_selected)
#
#root.mainloop()
"""
Здесь с помощью метода bind() устанавливаем для события <<TreeviewSelect>>
функцию-обработчик item_selected. В этой функции получаем все идентификаторы
выделенных строк с помощью метода tree.selection()
    for selected_item in tree.selection()
Используя полученный идентификатор, получаем выделенный элемент с помощью метода tree.item
    item = tree.item(selected_item)
Для получения самих значений обращаемся к атрибуту values:
    person = item["values"]
Складываем их в строку selected_people и отображаем ее в метке label.

Режим выделения
По умолчанию в Treeview можно выделить только один элемент (одну строку). За
установку режима выделения в Treeview отвечает параметр selectionmode, который
может принимать следующие значения:
* extended: позволяет выбрать несколько строк
* browse: позволяет выбрать только одну строку
* none: выделение строк недоступно
Например, изменим код Treeview, установив режим "extended":
    tree = ttk.Treeview(columns=columns, show="heading", selectmode="extended")
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
## определяем данные для отображения
#people = [("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com")]
#
#label = ttk.Label()
#label.pack(anchor=N, fill=X)
## определяем столбцы
#columns = ("name", "age", "email")
#tree = ttk.Treeview(columns=columns, show="headings", selectmode="extended")
#tree.pack(expand=1, fill=BOTH)
#
## определяем заголовки
#tree.heading("name", text="Имя", anchor=W)
#tree.heading("age", text="Возраст", anchor=W)
#tree.heading("email", text="Email", anchor=W)
#
#tree.column("#1", stretch=NO, width=70)
#tree.column("#2", stretch=NO, width=60)
#tree.column("#3", stretch=NO, width=100)
#
## добавляем данные
#for person in people:
#    tree.insert("", END, values=person)
#
#
#def item_selected(event):
#    selected_people = ""
#    for selected_item in tree.selection():
#        item = tree.item(selected_item)
#        person = item["values"]
#        selected_people = f"{selected_people}{person}\n"
#    label["text"] = selected_people
#
#
#tree.bind("<<TreeviewSelect>>", item_selected)
#
#root.mainloop()
"""
И теперь модно выделять несколько строк
"""