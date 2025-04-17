"""

    Установка тегов


"""
"""
    При добавлении элемента в Canvas этому элементу автоматически присваивается
числовой идентификатор. С помощью этого идентификатора затем мы можем
ссылаться на данный элемент. Однако Canvas также поддерживает добавление
тегов, через которые также можно ссылаться на элементы внутри Canvas. Более
того каждому элементу можно назначить несколько тегов. Также нескольким
элементам можно назначить один и тот же тег, благодаря чему можно ссылать не
только на один элемент, но и на группу элементов.

    Установка тегов
    
    Для установки тега элементу при его добавлении можно использовать параметр
tags, который получает список тегов:
    canvas.create_line(10, 10, 200, 100, fill="red", tags=["line"])
    В данном случае линии добавляется тег "line".
    
    Добавление тега
    
    Для добавления тега можно использовать метод addtag():
    addtag(название_тега, команда, идентификатор_элемента)
    Первый параметр - добавляемый тег, второй параметр - команда, обычно "withtag".
Третий параметр - идентификатор элемента, для которого добавляется тег:
    line_id = canvas.create_line(10, 10, 200, 100, fill="red", tags=["line"])
    canvas.addtag("figure", "withtag", line_id)
    Здесь для элемента line_id добавляется тег "figure"
    
    Получение тегов
    
    Для получения списка тегов для определенного элемента применяется метод
gettags(), в который передается идентификатор элемента:
"""
#from tkinter import *
#
#root = Tk()
#root.geometry("300x250")
#
#canvas = Canvas(bg="white", width=250, height=200)
#canvas.pack(anchor=NW)
#
#line_id = canvas.create_line(10, 10, 200, 100, fill="red", tags=["line", "figure"])
## получаем все теги для элемента line_id
#for tag in canvas.gettags(line_id):
#    print(tag)
#
#root.mainloop()
"""
    Также можно получить идентификаторы элементов по определенному тегу с
помощью метода find_withtag(), в который передается имя тега.
"""
#from tkinter import *
#
#root = Tk()
#root.geometry("300x250")
#
#canvas = Canvas(bg="white", width=250, height=200)
#canvas.pack(anchor=CENTER, expand=1)
#
#canvas.create_line(10, 10, 200, 10, fill="red", tags=["line", "figure"])
#canvas.create_line(10, 50, 200, 50, fill="blue", tags="line")
## получаем все элементы с тегом line
#for element_id in canvas.find_withtag("line"):
#    print(element_id)
#
#root.mainloop()
"""
    Удаление тега
    
    Для удаления тега применяется метод dtags():
    line_id = canvas.create_line(10, 10, 200, 10, fill="red", tags=["line", "figure"])
    # удаляем у элемента line_id тег "figure
    canvas.dtags(line_id, "figure")
    В метод dtags() передается идентификатор элемента и удаляемый тег.
    
    Конфигурация через тег
    
    С помощью метода itemconfigure() для элементов с определенным тегом можно
установить различные опции:
    itemconfigure: (tagOrId: str | _CanvasItemId, cnf: dict[str, Any] | None = ..., **kw: Any)
    Первый параметр - тег или идентификатор элемента, а второй - набор
устанавливаемых опций. Например:
"""
#from tkinter import *
#
#root = Tk()
#root.geometry("300x250")
#
#canvas = Canvas(bg="white", width=250, height=200)
#canvas.pack(anchor=CENTER, expand=1)
#
#canvas.create_line(10, 50, 200, 50, fill="blue", tags="line")
## устанавливаем для элементов с тегом "line" зеленый цвет
#canvas.itemconfigure("line", fill="green")
#
#root.mainloop()
"""
    Практическое использование тегов
    
    Одной из ключевых возможностей тегов состоит в том, что они позволяют
управлять группой элементов:
"""
#from tkinter import *
#from tkinter import ttk
#
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x250")
#
#red = "red"
#blue = "blue"
#green = "green"
#selected_color = StringVar(value=red)
#
#canvas = Canvas(bg="white", width=250, height=150)
#canvas.pack(anchor=NW)
#
#canvas.create_rectangle((10, 80, 130, 130), fill=selected_color.get(), outline="black", tags="house")
#canvas.create_polygon((10, 80), (70, 30), (130, 80), fill=selected_color.get(), outline="black", tags="house")
#
#def select():
#    canvas.itemconfigure("house", fill=selected_color.get())
#
#ttk.Radiobutton(text=red, value=red, variable=selected_color, command=select, padding=6).pack(anchor=NW)
#ttk.Radiobutton(text=blue, value=blue, variable=selected_color, command=select, padding=6).pack(anchor=NW)
#ttk.Radiobutton(text=green, value=green, variable=selected_color, command=select, padding=6).pack(anchor=NW)
#
#root.mainloop()
"""
    В данном случае на Canvas отрисованы две фигуры - прямоугольник и
многоугольник. Оба этих элемента имеют тег "house".
    На окне также определены три переключателя Radiobutton, которые привязаны к
переменной selected_color и позволяют выбрать цвет. При выборе одного из
переключателей срабатывает функция select, в которой для элементов с тегом
"house" устанавливается определенный цвет.
"""