#Наточка я люблю тебя 
import tkinter
import pygame
import time

#процесс звонка будильника
alarm_work = 0
#режим часы/будильник
alarm_mode = 0
alarm_min = 0 #минуты будильника
alarm_hour = 9 #часы будильника
a = time.localtime() #изначально время синхронизируем с временем компьютера
time_min = a.tm_min - 1 #min
time_hour = a.tm_hour #hour

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('music.mp3')


def change():

    global alarm_min, alarm_hour, time_min, time_hour
    
    time_min = (time_min + 1)%60
    if(time_min == 0):
        time_hour = (time_hour + 1)%24
    
    if(alarm_mode == 0): #если режим часов, то просто идет время
        if(time_min < 10):
            now_minute.set('0'+str(time_min))
        else:
            now_minute.set(str(time_min))

        if(time_min == 0):
            if(time_hour < 10):
                now_hour.set('0'+str(time_hour))
            else:
                now_hour.set(str(time_hour))

        pygame.mixer.music.pause()
        if(time_min == alarm_min and time_hour == alarm_hour): #если время, установленное на будильнике совпадает
                                                               #с текущим, то срабатывает будильник
            print('Пора вставать!')
            pygame.mixer.music.play()
    main_window.after(6000, change) #вызывает эту же функцию спустя минуту
    #60000 = 1 минин

    
def plus_minute(): #увеличение минут на единицу

    global alarm_min, time_min
    if(alarm_mode == 0):
        time_min = (time_min + 1)%60
        if(time_min < 10):
            now_minute.set('0'+str(time_min))
        else:
            now_minute.set(str(time_min))
    else:
        alarm_min = (alarm_min + 1)%60
        if(alarm_min < 10):
            now_minute.set('0'+str(alarm_min))
        else:
            now_minute.set(str(alarm_min))

def plus_hour(): #увеличение часов на единицу

    global alarm_hour, time_hour
    if(alarm_mode == 0):
        time_hour = (time_hour + 1)%24
        if(time_hour < 10):
            now_hour.set('0'+str(time_hour))
        else:
            now_hour.set(str(time_hour))
    else:
        alarm_hour = (alarm_hour + 1)%24
        if(alarm_hour < 10):
            now_hour.set('0'+str(alarm_hour))
        else:
            now_hour.set(str(alarm_hour))

def wait(): #если будильник звенит, то он откладывается на 5 минут и через 5 минут звонит снова

    global alarm_mode, alarm_min, alarm_hour
    if(time_min == alarm_min and time_hour == alarm_hour and alarm_mode == 0):
        pygame.mixer.music.pause()
        alarm_min = (alarm_min + 5)%60
        if(alarm_min == 0):
            alarm_hour = (alarm_hour + 1)%24

def make_alarm(): #смена режимов

    global alarm_mode, alarm_min, alarm_hour
    alarm_mode = (alarm_mode+1)%2
    if(alarm_mode == 1): #если режим будильника, то вызывается предыдущая функция
        print('Режим будильника')
        if(alarm_hour < 10):
            now_hour.set('0'+str(alarm_hour))
        else:
            now_hour.set(str(alarm_hour))
        if(alarm_min < 10):
            now_minute.set('0'+str(alarm_min))
        else:
            now_minute.set(str(alarm_min))

    else:
        print('Режим часов')
        if(time_hour < 10):
            now_hour.set('0'+str(time_hour))
        else:
            now_hour.set(str(time_hour))
        if(time_min < 10):
            now_minute.set('0'+str(time_min))
        else:
            now_minute.set(str(time_min))   

    if(time_min == alarm_min and time_hour == alarm_hour and alarm_mode == 1):
        pygame.mixer.music.pause()     

if __name__=="__main__":
               
    main_window = tkinter.Tk()

    time_frame = tkinter.Frame()
    button_frame = tkinter.Frame()

    now_hour = tkinter.StringVar()
    a = time.localtime()
    b = a.tm_hour
    if(int(b) < 10):
        now_hour.set('0'+str(b))
    else:
        now_hour.set(str(b))

    hour_label = tkinter.Label(time_frame, textvariable=now_hour)
    hour_label.pack(side='left')

    middle_label = tkinter.Label(time_frame, text=":")
    middle_label.pack(side='left')
        
    now_minute = tkinter.StringVar()
    d = a.tm_min
    if(int(d) < 10):
        now_minute.set('0'+str(d))
    else:
        now_minute.set(str(d))
    
    min_label = tkinter.Label(time_frame, textvariable=now_minute)
    min_label.pack(side='left')

    b1_button = tkinter.Button(button_frame, text='h', command=plus_hour)
    b1_button.pack(side='left')

    b2_button = tkinter.Button(button_frame, text='m', command=plus_minute)
    b2_button.pack(side='left')

    b3_button = tkinter.Button(button_frame, text='a', command=make_alarm)
    b3_button.pack(side='left')

    b4_button = tkinter.Button(button_frame, text='еще 5 минуток', command=wait)
    b4_button.pack(side='left')
        
    time_frame.pack()
    button_frame.pack()

    change()
                 
    main_window.mainloop()
