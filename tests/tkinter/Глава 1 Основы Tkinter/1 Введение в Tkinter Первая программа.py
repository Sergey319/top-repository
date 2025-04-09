from tkinter import *

root = Tk()     # создаём корневой объект - окно
root.title("Приложение на Tkinter")     # устанавливаем заголовок окна
root.geometry("300x250")    # устанавливаем размер окна

label = Label(text="Hello METANIT.COM")     # создаём текстовую метку
label.pack()    # размещаем метку в окне

root.mainloop()