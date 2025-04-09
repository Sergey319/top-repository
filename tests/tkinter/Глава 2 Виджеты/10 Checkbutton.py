from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

"""Элемент Checkbutton представляет собой флажок, который может находиться в двух состояниях: отмеченном и неотмеченном."""
"""Конструктор Checkbutton принимает ряд параметров, отметим основные из них:"""
#command: ссылка на функцию, которая вызывается при нажатии на флажок
#cursor: курсор при наведении на элемент
#image: графическое изображение, отображаемое на элементе
#offvalue: значение флажка в неотмеченном состоянии, по умолчанию равно 0
#onvalue: значение флажка в отмеченном состоянии, по умолчанию равно 1
#padding: отступы от текста до границы флажка
#state: состояние элемента, может принимать значения NORMAL (по умолчанию), DISABLED и ACTIVE
#text: текст элемента
#textvariable: привязанный к тексту объект StringVar
#underline: индекс подчеркнутого символа в тексте флажка
#variable: ссылка на переменную, как правило, типа IntVar, которая хранит состояние флажка
#width: ширина элемента
"""Создадим простейший флажок:"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#enabled = IntVar()
#
#enabled_checkbutton = ttk.Checkbutton(text="Включить",
#                                      variable=enabled)
#enabled_checkbutton.pack(padx=6, pady=6, anchor=NW)
#
#enabled_label = ttk.Label(textvariable=enabled)
#enabled_label.pack(padx=6, pady=6, anchor=NW)
#
#root.mainloop()
"""Отличительной чертой Checkbutton является возможность привязки к переменной через параметр variable, который представляет значение флажка. Здесь данный параметр привязан к переменной enabled типа IntVar. В отмеченном состоянии привязанный объект IntVar имеет значение 1, а в неотмеченном - 0. В итоге через IntVar мы можем получать значение, указанное пользователем."""
"""Обработка изменения флажка"""
"""С помощью параметра command можно установить функцию, которая будет вызываться при изменении состояния флажка:"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#
#def checkbutton_changed():
#    if enabled.get() == 1:
#        showinfo(title="Info", message="Включено")
#    else:
#        showinfo(title="Info", message="Отключено")
#
#
#enabled = IntVar()
#
#enabled_checkbutton = ttk.Checkbutton(text="Включить",
#                                      variable=enabled,
#                                      command=checkbutton_changed)
#enabled_checkbutton.pack(padx=6, pady=6, anchor=NW)
#
#root.mainloop()
"""Здесь при изменении состояния флажка срабатывает функция checkbutton_changed. В ней в зависимости от состояния флажка (а точнее в зависимости от значения переменной enabled) с помощью встроенной функции showinfo() отображаем сообщение о состоянии флажка:"""
"""onvalue и offvalue"""
"""Параметры onvalue и offvalue позволяют задать значение флажка в отмеченном и неотмеченном состоянии. По умолчанию они равны 1 и 0 соответственно. Однако мы можем передать им и другие, более удобные для нас значения."""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#
#def checkbutton_changed():
#    print(enabled.get())
#    showinfo(title="Info", message=enabled.get())
#
#
#enabled = StringVar()
#
#enabled_checkbutton = ttk.Checkbutton(text="Включить",
#                                      variable=enabled,
#                                      offvalue="Отключено",
#                                      onvalue="Включено",
#                                      command=checkbutton_changed)
#enabled_checkbutton.pack(padx=6, pady=6, anchor=NW)
#
#root.mainloop()
"""Теперь переменная enabled представляет StringVar, то есть хранит строку. Соответственно параметры offvalue и onvalue тоже представляют строку"""
"""Текст флажка"""
"""Для установки текста флажка можно использовать параметры text и textvariable. Причем мы можем привязать текст флажка к его значению с помощью textvariable:"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#enabled_on = "Включено"
#enabled_off = "Отключено"
#enabled = StringVar(value=enabled_on)
#
#enabled_checkbutton = ttk.Checkbutton(textvariable=enabled,
#                                      variable=enabled,
#                                      offvalue=enabled_off,
#                                      onvalue=enabled_on)
#enabled_checkbutton.pack(padx=6, pady=6, anchor=NW)
#
#root.mainloop()
"""В данном случае для хранения текста в отмеченном и неотмеченном состояниях определены две переменные: enabled_on и enabled_off. Переменная enabled инициализируется тем же значением (enabled_on), что и параметр onvalue, поэтому по умолчанию флажок будет отмечен. А поскольку его параметры textvariable и variable привязаны к одной и той же переменной enabled, то они будет изменяться синхронно"""
"""Обработка нескольких флажков"""
"""Аналогичным образом можно использовать наборы флажков:"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#
#def select():
#    result = "Выбрано: "
#    if python.get() == 1: result = f"{result} Python"
#    if javascript.get() == 1: result = f"{result} JavaScript"
#    if java.get() == 1: result = f"{result} Java"
#    languages.set(result)
#
#
#position = {"padx": 6, "pady": 6, "anchor": NW}
#
#languages = StringVar()
#languages_label = ttk.Label(textvariable=languages)
#languages_label.pack(**position)
#
#python = IntVar()
#python_checkbutton = ttk.Checkbutton(text="Python",
#                                     variable=python,
#                                     command=select)
#python_checkbutton.pack(**position)
#
#javascript = IntVar()
#javascript_checkbutton = ttk.Checkbutton(text="JavaScript",
#                                         variable=javascript,
#                                         command=select)
#javascript_checkbutton.pack(**position)
#
#java = IntVar()
#java_checkbutton = ttk.Checkbutton(text="Java",
#                                   variable=java,
#                                   command=select)
#java_checkbutton.pack(**position)
#
#root.mainloop()
"""В данном случае языки, которые соответствуют выбранным чекбоксам, будут отображаться на текстовой метке:"""
