"""

    Установка цвета


"""
"""
    Ряд виджетов в Tkinter поддерживают установку цвета для различных аспектов.
Например, у виджета Label можно установить параметры foreground и
background, которые отвечают за цвет текста и фона соответственно. У некоторых
виджетов настройки цвета спрятаны в параметре style.
    Цвет можно установить разными способами:
    * Именованные цвета, например, "red", который соответствует красному цвету.
    В зависимости от платформы набор доступных именованных цветов может
    отличаться. Все доступные именованные цвета можно посмотреть в
    документации. Например:
"""
#from tkinter import *
#from tkinter import ttk
#
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#ttk.Label(text="Hello World", foreground="red").pack(anchor=NW)
#
#root.mainloop()
"""
    * Можно использовать шестнадцатиричный код RGB в формате #RRGGBB:
"""
#from tkinter import *
#from tkinter import ttk
#
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#label = ttk.Label(text="Hello World",
#                  padding=8,
#                  foreground="#01579B",
#                  background="#B3E5FC")
#label.pack(anchor=CENTER, expand=True)
#
#root.mainloop()
"""
    Если нам даны отдельные коды RGB составляющих, то их можно сконвертировать в
шестнадцатиричный код цвета:
"""
