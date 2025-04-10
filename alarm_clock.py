import time 
import datetime
import pygame
import os

print(os.getcwd()) #/Users/paulinemomanyi/Desktop/DSpy
def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "DSpy_Refresher/AlarmSound.mp3"
    is_running = True
    
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        # for i in range(100000000): #test execution time to see if sleep still delays 1s
        #     pass
        if current_time==alarm_time:
            print("Wake Up!!")
            
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            
            #keep playing
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running=False
        time.sleep(1)
    
if (__name__ == "__main__"):
    alarm_time = input("Enter time as HH:MM:SS:")
    set_alarm(alarm_time)
    