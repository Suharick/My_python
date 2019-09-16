import tkinter
import tkinter.messagebox

class Time:

    def __init__(self):

        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.text_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(0)

        self.rb1 = tkinter.Radiobutton(self.top_frame, text='Дневное время (6:00-17:59)', variable=self.radio_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text='Вечернее время (18:00-23:59)', variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text='Непиковый период (00:00-5:59)', variable=self.radio_var, value=3)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.min_label = tkinter.Label(self.text_frame, text='Введите кол-во галлонов:')
        self.min_entry = tkinter.Entry(self.text_frame, width=10)

        self.min_label.pack(side='left')
        self.min_entry.pack(side='left')

        self.make_button = tkinter.Button(self.bottom_frame, text='Показать стоимость', command=self.cost)
        self.out_button = tkinter.Button(self.bottom_frame,  text='Выйти', command=self.main_window.destroy)

        self.make_button.pack(side='left')
        self.out_button.pack(side='left')

        self.top_frame.pack()
        self.text_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def cost(self):

        self.message = 'Ваши затраты = '
        a = 0

        if self.radio_var.get() == 1:
            a = 10
        if self.radio_var.get() == 2:
            a = 12
        if self.radio_var.get() == 3:
            a = 5

        b = (a * float(self.min_entry.get()))/100

        self.message = self.message + str(b)

        tkinter.messagebox.showinfo('Общая стоимость', self.message)
        
start = Time()
