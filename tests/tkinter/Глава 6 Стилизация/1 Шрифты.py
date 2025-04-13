"""

    Шрифты


"""
"""
    Имена шрифтов
    
    Ряд виджетов, например, Label или Text, поддерживают установку шрифта через
параметр font. Каждая платформа может определять свои специфические шрифты.
Но также библиотека Tk по умолчанию включает ряд именованных шрифтов,
которые могут использоваться на различных компонентах графического
интерфейса и которые доступны на всех платформах:
    * TkDefaultFont: шрифт по умолчанию, который применяется, если для виджета
    явным образом не определен шрифт
    * TkTextFont: шрифт по умолчанию, который применяется для виджетов Entry,
    Listbox и ряда других
    * TkFixedFont: шрифт с фиксированной шириной
    * TkMenuFont: шрифт для пунктов меню
    * TkHeadingFont: шрифт для заголовков в Listbox и в таблицах
    * TkCaptionFont: шрифт для строки статуса в окнах
    * TkSmallCaptionFont: шрифт малого размера для диалоговых окон
    * TkIconFont: шрифт для подписей к иконкам
    * TkTooltipFont: шрифт для всплывающих окон
    В принципе мы можем использовать эти шрифты не только в любых виджетах:
    ttk.Label(text="Hello World", font="TkTextFont")
    Tk также предоставляет дополнительный набор именованных шрифтов, которые
определены только на определенных платформах. Для их получения можно
использовать функцию name() из пакета tkinter.font:
"""
#from tkinter import *
#from tkinter import font
#
#root = Tk()
#
#for font_name in font.names():
#    print(font_name)
"""
    Например, на Windows мы получим следующий набор:
    fixed
    oemfixed
    TkDefaultFont
    TkMenuFont
    ansifixed
    systemfixed
    TkHeadingFont
    device
    TkTooltipFont
    defaultgui
    TkTextFont
    ansi
    TkCaptionFont
    system
    TkSmallCaptionFont
    TkFixedFont
    TkIconFont
    В данном случае выводится и платформа-независимые, и платформа-специальные
шрифты, например, "system".
"""
#from tkinter import *
#from tkinter import ttk
#
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#label = ttk.Label(text="Hello World", font="system")
#label.pack(anchor=NW, expand=1)
#
#root.mainloop()
"""
    Определение шрифта
    
    За определение шрифта в Tkinter отвечает класс Font из модуля tkinter.font. Он
принимает следующие параметры:
    * name: имя шрифта
    * family: семейство шрифтов
    * size: высота шрифта (в точках при положительном значении или в пикселях
    при негативном значении)
    * weight: вес шрифта. Принимает значение normal (обычный) или bold
    (жирный)
    * slant: наклон. Принимает значение roman (обычный) или italic (наклонный)
    * underline: подчеркивание. Принимает значение True (с подчеркиванием)
    или False (без подчеркивания)
    * overstrike: зачеркивание. Принимает значения True с зачеркиванием) или False (без зачеркивания)
    Для получения всех доступных семейств шрифтов на текущей платформе можно
использовать функцию families() из модуля tkinter.font
"""
#from tkinter import *
#from tkinter import font
#
#root = Tk()
#
#for family in font.families():
#    print(family)
"""
    Пример применения шрифтов:
"""
#from tkinter import *
#from tkinter import ttk
#from tkinter import font
#
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#font1 = font.Font(family="Arial", size=11, weight="normal", slant="roman", underline=True, overstrike=True)
#label1 = ttk.Label(text="Hello World", font=font1)
#label1.pack(anchor=NW)
#
#font2 = font.Font(family="Verdana", size=11, weight="normal", slant="roman")
#label2 = ttk.Label(text="Hello World", font=font2)
#label2.pack(anchor=NW)
#
#root.mainloop()
"""
    Также можно использовать определение шрифта в виде строки:
"""
#from tkinter import *
#from tkinter import ttk
#
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#label1 = ttk.Label(text="Hello World", font="Arial 11 normal roman")
#label1.pack(anchor=NW)
#
#label2 = ttk.Label(text="Hello World", font="Verdana 11 normal roman")
#label2.pack(anchor=NW)
#
#root.mainloop()
"""
    Например, в определении "Arial 11 normal roman", применяется семейство
шрифта Arial, высота 11 единиц, нежирный шрифт без наклона.
"""