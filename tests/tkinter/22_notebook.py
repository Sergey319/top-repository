from tkinter import *
from tkinter import ttk

"""
Notebook. Создание вкладок
"""

"""
Виджет Notebook представляет набор вкладок. Среди параметров виджета следует
выделить следующие:
"""
# width: ширина виджета
# height: высота виджета
# cursor: курсор при наведении на виджет
# padding: отступы от границ виджета до его содержимого
# style: стиль виджета
"""
Для управления вкладками Notebook предоставляет ряд методов, в частности, для
добавления вкладки применяется метод add()
"""
# add(child, state, sticky, padding, text, image, compound, underline)
"""
Параметры метода
"""
# child: добавляем виджет, для которого собственно и создается вкладка.
# Обычно это Frame, которых затем добавляет другие виджеты
# state: состояние вкладки. Возможные значения: "normal", "disabled", "hidden"
# sticky: определяет прикрепление виджета к определенной стороне вкладки
# padding: отступы от границ вкладки до внутреннего содержимого
# text: заголовок вкладки
# image: изображение в заголовке вкладки
# compound: управляет расположением изображения и текста в заголовке вкладки
# underline: определяет номер подчеркнутого символа в заголовке вкладки
"""
Кроме того, чтобы скрыть временно вкладку, применяется метод hide()
"""
# hide(tabId)
"""
В качестве параметра принимает идентификатор вкладки, который по умолчанию
представляет числовой индекс вкладки начиная с 0.
"""
"""
Чтобы совсем удалить вкладку, применяется метод forget()
"""
# forget(child)
"""
В качестве параметра в метод передается удаляемый виджет.
"""
"""
Рассмотрим простейший пример:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
## создаем набор вкладок
#notebook = ttk.Notebook()
#notebook.pack(expand=True, fill=BOTH)
#
## создаем пару фреймов
#frame1 = ttk.Frame(notebook)
#frame2 = ttk.Frame(notebook)
#
#frame1.pack(fill=BOTH, expand=True)
#frame2.pack(fill=BOTH, expand=True)
#
## добавляем фреймы в качестве вкладок
#notebook.add(frame1, text="Python")
#notebook.add(frame2, text="Java")
#
#root.mainloop()
"""
Здесь определяются два фрейма, для которых создаются отдельные вкладки
"""
"""
Добавление изображений
"""
"""
За установку изображения в заголовке вкладки отвечает параметр image метода
add. Кроме того, с помощью параметра compound можно задать расположение
картинки относительно текста. В частности, параметр compound может принимать
следующие значения:
"""
# top: изображение поверх текста
# bottom: изображение под текстом
# left: изображение слева от текста
# right: изображение справа от текста
# none: при наличии изображения отображается только изображение
# text: отображается только текст
# image: отображается только изображение
"""
Например, отобразим картинку слева от текста:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
## создаем набор вкладок
#notebook = ttk.Notebook()
#notebook.pack(expand=True, fill=BOTH)
#
## создаем пару фреймов
#frame1 = ttk.Frame(notebook)
#frame2 = ttk.Frame(notebook)
#
#frame1.pack(fill=BOTH, expand=True)
#frame2.pack(fill=BOTH, expand=True)
#
#python_logo = PhotoImage(file="python.png")
#java_logo = PhotoImage(file="java.png")
## добавляем фреймы в качестве вкладок
#notebook.add(frame1, text="Python", image=python_logo, compound=LEFT)
#notebook.add(frame2, text="Java", image=java_logo, compound=LEFT)
#
#root.mainloop()