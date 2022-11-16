#on admet la fonction global qui permet un transfert de variable san utiliser de return
#on admet le fonction event qui permet de récupérer les cliques et mouvement de la souris
#on admet la fonction quit qui stop le programme

#on considère la fonction tk qui perment de réaliser du graphique


#assigner la taille des cellules à cellSize
#assigner le nombre de cellule composant la largeur et la longueur du tableau (3 pour un morpion normale)
#créer canvasSize contenant la taille de la fenêtre principale


#créer flag contenant True


#créer victoire contenant "neutre"
#créer tour contenant 0
#assigner "red" à crossColor
#assigner "blue" à sphereColor



#définir la fonction initTableau qui permet de créer tableaAnalyse

    #récupérer tableAnalyse grâce à la fonction global

    #créer une liste nommée tableAnalyse contenant [[0,0,0],[0,0,0],[0,0,0]]



#définir la fonction fenêtre qui permet de remplir la fenêtre principale avec la grille de morpion
    
    #pour x de 0 à boardSize

        #alors
        #pour y de 0 à boardSize
            #créer un rectangle ayant comme points opposés : y * cellSize; x * cellSize et y * cellSize + cellSize; x * cellSize + cellSize


#définir la fonction reinit servant à remettre les valeur à 0

    #récupérer la variable victoire grâce à la fonction global
    
    #assigner 0 à tour
    #assigner la valeur "neutre" à la variable victoire
    #supprimer tous les dessin de la page principale
    #invoquer la fonction fenetre
    #invoquer la fonction initTableau


#définir la fonction croix contenant le paramètre cell et permettant de faire le dessin d'une croix

    #récupérer tour grâce à la fonction global

    #créer une des 2 diagonales de la croix d'épaisseur 5 et de couleur crossColor par rapport a cell et cellSize
    #créer l'autre diagonale de la croix d'épaisseur 5 et de couleur crossColor par rapport a cell et cellSize
    #insérer 1 dans tableAnalyse en position [cell[0]][cell[1]]
    #incrémenter tour de 1


#définir la fonction rond ayant comme paramètre cell et permettant de déssiner un rond


    #créer un oval d'épaisseur 5 et de couleur spherreColor par rapport à cell et cellSize
    #insérer -1 dans tableAnalyse en position [cell[0]][cell[1]]
    #incrémenter tour de 1



#définir la fonction analyse permettant de faire ue analyse de chaque cellule du tableau et donner la victoire si nécessaire

    #récupérer tableAnalyse et victoire grâce à la fonction global

    #créer la liste winAnalyse contenant [0,0,0,0,0,0,0,0] (liste des analyses)

    """analyse de chaque ligne"""
    #faire la somme des cellules composant la première ligne du tableau et l'assigner à la première valeur de winAnalyse
    #faire la somme des cellules composant la seconde ligne du tableau et l'assigner à la seconde valeur de winAnalyse
    #faire la somme des cellules composant la troisième ligne du tableau et l'assigner à la troisième valeur de winAnalyse

    """analyse de chaque colonnes"""
    #faire la somme des cellules composant la première colonne et l'assigner à la quatrième valeur de winAnalyse
    #faire la somme des cellules composant la seconde colonne et l'assigner à la cinquième valeur de winAnalyse
    #faire la somme des cellules composant la troisième colonne et l'assigner à la sixième valeur de winAnalyse

    """analyse de chaque diagonales"""
    #faire la somme des cellules composant la première diagonale et l'assigner à la septième valeur de winAnalyse
    #faire la somme des cellules composant la seconde diagonale et l'assigner à la huitième valeur de winAnalyse
        
    
    #si tour est iférieur ou égal à 9
        #alors
        #pour i entre 0 et 7 compris
            #alors
            #si la valeur en position [i] dans winAnalyse est égale à 3
                #alors
                #assigner "croix" à victoire
            #sinon si la valeur en position [i] dans winAnalyse est égale à -3
                #alors
                #assigner "rond" à victoire
            #sinon si tour est égal à 9 et victoire est égale à "neutre"
                #alors
                #assigner égalité à victoire
                    



#définir game avec les paramètre cell

    #récupérer flag et victoire grâce a la fonction global
    
    #si la position [cell[0]][cell[1]] de tableAnalyse est égale à 0
        #alors
        #si flag
            #alors
            #invoquer la fonction croix avec le paramètre cell
            #inverser la valeur de flag
        #sinon
            #alors
            #invoquer la fonction rond avec le paramètre cell
            #inverser la valeur de flag
    #invoquer la fonction analyse

    #si victoire est différent de "neutre"
        #alors
        #ouvrir une nouvelle fenêtre
        #si victoire est différent de "égalité"
            #alors
            #afficher { "Les gagnant sont les " victoire } en police "Courrier" de taille 30 et de couleur 'orange'
        #sinon
            #alors
            #afficher "Égalité" en police "Courrier" de taille 30 et de couleur 'orange' et un écart dans l'axe x de 50

        #créer un boutton réinitialiser avec comme texte "Réinitialiser" et qui invoque la fonction reinit et détruit la fenPrinc
        #créer un boutton quitter avec comme texte "Quitter" et qui invoque la fonction quit
    


#définir la fonction afficher avec comme paramètre event

    #récupérer victoire grâce à la fonction global
    
    # si victoire est égal à "neutre"
        #alors
        #assigner la valeur de event.x à abcisse
        #assigner la valeur de event.y à ordonnee
        #assigner à cell la liste [int (abscisse / cellSize), int (ordonnee/cellSize)] (coordonnée de la cellule cliqué)
        #invoquer game avec les paramètre cell

#créer une fenêtre de longueur canvasSize et de largeur canvasSize
#invoquer la fonction fenetre
#invoquer la fonction initTableau

#invoquer la fonction afficher quand <Button-1> est cliqué (clique gauche)