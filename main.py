# Alarm Clock
from datetime import datetime
from playsound import playsound  # Play sound

# User se alarm time input lena
alarm_time = input("Enter the time of alarm you want to set: HH:MM:SS AM/PM\n").strip()

# Alarm time ko extract karna
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()  # Upper case me convert karna taake AM/PM issue na ho

print(f"⏰ Alarm set for {alarm_time}...")


while True:
    now = datetime.now()
    current_hour = now.strftime("%I")  # 12-hour format
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")  # AM/PM

    if alarm_hour == current_hour and alarm_minute == current_minute and alarm_seconds == current_seconds and alarm_period == current_period:
        print("🚨 Wake Up! 🚨")
        playsound('alarm_sound.mp3')  # Play sound
        break  # ✅ Loop exit 