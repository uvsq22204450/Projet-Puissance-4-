import tkinter as tk
from random import randint

####################################################################################################################
#                                                                                                                  #
#   PUISSANCE 4   :    Thomas TRAN  /  Lis Ainhoa ALFARO LANDA   /   Hugo BOUZINAC   /   Clémentine HELLEGOUARCH   #
#                                                                                                                  #
####################################################################################################################


tour_joueur = randint(1,2) #choisi aléatoirement le joueur qui commence
L = []
MODE_PARTIE = 0
NB_COUP = 0 #nombre de coup joué 
PARTIE = 0 
DERNIER_COUP_I = 0 #la coordonnée i du dernier coupe joué
DERNIER_COUP_J = 0 #la coordonnée j du dernier coup joué
FIRST = tour_joueur #la couleur du joueur qui joue en premier
R = 0 #nombre de victoire du joueur rouge
J = 0 #nombre de victoire du joueur jaune

def widget_acceuil():
    global acceuil_jouer
    global acceuil_charger_partie
    global partie_normale
    global partie_personnalisee
    global entree_WIDTH
    global entree_HEIGHT
    global entree_GAGNE
    global valider
    global partie_aveugle
    global case_GAGNE
    global case_HEIGHT
    global case_WIDTH

    acceuil_jouer = tk.Button(racine, command = jouer, text = "JOUER", font=("helvetica", "40"), relief = "flat", bg = "#141414", fg = "gray69", width = 15)
    acceuil_charger_partie = tk.Button(racine, command = importer, text = "IMPORTER", font=("helvetica", "40"), relief = "flat", bg = "#141414", fg = "gray69", width = 15)
    partie_normale = tk.Button(racine, command = lambda : plateau(6, 7, 4, 1), text = "PARTIE NORMALE", font=("helvetica", "40"), relief = "flat", bg = "#141414", fg = "gray69", width = 15)
    partie_personnalisee = tk.Button(racine, command = partie_perso, text = "PARTIE PERSO", font=("helvetica", "40"), relief = "flat", bg = "#141414", fg = "gray69", width = 15)
    partie_aveugle = tk.Button(racine, command = lambda : plateau(6, 7, 4, 2), text = "PARTIE AVEUGLE", font=("helvetica", "40"), relief = "flat", bg = "#141414", fg = "gray69", width = 15)
    entree_HEIGHT = tk.Entry(racine, text = "Le nombre de case en hauteur", font=("helvetica", "20"), relief = "flat", fg = "#141414", bg = "gray69")
    entree_WIDTH = tk.Entry(racine, text = "Le nombre de case en largeur", font=("helvetica", "20"), relief = "flat", fg = "#141414", bg = "gray69")
    entree_GAGNE = tk.Entry(racine, text = "Le nombre de pion pour gagner", font=("helvetica", "20"), relief = "flat", fg = "#141414", bg = "gray69")
    valider = tk.Button(racine, command = valider_option, text = "VALIDER", font=("helvetica", "20"), relief = "flat", bg = "#141414", fg = "gray69", width = 15)
    case_HEIGHT = tk.Button(racine, text = "HAUTEUR", font=("helvetica", "20"), relief = "flat", bg = "#141414", fg = "gray69", width = 15, state = "disabled")
    case_WIDTH = tk.Button(racine, text = "LARGEUR", font=("helvetica", "20"), relief = "flat", bg = "#141414", fg = "gray69", width = 15, state = "disabled")
    case_GAGNE = tk.Button(racine, text = "PUISSANCE N", font=("helvetica", "20"), relief = "flat", bg = "#141414", fg = "gray69", width = 15, state = "disabled")

    acceuil_jouer.bind("<Enter>", lambda event : couleur_entree(event, acceuil_jouer))
    acceuil_jouer.bind("<Leave>", lambda event : couleur_sortie(event, acceuil_jouer))
    acceuil_charger_partie.bind("<Enter>", lambda event : couleur_entree(event, acceuil_charger_partie))
    acceuil_charger_partie.bind("<Leave>", lambda event : couleur_sortie(event, acceuil_charger_partie))
    partie_normale.bind("<Enter>", lambda event : couleur_entree(event, partie_normale))
    partie_normale.bind("<Leave>", lambda event : couleur_sortie(event, partie_normale))
    partie_personnalisee.bind("<Enter>", lambda event : couleur_entree(event, partie_personnalisee))
    partie_personnalisee.bind("<Leave>", lambda event : couleur_sortie(event, partie_personnalisee))
    partie_aveugle.bind("<Enter>", lambda event : couleur_entree(event, partie_aveugle))
    partie_aveugle.bind("<Leave>", lambda event : couleur_sortie(event, partie_aveugle))
    case_HEIGHT.bind("<Enter>", lambda event : couleur_entree(event, case_HEIGHT))
    case_HEIGHT.bind("<Leave>", lambda event : couleur_sortie(event, case_HEIGHT))
    case_WIDTH.bind("<Enter>", lambda event : couleur_entree(event, case_WIDTH))
    case_WIDTH.bind("<Leave>", lambda event : couleur_sortie(event, case_WIDTH))
    case_GAGNE.bind("<Enter>", lambda event : couleur_entree(event, case_GAGNE))
    case_GAGNE.bind("<Leave>", lambda event : couleur_sortie(event, case_GAGNE))
    valider.bind("<Enter>", lambda event : couleur_entree(event, valider))
    valider.bind("<Leave>", lambda event : couleur_sortie(event, valider))

def widget_plateau():
    global fond_plateau
    global remake
    global draw
    global victoire
    global tour
    global undo
    global score
    global menu
    global sauvegarder
    global bouton_triche

    fond_plateau = tk.Label(racine)
    remake = tk.Button(sous_page, text="REVANCHE", command = revanche, font=("helvetica", "10"), relief = "flat", bg = "#141414", fg = "gray69", width = 15) # création de bouton revanche
    draw = tk.Button(sous_page, text="ÉGALITÉ...",  font=("helvetica", "10"), bg = "#141414", fg = "gray69", width = 15, relief = "flat", state = "disabled") # création texte égalité
    victoire = tk.Button(sous_page, text=" ",  font=("helvetica", "10"), bg = "#141414", relief = "flat", width = 15, state = "disabled") #création du texte de victoire
    tour = tk.Button(sous_page, relief = "flat", font=("helvetica", "10"), width = 15, fg = "#141414", state = "disabled")
    undo = tk.Button(sous_page, text="ANNULER", font=("helvetica", "10"), command = annuler_coup,relief = "flat", bg = "#141414", fg = "gray69",width = 15)
    score = tk.Button(sous_page, relief = "flat", text="R " + str(R) + " | J " + str(J), font=("helvetica", "10"), bg = "#141414", fg = "gray69",width = 15, state = "disabled")
    menu = tk.Button(sous_page, relief = "flat", text="MENU", command = retour_menu, font=("helvetica", "10"), bg = "#141414", fg = "gray69",width = 15)
    sauvegarder = tk.Button(sous_page, relief = "flat", text="SAUVEGARDER", command = sauvegarder_partie, font=("helvetica", "10"), bg = "#141414", fg = "gray69",width = 15)

    remake.bind("<Enter>", lambda event : couleur_entree(event, remake))
    remake.bind("<Leave>", lambda event : couleur_sortie(event, remake))
    undo.bind("<Enter>", lambda event : couleur_entree(event, undo))
    undo.bind("<Leave>", lambda event : couleur_sortie(event, undo))
    menu.bind("<Enter>", lambda event : couleur_entree(event, menu))
    menu.bind("<Leave>", lambda event : couleur_sortie(event, menu))
    sauvegarder.bind("<Enter>", lambda event : couleur_entree(event, sauvegarder))
    sauvegarder.bind("<Leave>", lambda event : couleur_sortie(event, sauvegarder))
    tour.bind("<Enter>", visuel_tour_joueur_entree)
    tour.bind("<Leave>", visuel_tour_joueur_sortie)


def acceuil():
    acceuil_jouer.place(relx = 0.5, rely = 0.425, anchor = "center")
    acceuil_charger_partie.place(relx = 0.5, rely = 0.575, anchor = "center")

def jouer():
    acceuil_jouer.place_forget()
    acceuil_charger_partie.place_forget()
    partie_normale.place(relx= 0.5, rely = 0.35, anchor = "center")
    partie_personnalisee.place(relx= 0.5, rely = 0.5, anchor = "center")
    partie_aveugle.place(relx= 0.5, rely = 0.65, anchor = "center")

def partie_perso():
    partie_normale.place_forget()
    partie_personnalisee.place_forget()
    partie_aveugle.place_forget()
    entree_HEIGHT.place(relx = 0.5, rely = 0.3, anchor = "center")
    entree_WIDTH.place(relx = 0.5, rely = 0.5, anchor = "center")
    entree_GAGNE.place(relx = 0.5, rely = 0.7   , anchor = "center")
    case_HEIGHT.place(relx = 0.5, rely = 0.2, anchor = "center")
    case_WIDTH.place(relx = 0.5, rely = 0.4, anchor = "center")
    case_GAGNE.place(relx = 0.5, rely = 0.6, anchor = "center")
    valider.place(relx = 0.5, rely = 0.8, anchor = "center")

def valider_option():
    global HEIGHT
    global WIDTH
    global GAGNE

    HEIGHT = int(entree_HEIGHT.get())
    WIDTH = int(entree_WIDTH.get())
    GAGNE = int(entree_GAGNE.get())

    entree_GAGNE.place_forget()
    entree_HEIGHT.place_forget()
    entree_WIDTH.place_forget()
    valider.place_forget()
    case_GAGNE.place_forget()
    case_HEIGHT.place_forget()
    case_WIDTH.place_forget()
    partie_normale.place(relx= 0.5, rely = 0.4, anchor = "center")
    partie_personnalisee.place(relx= 0.5, rely = 0.6, anchor = "center")
    partie_aveugle.place(relx= 0.5, rely = 0.65, anchor = "center")
    plateau(HEIGHT, WIDTH, GAGNE, 1)
    
def plateau(haut, larg, puissance, mode):
    '''création du nouveau plateau'''
    global GAGNE
    global HEIGHT
    global WIDTH
    global NB_CASE
    global MODE_PARTIE

    GAGNE = puissance
    HEIGHT = haut
    WIDTH = larg
    NB_CASE = HEIGHT * WIDTH
    MODE_PARTIE = mode

    partie_personnalisee.place_forget()
    partie_normale.place_forget()
    partie_aveugle.place_forget()
    draw.grid_forget()
    victoire.grid_forget()


    plateau_visuel()
    plateau_parametre()
    if L == []:
        plateau_matrice()
    
    score.grid()
    menu.grid()
    sauvegarder.grid()
    tour.grid()
    undo.grid()

    fond_plateau.grid(column = 0, row = 0)
    if mode == 1:
        fond_plateau.bind("<Button-1>", placement)
    elif mode == 2:
        fond_plateau.bind("<Button-1>", placement_aveugle)
    racine.bind("<Return>", activation_triche)

def plateau_visuel():
    global fond_plateau


    fond_plateau.destroy() # destruction de l'ancien plateau

    fond_plateau = tk.Canvas(racine, bg="gray", height = 100*HEIGHT, width = 100*WIDTH)  # création du plateau
    for i in range(WIDTH):
        fond_plateau.create_line((i*100, 0), (i*100, HEIGHT*100), fill="white", width=1)
    for j in range(HEIGHT):
        fond_plateau.create_line((0, j*100), (WIDTH*100, j*100), fill="white", width=1)

def plateau_matrice():
    global L
    L = [[0] * WIDTH for i in range(HEIGHT)] #liste à 0

def plateau_parametre():
    global PARTIE
    global NB_COUP
    global tour_joueur
    global FIRST
    PARTIE = 0
    NB_COUP = 0
    if FIRST == 1:
        tour_joueur = 2
        FIRST = 2

    else: 
        tour_joueur = 1
        FIRST = 1

    if tour_joueur == 1:
        tour.config(background = "yellow2")
    else:
        tour.config(background = "#f34246")

def placement(event):
    '''permet de placer les pièces'''
    j = int(event.x)// 100 #la colonne sur laquelle on joue
    i = 0

    if PARTIE == 1:
        return()

    while i < HEIGHT and L[i][j] != 0:
        i += 1 #la case sur laquelle on joue

    if i >= HEIGHT: # envoie un message quand on ne peut pas jouer sur la colonne
            pas_la = tk.Button(sous_page, text="ACTION IMPOSSIBLE", font=("helvetica", "10"), bg = "gray69", fg = "#141414", width = 15, relief = "flat")
            pas_la.after(1000, pas_la.destroy)
            pas_la.grid(column= 0, row= 0)
    
    placement_matrice(i,j)
    placement_visuel(i,j)
    vérification_score(i,j)

def placement_matrice(i, j):
    global NB_COUP
    global tour_joueur
    global DERNIER_COUP_I 
    global DERNIER_COUP_J

    DERNIER_COUP_J = j
    DERNIER_COUP_I = i

    if tour_joueur == 1: 
        L[i][j] = 1 #créer la pièce (dans la liste)
        NB_COUP += 1
        tour.config(bg = "#f34246")
    else:
        L[i][j] = 2 #créer la pièce (dans la liste)
        NB_COUP +=1
        tour.config(bg = "yellow2")

def placement_visuel(i, j):
    if tour_joueur == 1: 
        cercle = fond_plateau.create_oval((j*100,HEIGHT*100 - i*100), ((j+1)*100,HEIGHT*100 - (i+1)*100), fill="yellow2", outline="white")
    else:
        cercle = fond_plateau.create_oval((j*100,HEIGHT*100 - i*100), ((j+1)*100,HEIGHT*100 - (i+1)*100), fill="#f34246", outline="white") #créer la pièce (visuel)

def vérification_score(i, j):
    global tour_joueur
    global R
    global J
    global PARTIE
    global DERNIER_COUP_I
    global DERNIER_COUP_J

    DERNIER_COUP_I = i
    DERNIER_COUP_J = j
    up = i
    down = i
    left = j
    right = j
    lign = 1
    col = 1
    diag_1 = 1
    diag_2 = 1
    
    while  right <= WIDTH-2 and L[i][right + 1] == tour_joueur: #comtpe les pièces de même couleur à droite
        right +=1
        lign += 1
    while left >= 1 and L[i][left - 1] == tour_joueur: #comtpe les pièces de même couleur à gauche 
        left -= 1
        lign += 1

    while up <= HEIGHT-2 and L[up + 1][j] == tour_joueur: #comtpe les pièces de même couleur en haut
        up +=1
        col += 1
    while down >= 1 and L[down - 1][j] == tour_joueur: #comtpe les pièces de même couleur  en bas
        down -= 1
        col += 1



    up = i #reset des valeurs
    down = i
    left = j
    right = j


    while up <= HEIGHT-2 and right <= WIDTH-2 and L[up + 1][right + 1] == tour_joueur: # compte en diagonale
        up += 1
        right += 1
        diag_1 += 1
    while down >= 1 and left >= 1 and L[down - 1][left - 1] == tour_joueur: # compte en diagonale
        down -= 1
        left -= 1
        diag_1 += 1


    up = i #reset des valeurs
    down = i
    left = j
    right = j


    while up <= HEIGHT-2 and left >= 1 and L[up + 1][left - 1] == tour_joueur: # compte en diagonale
        up += 1
        left -= 1
        diag_2 += 1
    while down >= 1 and right <= WIDTH-2 and L[down - 1][right + 1] == tour_joueur: # compte en diagonale
        down -= 1
        right += 1
        diag_2 += 1
          
    if tour_joueur == 1:
        tour_joueur = 2
        if col >= GAGNE or lign >= GAGNE or diag_1 >= GAGNE or diag_2 >= GAGNE : #vérifie si le joueur gagne
            PARTIE = 1
            J += 1
            score.config(text="R " + str(R) + " | J " + str(J))
            victoire.config(text = "JAUNE GAGNE", fg = "yellow2")
            remake.grid()
            victoire.grid()
    else:
        tour_joueur = 1
        if col >= GAGNE or lign >= GAGNE or diag_1 >= GAGNE or diag_2 >= GAGNE : #vérifie si le joueur gagne
            PARTIE = 1
            R += 1
            score.config(text="R " + str(R) + " | J " + str(J))
            victoire.config(text = "ROUGE GAGNE", fg = "#f34246")
            remake.grid()
            victoire.grid()

    if NB_COUP >= NB_CASE and PARTIE == 0: #vérifie que le plateau n'est pas rempli
        PARTIE = 1
        remake.grid()
        draw.grid()

def placement_aveugle(event):
    '''permet de placer les pièces'''
    j = int(event.x)// 100 #la colonne sur laquelle on joue
    i = 0

    if PARTIE == 1:
        return()

    while i < HEIGHT and L[i][j] != 0:
        i += 1 #la case sur laquelle on joue

    if i >= HEIGHT: # envoie un message quand on ne peut pas jouer sur la colonne
            pas_la = tk.Button(sous_page, text="ACTION IMPOSSIBLE", font=("helvetica", "10"), bg = "gray69", fg = "#141414", width = 15, relief = "flat")
            pas_la.after(1000, pas_la.destroy)
            pas_la.grid(column= 0, row= 1)
    
    placement_matrice(i,j)
    placement_visuel_aveugle(i,j)
    vérification_score(i,j)

def placement_visuel_aveugle(i, j):
    cercle = fond_plateau.create_oval((j*100,HEIGHT*100 - i*100), ((j+1)*100,HEIGHT*100 - (i+1)*100), fill="white", outline="white")

def annuler_coup():
    '''fonction qui annule le dernier coup'''
    
    if DERNIER_COUP_I == -1 or NB_COUP == 0: #si on est déjà revenu en arrière le tour d'avant, on ne peut plus le refaire
        pas_la = tk.Button(sous_page, text="ACTION IMPOSSIBLE", font=("helvetica", "10"), bg = "gray69", fg = "#141414", width = 15, relief = "flat")
        pas_la.after(1000, pas_la.destroy)
        pas_la.grid(column = 0, row = 0)
        return()
    
    annuler_coup_visuel()
    annuler_coup_matrice()

def annuler_coup_matrice():
    global tour_joueur
    global NB_COUP
    global DERNIER_COUP_I
    L[DERNIER_COUP_I][DERNIER_COUP_J] = 0 #restaure l'élément de la liste
    NB_COUP -= 1 #restaure le nombre de coup joué
    DERNIER_COUP_I = -1 #empêche de revenir en arrière deux fois
    if tour_joueur == 1:
        tour_joueur = 2
        tour.config(bg = "#f34246")
    else:
        tour_joueur = 1
        tour.config(bg = "yellow2")

def annuler_coup_visuel():
    carré = fond_plateau.create_rectangle((DERNIER_COUP_J*100,HEIGHT*100 - DERNIER_COUP_I*100), ((DERNIER_COUP_J+1)*100,HEIGHT*100 - (DERNIER_COUP_I+1)*100), fill="gray", outline="white") # restaure le plateau visuel

def revanche():
    global L
    L = []
    plateau(HEIGHT, WIDTH, GAGNE, MODE_PARTIE)

def retour_menu():
    global R
    global J
    global L

    R = 0
    J = 0
    score.config(text = "R " + str(R) + " | J " + str(J))

    remake.grid()
    draw.grid()
    victoire.grid()

    fond_plateau.grid_forget()
    score.grid_forget()
    sauvegarder.grid_forget()
    menu.grid_forget()
    undo.grid_forget()
    tour.grid_forget()
    remake.grid_forget()
    draw.grid_forget()
    victoire.grid_forget()
    L = []
    acceuil()

def importer():
    global HEIGHT
    global WIDTH
    global GAGNE
    global NB_COUP
    global tour_joueur
    global FIRST
    global L
    global MODE_PARTIE

    acceuil_jouer.place_forget()
    acceuil_charger_partie.place_forget()

    fichier = open("sauvegarde.txt", "r")
    save = fichier.read()
    fichier.close

    HEIGHT = int(save[0])
    WIDTH = int(save[1])
    GAGNE = int(save[2])
    MODE_PARTIE = int(save[3])
    NB_COUP = int(save[4])
    tour_joueur = int(save[5])
    FIRST = int(save[6])
    L = [[0] * WIDTH for i in range(HEIGHT)]
    for i in range (0, HEIGHT):
        for j in range(0, WIDTH):
            L[i][j] = int(save[i * WIDTH + j + 7])
    plateau(HEIGHT, WIDTH, GAGNE, MODE_PARTIE)
    placement_piece_sauvegarde()

def sauvegarder_partie():
    fichier = open("sauvegarde.txt", "w")

    fichier.write(str(HEIGHT))
    fichier.write(str(WIDTH))
    fichier.write(str(GAGNE))
    fichier.write(str(MODE_PARTIE))

    fichier.write(str(NB_COUP))
    fichier.write(str(tour_joueur))
    fichier.write(str(FIRST))

    for i in range (HEIGHT):
        for j in range(WIDTH):
            fichier.write(str(L[i][j]))

    fichier.close

    retour_menu()   

def placement_piece_sauvegarde():
    global L
    if MODE_PARTIE == 1:
        for i in range (HEIGHT):
            for j in range (WIDTH):
                if L[i][j] == 1:
                    cercle = fond_plateau.create_oval((j*100,HEIGHT*100 - i*100), ((j+1)*100,HEIGHT*100 - (i+1)*100), fill="yellow2", outline="white")
                elif L[i][j] == 2:
                    cercle = fond_plateau.create_oval((j*100,HEIGHT*100 - i*100), ((j+1)*100,HEIGHT*100 - (i+1)*100), fill="#f34246", outline="white")
    if MODE_PARTIE == 2:
        for i in range (HEIGHT):
            for j in range (WIDTH):
                if L[i][j] != 0:
                    cercle = fond_plateau.create_oval((j*100,HEIGHT*100 - i*100), ((j+1)*100,HEIGHT*100 - (i+1)*100), fill="white", outline="white")

def couleur_entree(event, widget):
    widget.config(bg = "gray69", fg = "#141414")

def couleur_sortie(event, widget):
    widget.config(fg = "gray69", bg = "#141414")

def visuel_tour_joueur_entree(event):
        tour.config(text="TOUR DU JOUEUR", bg = "gray69")

def visuel_tour_joueur_sortie(event):
    if tour_joueur == 1:
        tour.config(bg = "yellow2", text ="")
    else:
        tour.config(bg = "#f34246", text = "")

def activation_triche(event):
    bouton_triche = tk.Button(sous_page, text="GAGNE",command = triche, font=("helvetica", "10"), bg = "black", fg = "#141414", width = 15, relief = "flat", state = "active")
    bouton_triche.after(1000, bouton_triche.destroy)
    bouton_triche.grid(column = 1, row = 1)

def triche():
    global J
    global R
    global PARTIE

    if tour_joueur ==1:
        PARTIE = 1
        J += 1
        score.config(text="R " + str(R) + " | J " + str(J))
        victoire.config(text = "JAUNE GAGNE", fg = "yellow2")
        remake.grid()
        victoire.grid()
    else:
        PARTIE = 1
        R += 1
        score.config(text="R " + str(R) + " | J " + str(J))
        victoire.config(text = "ROUGE GAGNE", fg = "#f34246")
        remake.grid()
        victoire.grid()

        
        
        
n=int(input())
set=0
fichier = open("sauvegarde.txt", "r")
save = fichier.read()
score = tk.Button(sous_page, relief = "flat", text="R " + str(R) + " | J " + str(J), font=("helvetica", "10"), bg = "#141414", fg = "gray69",width = 15, state = "disabled")
victoire = tk.Button(sous_page, text=" ",  font=("helvetica", "10"), bg = "#141414", relief = "flat", width = 15, state = "disabled")
remake = tk.Button(sous_page, text="REVANCHE", command = revanche, font=("helvetica", "10"), relief = "flat", bg = "#141414", fg = "gray69", width = 15)
GAGNE= int(save[2])

def set_gagnant(jaune,rouge):
    J = jaune
    R = rouge
    if J == GAGNE*n :
        score.config(text="R " + str(R) + " | J " + str(J))
        victoire.config(text = "JAUNE GAGNE", fg = "yellow2")
        remake.grid()
        victoire.grid()
        print("Le joueur jouant des pions jaune gagne le set.")
        set = set+1
    if R == GAGNE*n:
        score.config(text="R " + str(R) + " | J " + str(J))
        victoire.config(text = "ROUGE GAGNE", fg = "#f34246")
        remake.grid()
        victoire.grid()
        print("Le joueur jouant des pions rouge gagne le set.")
        set = set+1

Debut_partie = 0
def altener(jaune,rouge):
    J = jaune
    R = rouge
    if J == Debut_partie :
        PARTIE = PARTIE + 1
        R == Debut_partie
    else :
        J == Debut_partie        
        
        
# création de la page
racine = tk.Tk()
racine.title("Puissance 4")
racine.geometry("1000x1000")
sous_page = tk.Frame(racine, bg = "#141414") #endroit des boutons
racine.config(bg = "#141414")
sous_page.grid(column=1, row = 0)

widget_plateau()
widget_acceuil()
acceuil()

racine.mainloop() # Lancement de la boucle principale
