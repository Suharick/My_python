import tkinter
import tkinter.messagebox

class Choice:
    
    def __init__(self):
        
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.var1 = tkinter.IntVar()
        self.var2 = tkinter.IntVar()
        self.var3 = tkinter.IntVar()
        self.var4 = tkinter.IntVar()
        self.var5 = tkinter.IntVar()
        self.var6 = tkinter.IntVar()
        self.var7 = tkinter.IntVar()

        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)
        self.var6.set(0)
        self.var7.set(0)

        self.cb1 = tkinter.Checkbutton(self.top_frame, text='Замена масла - $30.00', variable=self.var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame, text='Смазочные работы - $20.00', variable=self.var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame, text='Промывка радиатора - $40.00', variabl=self.var3)
        self.cb4 = tkinter.Checkbutton(self.top_frame, text='Замена жидкости в трансмиссии - $100.00', variable=self.var4)
        self.cb5 = tkinter.Checkbutton(self.top_frame, text='Осмотр - $35.00', variable=self.var5)
        self.cb6 = tkinter.Checkbutton(self.top_frame, text='Замена глушителя выхлопа $200.00', variable=self.var6)
        self.cb7 = tkinter.Checkbutton(self.top_frame, text='Перестановка шин - $20.00', variable=self.var7)

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()

        self.cost_button = tkinter.Button(self.bottom_frame, text='Показать стоимость', command=self.show_cost)
        self.out_button = tkinter.Button(self.bottom_frame,  text='Выйти', command=self.main_window.destroy)

        self.cost_button.pack(side='left')
        self.out_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def show_cost(self):
        
        self.message = 'Ваши затраты = '
        
        a=0

        if self.var1.get() == 1:
            a += 30
        if self.var2.get() == 1:
            a += 20
        if self.var3.get() == 1:
            a += 40
        if self.var4.get() == 1:
            a += 100
        if self.var5.get() == 1:
            a += 35
        if self.var6.get() == 1:
            a += 200
        if self.var7.get() == 1:
            a += 20

        self.message = self.message + str(a)

        tkinter.messagebox.showinfo('Общая стоимость', self.message)
        
start = Choice()
