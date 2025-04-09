from tkinter import *
from tkinter import ttk

"""Одной из примечательных особенностей Tkinter является то, что он позволяет привязать к ряду виджетов переменные определенных типов. При изменении значения виджета автоматически будет изменяться и значение привязанной переменной. Для привязки может использоваться переменная следующих типов:"""
#StringVar
#IntVar
#BooleanVar
#DoubleVar
"""Простейший пример:"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x150")
#
#message = StringVar()
#
#label = ttk.Label(textvariable=message)
#label.pack(anchor=NW, padx=6, pady=6)
#
#entry = ttk.Entry(textvariable=message)
#entry.pack(anchor=NW, padx=6, pady=6)
#
#button = ttk.Button(textvariable=message)
#button.pack(side=LEFT, anchor=N, padx=6, pady=6)
#
#root.mainloop()
"""В данном случае определяется переменная message, которая представляет класс StringVar, то есть такая переменная, которая хранит некоторую строку."""
"""С помощью параметра textvariable эта переменная привязана к тексту поля Entry, а также к тексту кнопки и метки:"""
#ttk.Label(textvariable=message)
"""И если мы изменим текст в поле Entry, автоматически синхронно изменится и значение привязанной переменной message. а поскольку к этой переменной также привязаны кнопка и метка, то автоматически также изменится текст метки и кнопки."""
"""Типы имеют параметр value, который позволяет установить значение по умолчанию. Кроме того, они имеют два метода:"""
#get(): возвращает значение
#set(value): устанавливает значение, которое передано через параметр
"""Применим эти методы. Например, мы могли бы установить привязку к переменной IntVar и выводить количество кликов:"""
#
#def click_button():
#    value = clicks.get()  # получаем значение
#    clicks.set(value + 1)  # устанавливаем новое значение
#
#
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x150")
#
#clicks = IntVar(value=0)  # значение по умолчанию
#
#btn = ttk.Button(textvariable=clicks, command=click_button)
#btn.pack(anchor=CENTER, expand=1)
#
#root.mainloop()
"""Отслеживание изменения переменной"""
"""Класс Stringvar позволяет отслеживать чтение и изменение своего значения. Для отслеживания у объекта StringVar вызывается метод trace_add()"""
#trace_add(trace_mode, function)
"""Первый параметр представляет отслеживаемое событие и может принимать следующие значения:"""
#write: изменение значения
#read: чтение значения
#unset: удаление значения
"""Также можно передать список из этих значений, если нам надо отслеживать несколько событий."""
"""Второй параметр представляет функцию, которая будет вызываться при возникновении события из первого параметра. Эта функция должна принимать один параметр."""
"""Посмотрим на примере:"""
#def check(*args):
#    print(name)
#    if name.get() == "admin":
#        result.set("запрещенное имя")
#    else:
#        result.set("норм")
#
#
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#name = StringVar()
#result = StringVar()
#
#name_entry = ttk.Entry(textvariable=name)
#name_entry.pack(padx=5, pady=5, anchor=NW)
#
#check_label = ttk.Label(textvariable=result)
#check_label.pack(padx=5, pady=5, anchor=NW)
#
## отслеживаем изменение значения переменной name
#name.trace_add("write", check)
#
#root.mainloop()
"""В данном случае текстовое поле name_entry привязано к переменной name, а метка check_label - к переменной result."""
"""Здесь мы отлеживаем изменение значения переменной name - при изменении срабатывает функция check, в которой изменяем переменную result в зависимости от значения name. Условимся, что name представляет имя пользователя, но имя "admin" запрещено."""
