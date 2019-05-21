import tkinter
import math

window=tkinter.Tk()
#window.geometry('410x250')

label=tkinter.Label(window, text = "Менеджер задач",font=("Arial Bold", 15)).grid(row=0, column=0, columnspan=6)

task=tkinter.Label(window, text = "Задача:")
task.grid(row=1, column=0)

kat=tkinter.Label(window, text = "Категория:")
kat.grid(row=2, column=0)

time=tkinter.Label(window, text = "Время:")
time.grid(row=3, column=0)

task_w = tkinter.Entry(window)
task_w.grid(row=1, column=1)

kat_w = tkinter.Entry(window)
kat_w.grid(row=2, column=1)

time_w = tkinter.Entry(window)
time_w.grid(row=3, column=1)

window.mainloop()