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
