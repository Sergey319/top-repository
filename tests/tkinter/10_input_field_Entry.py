import re
from tkinter import *
from tkinter import ttk
"""Элемент Entry представляет поле для ввода текста. С помощью конструктора Entry можно установить ряд параметров, основные из них:"""
#background: фоновый цвет
#cursor: курсор указателя мыши при наведении на текстовое поле
#foreground: цвет текста
#font: шрифт текста
#justify: устанавливает выравнивание текста. Значение LEFT выравнивает текст по левому краю, CENTER - по центру, RIGHT - по правому краю
#show: задает маску для вводимых символов
#state: состояние элемента, может принимать значения NORMAL (по умолчанию) и DISABLED
#textvariable: устанавливает привязку к элементу StringVar
#width: ширина элемента
"""Элемент Entry имеет ряд методов. Основные из них:"""
#insert(index, str): вставляет в текстовое поле строку по определенному индексу
#get(): возвращает введенный в текстовое поле текст
#delete(first, last=None): удаляет символ по индексу first. Если указан параметр last, то удаление производится до индекса last. Чтобы удалить до конца, в качестве второго параметра можно использовать значение END.
#focus(): установить фокус на текстовое поле
"""Простейшее текстовое поле:"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#ttk.Entry().pack(anchor=NW, padx=8, pady=8)
#
#root.mainloop()
"""Получение введенного текста"""
"""Для получения текста из Entry, можно использовать его метод get(). Так, определим элемент Entry и по нажатию на кнопку выведем введенный текст на текстовую метку:"""
#
#
#def show_message():
#    label["text"] = entry.get()  # получаем введенный текст
#
#
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#entry = ttk.Entry()
#entry.pack(anchor=NW, padx=6, pady=6)
#
#btn = ttk.Button(text="Click", command=show_message)
#btn.pack(anchor=NW, padx=6, pady=6)
#
#label = ttk.Label()
#label.pack(anchor=NW, padx=6, pady=6)
#
#root.mainloop()
"""Вставка и удаление текста"""
"""Рассмотрим вставку и удаление текста в Entry:"""
#
#
#def clear():
#    entry.delete(0, END)  # удаление введенного текста
#
#
#def display():
#    label[
#        "text"] = entry.get()  # получение введенного текста
#
#
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x150")
#
#label = ttk.Label()
#label.pack(anchor=NW, padx=6, pady=6)
#
#entry = ttk.Entry()
#entry.pack(anchor=NW, padx=6, pady=6)
#
## вставка начальных данных
#entry.insert(0, "Hello World")
#
#display_button = ttk.Button(text="Display", command=display)
#display_button.pack(side=LEFT, anchor=N, padx=6, pady=6)
#
#clear_button = ttk.Button(text="Clear", command=clear)
#clear_button.pack(side=LEFT, anchor=N, padx=6, pady=6)
#
#root.mainloop()
"""При запуске программы в текстовое поле сразу же добавляется текст по умолчанию:"""
#entry.insert(0, "Hello World")
"""Кнопка Clear очищает оба поля, вызывая метод delete:"""
#def clear():
#    entry.delete(0, END)
"""Вторая кнопка, используя метод get, получает введенный текст:"""
#def display():
#    label["text"] = entry.get()
"""Валидация"""
"""С помощью параметра validate конструктора Entry можно задать, когда проводить валидацию введенного значения. Этот параметр может принимать следующие значения:"""
#none: отсутствие валидации, значение по умолчанию
#focus: валидация при получении фокуса
#focusin: валидация при изменении фокуса
#focusout: валидация при потере фокуса
#key: валидация при каждом вводе нового символа
#all: валидация при изменении фокуса и вводе символов в поле
"""Параметр validatecommand позволяет установить команду валидации."""
"""Рассмотрим небольшой пример. Допустим, пользователь должен ввести номер телефона в формате +xxxxxxxxxxx. То есть сначала должен идти знак +, а затем 11 цифр, например, +12345678901:"""
#
#def is_valid(newval):
#    return re.match("^\+\d{0,11}$", newval) is not None
#
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#check = (root.register(is_valid), "%P")
#
#phone_entry = ttk.Entry(validate="key",
#                        validatecommand=check)
#phone_entry.pack(padx=5, pady=5, anchor=NW)
#
#root.mainloop()
"""Итак, параметр validate="key" указывает, что мы будем валидировать ввод при каждом нажатии на клавиатуру. Параметр validatecommand=check говорит, что валидировать ввод будет команда "check". Эта команда представляет кортеж из двух элементов:"""
#check = (root.register(is_valid), "%P")
"""Первый элемент - вызов метода root.register(is_valid) регистрирует функцию, которая собственно будет производить валидацию - это функция is_valid(). Второй элемент - подстановка "%P" представляет новое значение, которое передается в функцию валидации."""
"""Собственно саму валидацию выполняет функция is_valid(). Она принимает один параметр - текущее значение Entry, которое надо валидировать. Она возвращает True, если значение прошло валидацию, и False, если не прошло. Сама логика валидации представляет проверку строки на регулярное выражение "^\+\d*$". Если новое значение соответствует этому выражению, и в нем не больше 12 символов, то оно прошло валидацию."""
"""В итоге мы сможем ввести в текстовое поле только символ + и затем только 11 цифр."""
"""Теперь немного изменим код и добавим вывод ошибок валидации:"""
#
#def is_valid(newval):
#    result = re.match("^\+{0,1}\d{0,11}$",
#                      newval) is not None
#    if not result and len(newval) <= 12:
#        errmsg.set(
#            "Номер телефона должен быть в формате +xxxxxxxxxxx, где x представляет цифру")
#    else:
#        errmsg.set("")
#    return result
#
#
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#check = (root.register(is_valid), "%P")
#
#errmsg = StringVar()
#
#phone_entry = ttk.Entry(validate="key",
#                        validatecommand=check)
#phone_entry.pack(padx=5, pady=5, anchor=NW)
#
#error_label = ttk.Label(foreground="red",
#                        textvariable=errmsg, wraplength=250)
#error_label.pack(padx=5, pady=5, anchor=NW)
#
#root.mainloop()
"""Здесь для вывода ошибок валидации добавлен виджет Label. Если введенное значение не соответствует регулярному выражению (например, пользователь попытался ввести нецифровой символ), и длина ввода меньше и равно 12 символов (проверять ввод больше 12 символов нет смысла, так как номер телефона содержит только 12 символов), то в метке выводим сообщение об ошибке"""
"""Также мы можем передать значение параметра validate, чтобы в функции валидации в зависимости от того, нажал пользователь на клавишу или убрал фокус с поля, производить те или иные действия. В этом случае необходимо передать команде валидации дополнительный аргумент:"""
#check = (root.register(is_valid), "%P", "%V")
"""Здесь значение "%V" представляет событие, которое вызывает валидацию (focus/focusin/focusout/key). Тогда в функции валидации с помощью второго параметра мы сможем получить это значение:"""
#def is_valid(newval, op):
#    result=  re.match("^\+\d{0,11}$", newval) is not None
#    if op=="key":
#        # некоторые действия
#    elif op=="focus":
#        # некоторые действия
#    return result