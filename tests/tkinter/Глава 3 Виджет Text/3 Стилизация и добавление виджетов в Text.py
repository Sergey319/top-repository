from tkinter import *
from tkinter import ttk

"""
Стилизация и добавление виджетов в Text
"""
"""
Добавление тегов
Теги позволяют определить форматирование. Тег добавляется с помощью метода
add_tag() класса Text:

tag_add(tagName, index1, index2)

Первый параметр устанавливает имя тега, второй параметр - index1 указывает на
начальный символ, с которого начинает применяться тег. Дополнительно (но
необязательно) можно указать третий параметр, который устанавливает конечный
символ, к которому применяется тег.

Для прикрепления тега к определенному тексту также можно использовать метод
insert, который добавляет текст, и в качестве второго параметра передать тег или
набор тегов, которые будут применяться к добавленному тексту:

insert(index, text, tagName)
insert(index, text, (tagName1, tagName2,...tagNameN))

С помощью метода tag_configure() для тега можно сконфигурировать стили.

tag_configure(имя_тега, стили)

Стили представляют параметры background, bgstipple, borderwidth, elide, fgstipple,
font, foreground, justify, lmargin1, lmargin2, offset, overstrike, relief, rmargin, spacing1,
spacing2, spacing3, tabs, tabstyle, underline и wrap, которым передаются некоторые
значения.

Посмотрим на примере:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#editor = Text(wrap="none")
#editor.pack(expand=1, fill=BOTH)
#editor.insert("1.0", "Hello ")
## создаем тег highlightline и прикрепляем его к символам 1.0 до 1.2
#editor.tag_add("highlightline", "1.0", "1.2")
## добавляем текст, к которому применяется тег highlightline
#editor.insert("end", "World", "highlightline")
#editor.insert("end", "\nHello All!")
## устанавливаем стили тега highlightline
#editor.tag_config("highlightline", background="#ccc", foreground="red", font="TkFixedFont", relief="raised")
#
#root.mainloop()
"""
Здесь создается тег "highlightline", который прикрепляется сначала по 2-й символ в
первой строке. Далее добавляется текст "World", к которому применяется данный тег.
В конце конфигурируем тег, задавая его стилевые параметры.

Если в процессе программы тег стал не нужен, его можно удалить. Метод
tag_remove() удаляет тег с определенных символов:

editor.tag_remove("highlightline", "1.0", "1.2")

В данном случае удаляем тег "highlightline" с символов с 0 по 2-й в первой строке.

Также можно вообще удалить тег со всех символов, к которым он применяется:

editor.tag_delete("highlightline")
"""
"""
Добавление изображений и других виджетов

Виджет Text позволяет добавление изображений и других виджетов.
Для добавления изображений применяется метод image_create:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#editor = Text()
#editor.pack(expand=1, fill=BOTH)
#
#python_img = PhotoImage(file="python.png")
#editor.image_create("1.0", image=python_img)
#
#root.mainloop()
"""
В метод image_create в качестве первого параметра передается позиция вставки
изображения. В качестве второго параметра - image указывается файл
изображения.

Аналогично можно добавлять другие виджеты в Text с помощью метода
window_create():
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#editor = Text()
#editor.pack(expand=1, fill=BOTH)
#
#def click():
#    editor.insert("2.0", "Click\n")
#
#btn = ttk.Button(editor, text="Click", command=click)
#editor.window_create("1.0", window=btn)
#
#root.mainloop()
"""
Первый параметр метода window_create также позиция создания виджета, а
второй параметр - window указывает на добавляемый виджет, в данном случае это
кнопка, на которую также можно нажимать и также можно обрабатывать ее
нажатие
"""