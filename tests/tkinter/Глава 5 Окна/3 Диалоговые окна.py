"""

Диалоговые окна

"""
"""
    Tkinter обладает рядом встроенных диалоговых окон для различных задач.
Рассмотрим некоторые из них:

    filedialog
    Модуль filedialog предоставляет функциональность файловых диалоговых окон,
которые позволяют выбрать файл или каталог для различных задач. В частности в
модуле для работы с файлами определены следующие функции:
    * askopenfilename(): открывает диалоговое окно для выбора файла и
    возвращает путь к выбранному файлу. Если файл не выбран, возвращается
    пустая строка ""
    * askopenfilenames(): открывает диалоговое окно для выбора файлов и
    возвращает список путей к выбранным файлам. Если файл не выбран,
    возвращается пустая строка ""
    * asksaveasfilename(): открывает диалоговое окно для сохранения файла и
    возвращает путь к сохраненному файлу. Если файл не выбран, возвращается
    пустая строка ""
    * asksaveasfile(): открывает диалоговое окно для сохранения файла и
    возвращает сохраненный файл. Если файл не выбран, возвращается None
    * askdirectory(): открывает диалоговое окно для выбора каталога и возвращает
    путь к выбранному каталогу. Если файл не выбран, возвращается пустая строка ""
    * askopenfile(): открывает диалоговое окно для выбора файла и возвращает
    выбранный файл. Если файл не выбран, возвращается None
    * askopenfiles(): открывает диалоговое окно для выбора файлов и возвращает
    список выбранных файлов
    Рассмотрим открытие и сохранение файла на примере:
"""
#from tkinter import *
#from tkinter import ttk
#from tkinter import filedialog
#
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#root.grid_rowconfigure(index=0, weight=1)
#root.grid_columnconfigure(index=0, weight=1)
#root.grid_columnconfigure(index=1, weight=1)
#
#text_editor = Text()
#text_editor.grid(column=0, row=0, columnspan=2)
#
## открываем файл в текстовое поле
#def open_file():
#    filepath = filedialog.askopenfilename()
#    if filepath != "":
#        with open(filepath, "r") as file:
#            text = file.read()
#            text_editor.delete("1.0", END)
#            text_editor.insert("1.0", text)
#
## сохраняем текст из текстового поля в файл
#def save_file():
#    filepath = filedialog.asksaveasfilename()
#    if filepath != "":
#        text = text_editor.get("1.0", END)
#        with open(filepath, "w") as file:
#            file.write(text)
#
#open_button = ttk.Button(text="Открыть файл", command=open_file)
#open_button.grid(column=0, row=1, sticky=NSEW, padx=10)
#
#save_button = ttk.Button(text="Сохранить файл", command=save_file)
#save_button.grid(column=1, row=1, sticky=NSEW, padx=10)
#
#root.mainloop()
"""
    Здесь определены две кнопки. По нажатию на кнопку open_button вызывается
функция filedialog.askopenfilename(). Она возвращает путь к выбранному
файлу. И если в диалоговом окне не нажата кнопка отмены (то есть путь к файлу не
равен пустой строке), то считываем содержимое текстового файла и добавляем его
в виджет Text
    def open_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r") as file:
            text = file.read()
            text_editor.delete("1.0", END)
            text_editor.insert("1.0", text)
    По нажатию на кнопку save_button срабатывает функция
filedialog.asksaveasfilename(), которая возвращает путь к файлу для
сохранения текста из виджета Text. И если файл выбран, то открываем его и
сохраняем в него текст:
    def save_file():
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        text = text_editor.get("1.0", END)
        with open(filepath, "w") as file:
            file.write(text)
    Эти функции могут принимать ряд параметров:
    * confirmoverwrite: нужно ли подтверждение для перезаписи файла (для
    диалогового окна сохранения файла)
    * defaultextension: расширение по умолчанию
    * filetypes: шаблон типов файлов
    * initialdir: стартовый каталог, который откроется в окне
    * initialfile: файл по умолчанию
    * title: заголовок диалогового окна
    * typevariable: переменная, к котрой привязан выбранный файл
    Применение параметров:
    filedialog.askopenfiles(title="Выбор файла", initialdir="D://tkinter", defaultextension="txt", initialfile="hello")
    
    
    Выбор шрифта
    
"""
#from tkinter import *
#from tkinter import ttk
#
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#label = ttk.Label(text="Hello World")
#label.pack(anchor=NW, padx=10, pady=10)
#
#def font_changed(font):
#    label["font"] = font
#
#def select_font():
#    root.tk.call("tk", "fontchooser", "configure", "-font", label["font"], "-command", root.register(font_changed))
#    root.tk.call("tk", "fontchooser", "show")
#
#open_button = ttk.Button(text="Выбрать шрифт", command=select_font)
#open_button.pack(anchor=NW, padx=10, pady=10)
#
#root.mainloop()
"""
    По нажатию на кнопку вызывается функция select_font, в которой вначале
производится настройка диалогового окна установки шрифта
    root.tk.call("tk", "fontchooser", "configure", "-font", label["font"], "-command", root.register(font_changed))
    В частности, значение "configure" указывает, что в данном случае производится
настройка диалогового окна. Аргумент "-font" указывает, что следующее значение
представляет настройка шрифта, который будет выбран в диалоговом окне по
умолчанию. В качестве такового здесь используется шрифт метки label.
    Аргумент "-command" указывает, что дальше идет определение функции, которая
будет срабатывать при выборе шрифта. Здесь такой функцией является функция
font-changed. Функция выбора шрифта должна принимать один параметр - через
него будет передаваться выбранный шрифт. В данном случае просто
переустанавливаем шрифт метки.
    Для отображения окна выбора шрифта выполняется вызов
    root.tk.call("tk", fontchooser", "show")
    Таким образом, при нажатии на кнопку откроется окно выбора шрифта, а после его
выбора он будет применен к метке.

    
    Выбор цвета
    
    Для выбора цвета применяются функции из модуля colorchooser.askcolor():
"""
#from tkinter import *
#from tkinter import ttk
#from tkinter import colorchooser
#
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
#label = ttk.Label(text="Hello World")
#label.pack(anchor=NW, padx=10, pady=10)
#
#def select_color():
#    result = colorchooser.askcolor(initialcolor="black")
#    label["foreground"] = result[1]
#
#open_button = ttk.Button(text="Выбрать цвет", command=select_color)
#open_button.pack(anchor=NW, padx=10, pady=10)
#
#root.mainloop()
"""
    Здесь по нажатию на кнопку вызывается функция select_color. В этой функции
вызывается функция colorchooser.askcolor. С помощью параметра
initialcolor устанавливаем цвет, который выбран по умолчанию в диалоговом
окне. В данном случае это черный цвет ("black")
    Результатом функции является кортеж с определениями выбранного цвета.
Например, для красного цвета кортеж будет выглядеть следующим образом:
((255, 0, 0), "#ff0000"). То есть, обратившись ко второму элементу кортежа,
можно получить шестнадцатиричное значение цвета. Здесь выбранный цвет
применяется для установки цвета шрифта метки:
    label["foreground"] = result[1]
"""