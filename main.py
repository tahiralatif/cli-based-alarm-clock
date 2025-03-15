from datetime import datetime
from playsound import playsound  

alarm_time = input("Enter the time of alarm you want to set: HH:MM:SS AM/PM\n").strip()

alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()  

print(f"⏰ Alarm set for {alarm_time}...")

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")  

    if alarm_hour == current_hour and alarm_minute == current_minute and alarm_seconds == current_seconds and alarm_period == current_period:
        print("🚨 Wake Up! 🚨")
        playsound('alarm_sound.mp3')  
        break  
