import os
import time
import pygame

def clear_screen():
    os.system('cls')

def alarm(duration_seconds):
    elapsed_time = 0
    clear_screen()

    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        alarm_file = os.path.join(current_dir, "alarm.mp3")
        pygame.mixer.init()
        sound = pygame.mixer.Sound(alarm_file)

        while elapsed_time < duration_seconds:
            time.sleep(1)
            elapsed_time += 1
            remaining_time = duration_seconds - elapsed_time
            minutes_left = remaining_time // 60
            seconds_left = remaining_time % 60
            print(f"Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}", end="\r",flush=True)

        sound.play()
        while pygame.mixer.get_busy():
            continue
    except Exception as e:
        print(f"\nAn error occurred while playing the sound: {e}")
    finally:
        clear_screen()
        pygame.mixer.quit()

# Set the duration for the alarm in seconds
alarm_duration = 5
alarm(alarm_duration)