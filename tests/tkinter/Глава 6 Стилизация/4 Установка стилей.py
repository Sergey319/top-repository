"""

    Установка стилей


"""
"""
    Стиль описывает внешний вид виджета. За установку стиля в виджетах отвечает
параметр style. Встроенные виджеты по умолчанию применяют некоторые
встроенные стили. В частности, все кнопки применяют стиль TButton, который
описывает, как выглядят кнопки. Каждый стиль имеет имя. При создании,
изменении или применении стиля к виджетам, необходимо знать его имя.
    Чтобы узнать стиль определенного виджета, можно обратиться к его
параметру style:
"""
#from tkinter import *
#from tkinter import ttk
#
#root = Tk()
#
#label = ttk.Label(text="Hello World")
#label.pack(anchor=CENTER, expand=1)
#print(f"<<{label["style"]}>>")
"""
    Если возвращается пустая строка, то значит, что к виджету применяется стиль по
умолчанию. В этом случае название стиля можно получить с помощью метода
winfo_class():
"""
#from tkinter import *
#from tkinter import ttk
#
#root = Tk()
#
#label = ttk.Label(text="Hello World")
#print(label.winfo_class())
"""
    Как правило, встроенные стили называются по имени класса виджета и
предваряются буквой T. Например, для виджета Label - стиль TLabel, для Button - 
TButton.

    Определение и применение стилей
    
    Стиль в Tkinter представляет объект Style. У данного объекта есть метод configure(),
который позволяет настроить стиль
"""
#from tkinter import *
#from tkinter import ttk
#
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#label_style = ttk.Style()
#label_style.configure("My.TLabel",  # имя стиля
#                      font="helvetica 14",  # шрифт
#                      foreground="#004D40",  # цвет текста
#                      padding=10,  # отступы
#                      background="#B2DFDB")  # фоновый цвет
#
#label = ttk.Label(text="Hello World", style="My.TLabel")
#label.pack(anchor=CENTER, expand=1)
#
#root.mainloop()
"""
    Здесь создается стиль в виде объекта label_style. В методе configure() первым
параметром передается имя стиля - в данном случае "My.TLabel". Все остальные
параметры настраивают различные аспекты стиля, так здесь устанавливается
шрифт, цвет фона и текста и отступы.
"""