#
# Le jeu du morpion
#
######################################################################
#
# Dans ce dernier programme, vous allez dÃ©couvrir un aspect
# important de la programmation: l'imbrication.
#
# Ici, le plateau de jeu est une "liste de listes". Pour parcourir des
# listes de listes, il faut faire des boucles qui contiennent des
# boucles. Ces boucles sont dites "imbriquÃ©es".
#
######################################################################
# Remarque: Ce fichier source est prÃ©vu pour Ãªtre lu de la premiÃ¨re
# ligne Ã  la derniÃ¨re ligne en raffinant petit Ã  petit la structure
# des procÃ©dures les plus importantes du programme. Ainsi, certaines
# procÃ©dures et fonctions sont utilisÃ©es avant que leur dÃ©finition
# n'apparaissent. Le choix de leurs identifiants et les commentaires
# doivent suffir Ã  comprendre ce qu'elles font sans que l'on ait
# besoin de lire immÃ©diatement leurs implÃ©mentations.
######################################################################

# Nous aurons besoin d'arrÃªter le programme Ã  l'aide de la procÃ©dure
# 'exit' de la bibliothÃ¨que 'sys'.
import sys

# Le jeu du tic-tac-toe.
def game ():
    # Le plateau de jeu est une grille 3x3 Ã  deux dimensions.  En
    # Python, on peut reprÃ©senter une telle grille Ã  l'aide d'une
    # liste de 3 listes contenant 3 chaÃ®nes de caractÃ¨res. Les chaÃ®nes
    # de caractÃ¨res reprÃ©senteront l'Ã©tat de la case: " " pour vide, "X"
    # pour la croix et "O" pour le cercle. Initialement, toutes les cases
    # sont vides.
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    # On fait des tours de jeu tant que le jeu ne s'arrÃªte pas sur une
    # victoire oÃ¹ une Ã©galitÃ©.
    while True:
        turn (board)

# Un tour de jeu consiste Ã  faire jouer le joueur des croix puis le joueur
# des cercles.
def turn (board):
    play ("X", board)
    play ("O", board)

# Les tours de jeu sont similaires pour les deux joueurs:
def play (player, board):
    # D'abord, on affiche le plateau.
    print_board (board)
    # Ensuite, on regarde si la partie n'est pas dÃ©jÃ  terminÃ©e parce
    # qu'il n'y a plus de coup possible. Si la partie est terminÃ©e,
    # le programme sera arrÃªtÃ© par la procÃ©dure suivante:
    check_for_tie (board)
    # Si la partie n'est pas terminÃ©e alors on demande son choix au
    # joueur en lui demandant de choisir une ligne puis une colonne
    # dans la grille.
    print ("C'est au tour du joueur " + player + ".")
    print ("Ligne? (0, 1 ou 2)")
    line = int (input ())
    print ("Colonne? (0, 1 ou 2)")
    column = int (input ())
    # Bien sÃ»r, on ne peut jouer que dans les cases vides. On teste
    # donc si la case choisie est vide.
    if board[line][column] == " ":
        # Si oui, on modifie le plateau pour y mettre le symbole du
        # joueur.
        board[line][column] = player
        # On vÃ©rifie maintenant si le joueur a alignÃ© trois cases
        # identiques.
        check_if_game_is_won (player, board)
    else:
        # Ã‰crire dans une case non vide stoppe le jeu.
        invalid_choice ()

# Affiche le plateau de jeu.
def print_board (board):
    # On affiche la premiÃ¨re ligne.
    print ("-------")
    # Pour toutes les lignes numÃ©rotÃ©es de 0 Ã  2:
    for i in range (0, 3):
        # et pour toutes les colonnes numÃ©rotÃ©es de 0 Ã  2:
        for j in range (0, 3):
            # On affiche le contenu de la case Ã  la i-Ã¨me ligne et Ã 
            # la j-iÃ¨me colonne prÃ©cÃ©dÃ© d'une barre de sÃ©paration.
            print ("|" + board[i][j], end="")
        # La barre suivante termine la ligne:
        print ("|")
        # Et voici pour finir une ligne de sÃ©paration.
        print ("-------")

# Pour savoir si un joueur a gagnÃ©, on teste les lignes, les colonnes
# et les diagonales de la grille pour vÃ©rifier s'il a un alignement.
def check_if_game_is_won (player, board):
    # Ici, on met les lignes, les colonnes et les diagonales dans une
    # mÃªme liste en les concatÃ©nant Ã  l'aide de l'opÃ©rateur +.
    check_alignments (player, lines (board) + columns (board) + diagonals (board))

# Un alignement est une sÃ©quence des 3 symboles du joueur.
def check_alignment_for (player, line):
    if line == player * 3:
        game_is_over (player)

# On va tester tous les alignements possibles de la grille.
def check_alignments (player, candidates):
    for i in range (0, len (candidates)):
        check_alignment_for (player, candidates[i])

# La fonction suivante renvoie les colonnes du plateau.
def columns (board):
    tboard = [[]] * 3
    for i in range (0, 3):
        tboard[i] = [" "] * 3
    for i in range (0, 3):
        for j in range (0, 3):
            tboard[j][i] = board[i][j]
    return tboard

# La fonction suivante renvoie les lignes du plateau.
def lines (board):
    return (board)

# La fonction suivante renvoie les diagonales du plateau.
def diagonals (board):
    return [
        [ board[0][0], board[1][1], board[2][2] ],
        [ board[2][0], board[1][1], board[0][2] ]
    ]

# "count_empty_cells (board)" compte le nombre de cases vides dans la
# grille.
def count_empty_cells (board):
    # On utilise une variable avec laquelle on va compter le nombre de
    # cases vides au fur Ã  mesure du parcours du plateau.
    c = 0
    # On passe sur toutes les lignes...
    for i in range (0, 3):
        #  ... et sur toutes les colonnes:
        for j in range (0, 3):
            if board[i][j] == " ":
                # Si la case contient un espace alors on la compte comme vide.
                c = c + 1
    # Une fois le parcours du plateau effectuÃ©, le rÃ©sultat est dans "c".
    return c

# La procÃ©dure suivante teste s'il reste encore des cases vides pour jouer.
def check_for_tie (board):
    if count_empty_cells (board) == 0:
        # S'il ne reste plus de case, alors la partie est terminÃ©e sur
        # une Ã©galitÃ©.
        print ("EgalitÃ©!")
        sys.exit (0)

# La procÃ©dure suivante arrÃªte le programme suite Ã  un coup invalide.
def invalid_choice ():
    print ("Coup invalide!")
    sys.exit (0)

# La procÃ©dure suivante annonce le vainqueur et stoppe le programme.
def game_is_over (player, board):
    print (player + " a gagnÃ©!")
    print_board (board)
    sys.exit (0)

# Le programme principal
#########################
game ()
print_board (board)