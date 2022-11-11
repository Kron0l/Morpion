#on considère la librairie random qui permet de tirer un nombre aléatoire
import random
#assigner la liste des élément jouables (pierre,feuille,ciseaux) a possiblePlay
possiblePlay = ["pierre","feuille","ciseaux"]


#définir la fonction victoire
def victoire(scorePlayer):
    #afficher le texte de victoire (Bravo tu as gagné)
    print("Bravo tu as gagné")
    #incrémenter scorePlayer de 1
    scorePlayer=scorePlayer+1
    #retourner scorePlayer
    return scorePlayer

#définir la fonction défaite
def defaite(scoreBot):
    #afficher le texte de défaite (Dommage tu as perdu)
    print("Dommage tu as perdu")
    #incrémenter scoreBot de 1
    scoreBot=scoreBot+1
    #retourner scoreBot
    return scoreBot

#définir la fonction game utilisant les paramètre x et y
def game(x,y):
    #assigner la valeur de x a scorePlayer
    scorePlayer=x
    #assigner la valeur de y a scoreBot
    scoreBot=y
    #réinitialiser playerPlayName en lui assignant la valeur "neutre"
    playerPlayName="neutre"
    #assigner une nouvelle valeur aléatoire entre 0 et 2 a botPlay
    botPlay = random.randint(0,2)
    #tant que la valeur de playerName n'est pas dans la liste possiblePlay (tant que le joueur ne joue pas quelque chose de correct)
    while not (playerPlayName in (possiblePlay)):
        #alors 
        #demander au joueur "Que joues-tu ?" et assigner cette valeur a playerPlayName
        playerPlayName = input("Que joues-tu ?")
    #si playerPlayName et différent de stop
    if playerPlayName!="stop" :
        #alors
        #trouver dans la liste possiblePlay a quelle position se situe la valeur de playerPlayName et l'assigner a playerPlay
        playerPlay = possiblePlay.index(playerPlayName)
        #afficher ce qu'a joué le bot en affichant "Votre adversaire a joué" et l'objet correspondant a botPlay dans la liste possiblePlay
        print("Votre adversaire a joué",possiblePlay[botPlay] )
        #si la valeur de playerPlay est égale a celle de botPlay
        if playerPlay == botPlay :
            #alors
            #afficher Égalité
            print("Égalité")
        #sinon : la valeur de playerPlay est diffe=érente de celle de botPlay
        else :
            #alors
            #si la différence playerPlay et botPlay vaut 2 ou inversement (pierre/ciseaux ou ciseaux/pierre)
            if playerPlay-botPlay==2 or botPlay-playerPlay==2:
                #alors
                #si la valeur de playerPlay vaut 0 (pierre)
                if playerPlay==0:
                    #alors
                    #récupérer la valeur retourner par la fonction victoire avec le paramètre scorePlayer et l'assigner a scorePlayer
                    scorePlayer=victoire(scorePlayer)
                #sinon : si la valeur de botPlay vaut 0
                else :
                    #alors
                    #récuupérer la valeur retourner par la fonction défaite avec le paramètre scoreBot et l'assigner a scoreBot
                    scoreBot=defaite(scoreBot)
            #sinon si la valeur de playerPlay est supérieur a celle de botPlay (feuille>pierre ou ciseaux>feuille)
            elif playerPlay>botPlay:
                #alors
                #récupérer la valeur retourner par la fonction victoire avec le paramètre scorePlayer et l'assigner a scorePlayer
                scorePlayer=victoire(scorePlayer)
            #sinon si la valeur de playerPlay est inférieur a celle de botPlay (pierre<feuille ou feuille<ciseux)
            elif playerPlay<botPlay:
                #alors
                #récuupérer la valeur retourner par la fonction défaite avec le paramètre scoreBot et l'assigner a scoreBot
                scoreBot=defaite(scoreBot)
    #afficher le score en affichant scorePlayer puis ":" puis scoreBot
    print(scorePlayer,":",scoreBot)
    #si playerPlayName et différent de stop
    if playerPlayName!="stop" :
        #alors
        #exécuter la fonction game avec comme premier paramètre scorePlayer et en second scoreBot 
        game(scorePlayer,scoreBot)


#exécuter la fonction game avec comme premier paramètre 0 et en second 0 
game(0,0)
     
