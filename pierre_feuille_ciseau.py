#import la librairie random
import random
#assigner la liste des élément jouables (pierre,feuille,ciseaux) a possiblePlay
possiblePlay = ["pierre","feuille","ciseaux"]



def victoire(scorePlayer):
    #afficher le texte de victoire
    print("Bravo tu as gagné")
    #ajouter 1 au score du joueur(scorePlayer) et l'assigner a scorePlayer
    scorePlayer=scorePlayer+1
    return scorePlayer

def defaite(scoreBot):
    #afficher le texte de défaite
    print("Dommage tu as perdu")
    #ajouter un au score du bot(scoreBot) et l'assigner a scoreBot
    scoreBot=scoreBot+1
    return scoreBot

#tant que le joueur n'écrit pas stop
def game(x,y):
    scorePlayer=x
    #réinitialiser le score du bot
    scoreBot=y
    #alors 
    #réinitialiser playerPlay a la valeur neutre
    playerPlay="neutre"
    #assigner une nouvelle valeur aléatoire entre 0 et 2 a botPlay
    botPlay = random.randint(0,2)
    #assigner le nom du coup joué par rapport a botPlay sur la liste possiblePlay
    #botPlayName = possiblePlay[botPlay]
    #tant que le joueur n'a pas joué (valeur playerPlay par défaut("neutre"))
    while not (playerPlay in (possiblePlay)):
        #alors 
        #afficher ce que joue le bot
        #print (botPlayName)
        #demander au joueur de jouer et assigner ce qui a été joué a playerPlay
        playerPlay = input("Que joues-tu ?")
    #si le joueur n'a pas joué stop
    if playerPlay!="stop" :
        #alors
        #trouver dans la liste possiblePlay a quelle position se situe ce qu'a joué le joueur et l'asssigner a playerPlay
        playerPlay = possiblePlay.index(playerPlay)
        #si ce que joue le joueur est égal a ce que joue le bot
        if playerPlay == botPlay :
            #alors
            #afficher Égalité
            print("Égalité")
        #sinon : le joueur ne joue pas la même chose que le bot
        else :
            #alors
            #si la différence de l'index que joue le joueur et de l'index de ce que joue le bot vaut 2 ou inversement(pierre/ciseaux ou ciseaux/pierre)
            if playerPlay-botPlay==2 or botPlay-playerPlay==2:
                #alors
                #si c'est l'index de ce que joue le joueur qui vaut 0
                if playerPlay==0:
                    scorePlayer=victoire(scorePlayer)
                    #afficher le texte de victoire
                    #print(winText)
                    #ajouter 1 au score du joueur(scorePlayer) et l'assigner a scorePlayer
                    #scorePlayer=scorePlayer+1
                #sinon : si c'est l'index de ce que joue le bot qui vaut 0
                else :
                    scoreBot=defaite(scoreBot)
                    #afficher le texte de défaite
                    #print(looseText)
                    #ajouter un au score du bot(scoreBot) et l'assigner a scoreBot
                    #scoreBot=scoreBot+1
            #sinon si l'index de ce que joue le joueur et supérieur a ce que joue le bot
            elif playerPlay>botPlay:
                #alors
                #afficher le texte de victoire
                scorePlayer=victoire(scorePlayer)
                #print(winText)
                #ajouter 1 au score du joueur(scorePlayer) et l'assigner a scorePlayer
                #scorePlayer=scorePlayer+1
            #sinon si l'index de ce que joue le bot et supérieur a ce que joue le joueur
            elif playerPlay<botPlay:
                #alors
                scoreBot=defaite(scoreBot)
                #afficher le texte de défaite
                #print(looseText)
                #ajouter un au score du bot(scoreBot) et l'assigner a scoreBot
                #scoreBot=scoreBot+1
    #afficher ce que joue le joueur
    #print (playerPlay)
    #afficher le score en format "score du joueur : score du bot"
    print(scorePlayer,":",scoreBot)
    while playerPlay!="stop" :
        game(scorePlayer,scoreBot)
game(0,0)
     
