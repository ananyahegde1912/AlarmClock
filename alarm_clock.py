# Import Required Library
from tkinter import *
import datetime
import time
import winsound
from threading import *

# Create Object
root = Tk()

# Set geometry
root.geometry("400x400")
root.configure(bg="#FDE2FF")

# Use Threading
def Threading():
	t1=Thread(target=alarm)
	t1.start()

def alarm():
	# Infinite Loop
	while True:
		# Set Alarm
		set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

		# Wait for one seconds
		time.sleep(1)

		# Get current time
		current_time = datetime.datetime.now().strftime("%H:%M:%S")
		print(current_time,set_alarm_time)

		# Check whether set alarm is equal to current time or not
		if current_time == set_alarm_time:
			print("Time to Wake up")
			# Playing sound
			winsound.PlaySound("sound.wav",winsound.SND_ASYNC)

# Add Labels, Frame, Button, Optionmenus
# ----------------- Header Frame -----------------
header_frame = Frame(root, bg="white", bd=2, relief=RIDGE, height=40, width=250)
header_frame.pack(pady=20)
header_frame.pack_propagate(False)  # keeps the frame short and fixed size

# Header Label
Label(header_frame, text="⏰ Alarm Clock ⏰",
      font=("Comic Sans MS", 20, "bold"),
      fg="#545092",
      bg="white").pack(expand=True)

time_frame = Frame(root, bg="#FF6F91", bd=3, relief=RIDGE, height=35, width=200)
time_frame.pack(pady=(40, 20))  # space below the label
time_frame.pack_propagate(False)  # keeps frame size fixed

# Label inside frame
Label(time_frame, text="Set a Time ⬇️",
      font=("Arial Rounded MT Bold", 13, "bold"),
      fg="white",
      bg="#FF6F91",
      anchor="w",      # aligns text to the left
      padx=35).pack(expand=True)



frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23', '24'
		)
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)


Button(root,
       text="Set Alarm",
       font=("Arial Rounded MT Bold", 13),
       bg="#F4F4F7",
       fg="black").pack(pady=(70, 20))

# Execute Tkinter
root.mainloop()