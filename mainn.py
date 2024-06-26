import random

class RockPaperScissorsAI:
    def __init__(self):
        self.choices = ["Pierre", "Feuille", "Ciseaux"]
        self.history = {"Pierre": 0, "Feuille": 0, "Ciseaux": 0}

    def get_ai_choice(self):
        # Calculate the most frequent user choice
        most_frequent_user_choice = max(self.history, key=self.history.get)
        
        # Determine AI's choice to beat the most frequent user choice
        if most_frequent_user_choice == "Pierre":
            return "Feuille"
        elif most_frequent_user_choice == "Feuille":
            return "Ciseaux"
        else:
            return "Pierre"

    def update_history(self, user_choice):
        if user_choice in self.history:
            self.history[user_choice] += 1

    def play_round(self, user_choice):
        ai_choice = self.get_ai_choice()
        self.update_history(user_choice)
        return ai_choice

    def determine_winner(self, user_choice, ai_choice):
        if user_choice == ai_choice:
            return "Égalité"
        elif (user_choice == "Pierre" and ai_choice == "Ciseaux") or \
             (user_choice == "Feuille" and ai_choice == "Pierre") or \
             (user_choice == "Ciseaux" and ai_choice == "Feuille"):
            return "Utilisateur gagne"
        else:
            return "IA gagne"

def main():
    ai = RockPaperScissorsAI()
    while True:
        user_choice = input("Entrez votre choix (Pierre, Feuille, Ciseaux) ou 'quit' pour arrêter: ").capitalize()
        if user_choice == 'Quit':
            break
        if user_choice not in ai.choices:
            print("Choix invalide, veuillez réessayer.")
            continue

        ai_choice = ai.play_round(user_choice)
        print(f"L'IA choisit: {ai_choice}")

        result = ai.determine_winner(user_choice, ai_choice)
        print(f"Résultat: {result}\n")

main()
