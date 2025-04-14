"""

    Темы


"""
"""
    Тема представляет коллекцию стилей. Все стили одной темы проектируются таким
образом, чтобы визуально сочетаться друг с другом. Применение определенной
темы означает, что к виджетам будут применяться стили из данной темы.
    По умолчанию Tkinter уже предоставляет ряд тем. Чтобы их получить, можно
использовать метод theme_names() класса ttk.Style
"""
#from tkinter import ttk
#
#for theme in ttk.Style().theme_names():
#    print(theme)
"""
    Стоит учитывать, что на разных операционных системах свои встроенные темы.
    Для получения текущей темы можно использовать метод theme_use()
"""
#from tkinter import ttk
#
#current_theme = ttk.Style().theme_use()
#print(current_theme)
"""
    Для установки другой темы в этот метод в качестве параметра передается название
темы:
"""
#from tkinter import *
#from tkinter import ttk
#
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
## устанавливаем тему "classic"
#ttk.Style().theme_use("classic")
#
#ttk.Label(text="Hello World!").pack(anchor=NW, padx=5, pady=5)
#ttk.Button(text="Click").pack(anchor=CENTER, expand=1)
#
#root.mainloop()
"""
    Подобным образом мы можем определить небольшое приложение для выбора из
текущих тем:
"""
#from tkinter import *
#from tkinter import ttk
#
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
## выбранная тема
#selected_theme = StringVar()
#style = ttk.Style()
#
## изменение текущей темы
#def change_theme():
#    style.theme_use(selected_theme.get())
#
#ttk.Label(textvariable=selected_theme, font="Helvetica 13").pack(anchor=NW)
#
#for theme in style.theme_names():
#    ttk.Radiobutton(text=theme,
#                    value=theme,
#                    variable=selected_theme,
#                    command=change_theme).pack(anchor=NW)
#
#root.mainloop()
"""
    В данном случае каждый элемент Radiobutton представляет определенную тему.
При выборе определенной кнопки Radiobutton будет срабатывать функция
change_theme(), в которой будет изменена текущая тема
"""