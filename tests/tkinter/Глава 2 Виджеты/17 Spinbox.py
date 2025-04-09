from tkinter import *
from tkinter import ttk

"""
Spinbox
"""

"""
Виджет Spinbox позволяет выбрать значение (чаще число) из некоторого списка.
"""
"""
Основные параметры Spinbox:
"""
# values: набор значений виджета в виде списка или кортежа
# from_: минимальное значение (тип float)
# to: максимальное значение (тип float)
# increment: приращение значения (тип float)
# textvariable: определяет переменную StringVar, которая хранит текущее значение виджета
# command: указывает на функцию, которая вызывается при изменении значения виджета
# wrap: при значении True создает зацикленный список, при котором после минимального значения идет максимальное
# background: фоновый цвет
# foreground: цвет текста
# font: шрифт текста
# justify: выравнивание текста, принимает значение "left" (по левому краю), "right" (по правому краю) и "center" (по центру)
# width: ширина виджета
# state: состояние виджета
"""
Простейший Spinbox:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#spinbox = ttk.Spinbox(from_=1.0, to=100.0)
#spinbox.pack(anchor=NW)
#
#root.mainloop()
"""
В данном случае мы можем выбрать одно из чисел от 1 до 100. При нажатии на
стрелочки вверх и вниз на виджете значение виджета будет увеличиваться и
уменьшаться на единицу:
"""
"""
По умолчанию приращение идет на единицу, но с помощью параметра increment
можно установить другое значение, например, приращение на 2:
"""
#ttk.Spinbox(from_=1.0, to=100.0, increment=2)
"""
Также по умолчанию мы можем, не используя стрелочки, ввести в текстовое поле
виджета какое-либо значение, даже то, которое не входит в диапазон значений. Если
нам надо запретить ввод значений в текстовое поле и оставить доступными для
выбора значений только стрелочки, то для этого можно установить для параметра
state значение readonly:
"""
#spinbox = ttk.Spinbox(from_=1.0, to=100.0, state="readonly")
"""
С помощью параметра textvariable можно привязать значение Spinbox к
переменной StringVar:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x150")
#
#spinbox_var = StringVar(value=22)   # начальное значение 22
#
#label = ttk.Label(textvariable=spinbox_var)
#label.pack(anchor=NW)
#
#spinbox = ttk.Spinbox(from_=1.0, to=100.0, textvariable=spinbox_var)
#spinbox.pack(anchor=NW)
#
#root.mainloop()
"""
Здесь для наглядности добавлена метка, которая выводит выбранное значение. В
качестве начального значения применяется число 22
"""
"""
Получение текущего значения
"""
"""
Для получения текущего значения у Spinbox вызывается метод get()
"""
#current_value = spinbox.get()
"""
Обработка изменения значения
"""
"""
Чтобы обработать изменение значения нужно определить функцию, которая будет
срабатывать при изменении значения, и передать ее параметру command:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#def change():
#    label["text"] = spinbox.get()
#
#label = ttk.Label()
#label.pack(anchor=NW)
#
#spinbox = ttk.Spinbox(from_=1.0, to=100.0, command=change)
#spinbox.pack(anchor=NW)
#
#root.mainloop()
"""
В данном случае при изменении значения срабатывает функция change в которой
изменяем текст метки label в соответствии с новым значением
"""
"""
Установка набора значений
"""
"""
Данный виджет необязательно должен представлять список из числовых значений. В
реальности это может быть любой набор значений в виде списка или кортежа,
который можно установить с помощью параметра values:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x150")
#
#spinbox_var = StringVar()
#
#languages=["Python", "JavaScript", "C#", "Java", "C++"]
#
#label = ttk.Label(textvariable=spinbox_var)
#label.pack(anchor=NW)
#
#spinbox = ttk.Spinbox(textvariable=spinbox_var, values=languages)
#spinbox.pack(anchor=NW)
#
#root.mainloop()
"""
В данном случае Spinbox позволяет выбрать одно из значений списка languages
"""
