import random


def main():
    balance = 100

    print("╔════════════════════════════╗")
    print("║          🎲 DICE           ║")
    print("╚════════════════════════════╝")

    print(f"You have a balance of £{balance}")

    print()

    while True:
        bet = float(input(f"How much £{balance} would you like to bet? "))

        if bet <= balance:
            break

    print()

    while True:
        game = input("Which game would you like to play? \n1. Blackjack \n2. Coin Flip \n3. Slots \n4. Rock Paper Scissors \n5. Exit? ")

        if game == "1":
            blackjack(balance, bet)

        elif game == "4":
            rock_paper_scissors(balance, bet)

        elif game == "5":
            print("Okay have a good day.")
            break


def blackjack(balance, bet):
    print()
    print("Welcome to blackjack, the game is very simple don't go over 21.")


def rock_paper_scissors(balance, bet):

    while True:
        print()
        print("Welcome to Rock Paper Scissors! The game is very simple.")
        print("Rock beats Scissors, Scissors beats Paper and Paper beats Rock!")

        print("\n1. Rock \n2. Paper \n3. Scissors")

        choice = int(input("\nEnter your choice please "))

        while choice > 3 or choice < 1:
            choice = int(input("\nEnter a valid choice please "))

        if choice == 1:
            choice_name = "Rock"

        elif choice == 2:
            choice_name = "Paper"

        elif choice == 3:
            choice_name = "Scissors"

        print()

        print(f"User has chosen {choice_name} awaiting dealers choice")

        print()

        for _ in range(3):
            print("...")

        comp_choice = random.randint(1, 3)

        if comp_choice == 1:
            comp_choice_name = "Rock"

        elif comp_choice == 2:
            comp_choice_name = "Paper"

        else:
            comp_choice_name = "Scissors"

        print()

        print(f"Dealer choice was, {comp_choice_name}")
        print(f"{choice_name} vs {comp_choice_name}")

        if choice == comp_choice:
            print("It's a draw money returned")
            print(f"your total balance is {balance}")

        elif choice == 1 and comp_choice == 2:
            print("Dealer has won!")
            balance = balance - bet
            print(f"you have £{balance} left")

        elif choice == 1 and comp_choice == 3:
            print("You have won")
            balance = balance + bet
            print(f"your total balance has increased, you now hold £{balance}")

        elif choice == 2 and comp_choice == 1:
            print("You have won")
            balance = balance + bet
            print(f"your total balance has increased, you now hold £{balance}")

        elif choice == 2 and comp_choice == 3:
            print("Dealer has won")
            balance = balance - bet
            print(f"you have £{balance} left")

        elif choice == 3 and comp_choice == 1:
            print("Dealer has won")
            balance = balance - bet
            print(f"you have £{balance} left")

        elif choice == 3 and comp_choice == 2:
            print("You have won")
            balance = balance + bet
            print(f"your total balance has increased, you now hold £{balance}")

        again = int(input(
            "\nWould you like to play again or return back to menu? "
            "\n1. Play Again "
            "\n2. Return to Menu: "
        ))

        if again == 2:
            break


main()
