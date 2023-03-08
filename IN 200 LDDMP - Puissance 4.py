import tkinter as tk
from random import randint

####################################################################################################################
#                                                                                                                  #
#   PUISSANCE 4   :    Thomas TRAN  /  Lis Ainhoa ALFARO LANDA   /   Hugo BOUGNIAC   /   Clémentine HELLEHOURACH   #
#                                                                                                                  #
####################################################################################################################


tour_joueur = randint(1,2) #choisi aléatoirement le joueur qui commence
HEIGHT = int(input("Combien de cases de haut?")) #la hauteur de notre plateau
WIDTH = int(input("Combien de cases de large?")) #la largeur de notre plateau
GAGNE = 0 
a = 100000
while (a > HEIGHT) and (a > WIDTH):
    a = int(input("Combien de pièces faut-il pour gagner?"))
GAGNE = a #le nombre de pièces qu'il faut pour gagner
NB_CASE = HEIGHT * WIDTH
NB_COUP = 0 #nombre de coup joué 
PARTIE = 0 
DERNIER_COUP_I = 0 #la coordonnée i du dernier coupe joué
DERNIER_COUP_J = 0 #la coordonnée j du dernier coup joué
FIRST = tour_joueur #la couleur du joueur qui joue en premier
R = 0 #nombre de victoire du joueur rouge
J = 0 #nombre de victoire du joueur jaune

def plateau():
    '''création du nouveau plateau'''


    global PARTIE
    global fond_plateau
    global NB_COUP
    global L
    global remake
    global victoire
    global draw
    global tour_joueur
    global FIRST
    global tour
    global undo
    global score
    L = [[0] * WIDTH for i in range(HEIGHT)]
    PARTIE = 0
    NB_COUP = 0


    fond_plateau.destroy() # destruction des anciens éléments
    remake.destroy()
    victoire.destroy()
    draw.destroy()
    tour.destroy()
    undo.destroy()

    
    fond_plateau = tk.Canvas(racine, bg="gray", height = 100*HEIGHT, width = 100*WIDTH)  # création du plateau
    for i in range(WIDTH):
        fond_plateau.create_line((i*100, 0), (i*100, HEIGHT*100), fill="white", width=1)
    for j in range(HEIGHT):
        fond_plateau.create_line((0, j*100), (WIDTH*100, j*100), fill="white", width=1)


    remake = tk.Button(sous_page, text="REVANCHE", command = plateau, font=("helvetica", "10"), relief = "flat", bg = "#141414", fg = "gray69", activebackground = "gray99", activeforeground = "#141414", width = 15) # création de bouton revanche
    draw = tk.Button(sous_page, text="ÉGALITÉ...",  font=("helvetica", "10"), bg = "#141414", fg = "gray69", width = 15, relief = "flat") # création texte égalité
    victoire = tk.Button(sous_page, text=" ",  font=("helvetica", "10"), bg = "#141414", relief = "flat", width = 15) #création du texte de victoire
    tour = tk.Button(sous_page, relief = "flat", font=("helvetica", "10"), width = 15, fg = "#141414")
    tour.grid(column = 0, row = 1)
    undo = tk.Button(sous_page, text="ANNULER", font=("helvetica", "10"), command = annuler_coup,relief = "flat", bg = "#141414", fg = "gray69",width = 15)
    undo.grid(column = 0, row = 2)
    score = tk.Button(sous_page, relief = "flat", text="R " + str(R) + " | J " + str(J), font=("helvetica", "10"), bg = "#141414", fg = "gray69",width = 15)
    score.grid(column = 0, row = 0)


    fond_plateau.grid(column = 0, row = 0)
    fond_plateau.bind("<Button-1>", placement)
    remake.bind("<Enter>", b_couleur)
    remake.bind("<Leave>", b_couleur_2)

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
    i = int(event.x)// 100 #la colonne sur laquelle on joue
    j = 0

    if PARTIE == 1:
        return()

    while j < HEIGHT and L[j][i] != 0:
        j += 1 #la case sur laquelle on joue

    if j >= HEIGHT: # envoie un message quand on ne peut pas jouer sur la colonne
            pas_la = tk.Button(sous_page, text="ACTION IMPOSSIBLE", font=("helvetica", "10"), bg = "gray69", fg = "#141414", width = 15, relief = "flat")
            pas_la.after(1000, pas_la.destroy)
            pas_la.grid(column= 0, row= 1)
    
    placement_matrice(i,j)
    placement_visuel(i,j)
    vérification_score(i,j)

def placement_matrice(i, j):
    global NB_COUP
    global tour_joueur
    if tour_joueur == 1: 
        L[j][i] = 1 #créer la pièce (dans la liste)
        NB_COUP += 1
        tour.config(bg = "#f34246")
    else:
        L[j][i] = 2 #créer la pièce (dans la liste)
        NB_COUP +=1
        tour.config(bg = "yellow2")

def placement_visuel(i, j):
    if tour_joueur == 1: 
        cercle = fond_plateau.create_oval((i*100,HEIGHT*100 - j*100), ((i+1)*100,HEIGHT*100 - (j+1)*100), fill="yellow2", outline="white")
    else:
        cercle = fond_plateau.create_oval((i*100,HEIGHT*100 - j*100), ((i+1)*100,HEIGHT*100 - (j+1)*100), fill="#f34246", outline="white") #créer la pièce (visuel)

def vérification_score(i, j):
    global tour_joueur
    global R
    global J
    global PARTIE
    global DERNIER_COUP_I
    global DERNIER_COUP_J

    DERNIER_COUP_I = i
    DERNIER_COUP_J = j
    up = j
    down = j
    left = i
    right = i
    lign = 1
    col = 1
    diag_1 = 1
    diag_2 = 1
    
    while  right <= WIDTH-2 and L[j][right + 1] == tour_joueur: #comtpe les pièces de même couleur à droite
        right +=1
        lign += 1
    while left >= 1 and L[j][left - 1] == tour_joueur: #comtpe les pièces de même couleur à gauche 
        left -= 1
        lign += 1

    while up <= HEIGHT-2 and L[up + 1][i] == tour_joueur: #comtpe les pièces de même couleur en haut
        up +=1
        col += 1
    while down >= 1 and L[down - 1][i] == tour_joueur: #comtpe les pièces de même couleur  en bas
        down -= 1
        col += 1



    up = j # reset des valeurs
    down = j
    left = i
    right = i


    while up <= HEIGHT-2 and right <= WIDTH-2 and L[up + 1][right + 1] == tour_joueur: # compte en diagonale
        up += 1
        right += 1
        diag_1 += 1
    while down >= 1 and left >= 1 and L[down - 1][left - 1] == tour_joueur: # compte en diagonale
        down -= 1
        left -= 1
        diag_1 += 1


    up = j # reset des valeurs
    down = j
    left = i
    right = i


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
            victoire.grid(column = 0, row = 4)
            remake.grid(column = 0 , row =3)
    else:
        tour_joueur = 1
        if col >= GAGNE or lign >= GAGNE or diag_1 >= GAGNE or diag_2 >= GAGNE : #vérifie si le joueur gagne
            PARTIE = 1
            R += 1
            score.config(text="R " + str(R) + " | J " + str(J))
            victoire.config(text = "ROUGE GAGNE", fg = "#f34246")
            victoire.grid(column = 0, row = 4)
            remake.grid(column = 0 , row = 3)

    if NB_COUP >= NB_CASE and PARTIE == 0: #vérifie que le plateau n'est pas rempli
        PARTIE = 1
        draw.grid(column = 0, row = 4)
        remake.grid(column = 0 , row = 3)

def annuler_coup():
    '''fonction qui annule le dernier coup'''
    
    if DERNIER_COUP_I == -1 or NB_COUP == 0: #si on est déjà revenu en arrière le tour d'avant, on ne peut plus le refaire
        pas_la = tk.Button(sous_page, text="ACTION IMPOSSIBLE", font=("helvetica", "10"), bg = "gray69", fg = "#141414", width = 15, relief = "flat")
        pas_la.after(1000, pas_la.destroy)
        pas_la.grid(column= 0, row= 1)
        return()
    
    annuler_coup_visuel()
    annuler_coup_matrice()

def annuler_coup_matrice():
    global tour_joueur
    global NB_COUP
    global DERNIER_COUP_I
    L[DERNIER_COUP_J][DERNIER_COUP_I] = 0 #restaure l'élément de la liste
    NB_COUP -= 1 #restaure le nombre de coup joué
    DERNIER_COUP_I = -1 #empêche de revenir en arrière deux fois
    if tour_joueur == 1:
        tour_joueur = 2
        tour.config(bg = "#f34246")
    else:
        tour_joueur = 1
        tour.config(bg = "yellow2")

def annuler_coup_visuel():
    carré = fond_plateau.create_rectangle((DERNIER_COUP_I*100,HEIGHT*100 - DERNIER_COUP_J*100), ((DERNIER_COUP_I+1)*100,HEIGHT*100 - (DERNIER_COUP_J+1)*100), fill="gray", outline="white") # restaure le plateau visuel

def importer():
    pass

def sauvegarder():
    pass

def b_couleur(event):
    remake.config(bg = "gray69", fg = "#141414")

def b_couleur_2(event):
    remake.config(fg = "gray69", bg = "#141414")

def u_couleur(event):
    undo.config(bg = "gray69", fg = "#141414")

def u_couleur_2(event):
    undo.config(fg = "gray69", bg = "#141414")

def tour_du_joueur(event):
        tour.config(text="TOUR DU JOUEUR", bg = "gray69")

def tour_du_joueur_2(event):
    if tour_joueur == 1:
        tour.config(bg = "yellow2", text ="")
    else:
        tour.config(bg = "#f34246", text = "")

# création de la page

racine = tk.Tk()
racine.title("Puissance 4")
sous_page = tk.Frame(racine, bg = "#141414") #endroit des boutons
menu_barre = tk.Menu()
menuFichier  = tk.Menu(menu_barre, tearoff = 0) #barre pour sauvegarder
menu_barre.add_cascade(label="Fichier", menu=menuFichier)
menuFichier.add_command(label="Enregister", command = sauvegarder) 
menuFichier.add_command(label="Importer", command = importer)
racine.config(menu = menu_barre)
racine.config(bg = "#141414")
sous_page.grid(column=1, row = 0)

#Pour permettre à la fonction plateau le .destroy
fond_plateau = tk.Label(racine)
victoire = tk.Label(racine)
draw = tk.Label(racine)
remake = tk.Label(racine)
tour = tk.Label(racine)
undo = tk.Label(racine)
score = tk.Label(racine)

plateau() #création du plateau

#fonction visuelle des deux boutons
undo.bind("<Enter>", u_couleur)
undo.bind("<Leave>", u_couleur_2)
tour.bind("<Enter>", tour_du_joueur)
tour.bind("<Leave>", tour_du_joueur_2)

racine.mainloop() # Lancement de la boucle principale