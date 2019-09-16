import tkinter

class Info:
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        self.text_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()
        
        self.button_inf = tkinter.Button(self.button_frame,text='Показать информацию',command = self.inf)
        self.button_out = tkinter.Button(self.button_frame,text='Выйти',command = self.main_window.destroy)

        self.button_inf.pack(side='left')
        self.button_out.pack(side='left')

        self.text_frame.pack()
        self.button_frame.pack()


    def inf(self):
        self.label = tkinter.Label(self.text_frame, text = 'Стивен Маркус\n 274 Бейли\n Уэйнзвиль, Северная Каролина 27999')
        self.label.pack(side = 'left')

    
but=Info()
