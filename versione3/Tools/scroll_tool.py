import pyautogui
import time



attesa = 5


for i in range(attesa):
    print(f"Scroll tra {attesa-i} secondi")
    time.sleep(1)

pyautogui.scroll(-130)  # Spostati con la rotellina in giù