#For any additional informations don't hesitate to contact me.
#Also do not forget to star my work on GitHub! https://github.com/seifbg

from tkinter import *                           #Tkinter for GUI
from tkinter.messagebox import showerror
import datetime
import time
import winsound

def alarm(set_alarm_timer):     #The main function in this program, it will compare the time entered by the user with the actual pc time
    while True:                    #as it prompts the actual time each second
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:", date)
        print(now)
        if now == set_alarm_timer:
            print("Time to wake up")
            winsound.PlaySound("Alarm01", winsound.SND_ASYNC). #You can add any sound here, you only need to add the sound file into the python project folder
            break

def actual_time():                          #A function to verify the input before applying the alarm() function.
        set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
        if(hour.get().isdigit() and min.get().isdigit() and sec.get().isdigit()):
            alarm(set_alarm_timer)
        else:
            showerror(title='Syntax Error', message='Please make sure you filled it correctly!')

#This is the GUI Part
clock = Tk()

clock.title("Alarm Clock 2023")  #Application title
clock.geometry("400x200")        #Frame Size
clock.resizable(width=FALSE,height=FALSE)         #The application cannot be re-sized. Turn it to TRUE if you want to resize it manually.


#All the labels and buttons needed.
time_format = Label(clock, text="Enter time in 24 hours format!", fg="black", font=("Arial",9)).place(x=145,y=132)
addTime = Label(clock,text=" Hour     Min   Sec",font=80).place(x = 110, y=30)
setYourAlarm = Label(clock,text="When to wake you up?", fg="Blue", relief="flat",font=("Helevetica",7,"bold")).place(x=140,y=10)
remarque = Label(clock, text="Important:", fg="red", font=("Windows",10,"italic")).place(x=80,y=131)
copyright_text = Label(clock, text="Made by SEIFEDDINE BEN GHARBIA",fg="green",font=("Myanmar Text",10)).place(x=170,y=180)
submit = Button(clock,text = "Set Alarm", fg="Blue", width=10,command = actual_time).place(x=160, y=90)


#Defining Variables so we can use them later in the code.
hour = StringVar()
min = StringVar()
sec = StringVar()

#Those are the inputs that the user must fill.
hourTime = Entry(clock, textvariable=hour, bg="pink", width=10).place(x=110, y=60)
minTime = Entry(clock, textvariable=min, bg="pink", width=10).place(x=170, y=60)
secTime = Entry(clock, textvariable=sec, bg="pink", width=10).place(x=230, y=60)



#The application will work endlessly until it is stopped manually.
clock.mainloop()
