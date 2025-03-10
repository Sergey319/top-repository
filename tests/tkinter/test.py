from tkinter import *
from tkinter import ttk

day = Tk()

day.title("Подсчёт одного дня")
day.geometry("1600x900+150+50")

for c in range(16):
    day.columnconfigure(index=c, weight=1)

size = ttk.Label(text="размер", font=("Arial", 14), borderwidth=2, relief="ridge", anchor=CENTER)
size.grid(row=0, column=0, columnspan=3, sticky=NSEW)

pachka = ttk.Label(text="пачка", font=("Arial", 14), borderwidth=2, relief="ridge", anchor=CENTER)
pachka.grid(row=0, column=3, columnspan=4, sticky=NSEW)

day.mainloop()