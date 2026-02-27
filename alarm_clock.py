from tkinter import *
import datetime
import time
import winsound
from threading import *

root = Tk()

root.geometry("400x400")
root.configure(bg="#E2EDFF")

def Threading():
    t1 = Thread(target=alarm)
    t1.start()

def alarm():
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)

        if current_time == set_alarm_time:
            print("Time to Wake up")
            for _ in range(10):
                winsound.Beep(6000, 300)  # 300ms beep
                time.sleep(0.1)
           

header_frame = Frame(root, bg="white", bd=2, relief=RIDGE, height=40, width=250)
header_frame.pack(pady=20)
header_frame.pack_propagate(False)

Label(header_frame, text="⏰ Alarm Clock ⏰",
      font=("Comic Sans MS", 20, "bold"),
      fg="#545092",
      bg="white").pack(expand=True)

time_frame = Frame(root, bg="#545092", bd=3, relief=RIDGE, height=35, width=200)
time_frame.pack(pady=(40, 20))
time_frame.pack_propagate(False)

Label(time_frame, text="Set a Time ⬇️",
      font=("Arial Rounded MT Bold", 13, "bold"),
      fg="white",
      bg="#FF6F91",
      anchor="w",
      padx=35).pack(expand=True)

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('00','01','02','03','04','05','06','07',
         '08','09','10','11','12','13','14','15',
         '16','17','18','19','20','21','22','23','24')
hour.set(hours[0])
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = tuple(f"{i:02}" for i in range(61))
minute.set(minutes[0])
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = tuple(f"{i:02}" for i in range(61))
second.set(seconds[0])
secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(root,
       text="Set Alarm",
       font=("Arial Rounded MT Bold", 13),
       bg="#F4F4F7",
       fg="black",
       command=Threading).pack(pady=(70, 20))

root.mainloop()
