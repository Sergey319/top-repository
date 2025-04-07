from tkinter import *
from tkinter import ttk

from win32comext.mapi.emsabtags import PR_EMS_AB_OOF_REPLY_TO_ORIGINATOR

"""Scrollbar и прокрутка виджета"""
"""Виджет Scrollbar прокручивать содержимое контейнера, которое больше размеров этого контейнера."""
"""Основные параметры конструктора Scrollbar:"""
# orient: направление прокрутки. Может принимать следующие значения: vertical (вертикальная прокрутка) и horizontal (горизонтальная прокрутка).
# command: команда прокрутки
"""Scrollbar не используется сам по себе, он применяется лишь для прокручиваемого виджета.
Не все виджеты в tkinter являются прокручиваемыми.
Для прокрутки по вертикали прокручиваемый виджет имеет yview, а для прокрутки по горизонтали - метод xview (виджет может иметь только один из этих методов).
Примером прокручиваемого виджета может служить Listbox или Text.
Этот метод используется в качестве команды для Scrollbar"""
#listbox = Listbox()
## вертикальная прокрутка
#scrollbar = ttk.Scrollbar(orient="vertical", command = listbox.yview)
"""Но прокручиваемый виджет должен также взаимодействовать со Scrollbar.
Для этого у прокручиваемого виджета имеются параметры yscrollcommand и/или xscrollcommand, которые должны принимать вызов метода set объекта Scrollbar:"""
#languages = ["Python", "JavaScript", "C#", "Java", "C++", "Rust", "Kotlin", "Swift",
#             "PHP", "Visual Basic.NET", "F#", "Ruby", "R", "Go", "C",
#             "T-SQL", "PL-SQL", "Typescript", "Assembly", "Fortran"]
#
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#languages_var = StringVar(value=languages)
#listbox = Listbox(listvariable=languages_var)
#listbox.pack(side=LEFT, fill=BOTH, expand=1)
#
#scrollbar = ttk.Scrollbar(orient="vertical", command=listbox.yview)
#scrollbar.pack(side=RIGHT, fill=Y)
#
#listbox["yscrollcommand"] = scrollbar.set
#
#root.mainloop()
"""
В конструкторе scrollbar ассоциируется с функцией, которую надо выполнить при прокрутке.
В данном случае это метод yview элемента listbox.
В итоге мы сможем прокручивать элементы по вертикали"""
"""
И так как необходимо прокручивать listbox по вертикали, то у него задается параметр listbox["yscrollcommand"]=scrollbar.set"""
"""
Ручная прокрутка

В принципе для прокрутки виджета (который поддерживает прокрутку)
использовать Scrollbar необязательно. Для прокрутки виджет может содержать
специальные методы:
"""
# yview_scroll(number, what): сдвигает текущее положение по вертикали. Параметр number указывает количество, на которое надо сдвигать. А параметр what определяет единицы сдвига и может принимать следующие значения: "units" (элемент) и "pages" (страницы)
# xview_scroll(number, what): сдвигает текущее положение по горизонтали
# yview_moveto(fraction): сдвигает область просмотра по вертикали на определенную часть, которая выражается во float от 0 до 1
# xview_moveto(fraction): сдвигает область просмотра на определенную часть по горизонтали
"""
Например, сдвиг на два элемента списка вниз:
"""
#languages = ["Python", "JavaScript", "C#", "Java", "C++", "Rust", "Kotlin", "Swift",
#             "PHP", "Visual Basic.NET", "F#", "Ruby", "R", "Go",
#             "T-SQL", "PL-SQL", "Typescript"]
#
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#languages_var = StringVar(value=languages)
#listbox = Listbox(listvariable=languages_var)
#listbox.pack(expand=1, fill=BOTH)
## создаем скрол на 1 элемент внизу
#listbox.yview_scroll(number=1, what="units")
#
#root.mainloop()
