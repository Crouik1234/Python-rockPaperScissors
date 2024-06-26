import random 
import Main

probaPierre = 1/3 * 100
probaFeuille = 1/3 * 100 
probaCiseaux = 1/3 * 100

population = [1,2,3]

def player1() :
    pick = random.choices(population,weights=(probaPierre,probaFeuille,probaCiseaux))
    print(pick)

    player = Main.party(pick)
    if player == 1:
        probaCiseaux = probaCiseaux * 0.8
        probaFeuille = probaFeuille * 1.2
    elif player == 2:
        probaPierre = probaPierre * 0.8
        probaCiseaux = probaCiseaux * 1.2
    elif player == 3:
        probaFeuille = probaFeuille * 0.8
        probaPierre = probaPierre * 1.2
    print(probaPierre)
    print(probaFeuille)
    print(probaCiseaux)

player1()