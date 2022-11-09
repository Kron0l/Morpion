#import la librairie random
import random
#assigner le message de victoire a winText
winText="Bravo tu as gagné"
#assigner le message de défaite a looseText
looseText="Dommage tu as perdu"
#assigner la valeur par défaut null a botPlay
botPlay = "null"
#assigner la liste des élément jouables (pierre,feuille,ciseaux) a possiblePlay
possiblePlay = ["pierre","feuille","ciseaux"]
#assigner une valeur aléatoire de 0 à 2
botPlay = random.randint(0,2)
#assigner le nom du coup joué par rapport a botPlay sur la liste possiblePlay
#botPlayName = possiblePlay[botPlay]
#assigner la valeur par défaut neutre a playerPlay
playerPlay="neutre"
#réinitialiser le score du joueur
scorePlayer=0
#réinitialiser le score du bot
scoreBot=0

#tant que le joueur n'écrit pas stop
while playerPlay!="stop" :
    #alors 
    #réinitialiser playerPlay a la valeur neutre
    playerPlay="neutre"
    #assigner une nouvelle valeur aléatoire entre 0 et 2 a botPlay
    botPlay = random.randint(0,2)
    #assigner le nom du coup joué par rapport a botPlay sur la liste possiblePlay
    #botPlayName = possiblePlay[botPlay]
    #tant que le joueur n'a pas joué (valeur playerPlay par défaut("neutre"))
    while playerPlay=="neutre":
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
                    #afficher le texte de victoire
                    print(winText)
                    #ajouter 1 au score du joueur(scorePlayer) et l'assigner a scorePlayer
                    scorePlayer=scorePlayer+1
                #sinon : si c'est l'index de ce que joue le bot qui vaut 0
                else :
                    #afficher le texte de défaite
                    print(looseText)
                    #ajouter un au score du bot(scoreBot) et l'assigner a scoreBot
                    scoreBot=scoreBot+1
            #sinon si l'index de ce que joue le joueur et supérieur a ce que joue le bot
            elif playerPlay>botPlay:
                #alors
                #afficher le texte de victoire
                print(winText)
                #ajouter 1 au score du joueur(scorePlayer) et l'assigner a scorePlayer
                scorePlayer=scorePlayer+1
            #sinon si l'index de ce que joue le bot et supérieur a ce que joue le joueur
            elif playerPlay<botPlay:
                #alors
                #afficher le texte de défaite
                print(looseText)
                #ajouter un au score du bot(scoreBot) et l'assigner a scoreBot
                scoreBot=scoreBot+1
    #afficher ce que joue le joueur
    #print (playerPlay)
    #afficher le score en format "score du joueur : score du bot"
    print(scorePlayer,":",scoreBot)
     
