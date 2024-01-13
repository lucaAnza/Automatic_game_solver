import pyautogui
from colorama import Fore, Style
import os
import cv2

if __name__ == "__main__" or __name__ == 'solverBot':
    import decoratori
    import print_coloured as p
else:

    from Package import decoratori
    from Package import print_coloured as p


# Setting
os.system("color")  # abilita i colori nella shell


# Global
delay_keyPress_single = 0.04
delay_keyPress_combo = 0.01
num_righe = 6
num_colonne = 5
offset = 100

# {Fore.GREEN}{datetime.datetime.now().strftime('%H:%M:%S:%f')[:-3]} \t
# 6a

mm1 = [
    [1, 2, 3, 3, 5],
    [2, 1, 1, 5, 5],
    [5, 5, 3, 2, 1],
    [1, 3, 3, 4, 2],
    [1, 2, 2, 3, 3],
    [5, 5, 3, 1, 5]
]

mm2 = [
    [0, 1, 3, 4, 5],
    [4, 3, 2, 1, 4],
    [1, 2, 3, 4, 5],
    [2, 2, 3, 1, 1],
    [1, 2, 2, 4, 4],
    [1, 2, 4, 4, 5]
]

mm3 = [
    [3, 3, 1, 1, 2],
    [3, 4, 1, 1, 4],
    [1, 2, 4, 3, 3],
    [1, 3, 4, 4, 2],
    [3, 3, 1, 2, 3],
    [2, 2, 1, 3, 1]
]


mm4 = [
    [6, 4, 3, 2, 1],
    [1, 2, 0, 4, 6],
    [6, 4, 3, 2, 1],
    [1, 2, 0, 4, 6],
    [6, 9, 3, 6, 1],
    [1, 2, 0, 4, 6]
]

mm5 = [
    [1, 0, 1, 0, 1],
    [2, 9, 2, 9, 2],
    [3, 0, 3, 0, 3],
    [4, 1, 4, 3, 4],
    [6, 2, 6, 2, 6],
    [7, 3, 7, 3, 7]
]


mm6 = [
    [4, 3, 1, 1, 2],
    [1, 2, 4, 4, 3],
    [4, 3, 1, 3, 1],
    [2, 3, 1, 2, 3],
    [1, 4, 3, 4, 1],
    [4, 3, 4, 3, 4]
]

x_start = 920
offset = 95
y_startR0 = 395
y_startR1 = y_startR0+offset
y_startR2 = y_startR1+offset
y_startR3 = y_startR2+offset
y_startR4 = y_startR3+offset
y_startR5 = y_startR4+offset


dizionario_movimenti_nativo = {
    # R0
    'M[0][0] basso': (x_start , y_startR0 , x_start , y_startR0+offset),
    'M[0][0] dx': (x_start , y_startR0 , x_start+offset , y_startR0),
    'M[0][1] sx': (x_start+(offset) , y_startR0 , x_start+(offset)-offset , y_startR0),
    'M[0][1] basso': (x_start+(offset) , y_startR0 , x_start+(offset) , y_startR0+offset),
    'M[0][1] dx':  (x_start+(offset) , y_startR0 , x_start+(offset)+offset , y_startR0),
    'M[0][2] sx':  (x_start+(offset*2) , y_startR0 , x_start+(offset*2)-offset , y_startR0),
    'M[0][2] basso':  (x_start+(offset*2) , y_startR0 , x_start+(offset*2) , y_startR0+offset),
    'M[0][2] dx':  (x_start+(offset*2) , y_startR0 , x_start+(offset*2)+offset , y_startR0),
    'M[0][3] sx':  (x_start+(offset*3) , y_startR0 , x_start+(offset*3)-offset , y_startR0),
    'M[0][3] basso':  (x_start+(offset*3) , y_startR0 , x_start+(offset*3) , y_startR0+offset),
    'M[0][3] dx':  (x_start+(offset*3) , y_startR0 , x_start+(offset*3)+offset , y_startR0),
    'M[0][4] sx':  (x_start+(offset*4) , y_startR0 , x_start+(offset*4)-offset , y_startR0),
    'M[0][4] basso':  (x_start+(offset*4) , y_startR0 , x_start+(offset*4) , y_startR0+offset),
    # R1
    'M[1][0] basso': (x_start,y_startR1,x_start,y_startR1+offset),
    'M[1][0] dx': (x_start,y_startR1,x_start+offset,y_startR1),
    'M[1][0] alto': (x_start,y_startR1,x_start,y_startR1-offset),
    'M[1][1] sx': (x_start+(offset),y_startR1,x_start+(offset)-offset,y_startR1),
    'M[1][1] basso': (x_start+(offset),y_startR1,(x_start+(offset)),y_startR1+offset),
    'M[1][1] dx': (x_start+(offset),y_startR1,x_start+(offset)+offset,y_startR1),
    'M[1][1] alto': (x_start+(offset),y_startR1,x_start+(offset),y_startR1-offset),
    'M[1][2] sx': (x_start+(offset*2),y_startR1,x_start+(offset*2)-offset,y_startR1),
    'M[1][2] basso': (x_start+(offset*2),y_startR1,x_start+(offset*2),y_startR1+offset),
    'M[1][2] dx': (x_start+(offset*2),y_startR1,x_start+(offset*2)+offset,y_startR1),
    'M[1][2] alto': (x_start+(offset*2),y_startR1,x_start+(offset*2),y_startR1-offset),
    'M[1][3] sx': (x_start+(offset*3),y_startR1,x_start+(offset*3)-offset,y_startR1),
    'M[1][3] basso': (x_start+(offset*3),y_startR1,x_start+(offset*3),y_startR1+offset),
    'M[1][3] dx': (x_start+(offset*3),y_startR1,x_start+(offset*3)+offset,y_startR1),
    'M[1][3] alto': (x_start+(offset*3),y_startR1,x_start+(offset*3),y_startR1-offset),
    'M[1][4] sx': (x_start+(offset*4),y_startR1,x_start+(offset*4)-offset,y_startR1),
    'M[1][4] basso': (x_start+(offset*4),y_startR1,x_start+(offset*4),y_startR1+offset),
    'M[1][4] alto': (x_start+(offset*4),y_startR1,x_start+(offset*4),y_startR1-offset),
    # R2
    'M[2][0] basso': (x_start,y_startR2,x_start,y_startR2+offset),
    'M[2][0] dx': (x_start,y_startR2,x_start+offset,y_startR2),
    'M[2][0] alto': (x_start,y_startR2,x_start,y_startR2-offset),
    'M[2][1] sx': (x_start+(offset),y_startR2,x_start+(offset)-offset,y_startR2),
    'M[2][1] basso': (x_start+(offset),y_startR2,(x_start+(offset)),y_startR2+offset),
    'M[2][1] dx': (x_start+(offset),y_startR2,x_start+(offset)+offset,y_startR2),
    'M[2][1] alto': (x_start+(offset),y_startR2,x_start+(offset),y_startR2-offset),
    'M[2][2] sx': (x_start+(offset*2),y_startR2,x_start+(offset*2)-offset,y_startR2),
    'M[2][2] basso': (x_start+(offset*2),y_startR2,x_start+(offset*2),y_startR2+offset),
    'M[2][2] dx': (x_start+(offset*2),y_startR2,x_start+(offset*2)+offset,y_startR2),
    'M[2][2] alto': (x_start+(offset*2),y_startR2,x_start+(offset*2),y_startR2-offset),
    'M[2][3] sx': (x_start+(offset*3),y_startR2,x_start+(offset*3)-offset,y_startR2),
    'M[2][3] basso': (x_start+(offset*3),y_startR2,x_start+(offset*3),y_startR2+offset),
    'M[2][3] dx': (x_start+(offset*3),y_startR2,x_start+(offset*3)+offset,y_startR2),
    'M[2][3] alto': (x_start+(offset*3),y_startR2,x_start+(offset*3),y_startR2-offset),
    'M[2][4] sx': (x_start+(offset*4),y_startR2,x_start+(offset*4)-offset,y_startR2),
    'M[2][4] basso': (x_start+(offset*4),y_startR2,x_start+(offset*4),y_startR2+offset),
    'M[2][4] alto': (x_start+(offset*4),y_startR2,x_start+(offset*4),y_startR2-offset),
    # R3
    'M[3][0] basso': (x_start,y_startR3,x_start,y_startR3+offset),
    'M[3][0] dx':(x_start,y_startR3,x_start+offset,y_startR3),
    'M[3][0] alto': (x_start,y_startR3,x_start,y_startR3-offset),
    'M[3][1] sx': (x_start+(offset),y_startR3,x_start+(offset)-offset,y_startR3),
    'M[3][1] basso': (x_start+(offset),y_startR3,(x_start+(offset)),y_startR3+offset),
    'M[3][1] dx': (x_start+(offset),y_startR3,x_start+(offset)+offset,y_startR3),
    'M[3][1] alto': (x_start+(offset),y_startR3,x_start+(offset),y_startR3-offset),
    'M[3][2] sx': (x_start+(offset*2),y_startR3,x_start+(offset*2)-offset,y_startR3),
    'M[3][2] basso': (x_start+(offset*2),y_startR3,x_start+(offset*2),y_startR3+offset),
    'M[3][2] dx': (x_start+(offset*2),y_startR3,x_start+(offset*2)+offset,y_startR3),
    'M[3][2] alto': (x_start+(offset*2),y_startR3,x_start+(offset*2),y_startR3-offset),
    'M[3][3] sx': (x_start+(offset*3),y_startR3,x_start+(offset*3)-offset,y_startR3),
    'M[3][3] basso': (x_start+(offset*3),y_startR3,x_start+(offset*3),y_startR3+offset),
    'M[3][3] dx': (x_start+(offset*3),y_startR3,x_start+(offset*3)+offset,y_startR3),
    'M[3][3] alto': (x_start+(offset*3),y_startR3,x_start+(offset*3),y_startR3-offset),
    'M[3][4] sx': (x_start+(offset*4),y_startR3,x_start+(offset*4)-offset,y_startR3),
    'M[3][4] basso': (x_start+(offset*4),y_startR3,x_start+(offset*4),y_startR3+offset),
    'M[3][4] alto': (x_start+(offset*4),y_startR3,x_start+(offset*4),y_startR3-offset),
       # R4
    'M[4][0] basso': (x_start,y_startR4,x_start,y_startR4+offset),
    'M[4][0] dx': (x_start,y_startR4,x_start+offset,y_startR4),
    'M[4][0] alto': (x_start,y_startR4,x_start,y_startR4-offset),
    'M[4][1] sx': (x_start+(offset),y_startR4,x_start+(offset)-offset,y_startR4),
    'M[4][1] basso': (x_start+(offset),y_startR4,(x_start+(offset)),y_startR4+offset),
    'M[4][1] dx': (x_start+(offset),y_startR4,x_start+(offset)+offset,y_startR4),
    'M[4][1] alto': (x_start+(offset),y_startR4,x_start+(offset),y_startR4-offset),
    'M[4][2] sx': (x_start+(offset*2),y_startR4,x_start+(offset*2)-offset,y_startR4),
    'M[4][2] basso': (x_start+(offset*2),y_startR4,x_start+(offset*2),y_startR4+offset),
    'M[4][2] dx': (x_start+(offset*2),y_startR4,x_start+(offset*2)+offset,y_startR4),
    'M[4][2] alto': (x_start+(offset*2), y_startR4, x_start+(offset*2), y_startR4-offset),
    'M[4][3] sx': (x_start+(offset*3),y_startR4,x_start+(offset*3)-offset,y_startR4),
    'M[4][3] basso': (x_start+(offset*3),y_startR4,x_start+(offset*3),y_startR4+offset),
    'M[4][3] dx': (x_start+(offset*3),y_startR4,x_start+(offset*3)+offset,y_startR4),
    'M[4][3] alto': (x_start+(offset*3),y_startR4,x_start+(offset*3),y_startR4-offset),
    'M[4][4] sx': (x_start+(offset*4),y_startR4,x_start+(offset*4)-offset,y_startR4),
    'M[4][4] basso': (x_start+(offset*4),y_startR4,x_start+(offset*4),y_startR4+offset),
    'M[4][4] alto':  (x_start+(offset*4),y_startR4,x_start+(offset*4),y_startR4-offset),
    # R5
    'M[5][0] dx': (x_start,y_startR5,x_start+offset,y_startR5),
    'M[5][0] alto': (x_start,y_startR5,x_start,y_startR5-offset),
    'M[5][1] sx': (x_start+(offset),y_startR5,x_start+(offset)-offset,y_startR5),
    'M[5][1] dx': (x_start+(offset),y_startR5,x_start+(offset)+offset,y_startR5),
    'M[5][1] alto': (x_start+(offset),y_startR5,x_start+(offset),y_startR5-offset),
    'M[5][2] sx': (x_start+(offset*2),y_startR5,x_start+(offset*2)-offset,y_startR5),
    'M[5][2] dx': (x_start+(offset*2),y_startR5,x_start+(offset*2)+offset,y_startR5),
    'M[5][2] alto': (x_start+(offset*2),y_startR5,x_start+(offset*2),y_startR5-offset),
    'M[5][3] sx': (x_start+(offset*3),y_startR5,x_start+(offset*3)-offset,y_startR5),
    'M[5][3] dx': (x_start+(offset*3),y_startR5,x_start+(offset*3)+offset,y_startR5),
    'M[5][3] alto': (x_start+(offset*3),y_startR5,x_start+(offset*3),y_startR5-offset),
    'M[5][4] sx': (x_start+(offset*4),y_startR5,x_start+(offset*4)-offset,y_startR5),
    'M[5][4] alto': (x_start+(offset*4),y_startR5,x_start+(offset*4),y_startR5-offset),
}


@decoratori.timestamp_decorator
def send_input_gui(string):
    p.print_red_ts(f"COMANDO PASSATO: {string}")

    c1, c2 = string.split('+')
    if c2 != '':  # se si usa CTRL o ALT come opzione
        p.print_green_ts(f"Pressed Key: {c1}+{c2}")
        pyautogui.hotkey(c1, c2, interval=delay_keyPress_combo)
    else:
        p.print_green_ts(f"Pressed Key: {c1}")
        pyautogui.press(c1, interval=delay_keyPress_single)

#Funzione che dati in input start(x,y) e end(x,y) clicca sullo schermo partendo da start e arriva in end in speed secondi.
@decoratori.timestamp_decorator
def send_native_touch( start = (0,0) , end = (0,0) , speed = 0.002 ):
    #print(f"clicked - start = ({start[0] , start[1]}) e end = ({end[0] , end[1]})")
    pyautogui.moveTo(start, duration=0.001)
    pyautogui.mouseDown()  #Click left mouse
    pyautogui.moveTo(end , duration=speed)  
    pyautogui.mouseUp()  #Release left mouse
    pyautogui.moveTo(1205,960, duration=0.001)  # esci dalla zona utile



# Funzione che ritorna l'indice di colonna del primo elemento di una successione di 2
def check_adj_row(l):
    for i in range(len(l)):  # range 0-4
        '''print(
            f'check index {i} -> is M[{i}]-> {l[i]} == M[{i+1}]-> {l[i+1]}')'''
        if (i == 4):
            return -1
        elif l[i] == 5:  # stella
            return i+offset
        else:
            if l[i] == l[i+1]:
                return i


def check_adj_row2(l):
    temp_adj = []
    for i in range(len(l)):  # range 0-4
        if (i == 4):
            break
        elif l[i] == 5:  # stella
            # Per fare in modo che esista sempre un elemento temp_adj[0]
            temp_adj.append(-1)
            temp_adj[0] = i+offset
            return temp_adj
        else:
            if l[i] == l[i+1]:
                temp_adj.append(i)
    return temp_adj


# MANCA: controllo in line se indice minore di 4


def check_adj_column(M, j):
    for i in range(6):
        if (i == 5):
            return -1
        else:
            if M[i][j] == M[i+1][j]:
                return i


def check_adj_column2(M, j):
    temp_adj = []
    for i in range(6):
        if (i == 5):
            break
        else:
            if M[i][j] == M[i+1][j]:
                temp_adj.append(i)
    return temp_adj


# controlla che il range sia valido per controllo orizzontale (e verticale outofline)
def valid_bound(i, j):
    if ((i >= 0 and i <= 5) and (j >= 0 and j <= 4)):
        return True
    p.print_red_ts(f"(((OOB)))")
    return False


# controlla che il range sia valido per controllo verticale
def valid_col_bound(i):
    if (i >= 0 and i <= 5):
        return True
    p.print_red_ts(f"(((OOB)))")
    return False

# @decoratori.timestamp_decorator


def check_column_feasibility(i, j, matrice):
    el1 = matrice[i][j]
    el2 = matrice[i+1][j]

    # controllo sinistra
    if ((valid_bound(i-1, j-1)) and (matrice[i-1][j-1] == el1)):
        return (f"M[{i-1}][{j-1}] dx")

    elif ((valid_bound(i+2, j-1)) and (matrice[i+2][j-1] == el2)):
        return (f"M[{i+2}][{j-1}] dx")

    # controllo destra
    elif (valid_bound(i-1, j+1) and (matrice[i-1][j+1] == el1)):
        return (f"M[{i-1}][{j+1}] sx")

    elif (valid_bound(i+2, j+1) and (matrice[i+2][j+1] == el2)):
        return (f"M[{i+2}][{j+1}] sx")

    # Controllo in line alto - basso
    elif ((valid_col_bound(i+3)) and (matrice[i+3][j] == el2)):
        return (f"M[{i+3}][{j}] alto")

    elif ((valid_col_bound(i-2)) and (matrice[i-2][j] == el1)):
        return (f"M[{i-2}][{j}] basso")

    # nessuna possibile mossa trovata
    p.print_red_ts(
        f"Nessuna mossa valida trovata per elemento M[{i}][{j}] -> {matrice[i][j]}\n")
    return False


# @decoratori.timestamp_decorator
def check_row_feasibility(i, j, matrice):
    el1 = matrice[i][j]
    el2 = matrice[i][j+1]
    # controllo inline dx e sx:
    if (valid_bound(i, j-2) and (matrice[i][j-2] == el1)):
        return (f"M[{i}][{j-2}] dx")

    elif (valid_bound(i, j+3) and (matrice[i][j+3] == el2)):
        return (f"M[{i}][{j+3}] sx")

    # controllo elementi di sinistra:
    elif (valid_bound(i-1, j-1) and (matrice[i-1][j-1] == el1)):
        return (f"M[{i-1}][{j-1}] basso")

    elif (valid_bound(i+1, j-1) and (matrice[i+1][j-1] == el1)):
        return (f"M[{i+1}][{j-1}] alto")

    # controllo elementi di dx:
    elif (valid_bound(i-1, j+2) and (matrice[i-1][j+2] == el2)):
        return (f"M[{i-1}][{j+2}] basso")

    elif (valid_bound(i+1, j+2) and (matrice[i+1][j+2] == el2)):
        return (f"M[{i+1}][{j+2}] alto")

    # nessuna possibile mossa trovata
    p.print_red_ts(
        f"Nessuna mossa valida trovata per elemento M[{i}][{j}] -> {matrice[i][j]}\n")
    return False


def check_hop_adj_row(l):
    temp_hops = []
    for i in range(len(l)):
        if (i == 3):
            break
        elif l[i] == l[i+2]:
            temp_hops.append(i)
    return temp_hops


def check_hop_adj_col(M, j):
    temp_hops = []
    for i in range(6):
        if (i == 4):
            break
        else:
            if M[i][j] == M[i+2][j]:
                temp_hops.append(i)
    return temp_hops


def check_hop_row_feasibility(i, j, M):
    el1 = M[i][j]
    # controllo superiore:
    if ((valid_bound(i-1, j+1)) and (M[i-1][j+1] == el1)):
        return (f"M[{i-1}][{j+1}] basso")
    elif ((valid_bound(i+1, j+1)) and (M[i+1][j+1] == el1)):
        return (f"M[{i+1}][{j+1}] alto")

    p.print_red_ts(f"Nessuna mossa valida trovata per hop M[{i}][{j}]\n")
    return False


def check_hop_column_feasibility(i, j, M):
    el1 = M[i][j]
    if ((valid_bound(i+1, j-1)) and (M[i+1][j-1] == el1)):
        return (f"M[{i+1}][{j-1}] dx")
    elif ((valid_bound(i+1, j+1)) and (M[i+1][j+1] == el1)):
        return (f"M[{i+1}][{j+1}] sx")
    p.print_red_ts(f"Nessuna mossa valida trovata per hop M[{i}][{j}]\n")
    return False


@decoratori.timestamp_decorator
def scan_matrice(matrice):
    mossa = False
    for i in range(6):  # controllo per righe
        if mossa == True:
            break
        #### LOGICA CON LISTA DI INDICI:####

        l_adj = check_adj_row2(matrice[i])  # Ritorna indice di colonna

        if len(l_adj) == 0:
            p.print_red_ts(f"Nessun elemento adiacente nella riga: {i}\n")
        # Condizione Stella
        elif l_adj[0] >= offset:
            c = l_adj[0]
            c = c-offset
            p.print_magenta_ts(f"Stella trovata in posizione [{i}][{c}]")
            if (i == 5):    # Nel caso la stella sia in fondo
                # OLD = send_input_gui(dizionario_movimenti[f'M[{i}][{c}] alto'])
                print(f'dizionario_movimenti_nativo[M[{i}][{c}] alto]')
                cc = dizionario_movimenti_nativo[f'M[{i}][{c}] alto']
                send_native_touch( start=(cc[0] , cc[1]) , end = (cc[2] , cc[3]))
            else:
                # OLD = send_input_gui(dizionario_movimenti[f'M[{i}][{c}] basso'])
                print(f'dizionario_movimenti_nativo[M[{i}][{c}] basso]')
                cc = dizionario_movimenti_nativo[f'M[{i}][{c}] basso']
                send_native_touch( start=(cc[0] , cc[1]) , end = (cc[2] , cc[3]))
            mossa = True
            break
        # Condizione di adiacenza sulla riga
        elif len(l_adj) > 0:
            p.print_green_ts(f"Trovati elementi simili nella riga {i}")
            p.print_magenta_ts(f"Inizio controllo feasibility <Row {i}>")

            # CONTROLLO RIGA
            # ciclo per iterare gli indici con adiacenze
            for k in range(len(l_adj)):
                p.print_green_ts(f"Controllo coppia adiacente n.{k+1}")
                move = check_row_feasibility(i, l_adj[k], matrice)
                if move and isinstance(move, str):  # mossa valida trovata
                    p.print_magenta_ts("pass!")
                    # OLD =  send_input_gui(dizionario_movimenti[move])
                    print(f'dizionario_movimenti_nativo[{move}]]')
                    cc = dizionario_movimenti_nativo[move]
                    send_native_touch( start=(cc[0] , cc[1]) , end = (cc[2] , cc[3]))
                    mossa = True
                    break
                print()
        # condizione no adiacenza della riga
        else:
            p.print_red_ts(
                f"Errore non determinato -> check SolverBot.scan_matrice() \n")

    # CONTROLLO COLONNE
    exit = False
    if mossa != True:
        p.print_magenta_ts("    -->>Controllo colonne<<--    \n")
        for j in range(5):  # controllo per colonne
            if exit == True:
                break
            col_adj = check_adj_column2(matrice, j)
            if len(col_adj) > 0:  # condizione di adiacenza
                p.print_green_ts(f"Trovati elementi simili nella colonna: {j}")

                # CONTROLLO COLONNA
                for k in range(len(col_adj)):
                    p.print_green_ts(f"Controllo coppia adiacente n.{k}")
                    move2 = check_column_feasibility(col_adj[k], j, matrice)
                    if move2 and isinstance(move2, str):  # mossa valida trovata
                        p.print_magenta_ts("pass!")
                        # OLD =  send_input_gui(dizionario_movimenti[move2])
                        print(f'dizionario_movimenti_nativo[{move2}]]')
                        cc = dizionario_movimenti_nativo[move2]
                        send_native_touch( start=(cc[0] , cc[1]) , end = (cc[2] , cc[3]))
                        exit = True
                        mossa = True
                        break
                    print()
            else:
                p.print_red_ts(f"Nessun elemento adiacente nella colonna: {j}")

    if mossa != True:
        p.print_cyan_ts(
            f"Nessuna soluzione trovata per adiacenze... Inizio controllo by hop")
        # CONTROLLO HOP ORIZZONTALI
        for i in range(6):
            if mossa == True:
                break
            hops_or = check_hop_adj_row(matrice[i])
            if len(hops_or) == 0:
                p.print_red_ts(f"Nessun hop nella riga {i}")
                continue
            # hop trovato!
            else:
                p.print_green_ts(f"Trovati due hop nella riga {i}")
                p.print_magenta_ts(f"Inzio controllo feasibility <Row {i}>")
                for k in range(len(hops_or)):
                    p.print_green_ts(f"Controllo hop n.{k+1}")
                    move = check_hop_row_feasibility(i, hops_or[k], matrice)
                    if move and isinstance(move, str):
                        p.print_magenta_ts("pass!")
                        # OLD =  send_input_gui(dizionario_movimenti[move])
                        print(f'dizionario_movimenti_nativo[{move}]]')
                        cc = dizionario_movimenti_nativo[move]
                        send_native_touch( start=(cc[0] , cc[1]) , end = (cc[2] , cc[3]))
                        mossa = True
                        break

        # CONTROLLO HOP VERTICALI
        if mossa != True:
            p.print_magenta_ts("    -->>Controllo hop colonne<<-- \n")
            for j in range(5):
                if mossa == True:
                    break
                hops_vert = check_hop_adj_col(matrice, j)
                if len(hops_vert) == 0:
                    p.print_red_ts(f"Nessun hop nella colonna {j}")
                    continue
                else:
                    p.print_green_ts(f"Trovati due hop nella colonna {j}")

                    for k in range(len(hops_vert)):
                        p.print_green_ts(f"Controllo coppia adiacenze n.{k+1}")
                        move2 = check_hop_column_feasibility(
                            hops_vert[k], j, matrice)
                        if move2 and isinstance(move2, str):
                            p.print_magenta_ts("pass!")
                            # OLD =  send_input_gui(dizionario_movimenti[move2])
                            print(f'dizionario_movimenti_nativo[{move2}]]')
                            cc = dizionario_movimenti_nativo[move2]
                            send_native_touch( start=(cc[0] , cc[1]) , end = (cc[2] , cc[3]))
                            mossa = True
                            break
        if mossa != True:
            p.print_red_ts("NESSUNA MOSSA VALIDA ---> CHECK: scan_matrice\n")


# Funzione che passata un img aperta con opencv2, restituisce una matrice di immagini ritagliate


def matrix_from_img(img, delay=200, open_img=False):
    # Dimnensione immagine
    altezza_immagine, larghezza_immagine, _ = img.shape

    # Calcola le dimensioni delle celle nella tua nuova griglia
    larghezza_cella = larghezza_immagine // num_colonne
    altezza_cella = altezza_immagine // num_righe

    coordinate_celle = []

    matrice_immagini = [
        [],
        [],
        [],
        [],
        [],
        []
    ]

    for riga in range(num_righe):
        for colonna in range(num_colonne):
            # Calcola le coordinate della cella corrente
            x1 = colonna * larghezza_cella
            y1 = riga * altezza_cella
            x2 = x1 + larghezza_cella
            y2 = y1 + altezza_cella

            # Aggiungi le coordinate alla lista
            coordinate_celle.append((x1, y1, x2, y2))

            # Ritaglia la cella dall'immagine
            cell_img = img[y1:y2, x1:x2]
            # cv2.imshow("Cella Ritagliata", cell_img)
            # cv2.waitKey(2000)
            matrice_immagini[riga].append(cell_img)

    if (open_img):
        cont = 1
        for i in range(num_righe):
            for j in range(num_colonne):
                cv2.imshow(f"Immagine {cont}",
                           matrice_immagini[i][j])
                cv2.waitKey(delay)
                cont += 1
        cv2.destroyAllWindows()

    return matrice_immagini


# MAIN
if (__name__ == '__main__'):
    scan_matrice(mm6)