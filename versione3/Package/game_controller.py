from Package import webhook
from Package import print_coloured
from Package import solverBot
from Package import screenBot
from Package import analyseBot
import time
import sys
import pyautogui
import cv2
import tracemalloc
import subprocess
import pyfiglet
from colorama import Fore, Style
from Package import globals


def failed_game_wh():
    webhook.webhook_print(globals.chri_webhook , "Error" , "Partita non avviata per eccezione, script terminato" , color = 'ff0000')
    


def game_started_successfully():
    webhook.webhook_print(globals.chri_webhook , "Success" , "Partita avviata correttamente" , color = '00ff00')


def check_error():
    print_coloured.print_cyan_ts("Possibile conflitto trovato... going to sleep")
    webhook.webhook_print(globals.chri_webhook , "Intervento" , "Situazione di stallo, going to sleep" , color = 'ff0000')
    time.sleep(8)
    solverBot.send_native_touch(start = (1100 , 540) , end = (1100 , 540) , speed=0.1)    # Clicca torna a giocare
    solverBot.send_native_touch(start = (1100 , 540) , end = (1100 , 540) , speed=1)    # Clicca torna a giocare

def stall_fixed():
    print_coloured.print_cyan_ts("Conflitto superato... continuo a giocare")
    webhook.webhook_print(globals.chri_webhook , "Intervento" , "Conflitto superato... continuo a giocare! " , color = '00ff00')
    


def create_new_game():
    webhook.webhook_print(globals.chri_webhook , "Iterazioni raggiunte" , "Chiusura partita attuale" , color = 'ff0000')
    
    #Logica per riavere la matrice funzionale 
    time.sleep(20)
    solverBot.send_native_touch(start = (1100 , 540) , end = (1100 , 540) , speed=0.1)    # Clicca torna a giocare
    solverBot.send_native_touch(start = (1100 , 540) , end = (1100 , 540) , speed=1)    # Clicca torna a giocare
    time.sleep(2)

    label = f'kz32'
    screenBot.take_screenshot(870, 330, 490, 620, label)
    img_name = f"./Screenshot/screenshot{label}.png"
    immagine = cv2.imread(img_name)
    if immagine is None:
        print("Errore nel caricamento dell'immagine [ game_controller.py [create_new_game()]  ]")
        sys.exit()

    matrix_number = analyseBot.get_matrix_item(immagine , type="Number" , x = globals.x_global , y = globals.y_global , side = globals.side_global)  
    
    counter = 0
    analyseBot.print_matrix(matrix_number)
    # esegue mossa fino a quando la matrice risulta leggibile -> tempo da bruciare
    while (analyseBot.checkMatrixProduct(matrix_number) != 0):
        label = f'kz32'
        screenBot.take_screenshot(870, 330, 490, 620, label)
        img_name = f"./Screenshot/screenshot{label}.png"
        immagine = cv2.imread(img_name)
        if immagine is None:
            print("Errore nel caricamento dell'immagine [ game_controller.py [create_new_game()] ")
            sys.exit()
        matrix_number = analyseBot.get_matrix_item(immagine , type="Number" , x = globals.x_global , y = globals.y_global , side = globals.side_global)   

        if counter % 10 == 0:      # Debug
            print_coloured.print_green_ts("Partita in chiusura... attendere")
        
        solverBot.send_native_touch(start = (920 , 395) , end = (920 , 490) , speed=0.5)    # Esegue M[0][0] giu' 
        time.sleep(4)
        counter += 1
        
    # tempo esaurito, iniziare nuova partita
    print_coloured.print_green_ts("partita terminata! currently in the end game menu")
    time.sleep(5)
    pyautogui.click(x=1110,y=939)   # Clicca il pulsante "Torna alla sala giochi"
    time.sleep(0.5)
    pyautogui.click(x=1110,y=939)   # Clicca il pulsante "Torna alla sala giochi"  [fatto 2 volte per problemi con l'APP]
    
    
    # Macro -> 1. Slide 2. Select Game 3. Start Game
    time.sleep(4)
    pyautogui.scroll(-230)  # Spostati con la rotellina in giù
    webhook.webhook_print(globals.luke_webhook , "Update" , "🏆 Trofei 🏆" , color = '03b2f8' , img_name = "screenshot_update_trofei.png" , trofei_screen= True)
    time.sleep(4)
    solverBot.send_native_touch(start = (1100 , 930) , end = (1100 , 930) , speed=0.1)  #Select the game
    solverBot.send_native_touch(start = (1100 , 930) , end = (1100 , 930) , speed=1)    #Select the game 
    time.sleep(4)
    solverBot.send_native_touch(start = (1100 , 930) , end = (1100 , 930) , speed=0.1)  #Click start game
    solverBot.send_native_touch(start = (1100 , 930) , end = (1100 , 930) , speed=1)    #Click start game
        

#Funzione per monitorare la memoria
def memory_stats(action="None"):
        MB = 1048576
        if (action == "Start"):
            tracemalloc.start()
        if (action == "Stop"):
            tracemalloc.stop()
        if (action == "Print"):
            current, peak = tracemalloc.get_traced_memory()
            print(
                f"Istantanea = {int(current/MB)}Mb  ( {current}B )\n-----Picco = {int(peak/MB)}Mb  ( {peak}B )")
            

#Funzione che chiude il processo di Bluestack-App player e Bluestack X
def close_bluestacks():
    try:
        #Bluestacks-5 close
        powershell_command = 'Stop-Process -Name "HD-Player" -Force'  # Costruisci il comando PowerShell per chiudere BlueStacks
        subprocess.run(["powershell", "-Command", powershell_command], check=True)   # Esegui il comando PowerShell
        print("BlueStacks 5 chiuso con successo.")

        #Bluestacks-X close
        powershell_command = 'Stop-Process -Name "BlueStacks X" -Force'  # Costruisci il comando PowerShell per chiudere BlueStacks
        subprocess.run(["powershell", "-Command", powershell_command], check=True)   # Esegui il comando PowerShell
        print("BlueStacks X chiuso con successo.")

        print("Sto per cliccare il pulsante per salvare la partita")
        time.sleep(3) 
        solverBot.send_native_touch(start = (1100 , 920) , end = (1100 , 920) , speed=1)  #Click save game
        time.sleep(10)
        print("Partita salvata! vado a dormire.")

    except subprocess.CalledProcessError:
        print("Errore durante la chiusura di BlueStacks.")
        sys.exit(1)


# Stampa il menu e restituisce l'inizializzazione della variabile fig ( serve per avere una stampa formattata )
def print_menu():
    # MAIN
    print("\n\n")
    testo = "Game Solver"
    fig = pyfiglet.Figlet()
    ascii_art = fig.renderText(testo)
    print(f"{Fore.GREEN} {ascii_art} {Style.RESET_ALL}", end='')
    print(f"{Fore.GREEN}Developed by lucaAnza & Manillin !{Style.RESET_ALL}")
    print("\n\n")
    print(f"{Fore.GREEN}Press S to start! {Style.RESET_ALL}", end='')
    print(f"{Fore.GREEN}Press E to finish the game! {Style.RESET_ALL}", end='')
    fuck_it_we_ball = input("")
    if fuck_it_we_ball == 'e':
        globals.game_iteration = 0  
    elif fuck_it_we_ball != 's':
        print(f"{Fore.RED}Script terminated...{Style.RESET_ALL}")
        sys.exit(1)
    time.sleep(2)
    return fig


            