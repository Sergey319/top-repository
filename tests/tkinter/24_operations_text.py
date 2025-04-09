from tkinter import *
from tkinter import ttk

"""
Основные операции с виджетом Text
"""

"""
Добавление текста

Для добавления текста применяется метод insert():

insert(index, chars)

Первый параметр представляет позицию вставки в формате "line.column" - сначала
идет номер строки, а затем номер символа. Второй параметр - собственно
вставляемый текст. Например, вставка в начало:

editor.insert("1.0", "Hello")

Для вставки в конец для позиции передается значение END:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#editor = Text()
#editor.pack(fill=BOTH, expand=1)
#
#editor.insert("1.0", "Hello World")    # вставка в начало
#editor.insert(END, "\nBay World")      # вставка в конец
#root.mainloop()
"""
Получение текста
Для получения введенного текста применяется метод get():

get(start, end)

Параметр start указывает на начальный символ, а end - на конечный символ, текст
между которыми надо получить. Оба параметра в формате "line.column", где line -
номер строки, а column - номер символа. Для указания последнего символа применяется константа END:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("300x200")
#
#editor = Text(height=5)
#editor.pack(anchor=N, fill=X)
#
#label = ttk.Label()
#label.pack(anchor=N, fill=BOTH)
#
#def get_text():
#    label["text"] = editor.get("1.0", "end")
#
#button = ttk.Button(text="Click", command=get_text)
#button.pack(side=BOTTOM)
#
#root.mainloop()
"""
В данном случае по нажатию на кнопку срабатывает функция get_text(), которая
получает текст и передает его для отображения в метку label.

Удаление текста
Для удаления текста применяется метод delete()

delete(start, end)

Параметр start указывает на начальный символ, а end - на конечный символ, текст
между которыми надо удалить. Оба параметра в формате "line.column", где line -
номер строки, а column - номер символа. Для указания последнего символа
применяется константа END. Например, определим кнопку, которая будет удалять
весь текст из виджета:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("300x200")
#
#editor = Text(height=10)
#editor.pack(anchor=N, fill=BOTH)
#
#def delete_text():
#    editor.delete("1.0", END)
#
#button = ttk.Button(text="Clear", command=delete_text)
#button.pack(side=BOTTOM)
#
#root.mainloop()
"""
Замена текста
Для замены текста применяется метод replace():

replace(start, end, chars)

Параметр start указывает на начальный символ, а end - на конечный символ, текст
между которыми надо заменить. Оба параметра в формате "line.column", где line -
номер строки, а column - номер символа. Для указания последнего символа
применяется константа END. Последний параметр - chars - строка, на которую надо
заменить. Например, замена первых четырех символов на строку "дама":
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("300x200")
#
#editor = Text(height=10)
#editor.pack(anchor=N, fill=BOTH)
#editor.insert("1.0", "мама мыла раму")
#
#def edit_text():
#    editor.replace("1.0", "1.4", "дама")
#
#button = ttk.Button(text="Replace", command=edit_text)
#button.pack(side=BOTTOM)
#
#root.mainloop()
"""
Повтор и отмена операций
Методы edit_undo() и edit_redo() позволяют соответственно отменить и повторить
операцию (добавление, изменение, удаление текста). Данные методы применяются,
если в виджете Text параметр undo равен True. Стоит отметить, что данные методы
оперируют своим стеком операций, в котором сохраняются данные операций.
Однако если стек для соответствующего метода пуст, то вызов метода вызывает
исключение. Простейший пример, где по нажатию на кнопку вызывается отмена
или возврат операции:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#root.grid_columnconfigure(0, weight=1)
#root.grid_columnconfigure(1, weight=1)
#root.grid_rowconfigure(0, weight=1)
#
#editor = Text(undo=True)
#editor.grid(column=0, columnspan=2, row=0, sticky=NSEW)
#
#def undo():
#    editor.edit_undo()
#
#def redo():
#    editor.edit_redo()
#
#redo_button = ttk.Button(text="Undo", command=undo)
#redo_button.grid(column=0, row=1)
#clear_button = ttk.Button(text="Redo", command=redo)
#clear_button.grid(column=1, row=1)
#
#root.mainloop()
"""
Выделение текста
Для управления выделением текста виджет Text обладает следующими методами:
* selection_get(): возвращает выделенный фрагмент
* selection_clear(): снимает выделение
Применим данные методы:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#def get_selection():
#    label["text"] = editor.selection_get()
#
#def clear_selection():
#    editor.selection_clear()
#
#editor = Text(height=5)
#editor.pack(fill=X)
#
#label = ttk.Label()
#label.pack(anchor=NW)
#
#get_button = ttk.Button(text="Get selection", command=get_selection)
#get_button.pack(side=LEFT)
#clear_button = ttk.Button(text="Clear", command=clear_selection)
#clear_button.pack(side=RIGHT)
#
#root.mainloop()
"""
В данном случае по нажатию на кнопку get_button срабатывает функция
get_selection, которая передает в метку label выделенный текст. При нажатии на
кнопку clear_button срабатывает функция clear_selection, которая снимает выделение
"""
"""
События
Достаточно часто встречается необходимость обработки ввода текста. Для виджета
Text определенно событие <<Modified>>, которое срабатывает при изменении
текста в текстовом поле. Однако оно срабатывает один раз. И в этом случае мы
можем обработать стандартные события клавиатуры. Например, событие
освобождения клавиши <KeyRelease>:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#def on_modified(event):
#    label["text"] = editor.get("1.0", END)
#
#editor = Text(height=8)
#editor.pack(fill=X)
#editor.bind("<KeyRelease>", on_modified)
#
#label = ttk.Label()
#label.pack(anchor=NW)
#
#root.mainloop()
"""
В данном случае при освобождении клавиши будет срабатывать функция
on_modified, в которой передается весь введенный текст в метку label

Другую распространенную задачу представляет динамическое получение
выделенного текста. В этом случае мы можем обработать событие <<Selection>>.
Например, при выделении текста выведем выделенный фрагмент в метку Label:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#def on_modified(event):
#    label["text"] = editor.selection_get()
#
#editor = Text(height=8)
#editor.pack(fill=X)
#editor.bind("<<Selection>>", on_modified)
#
#label = ttk.Label()
#label.pack(anchor=NW)
#
#root.mainloop()