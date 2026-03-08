# AlarmClock

## **Description**

I created an Alarm Clock app that allows users to set an alarm for a specific hour, minute, and second. When the alarm time is reached, the app plays a beep sound to alert the user.

## **Features**

- Users can select the hour (00-24), minute (00-60), and second (00-60) using dropdown menus.
- Users can press the "Set Alarm" button to start the alarm.
- When the alarm time is reached, it beeps multiple times to alert the user.


<img width="439" height="299" alt="Screenshot 2026-03-07 194942" src="https://github.com/user-attachments/assets/8a329c78-df2b-4e3c-ac52-064776238947" />

## **How It Works**

- I used `OptionMenu` widgets in Tkinter to create dropdowns for hour, minute, and second selections.
- The "Set Alarm" button triggers a function that continuously checks the current time.
- When the current time matches the user-set time, `winsound.Beep` is used to play the alarm sound.
  - `6000` in `winsound.Beep(6000, 300)` is the frequency in Hertz (how high or low the beep sounds).
  - `300` is the duration of each beep in milliseconds.
  - `time.sleep(0.1)` creates a short pause between consecutive beeps. 'def Threading ()'


## **Future Improvements**

- Add a snooze button for flexibility.
- Add a visual or pop-up notification in addition to the sound alarm.
