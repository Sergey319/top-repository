from tkinter import *
from tkinter import ttk
"""Метод grid() позволяет поместить виджет в определенную ячейку условной сетки или грида."""
"""Метод grid применяет следующие параметры:"""
#column: номер столбца, отсчет начинается с нуля
#row: номер строки, отсчет начинается с нуля
#columnspan: сколько столбцов должен занимать элемент
#rowspan: сколько строк должен занимать элемент
#ipadx и ipady: отступы по горизонтали и вертикали соответственно от границ элемента до его содержимого
#padx и pady: отступы по горизонтали и вертикали соответственно от границ ячейки грида до границ элемента
#sticky: выравнивание элемента в ячейке, если ячейка больше элемента. Может принимать значения n, e, s, w, ne, nw, se, sw, которые указывают соответствующее направление выравнивания
"""Установка ячейки виджета"""
"""Например, определим грид из 9 кнопок:"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#for r in range(3):
#    for c in range(3):
#        btn = ttk.Button(text=f"({r},{c})")
#        btn.grid(row=r, column=c)
#
#root.mainloop()
"""Здесь в цикле создается девять кнопок, каждая из которых помещается в свою ячейку."""
"""По умолчанию для каждой ячейки выделяется столько места, сколько необходимо для виджета в ней. Соответственно мы получаем небольшую таблицу и много пустого места вне грида, что, возможно, смотрится не лучшим образом. И ситуация усугубляется, если мы попробуем растянуть окно - появится еще больше пустого пространства. Чтобы решить эту проблему, надо сконфигурировать грид у контейнера."""
"""Конфигурация грида"""
"""Для конфигурации грида в контейнере применяются два метода:"""
#container.columnconfigure(index, weight)
#container.rowconfigure(index, weight)
"""Метод columnconfigure() настраивает столбец. В качестве параметра index метод получает индекс столбца, а через параметр weight устанавливает его вес. Столбцы распределяются по всей ширине контейнера в соответствии со своим весом."""
"""Метод rowconfigure() настраивает строку аналогичным образом. В качестве параметра index метод получает индекс строки, а через параметр weight устанавливает ее вес. Строки распределяются по всей длине контейнера в соответствии со своим весом."""
"""Например, изменим код выше, добавив конфигурацию строк и столбцов:"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#for c in range(3): root.columnconfigure(index=c, weight=1)
#for r in range(3): root.rowconfigure(index=r, weight=1)
#
#for r in range(3):
#    for c in range(3):
#        btn = ttk.Button(text=f"({r},{c})")
#        btn.grid(row=r, column=c)
#
#root.mainloop()
"""Поскольку у нас три строки, для упрощения в цикле для каждой строки устанавливаем вес 1. То есть в итоге каждая из трех строк будет занимать треть высоты контейнера (пространство_контейнера / сумму всех весов строк)."""
"""Аналогично в цикле для каждого столбца устанавливаем вес 1. То есть в итоге каждый из трех столбец будет занимать треть ширины контейнера."""
"""Отступы"""
"""Параметры padx и pady повзвозяют установить отступы по горизонтали и вертикали соответственно от границ ячейки грида до границ виджета, а ipadx и ipady - отступы по горизонтали и вертикали соответственно от границ виджета до его содержимого"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#for c in range(3): root.columnconfigure(index=c, weight=1)
#for r in range(3): root.rowconfigure(index=r, weight=1)
#
#for r in range(3):
#    for c in range(3):
#        btn = ttk.Button(text=f"({r},{c})")
#        btn.grid(row=r, column=c, ipadx=6, ipady=6, padx=4,
#                 pady=4)
#
#root.mainloop()
"""В данном случае внешние отсуты равны 4 единиц, а внутренние - 6 единицам."""
"""Для параметров padx и pady можно установить отступы с двух сторон в виде списка:"""
#btn.grid(row=r, column=c, ipadx=6, ipady=6, padx=[15, 4], pady=4)
"""Здесь внешний отступ слева равен 10, а справа - 4 единицам."""
"""Объединение ячеек"""
"""Параметр columnspan указывает, столько столбцов, а параметр rowspan сколько строк должен занимать виджет. То есть с помощью подобных параметров мы можем объединить ячейки."""
"""Растяжение на два столбца:"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#for c in range(2): root.columnconfigure(index=c, weight=1)
#for r in range(2): root.rowconfigure(index=r, weight=1)
#
#btn1 = ttk.Button(text="button 1")
## columnspan=2 - растягиваем на два столбца
#btn1.grid(row=0, column=0, columnspan=2, ipadx=70, ipady=6,
#          padx=5, pady=5)
#
#btn3 = ttk.Button(text="button 3")
#btn3.grid(row=1, column=0, ipadx=6, ipady=6, padx=5, pady=5)
#
#btn4 = ttk.Button(text="button 4")
#btn4.grid(row=1, column=1, ipadx=6, ipady=6, padx=5, pady=5)
#
#root.mainloop()
"""Растяжение на две строки:"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#for c in range(2): root.columnconfigure(index=c, weight=1)
#for r in range(2): root.rowconfigure(index=r, weight=1)
#
#btn2 = ttk.Button(text="button 2")
## rowspan=2 - растягиваем на две строки
#btn2.grid(row=0, column=1, rowspan=2, ipadx=6, ipady=55,
#          padx=5, pady=5)
#
#btn1 = ttk.Button(text="button 1")
#btn1.grid(row=0, column=0, ipadx=6, ipady=6, padx=5, pady=5)
#
#btn3 = ttk.Button(text="button 3")
#btn3.grid(row=1, column=0, ipadx=6, ipady=6, padx=5, pady=5)
#
#root.mainloop()
"""Выравнивание"""
"""Параметр sticky задает выравнивание виджета в ячейке, если размер ячейки больше размера этого виджета. Этот параметр может принимать следующие значения:"""
#n: положение вверху по центру
#e: положение в правой части контейнера по центру
#s: положение внизу по центру
#w: положение в левой части контейнера по центру
#nw: положение в верхнем левом углу
#ne: положение в верхнем правом углу
#se: положение в нижнем правом углу
#sw: положение в нижнем левом углу
#ns: растяжение по вертикали
#ew: растяжение по горизонтали
#nsew: растяжение по горизонтали и вертикали
"""По умолчанию виджет позиционируется по центру ячейки"""
"""Например, растянем виджет по всему пространству ячейки (значение NSEW):"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#for c in range(3): root.columnconfigure(index=c, weight=1)
#for r in range(3): root.rowconfigure(index=r, weight=1)
#
#for r in range(3):
#    for c in range(3):
#        btn = ttk.Button(text=f"({r},{c})")
#        btn.grid(row=r, column=c, ipadx=6, ipady=6, padx=4,
#                 pady=4, sticky=NSEW)
#
#root.mainloop()