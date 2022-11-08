#import la librairie random
import random
#assigner le message de victoire a winText
winText="Bravo tu as gagné"
#assigner le message de défaite a looseText
looseText="Dommage tu as perdu"
botPlay = "null"
possiblePlay = ["pierre","feuille","ciseaux"]
botPlay = random.randint(0,2)
botPlayName = possiblePlay[botPlay]
playerPlay="neutre"
scorePlayer=0
scoreBot=0

while playerPlay!="stop" :
    playerPlay="neutre"
    botPlay = random.randint(0,2)
    botPlayName = possiblePlay[botPlay]
    while playerPlay=="neutre":
        #print (botPlayName)
        playerPlay = input("Que joues-tu ?")
    if playerPlay!="stop" :
        playerPlay = possiblePlay.index(playerPlay)
        if playerPlay == botPlay :
            print("Égalité")
        else :
            if playerPlay-botPlay==2 or botPlay-playerPlay==2:
                if playerPlay==0:
                    print(winText)
                    scorePlayer=scorePlayer+1
                else :
                    print(looseText)
                    scoreBot=scoreBot+1
            elif playerPlay>botPlay:
                print(winText)
                scorePlayer=scorePlayer+1
            elif playerPlay<botPlay:
                print(looseText)
                scoreBot=scoreBot+1
    
    #print (playerPlay)
    print(scorePlayer,":",scoreBot)
     
