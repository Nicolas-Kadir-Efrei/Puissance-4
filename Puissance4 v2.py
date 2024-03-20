# Paramètres initiaux du jeu
NB_LIGNE = 6
NB_COLONNE = 7


# Les variables du jeu puissance 4

#Grille principale du jeu puissance 4 
grille_jeu =[]

# Les jetons du joueurs, 0 prend le X et 1 prend O
jetons = ["X","O"]

def tour_joueur(tour):
    #v1
    # if(tour%2 == 0):
    #     return 0
    # else:
    #     return 1
    #v2
    # if(tour%2 == 0):
    #     return 0
    # return 1
    #v3
    # joueur = tour%2
    # return joueur
    return tour%2


#initialiser la grille en mettant des espaces vide sur toute la matrice
def initialiser_grille(grille_jeu):
    for i in range(NB_LIGNE):
        l = []
        for j in range(NB_COLONNE):
            l.append(" ")
        grille_jeu.append(l)

def afficher_grille(grille_jeu):
    for i in range(NB_LIGNE):
        ligne = "   ||   ".join(grille_jeu[i])
        print(ligne)
    print("\n")

def placer_jeton(grille_jeu,joueur,lig,col):
    jeton_joueur = jetons[joueur]
    grille_jeu[lig][col] = jeton_joueur

def placer_jeton_v2(grille_jeu,joueur,col):
    jeton_joueur = jetons[joueur]
    for i in range(NB_LIGNE-1,-1,-1):
        if(grille_jeu[i][col] == " "):
            grille_jeu[i][col] = jeton_joueur
            break

def estEgalite(grille_jeu):
    for j in range(NB_COLONNE):
        if(grille_jeu[0][j] == " "):
            return False
    return True


def gagner_horizontal(grille_jeu,joueur):
    jeton_joueur = jetons[joueur]

    for i in range(NB_LIGNE):
        # if(grille_jeu[i][0] == grille_jeu[i][1] == grille_jeu[i][2] == grille_jeu[i][3] == jeton_joueur):
        #     return True
        # if(grille_jeu[i][1] == grille_jeu[i][2] == grille_jeu[i][3] == grille_jeu[i][4] == jeton_joueur):
        #     return True
        # if(grille_jeu[i][2] == grille_jeu[i][3] == grille_jeu[i][4] == grille_jeu[i][5] == jeton_joueur):
        #     return True
        # if(grille_jeu[i][3] == grille_jeu[i][4] == grille_jeu[i][5] == grille_jeu[i][6] == jeton_joueur):
        #     return True
        for j in range(NB_COLONNE-3):
            if(grille_jeu[i][j+0] == grille_jeu[i][j+1] == grille_jeu[i][j+2] == grille_jeu[i][j+3] == jeton_joueur):
                return True
    return False

def gagner_verticale(grille_jeu,joueur):
    jeton_joueur = jetons[joueur]
    for j in range(NB_COLONNE):
        for i in range(NB_LIGNE-3):
            if(grille_jeu[i+0][j] == grille_jeu[i+1][j] == grille_jeu[i+2][j] == grille_jeu[i+3][j] == jeton_joueur):
                return True
    return False


tour = 0
initialiser_grille(grille_jeu)
afficher_grille(grille_jeu)
while True:
    # Avec la fonction tour_joueur, Afficher le joueur actuelle
    joueur_actuelle = tour_joueur(tour)
    print("C'est le tour du joueur ", joueur_actuelle)
    # Demander au joueur la ligne et la colonne pour placer le jeton
    #lig = int(input("Choisissez la ligne entre (0-5): "))
    col = int(input("Choisissez la colonne entre (0-6): "))
    # Avec la fonction placer_jeton, placez le jeton du joueur actuel
    placer_jeton_v2(grille_jeu,joueur_actuelle,col)
    # Avec la fonction afficher_grille, affichez la grille actuel
    afficher_grille(grille_jeu)
    #Vérifier si le joueur actuelle a gagné
    if(gagner_horizontal(grille_jeu,joueur_actuelle) or gagner_verticale(grille_jeu,joueur_actuelle)):
        print("Le joueur " , joueur_actuelle  , " a gagné")
        break
    #Vérifier si la grille est remplise
    if(estEgalite(grille_jeu)):
        print("la grille est remplise")
        print("match nul")
        break
    # Incrementez la variable tour
    tour += 1



# joueur_actuelle = tour_joueur(tour)
# print(jetons[tour_joueur(tour)])


# afficher_grille(grille_jeu)

# placer_jeton(grille_jeu,tour_joueur(tour),3,4)
# afficher_grille(grille_jeu)



