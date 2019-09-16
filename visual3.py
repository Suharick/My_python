import tkinter

class Count:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.text1_frame = tkinter.Frame()
        self.text2_frame = tkinter.Frame()
        self.text3_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.gallon_label = tkinter.Label(self.text1_frame, text='Введите кол-во галлонов:')
        self.gallon_entry = tkinter.Entry(self.text1_frame, width=10)

        self.gallon_label.pack(side='left')
        self.gallon_entry.pack(side='left')

        self.mil_label = tkinter.Label(self.text2_frame, text='Введите кол-во миль:')
        self.mil_entry = tkinter.Entry(self.text2_frame, width=10)

        self.mil_label.pack(side='left')
        self.mil_entry.pack(side='left')

        self.result1_label = tkinter.Label(self.text3_frame, text='Мили в галлон:')
        self.value = tkinter.StringVar()
        self.result2_label = tkinter.Label(self.text3_frame, textvariable=self.value)

        self.result1_label.pack(side='left')
        self.result2_label.pack(side='left')

        self.make_button = tkinter.Button(self.bottom_frame, text='Вычислить', command=self.convert)
        self.out_button = tkinter.Button(self.bottom_frame,  text='Выйти', command=self.main_window.destroy)

        self.make_button.pack(side='left')
        self.out_button.pack(side='left')

        self.text1_frame.pack()
        self.text2_frame.pack()
        self.text3_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        
        a1 = float(self.gallon_entry.get())
        a2 = float(self.mil_entry.get())
        res = a2/a1

        self.value.set(res)

task = Count()

