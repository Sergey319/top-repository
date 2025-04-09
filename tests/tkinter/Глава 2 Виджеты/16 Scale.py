from tkinter import *
from tkinter import ttk

"""
Scale
"""

"""
Scale представляет ползунок со шкалой, на которой можно выбрать одно из
числовых значений.
"""
"""
Среди параметров Scale следует отметить следующее:
"""
# orient: направление виджета. Может принимать значения HORIZONTAL/"horizontal" и VERTICAL/"vertical"
# from_: начальное значение шкалы виджета, представляет тип float
# to: конечное значение шкалы виджета, представляет тип float
# length: длина виджета
# command: функция, которая выполняется при изменении текущего значения
# value: текущее значение шкалы виджета, представляет тип float
# variable: переменная IntVar или DoubleVar, к которой привязано текущее значение виджета
"""
Простейший Scale в горизонтальной и вертикальной ориентации:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x250")
#
#verticalScale = ttk.Scale(orient=VERTICAL, length=200, from_=1.0, to=100.0, value=50)
#verticalScale.pack()
#
#horizontalScale = ttk.Scale(orient=HORIZONTAL, length=200, from_=1.0, to=100.0, value=30)
#horizontalScale.pack()
#
#root.mainloop()
"""
Привязка к переменной
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#val = IntVar(value=10)
#
#ttk.Label(textvariable=val).pack(anchor=NW)
#
#horizontalScale = ttk.Scale(orient=HORIZONTAL, length=200, from_=1.0, to=100.0, variable=val)
#horizontalScale.pack(anchor=NW)
#
#root.mainloop()
"""
В данном случае и метка Label, и виджет Scale привязаны к переменной val:
"""
"""
Обработка изменения значения
"""
"""
Параметр command позволяет установить функцию, которая будет выполняться при
изменении текущего значения Scale. В качестве параметра в эту функцию передается новое значение:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#def change(newVal):
#    label["text"] = newVal
#    # или так
#    # label["text"] = scale.get()
#
#label = ttk.Label()
#label.pack(anchor=NW)
#
#scale = ttk.Scale(orient=HORIZONTAL, length=200, from_=1.0, to=100.0, command=change)
#scale.pack(anchor=NW)
#
#root.mainloop()
"""
В данном случае новое значение Scale передается в метку label:
"""
"""
Для получения текущего значения Scale можно использовать его метод get():
"""
# label["text"] = scale.get()
"""
Стоит учитывать, что передаваемое в функцию значение newVal представляет строку,
а точнее значение типа float в строковом виде. Но что делать, если мы хотим
выводить в метке label не строку или даже float, а целое число? В этом случае
необходимо выполнить цепь преобразований:
"""
#def change(newVal):
#    float_value = float(newVal)     # получаем из строки значение float
#    int_value = round(float_value)  # округляем до целочисленного значения
#    label["text"] = int_value
