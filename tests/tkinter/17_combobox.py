#from cProfile import label
#from cgitb import text
from tkinter import *
from tkinter import ttk

"""
Combobox
"""
"""
Виджет Combobox представляет выпадающий список, из которого пользователь
может выбрать один элемент. Фактически он представляет комбинацию виджетов
Entry и Listbox
"""
"""
Основные параметры конструктора Combobox:
"""
# values: список строк для отображения в Combobox
# background: фоновый цвет
# cursor: курсор указателя мыши при наведении на текстовое поле
# foreground: цвет текста
# font: шрифт текста
# justify: устанавливает выравнивание текста. Значение LEFT выравнивает текст по левому краю, CENTER - по центру, RIGHT - по правому краю
# show: создает маску для вводимых символов
# state: состояние элемента, может принимать значения NORMAL (по умолчанию) и DISABLED
# textvariable: устанавливает привязку к элементу StringVar
# height: высота элемента
# width: ширина элемента
"""
Определим простейший выпадающий список:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#languages = ["Python", "C#", "Java", "JavaScript"]
#combobox = ttk.Combobox(values=languages)
#combobox.pack(anchor=NW, padx=6, pady=6)
#
#root.mainloop()
"""
Здесь для элемента combobox в качестве источника значений устанавливается
список languages:
"""
"""
С помощью параметра textvariable мы можем установить привязку к выбранному
в Combobox значению:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#languages = ["Python", "C#", "Java", "JavaScript"]
## по умолчанию будет выбран первый элемент из languages
#languages_var = StringVar(value=languages[0])
#
#label = ttk.Label(textvariable=languages_var)
#label.pack(anchor=NW, padx=6, pady=6)
#
#combobox = ttk.Combobox(textvariable=languages_var, values=languages)
#combobox.pack(anchor=NW, padx=6, pady=6)
#
#print(combobox.get())
#root.mainloop()
"""
Здесь выбранный в Combobox элемент привязан к переменной languages_var. По
умолчанию выбран первый элемент списка languages. Для отслеживания изменения
выбора определена метка Label, которая отображает выбранный элемент:
"""
"""
По умолчанию мы можем ввести в текстовое поле в Combobox любое значение,
даже то, которого нет в списке. Такое поведение не всегда может быть удобно. В
этом случае мы можем установить для виджета состояние только для чтения,
передав параметру "state" значение "readonly":
"""
#combobox = ttk.Combobox(textvariable=languages_var, values=languages, state="readonly")
"""
Выбранный элемент можно получить с помощью метода get() класса Combobox
"""
#selection = combobox.get()
"""
Либо с помощью метода get() привязанной переменной
"""
#selection = languages_var.get()
"""
Для установки нового значения можно использовать метод set():
"""
#languages_var.set(new_value)
#combobox.set(new_value)
"""
Для установки по идексу из привязанного набора значений также можно
использовать метод current(newindex), где с помощью параметра newindex
задается индекс выбранного значения. Например, выберем второй элемент:
"""
#combobox.current(1)
