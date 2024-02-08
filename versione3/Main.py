import cv2
import sys
import time
import datetime
import os
from colorama import Fore, Style
from discord_webhook import DiscordWebhook, DiscordEmbed
import sys
from Package import *



try:
    # Setting
    os.system("color")  # abilita i colori nella shell

    # Globals init
    num_righe = globals.num_righe
    num_colonne = globals.num_colonne
    cpu_02 = globals.cpu_02
    x_global = globals.x_global
    y_global = globals.y_global
    side_global = globals.side_global
    # Locals init
    how_much = 2000
    consecutive_error = 0
    general_counter = 0

    # MAIN
    
    fig = game_controller.print_menu()
    game_controller.memory_stats("Start")
    game_iteration = globals.game_iteration # Here, because it could be change by print_menu()
    
    while (consecutive_error < 100):

        print(f"\n{Fore.MAGENTA}------------------Iterazione({general_counter})------------------{Style.RESET_ALL}")
        start_time = datetime.datetime.now()  # debugging tempo

        # logica per new_game:
        if general_counter == game_iteration:
            try:
                asc = fig.renderText("TERMINAZIONE GAME")
                print_coloured.print_red_ts("")
                print(f"{Fore.RED}{asc}{Style.RESET_ALL}")
                game_controller.create_new_game()
                #Ripristino variabili ciclo
                consecutive_error = 0
                general_counter = 0
                game_controller.game_started_successfully()
                time.sleep(2)
                webhook.webhook_print(globals.chri_webhook , "Update" , "Inizio partita" , color = '03b2f8' , img_name="screenshot_partita_nuova.png")
            except Exception as e:
                print_coloured.print_red_ts(e)
                time.sleep(5)
                game_controller.failed_game_wh()
                sys.exit()
                

        # potenziale fix when stuck
        if consecutive_error == 80:
            game_controller.check_error()

        
        # Ossigeno al processore
        time.sleep(cpu_02)  
      
        # Cattura screenshot
        label = f'kz32'
        screenBot.take_screenshot(870, 330, 490, 620, label)
        img_name = f"Screenshot/screenshot{label}.png"
        immagine = cv2.imread(img_name)
        if immagine is None:
            print("Errore nel caricamento dell'immagine [Main.py]")
            sys.exit()
        matrix_number = analyseBot.get_matrix_item(immagine , type="Number" , x = x_global , y = y_global , side = side_global)  

        # Se almeno un elemento non l'ha riconosciuto [ prod == 0] non entra.
        prod = analyseBot.checkMatrixProduct(matrix_number)
        if (prod != 0):

            # Debug analisi
            print(f"\n{Fore.YELLOW}Matrix : ")
            analyseBot.print_matrix(matrix_number)
            print(f"{Style.RESET_ALL}\n")

            print(
                f'{Fore.GREEN}Check della matrice andato a buon fine!{Style.RESET_ALL}')

            if consecutive_error == 80:    # Se entra cui significa che è riuscito a risolvere lo stallo
                game_controller.stall_fixed()
            consecutive_error = 0   
            solverBot.scan_matrice(matrix_number)  # Esegue una mossa in base alla matrice di item dati in input
        else:
            print(f'{Fore.RED}Error {consecutive_error} {Style.RESET_ALL}')
            # Debug analisi
            print(f"\n{Fore.YELLOW}Matrix : ")
            analyseBot.print_matrix(matrix_number)
            print(f"{Style.RESET_ALL}\n")
            consecutive_error += 1

        end_time = datetime.datetime.now()
        exe_time = end_time-start_time
        print(f"{Fore.CYAN}Tempo esecuzione WHILE : {exe_time}{Style.RESET_ALL}")
        print(f"\n{Fore.MAGENTA}------------------Iterazione({general_counter})------------------{Style.RESET_ALL}\n\n")
        general_counter += 1

        
        #Ogni [how_much] cicli, manda sul server discord un aggiornamento. E controlla che la sessione non si scaduta
        if (general_counter % how_much == 0):
            # Controllo memoria
            game_controller.memory_stats("Print")
            
            # Update bot discord
            webhook.webhook_print(globals.luke_webhook , "Update" , f"⬤ Complimenti hai raggiunto {general_counter} iterazioni!" , color = '03b2f8' , img_name=f'screenshot_{general_counter}_iterazioni.png')
            webhookL = DiscordWebhook(url=globals.luke_webhook)
            print_coloured.print_green_ts("Webhook sent!")

            # possibile caso in cui riconosce tutti 3 ( Possibile schermata bianca ) [ 3 perchè per la pizza si riconosce pixel bianco ]
            if (prod == 205891132094649):  
                print(f"Riconosciuto Matrice con prodotto pari {prod}")
                close = True
                for i in range(num_righe) : 
                    for j in range(num_colonne-1) :
                        if( matrix_number[i][j] != matrix_number[i][j+1]):
                            close = False
                if(close) : 
                    print("Chiusura bluestacks causa : Matrice composta da tutti 3")
                    # Chiude l'applicazione Bluestacks
                    game_controller.close_bluestacks()
                    sys.exit(1)
    
    game_controller.memory_stats("Stop")


except Exception as e:
    print(f"Errore{e}")
    webhook.webhook_print(globals.chri_webhook , "Errore durante l'esecuzione" , f"Error: {e}" , color = 'ff0000' )
    game_controller.close_bluestacks() # Chiude l'applicazione Bluestacks
    sys.exit(1)



# webhook in caso di terminazione
webhook.webhook_print(globals.chri_webhook , "Checkpoint" , "Script terminated... check terminal" , color = '03b2f8' )
webhook.webhook_print(globals.luke_webhook , "Update" , "TERMINAZIONE" , color = '03b2f8' , img_name='screenshot_dd_termination.png')
game_controller.close_bluestacks() # Chiude l'applicazione Bluestacks
    

