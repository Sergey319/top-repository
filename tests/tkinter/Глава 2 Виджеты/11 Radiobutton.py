from tkinter import *
from tkinter import ttk
from itertools import chain

"""Виджет Radiobutton представляет переключатель, который может находиться в двух состояниях: отмеченном или неотмеченном. Но в отличие от Checkbutton переключатели могут создавать группу, из которой одномоментно мы можем выбрать только один переключатель."""
"""Среди параметров конструктора Radiobutton стоит выделить следующие:"""
#command: ссылка на функцию, которая вызывается при нажатии на переключатель
#cursor: курсор при наведении на виджет
#image: графическое изображение, отображаемое виджетом
#padding: отступы от содержимого до границы переключателя
#state: состояние виджета, может принимать значения NORMAL (по умолчанию), DISABLED и ACTIVE
#text: текст виджета
#textvariable: устанавливает привязку к переменной StringVar, которая задает текст переключателя
#underline: индекс подчеркнутого символа в тексте виджета
#variable: ссылка на переменную, как правило, типа IntVar, которая хранит состояние переключателя
#value: значение переключателя
#width: ширина виджета
"""Определим группу переключателей:"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#position = {"padx": 6, "pady": 6, "anchor": NW}
#
#python = "Python"
#java = "Java"
#javascript = "JavaScript"
#
#lang = StringVar(
#    value=java)  # по умолчанию будет выбран элемент с value=java
#
#header = ttk.Label(textvariable=lang)
#header.pack(**position)
#
#python_btn = ttk.Radiobutton(text=python, value=python,
#                             variable=lang)
#python_btn.pack(**position)
#
#javascript_btn = ttk.Radiobutton(text=javascript,
#                                 value=javascript,
#                                 variable=lang)
#javascript_btn.pack(**position)
#
#java_btn = ttk.Radiobutton(text=java, value=java,
#                           variable=lang)
#java_btn.pack(**position)
#
#root.mainloop()
"""Здесь определено три переключателя. Все они привязаны к одной переменной lang, которая представляет тип StringVar. При этом они имеют разные значения, устанавливаемые через параметр value. Начальное значение переменной lang ("java") соответствует значению value последнего переключателя, поэтому по умолчанию будет выбран последний переключатель.А при выборе одного переключателя, другой автоматически перейдет в неотмеченное состояние."""
"""Для вывода выделенного значения над переключателями определена текстовая метка, которая отображает значение переменной lang:"""
"""В примере выше отображаемый текст (параметр text) и значение (параметр value) совпадают, но это необязательно"""
"""Обработка выбора пользователя"""
"""Параметр command позволяет установить функцию, которая обрабатывает выбор переключателя. Например:"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#position = {"padx": 6, "pady": 6, "anchor": NW}
#languages = ["Python", "JavaScript", "Java", "C#"]
#selected_language = StringVar()  # по умолчанию ничего не выбрано
#
#header = ttk.Label(text="Выберите язык")
#header.pack(**position)
#
#
#def select():
#    header.config(text=f"Выбран {selected_language.get()}")
#
#
#for lang in languages:
#    lang_btn = ttk.Radiobutton(text=lang, value=lang,
#                               variable=selected_language,
#                               command=select)
#    lang_btn.pack(**position)
#
#root.mainloop()
"""Здесь для упрощения данные переключателей определены в виде списка languages. В цикле for пробегаемся по всем элементам списка и создаем переключатель. При нажатии на каждый переключатель будет срабатывать функция select(), которая установит для метки header соответствующий текст:"""
"""Установка изображения"""
"""Для установки изображения применяется параметр image:"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#position = {"padx": 6, "pady": 6, "anchor": NW}
#
#python = "Python"
#java = "Java"
#csharp = "C#"
#
#lang = StringVar(
#    value=java)  # по умолчанию будет выбран элемент с value=java
#
#header = ttk.Label(textvariable=lang)
#header.pack(**position)
#
#python_img = PhotoImage(file="./python_sm.png")
#csharp_img = PhotoImage(file="./csharp_sm.png")
#java_img = PhotoImage(file="./java_sm.png")
#
#python_btn = ttk.Radiobutton(value=python, variable=lang,
#                             image=python_img)
#python_btn.pack(**position)
#
#csharp_btn = ttk.Radiobutton(value=csharp, variable=lang,
#                             image=csharp_img)
#csharp_btn.pack(**position)
#
#java_btn = ttk.Radiobutton(value=java, variable=lang,
#                           image=java_img)
#java_btn.pack(**position)
#
#root.mainloop()
"""Параметру image передается объект PhotoImage, в конструкторе которого через параметр file устанавливается путь к изображению. Здесь предполагается, что в одной папке с файлом приложения находятся файлы изображений "python_sm.png", "csharp_sm.png" и "java_sm.png"."""
"""Если необходимо также отображать и текст, то для этого можно установить параметр compound, который определяет положение текста по отношению к изображению с помощью одного из следующих значений:"""
#top: изображение поверх текста
#bottom: изображение под текстом
#left: изображение слева от текста
#right: изображение справа от текста
#none: при наличии изображения отображается только изображение
#text: отображается только текст
#image: отображается только изображение
"""Например, отобразим картинку поверх текста:"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#position = {"padx": 6, "pady": 6, "anchor": NW}
#
#languages = [
#    {"name": "Python",
#     "img": PhotoImage(file="./python_sm.png")},
#    {"name": "C#",
#     "img": PhotoImage(file="./csharp_sm.png")},
#    {"name": "Java",
#     "img": PhotoImage(file="./java_sm.png")}
#]
#
#lang = StringVar(value=languages[0][
#    "name"])  # по умолчанию будет выбран элемент с value=python
#
#header = ttk.Label(textvariable=lang)
#header.pack(**position)
#
#for l in languages:
#    btn = ttk.Radiobutton(value=l["name"], text=l["name"],
#                          variable=lang, image=l["img"],
#                          compound="top")
#    btn.pack(**position)
#
#root.mainloop()