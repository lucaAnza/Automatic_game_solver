# Questo tool serve per calibrare bene lo scroll del mouse. Questo permette di avviare il minigioco.

import pyautogui
import time


attesa = 5

for i in range(attesa):
    print(f"Scroll tra {attesa-i} secondi")
    time.sleep(1)

pyautogui.scroll(-70)  # Spostati con la rotellina in giù