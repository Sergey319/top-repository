from tkinter import *
from tkinter import ttk

"""
Progressbar
"""
"""
Виджет Progressbar предназначен для отображения хода выполнения какого-либо
процесса. Основные параметры Progressbar:
"""
# value: текущее значение виджета (тип float)
# maximum: максимальное значение (тип float)
# variable: определяет переменную IntVar/DoubleVar, которая хранит текущее значение виджета
# mode: определяет режим, принимает значения "determinate" (конечный) и "indeterminate" (бесконечный)
# orient: определяет ориентацию виджета, принимает значения "vertical" (вертикальный) и "horizontal" (горизонтальный)
# length: длина виджета
"""
Определим вертикальный и горизонтальный Progressbar:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x150")
#
## вертикальный Progressbar
#ttk.Progressbar(orient="vertical", length=100, value=40).pack(pady=5)
#
## горизонтальный Progressbar
#ttk.Progressbar(orient="horizontal", length=150, value=20).pack(pady=5)
#
#root.mainloop()
"""
С помощью параметра variable можно привязать значение прогрессбара к
переменной типа IntVar или DoubleVar:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x150")
#
#value_var = IntVar(value=30)
#
#progressbar = ttk.Progressbar(orient="horizontal", variable=value_var)
#progressbar.pack(fill=X, padx=6, pady=6)
#
#label = ttk.Label(textvariable=value_var)
#label.pack(anchor=NW, padx=6, pady=6)
#
#root.mainloop()
"""
В данном случае значение прогрессбара привязано к переменной value_var,
значение которой выводит метка label
"""
"""
Методы Progressbar
"""
"""
Некоторые важные методы виджета:
"""
# start([interval]): запускает перемещение индикатора через определенные интервалы времени. Каждый раз, когда пройдет очередной интервал, индикатор смещается на одно деление вперед. По умолчанию интервал равен 50 миллисекунд
# step([delta]): увеличивает значение индикатора на значение из параметра delta (по умолчанию равен 1.0)
# stop(): останавливает перемещение индикатора
"""
Применим методы:
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x150")
#
#value_var = IntVar()
#
#progressbar = ttk.Progressbar(orient="horizontal", variable=value_var)
#progressbar.pack(fill=X, padx=6, pady=6)
#
#label = ttk.Label(textvariable=value_var)
#label.pack(anchor=NW, padx=6, pady=6)
#
#def start(): progressbar.start(1000)    # запускаем progressbar
#def stop(): progressbar.stop()          # останавливаем progressbar
#
#start_btn = ttk.Button(text="Start", command=start)
#start_btn.pack(anchor=SW, side=LEFT, padx=6, pady=6)
#stop_btn = ttk.Button(text="Stop", command=stop)
#stop_btn.pack(anchor=SE, side=RIGHT, padx=6, pady=6)
#
#root.mainloop()
"""
В данном случае по нажатию на кнопку start_btn запускаем перемещение
индикатора - через каждые 1000 миллисекунд (1 секунду) индикатор перемещается
на одно деление вперед. По нажатию на кнопку stop_btn останавливаем движение
индикатора
"""
"""
Режим прогрессбара
"""
"""
Параметр mode отвечает за установку режима прогрессбара и может принимать два
значения:

"indeterminate": прогрессбар показывает индикатор, который перемещается
без остановки между двумя краями виджета, то есть фактически бесконечно
продолжает перемещение. Данный режим подходит, когда сложно рассчитать,
насколько должен перемещаться индикатор при отображении хода некоторой
задачи

"determinate": индикатор прогрессбара проходит от начала до конца и затем
завершает перемещение. Значение по умолчанию. Подходит для отображения
таких процессов, где можно подсчитать перемещение индикатора. Например,
копируется 100 файлов, и, если параметр maximum равен 100, при копировании
одного файла перемещаем индикатор на одно деление вперед
"""
"""
Применение режима "determinate" по сути уже рассматривалось выше, так как это
режим по умолчанию. Посмотрим на пример применения режима "indeterminate":
"""
#root = Tk()
#root.title("METANIT.COM")
#root.geometry("250x150")
#
#progressbar = ttk.Progressbar(orient="horizontal", mode="indeterminate")
#progressbar.pack(fill=X, padx=10, pady=10)
#
#start_btn = ttk.Button(text="Start", command=progressbar.start)
#start_btn.pack(anchor=SW, side=LEFT, padx=10, pady=10)
#
#stop_btn = ttk.Button(text="Stop", command=progressbar.stop)
#stop_btn.pack(anchor=SE, side=RIGHT, padx=10, pady=10)
#
#root.mainloop()