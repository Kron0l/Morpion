#on considère la librairie random qui permet de tirer un nombre aléatoire
#assigner la liste des élément jouables (pierre,feuille,ciseaux) a possiblePlay


#définir la fonction victoire
    #afficher le texte de victoire (Bravo tu as gagné)
    #incrémenter scorePlayer de 1
    #retourner scorePlayer

#définir la fonction défait
    #afficher le texte de défaite (Dommage tu as perdu)
    #incrémenter scoreBot de 1
    #retourner scoreBot

#définir la fonction game utilisant les paramètre x et y
    #assigner la valeur de x a scorePlayer
    #assigner la valeur de y a scoreBot
    #réinitialiser playerPlayName en lui assignant la valeur "neutre"
    #assigner une nouvelle valeur aléatoire entre 0 et 2 a botPlay
    #tant que la valeur de playerName n'est pas dans la liste possiblePlay (tant que le joueur ne joue pas quelque chose de correct)
        #alors 
        #demander au joueur "Que joues-tu ?" et assigner cette valeur a playerPlayName
    #si playerPlayName et différent de stop
        #alors
        #trouver dans la liste possiblePlay a quelle position se situe la valeur de playerPlayName et l'assigner a playerPlay
        #si la valeur de playerPlay est égale a celle de botPlay
            #alors
            #afficher Égalité
        #sinon : la valeur de playerPlay est diffe=érente de celle de botPlay
            #alors
            #si la différence playerPlay et botPlay vaut 2 ou inversement (pierre/ciseaux ou ciseaux/pierre)
                #alors
                #si la valeur de playerPlay vaut 0 (pierre)
                    #alors
                    #récupérer la valeur retourner par la fonction victoire avec le paramètre scorePlayer et l'assigner a scorePlayer
                #sinon : si la valeur de botPlay vaut 0
                    #alors
                    #récuupérer la valeur retourner par la fonction défaite avec le paramètre scoreBot et l'assigner a scoreBot
            #sinon si la valeur de playerPlay est supérieur a celle de botPlay (feuille>pierre ou ciseaux>feuille)
                #alors
                #récupérer la valeur retourner par la fonction victoire avec le paramètre scorePlayer et l'assigner a scorePlayer
            #sinon si la valeur de playerPlay est inférieur a celle de botPlay (pierre<feuille ou feuille<ciseux)
                #alors
                #récuupérer la valeur retourner par la fonction défaite avec le paramètre scoreBot et l'assigner a scoreBot
    #afficher le score en affichant scorePlayer puis ":" puis scoreBot
    #si playerPlayName et différent de stop
        #alors
        #exécuter la fonction game avec comme premier paramètre scorePlayer et en second scoreBot 


#exécuter la fonction game avec comme premier paramètre 0 et en second 0 
     
