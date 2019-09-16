import tkinter

class Translator:
    def __init__(self):
        
        self.main_window = tkinter.Tk()
        
        self.text_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()

        self.text_frame.pack()
        self.button_frame.pack()

        self.value = tkinter.StringVar()
        self.text_label = tkinter.Label(self.text_frame, textvariable=self.value)
        self.text_label.pack()

        self.button_left = tkinter.Button(self.button_frame,text = 'left',command=self.left)
        self.button_medium = tkinter.Button(self.button_frame,text='medium',command=self.medium)
        self.button_right = tkinter.Button(self.button_frame,text='right',command=self.right)

        self.button_left.pack(side='left')
        self.button_medium.pack(side='left')
        self.button_right.pack(side='left')

    def left(self):
        self.value.set('левый')

    def medium(self):
        self.value.set('центральный')

    def right(self):
        self.value.set('правый')

but=Translator()
