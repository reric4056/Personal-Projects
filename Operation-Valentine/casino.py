import random

class Casino:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __repr__(self):
        return f"Casino(name={self.name}, location={self.location})"

    def welcome(self):
        print(f"Welcome to {self.name} located in {self.location}!")
        print("Try your luck and place your bets!")

    def play(self, agent):
        while True:
            print("\n--- Casino Menu ---")
            print("1. Play High Card")
            print("2. Play BlackJack")
            print("3. Play Roulette")
            print("4. View Available Funds")
            print("5. Exit Casino")

            choice = input("Choose an option: ")

            if choice == "1":
                try:
                    wager = float(input("Enter your wager amount: "))
                    self.high_card(agent, wager)
                except ValueError:
                    print("Invalid input. Please enter a numeric value for the wager.")

            elif choice == "2":
                print("BlackJack is currently under development. Please check back later.")

            elif choice == "3":
                print("Roulette is currently under development. Please check back later.")

            elif choice == "4":
                print(f"Current balance for Agent {agent.codename}: ${agent.money}")

            elif choice == "5":
                print("Exiting the casino. Good luck on your missions!")
                break

            else:
                print("Invalid choice. Please select a valid option from the menu.")

    def card_name(self, value):
        face_cards = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}
        return face_cards.get(value, str(value))

    def high_card(self, agent, wager):
        if wager <= 0:
            print("Invalid wager.")
            return

        if wager > agent.money:
            print("Insufficient funds for this wager.")
            return

        agent.money -= wager

        agent_card = random.randint(2, 14)
        dealer_card = random.randint(2, 14)

        print(f"Agent {agent.codename} drew: {self.card_name(agent_card)}")
        print(f"Dealer drew: {self.card_name(dealer_card)}")

        if agent_card > dealer_card:
            winnings = wager * 2
            agent.money += winnings
            print(f"Congratulations! You won ${winnings}. Your new balance is ${agent.money}.")
        elif agent_card < dealer_card:
            print(f"Sorry, you lost the wager of ${wager}. Your new balance is ${agent.money}.")
        else:
            agent.money += wager
            print(f"It's a tie! Your wager of ${wager} has been returned. Your balance remains ${agent.money}.")

        print(f"Current balance for Agent {agent.codename}: ${agent.money}")


