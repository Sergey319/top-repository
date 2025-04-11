from tkinter import *
from tkinter import ttk

"""
Создание таблиц
"""
"""
Для отображения данных в виде таблицы параметру show предпочтительно
передать значение "headings" (если надо отображать заголовки), либо " " (для
таблицы без заголовков). Определим небольшую таблицу с тремя столбцами:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
## определяем данные для отображения
#people = [("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com")]
#
## определяем столбцы
#columns = ("name", "age", "email")
#
#tree = ttk.Treeview(columns=columns, show="headings")
#tree.pack(fill=BOTH, expand=1)
#
## определяем заголовки
#tree.heading("name", text="Имя")
#tree.heading("age", text="Возраст")
#tree.heading("email", text="Email")
#
## добавляем данные
#for person in people:
#    tree.insert("", END, values=person)
#
#root.mainloop()
"""
Здесь данные, которые будут отображаться в таблице, определены в виде списка
people, который хранит набор кортежей. Каждый кортеж состоит из трех элементов.
Условно будем считать, что первый элемент кортежа представляет имя
пользователя, второй - возраст, а третий - электронный адрес. И эти данные нам
надо отобразить в таблице:
people = [("Tom", 38, "tom@mail.com"), ("Bob", 42, "bob@mail.com"), ("Sam", 28, "sam@mail.com")]
Для отображения этих данных определяем три столбца: name, age и email в виде
кортежа и передаем их параметру columns:
columns = ("name", "age", "email")
tree = ttk.Treeview(columns=columns, show="headings")
Далее нам надо настроить заголовки столбца с помощью метода heading() класса
Treeview (по умолчанию столбцы не имеют никаких заголовков). Данный метод
принимает ряд параметров:
tree. heading("name", text="Имя")
Первый параметр указывает на имя столбца. В примере выше определяем также
параметр text, который определяет текст заголовка.
И последний момент - добавляем сами данные в таблицу с помощью метода insert() класса Treeview
tree.insert("", END, values=person)
Первый параметр - пустая строка "" указывает, что элемент добавляется как
элемент верхнего уровня (то есть у него нет родительского элемента). Значение END
указывает, что элемент добавляется в конец набора. И параметр values в качестве
добавляемых данных устанавливает кортеж person.
В итоге мы получаем таблицу

Настройка столбца
Вполне возможно. что изначальные настройки столбцов нас не устраивает. Например,
текст заголовка располагается по умолчанию по центру, а данные столбца
выравниваются по левому краю. Кроме того, каждый столбец имеет некоторую
начальную ширину, в следствие чего ширина виджета может оказаться больше
ширины окна. Либо мы захотим как-то иначе настроить вид столбца.
Прежде всего мы можем настроить заголовки столбца с помощью метода
heading():
heading(column, text, image, anchor, command)
Параметры метода:
* column: имя настраиваемого столбца
* text: текст заголовка
* image: картинка для заголовка
* anchor: устанавливает выравнивание заголовка по определенному краю.
    Может принимать значения n, e, s, w, ne, nw, se, sw, c
* command: функция, выполняемая при нажатии на заголовок
Для настройки столбца в целом применяется метод column():
column(column, width, minwidth, stretch, anchor)
* column: индекс настраиваемого столбца в формате "# номер столбца"
* width: ширина столбца
* minwidth: минимальная ширина
* anchor: устанавливает выравнивание заголовка по определенному краю.
    Может принимать значения n, e, s, w, ne, nw, se, sw, c
* stretch: указывает, будет ли столбец растягиваться при растяжении
    контейнера. Если будет, то значение True, иначе значение False
Применим некоторые из этих параметров:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
## определяем данные для отображения
#people = [("Tom", 38, "tom@mail.com"), ("Bob", 42, "bob@mail.com"), ("Sam", 28, "sam@mail.com")]
#
## определяем столбцы
#columns = ("name", "age", "email")
#
#tree = ttk.Treeview(columns=columns, show="headings")
#tree.pack(fill=BOTH, expand=1)
#
## определяем заголовки с выравниванием по левому краю
#tree.heading("name", text="Имя", anchor=W)
#tree.heading("age", text="Возраст", anchor=W)
#tree.heading("email", text="Email", anchor=W)
#
## настраиваем столбцы
#tree.column("#1", stretch=NO, width=70)
#tree.column("#2", stretch=NO, width=20)
#tree.column("#3", stretch=NO, width=100)
#
## добавляем данные
#for person in people:
#    tree.insert("", END, values=person)
#
#root.mainloop()
"""
В данном случае для заголовков устанавливаем выравнивание по левому краю. Для
столбцов запрещаем растяжение и устанавливаем ширину.
При добавлении изображения оно помещается в правой части. Например,
установка изображения для третьего столбца:
"""
## предполагается, что в папке приложения располагается файл email_icon_micro.png
#email_icon = PhotoImage(file="./email_icon_micro.png")
#tree.heading("email", text="Email", anchor=W, image=email_icon)

#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#
## определяем данные для отображения
#people = [("Tom", 38, "tom@mail.com"), ("Bob", 42, "bob@mail.com"), ("Sam", 28, "sam@mail.com")]
#
## определяем столбцы
#columns = ("name", "age", "email")
#
#tree = ttk.Treeview(columns=columns, show="headings")
#tree.pack(fill=BOTH, expand=1)
#
#email_icon = PhotoImage(file="email_icon_micro.png")
#
## определяем заголовки с выравниванием по левому краю
#tree.heading("name", text="Имя", anchor=W)
#tree.heading("age", text="Возраст", anchor=W)
#tree.heading("email", text="Email", anchor=W, image=email_icon)
#
## настраиваем столбцы
#tree.column("#1", stretch=NO, width=70)
#tree.column("#2", stretch=NO, width=20)
#tree.column("#3", stretch=NO, width=100)
#
## добавляем данные
#for person in people:
#    tree.insert("", END, values=person)
#
#root.mainloop()
"""
Добавление к Treeview прокрутки
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x200")
#root.rowconfigure(index=0, weight=1)
#root.columnconfigure(index=0, weight=1)
#
## определяем данные для отображения
#people = [
#    ("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com"),
#    ("Alice", 33, "alice@email.com"), ("Kate", 21, "kate@email.com"), ("Ann", 24, "ann@email.com"),
#    ("Mike", 34, "mike@email.com"), ("Alex", 52, "alex@email.com"), ("Jess", 28, "jess@email.com"),
#    ]
#
## определяем столбцы
#columns = ("name", "age", "email")
#
#tree = ttk.Treeview(columns=columns, show="headings")
#tree.grid(row=0, column=0, sticky=NSEW)
#
## определяем заголовки
#tree.heading("name", text="Имя", anchor=W)
#tree.heading("age", text="Возраст", anchor=W)
#tree.heading("email", text="Email", anchor=W)
#
#tree.column("#1", stretch=NO, width=70)
#tree.column("#2", stretch=NO, width=60)
#tree.column("#3", stretch=NO, width=100)
#
## добавляем данные
#for person in people:
#    tree.insert("", END, values=person)
#
## добавляем вертикальную прокрутку
#scrollbar = ttk.Scrollbar(orient=VERTICAL, command=tree.yview)
#tree.configure(yscroll=scrollbar.set)
#scrollbar.grid(row=0, column=1, sticky=NS)
#
#root.mainloop()
