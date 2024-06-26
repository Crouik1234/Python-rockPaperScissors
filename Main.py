
import random
from re import L
from time import sleep
r = 1

def party(ia):
    
    print("Partie en ", r,"manches!")
    sleep(1)
    for loop in range(r):
        start = False
        while start == 0 :
            print("Quel est ton choix?")
            print("1:Pierre")
            print("2:Feuille")
            print("3:Ciseau")
            print("Choisie !")
            user_choice = int(input())
            if user_choice > 3:
                print("Impossible")
            else: 
                start = True  
        print("Pret?")
        sleep(1)
        print("3")
        sleep(1)
        print("2")
        sleep(1)
        print("1...")
        sleep(1)
        if user_choice == 1:
            print("Vous: Pierre")
        elif user_choice == 2:
            print("Vous: Feuille")
        elif user_choice == 3:
            print("Vous: Ciseau")
        
        IAchoice = ia
        

            
        if IAchoice == 1:
            print("IA: Pierre")
        elif IAchoice == 2:
            print("IA: Feuille")
        elif IAchoice == 3:
            print("IA: Ciseau")

        # Règles :
        # Résultat = IAchoice - User_choice
        # si Résultat = 
        # 0 : Egalité
        # -1 : Perdu IA
        # 1 : Gagné IA
        # -2 : Gagné IA
         # 2 : Perdu IA
        result = IAchoice - user_choice
        if result == 0:
            print("Egalité !")
        elif result == -1:
            print("Vous avez gagné !")
        elif result == 1:
            print("Vous avez perdu !")
        elif result == -2:
            print("Vous avez perdu !")
        elif result == 2:
            print("Vous avez gagné !")
    return(user_choice)


class gen():
    def __init__(self, last_adv_choice):
        if last_adv_choice == 1:
            print("test",last_adv_choice)
        if last_adv_choice == 2:
            print("test",last_adv_choice)
        if last_adv_choice == 3:
            print("test",last_adv_choice)

option1 = 1
option2 = 2
option3 = 3
