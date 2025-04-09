from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

"""
Виджет Text
"""

"""
Создание многострочного текстового поля
"""
"""
Text предназначен для отображения и редактирования многострочного текста.
Стоит отметить, что данный виджет доступен только в основном пакете tkinter, в пакете tkinter.ttk аналога нет.
"""
"""
Основные параметры конструктора Text:
* bd/borderwidth: толщина границы
* bg/background: фоновый цвет
* fg/foreground: цвет текста
* font: шрифт текста, например, font="Arial 14" - шрифт Arial высотой 14px,
    или font=("Verbana", 13, "bold") - шрифт Verbana высотой 13px с
    выделением жирным
* height: высота в строках
* padx: отступ от границ кнопки до ее текста справа и слева
* pady: отступ от границ кнопки до ее текста сверху и снизу
* relief: определяет тип границы, может принимать значения SUNKEN, RAISED,
    GROOVE, RIDGE
* state: устанавливает состояние кнопки, может принимать значения DISABLED,
    ACTIVE, NORMAL (по умолчанию)
* width: ширина в символах
* wrap: указывает, каким образом переносить текст, если он не вмещается в
    границы виджета
"""
"""
Простейший Text:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#editor = Text()
#editor.pack(fill=BOTH, expand=1)
#
#root.mainloop()
"""
Перенос текста

Иногда предложения в текстовом поле могут быть очень большими, что могут не
помещаться в отведенное для них пространство виджета. В этом случае большое
значение имеет стратегия переноса, которая устанавливается с помощью параметра
wrap. этот параметр может принимать следующие параметры:
* none: переносы отсутствуют, но можно сделать горизонтальную прокрутку
* char: переносы осуществляются по символам
* word: переносы осуществляются по словам
"""
"""
Сравнение:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#char_editor = Text(height=5, wrap="char")
#char_editor.pack(anchor=N, fill=X)
#
#word_editor = Text(height=5, wrap="word")
#word_editor.pack(anchor=S, fill=X)
#
#root.mainloop()
"""
Прокрутка текста

Используя Scrollbar, можно добавить в Text прокрутку текста:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#root.grid_columnconfigure(0, weight=1)
#root.grid_rowconfigure(0, weight=1)
#
#editor = Text(wrap="none")
#editor.grid(column=0, row=0, sticky=NSEW)
#
#ys = ttk.Scrollbar(orient="vertical", command=editor.yview)
#ys.grid(column=1, row=0, sticky=NS)
#xs = ttk.Scrollbar(orient="horizontal", command=editor.xview)
#xs.grid(column=0, row=1, sticky=EW)
#
#editor["yscrollcommand"] = ys.set
#editor["xscrollcommand"] = xs.set
#
#root.mainloop()
"""
Здесь для виджета определяются две полосы прокрутки - вертикальная и
горизонтальная, соответственно, для каждой определяется свой элемент Scrollbar.
Один (ys) имеет вертикальную ориентацию, а второй (xs) - горизонтальную. А у Text
устанавливаются команды yscrollcommand и xscrollcommand с помощью
соответствующих скроллбаров.
"""
"""
Стоит отметить, что поскольку создание прокрутки для виджета Text является
довольно распространенной задачей, то в Tkinter также по умолчанию есть аналог
виджета Text с готовой вертикальной прокруткой - ScrolledText (в пакете
tkinter.scrolledtext):
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x150")
#
#st = ScrolledText(root, width=50, height=10)
#st.pack(fill=BOTH, side=LEFT, expand=True)
#
#root.mainloop()
