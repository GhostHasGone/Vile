# Imports

import random
import os
from time import sleep
from colorama import Fore, Style
from title import display_title


red = Fore.RED
blue = Fore.BLUE
endColor = Style.RESET_ALL

class Player:
    def __init__(self, name, is_bot=False):
        self.name = name
        self.lives = 2
        self.is_bot = is_bot

    def shoot(self, chamber):
        # Pop the next bullet from the chamber.
        bullet = chamber.pop(0)
        return bullet == "live"

    def lose_life(self):
        self.lives -= 1

def load_chamber(round_data):
    # Create the chamber with the given number of blanks and live rounds.
    bullets = ["blank"] * round_data["blanks"] + ["live"] * round_data["live"]
    random.shuffle(bullets)
    return bullets

def bot_decision(chamber):
    """
    The bot calculates the probability of drawing a live bullet:
    - If the chance is high (>= 50%), it shoots.
    - If moderate (>= 30% and <50%), it mostly shoots (60% chance).
    - Otherwise, it passes.
    """
    live_count = chamber.count("live")
    total = len(chamber)
    probability = live_count / total

    if probability >= 0.5:
        return "s"
    elif probability >= 0.3:
        return "s" if random.random() < 0.6 else "p"
    else:
        return "p"

def play_game():
    rounds = [
        {"blanks": 5, "live": 2},
        {"blanks": 7, "live": 3},
        {"blanks": 10, "live": 4}
    ]

    human = Player(f"{blue}You{endColor}")
    bot = Player(f"Your {red}opponent{endColor}", is_bot=True)

    for round_num, round_data in enumerate(rounds, 1):
        os.system('cls')
        print(f"\n--- Round {round_num} ---")
        chamber = load_chamber(round_data)

        # Ominous info before the round begins.
        total_live = round_data["live"]
        total_blanks = round_data["blanks"]
        print(
            f"\nYou're faced with a man who wants you dead. In this round's gun, there are {total_live} live bullets and {total_blanks} blanks."
        )
        print("Choose wisely, and stay alive...\n")

        round_over = False

        # Continue the round until a live bullet is fired or the chamber is empty.
        while chamber and not round_over:
            # Human's turn.
            action = input(f"Do {human.name} Shoot (S) or Pass (P)? ").strip().lower()
            if action == "s":
                if human.shoot(chamber):
                    print(f"{human.name} choose to shoot...")
                    sleep(2)
                    bot.lose_life()
                    print(f"A loud bang! {bot.name} loses a life. ({bot.lives} remaining)\n")
                    sleep(3)
                    round_over = True
                else:
                    print(f"{human.name} choose to shoot...")
                    sleep(2)
                    print(f"*click* It's a blank. {bot.name} lets out a sigh of relief")
            else:
                print(f"{human.name} hesitate and lower the gun.\n")

            # If a live bullet was fired, end the round.
            if round_over:
                break

            # Bot's turn.
            print(f"\n{bot.name} is thinking...", end="", flush=True)
            sleep(2)
            print("")
            bot_action = bot_decision(chamber)
            if bot_action == "s":
                print(f"{bot.name} chooses to shoot...")
                if bot.shoot(chamber):
                    sleep(3)
                    human.lose_life()
                    print(f"A loud bang! {human.name} lose a life. ({human.lives} remaining)")
                    sleep(2)
                    round_over = True
                else:
                    sleep(2)
                    print(f"*click* It's a blank. {human.name} feel your heart pounding.\n")
            else:
                print(f"{bot.name} hesitates and lowers the gun.\n")

        # End-of-round recap.
        if round_over:
            print("The round is over. Resetting for the next round...\n")
            sleep(3)

        # If either player's lives have dropped to 0, end the game.
        if human.lives == 0 or bot.lives == 0:
            os.system('cls')
            if bot.lives == 0:
                print("Your opponent slumps forward. \nThe room feels smaller, you're alone... \nBut something is still watching.")
            elif human.lives == 0:
                print(f"Darkness rushed in before {human.name} hit the ground. \n{human.name} wake up sitting at the same table... \nThe game isn't over")
            sleep(3)
            return

def start_menu():
    os.system('cls')
    display_title()
    print("A game about choices. \nDon't make a wrong one, your life depends on it.\n")
    print(f"{red}1. Start Game{endColor}")
    print(f"{blue}2. Exit{endColor}")

    choice = input("\nSelect an option: ").strip()
    if choice == "1":
        os.system('cls')
        print("Good Luck :)")
        sleep(3)
        os.system('cls')
        play_game()
    elif choice == "2":
        os.system('cls')
        print("You fear the inevitable, the game remains unfinished.")
        sleep(5)
        exit()
    else:
        start_menu()

if __name__ == "__main__":
    start_menu()