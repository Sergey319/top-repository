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
    label_style.configure("My.TLabel",          # имя стиля
                        font="helvetica 14",    # шрифт
                        foreground="#004D40",   # цвет текста
                        padding=10,             # отступы
                        background="#B2DFDB")   # фоновый цвет
    Затем применяем этот стиль, передавая его параметру style:
    label = ttk.Label(text="Hello World", style="My.TLabel")
    
    Имена стилей
    
    Имя создаваемых стилей имеют следующий формат:
    НОВЫЙ_СТИЛЬ.встроенный_стиль
    Например, в примере выше название стиля "My.TLabel" указывает, что фактически
он называется "My" и наследуется от "TLabel". И те параметры, которые не будут
явным образом определены, будут унаследованы от родительского стиля "TLabel"

    Расширение встроенных стилей
    
    Вместо создания новых стилей можно просто изменить отдельные характеристики
уже существующих:
"""
#from tkinter import *
#from tkinter import ttk
#
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#ttk.Style().configure("TLabel", font="helvetica 13", foreground="#004D40", padding=8, background="#B2DFDB")
#
#ttk.Label(text="Hello World!").pack(anchor=NW, padx=6, pady=6)
#ttk.Label(text="Bye World..").pack(anchor=NW, padx=6, pady=6)
#
#root.mainloop()
"""
    В данном случае изменяется встроенный стиль TLabel. Он применяется к меткам по
умолчанию, поэтому данный стиль не надо явным образом устанавливать для
меток.

    Применение стиля ко всем виджетам
    
    Выше стиль применялся к меткам Label, к другим же типам виджетов он не
применялся. Если же мы хотим, чтобы у нас был бы общий стиль для всех типов
виджетов, то в метод configure() в качестве имени стиля передается "."
"""
#from tkinter import *
#from tkinter import ttk
#
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#ttk.Style().configure(".", font="helvetica 13", foreground="#004D40", padding=8, background="#B2DFDB")
#
#ttk.Label(text="Hello World!").pack(anchor=NW, padx=6, pady=6)
#ttk.Button(text="Click").pack(anchor=NW, padx=6, pady=6)
#
#root.mainloop()
"""
    Подобный стиль также не надо явно применять, он применяется автоматически ко
всем виджетам
"""