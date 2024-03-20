LIGNE_GRILLE = 6
COLONNE_GRILLE = 7

#la grille du jeu
jeu = []

#Initialiser la grille

def initialiser_jeu(jeu,LIGNE_GRILLE,COLONNE_GRILLE):
    for i in range(LIGNE_GRILLE):
        ligne = []
        for j in range(COLONNE_GRILLE):
            ligne.append(-1)
        jeu.append(ligne)

# Afficher la grille du jeu
def afficher_jeu(jeu):

    for i in range(len(jeu)):
        s = ""
        for j in range(len(jeu[i])):
            jeton = ""
            if jeu[i][j] == 0:
                jeton = "O"
            elif jeu[i][j] == 1:
                jeton = "X"
            else:
                jeton = " "
            s += " | " + jeton + " | "
        print(s)
    print(" ")


def tour_joueur(tour):
    joueur = tour % 2
    # print(f"C'est le tour joueur {joueur}")
    return joueur


#Placer jeton sur la grille du jeu
# def placer_jeton(jeu,joueur,lig,col):
#     if 0<=lig<LIGNE_GRILLE and 0<=col<COLONNE_GRILLE:
#         jeu[lig][col] = joueur

def placer_jeton(jeu,joueur,col):

    for i in range(LIGNE_GRILLE-1,-1,-1):
        if(jeu[i][col]== -1 ):
            jeu[i][col] = joueur
            break




#print(jeu)

# placer_jeton(jeu,0,2,2)
# placer_jeton(jeu,1,5,6)
# afficher_jeu(jeu)
# joueur_actuel  = tour_joueur(18)
# print(f"C'est le tour du joueur {joueur_actuel}")

#TOUR 0
# tour = 0
# print(f"Le tour actuel : {tour}")
# joueur_actuel = tour_joueur(tour)

# col = 2
# placer_jeton(jeu,joueur_actuel,col)
# afficher_jeu(jeu)
# #TOUR 1
# tour +=1
# print(f"Le tour actuel : {tour}")
# joueur_actuel = tour_joueur(tour)
# col = 2
# placer_jeton(jeu,joueur_actuel,col)
# afficher_jeu(jeu)
        
tour = 0
initialiser_jeu(jeu,LIGNE_GRILLE,COLONNE_GRILLE)
print("Initialisation de la partie")
afficher_jeu(jeu)
joueur_actuel= 0

while True:
    print(f"C'est le tour {tour}")
    joueur_actuel = tour_joueur(tour)
    print(f"C'est le tour du joueur {joueur_actuel}")
    col = int(input("Placez votre jeton entre 0 et 6 : "))
    placer_jeton(jeu,joueur_actuel,col)
    afficher_jeu(jeu)
    tour+=1