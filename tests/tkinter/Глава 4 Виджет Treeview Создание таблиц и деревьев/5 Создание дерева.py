from tkinter import *
from tkinter import ttk

"""
    Создание дерева

    Для определения дерева параметру show виджета Treeview передается значение
tree (дерево без заголовка) или tree headings (дерево с заголовком).
Определим простейшее дерево:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
## создаем дерево
#tree = ttk.Treeview(show="tree")
#tree.pack(expand=1, fill=BOTH)
#
## добавляем данные
#tree.insert("", END, iid=1, text="Административный отдел")
#tree.insert("", END, iid=2, text="IT-отдел")
#tree.insert("", END, iid=3, text="Отдел продаж")
#
#root.mainloop()
"""
    Здесь данные для отображения представлены условно представлены списком
отделов некоторого предприятия. Каждый отдел добавляется как элемент верхнего
уровня, поэтому в методе tree.insert в качестве первого аргумента указывается
пустая строка "". Также устанавливаем для каждого добавляемого элемента
параметр text название отдела и его идентификатор - параметр iid. Конечно, мы
могли положиться на tkinter, который установил бы идентификаторы
автоматически. Однако ручная установка идентификаторов потом упростит
добавление в них вложенных элементов
    Однако визуально пока никакого дерева по сути нет, а сами данные не являются
иерархическими. Но теперь добавим в некоторые отделы сотрудников: 
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#tree = ttk.Treeview(show="tree")
#tree.pack(expand=1, fill=BOTH)
#
## добавляем отделы
#tree.insert("", END, iid=1, text="Административный отдел", open=True)
#tree.insert("", END, iid=2, text="IT-отдел")
#tree.insert("", END, iid=3, text="Отдел продаж")
#
## добавляем сотрудников отдела
#tree.insert("1", index=END, text="Tom")
#tree.insert("2", index=END, text="Bob")
#tree.insert("2", index=END, text="Sam")
#
#root.mainloop()
"""
    При добавлении каждого сотрудника указываем в качестве первого параметра
идентификатор элемента-отдела
    tree.insert("2", index=END, text="Bob")

    Также устанавливаем текстовую метку элемента - параметр text - он представляет
имя условного сотрудника
    По умолчанию все элементы, которые содержат вложенные подэлементы, закрыты.
Чтобы их открыть по умолчанию, у элемента для параметра open передается
значение True (по умолчанию равно False):
    tree.insert("", END, iid=1, text="Административный отдел", open=True)
    
    Установка заголовка
    
    Если в Treeview параметр show имеет значение "tree headings" (это значение по
умолчанию), то мы можем также установить заголовок:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#tree = ttk.Treeview()
## установка заголовка
#tree.heading("#0", text="Отделы", anchor=NW)
#tree.pack(expand=1, fill=BOTH)
#
#tree.insert("", END, iid=1, text="Административный отдел", open=True)
#tree.insert("", END, iid=2, text="IT-отдел")
#tree.insert("", END, iid=3, text="Отдел продаж")
#
#tree.insert("1", index=END, text="Tom")
#tree.insert("2", index=END, text="Bob")
#tree.insert("2", index=END, text="Sam")
#
#root.mainloop()