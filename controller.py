# Cryptography Project - Controller for Cipher Machines
import elGamalAlgorithm
import rsaAlgorithm


def mainFunction():
    while True:
        choice = get_user_choice()
        if choice == 1:
            rsaAlgorithm.controller_RSA()
        elif choice == 2:
            elGamalAlgorithm.controller_ElGamal()
        elif choice == 0:
            print("-----------------------------\nQuiting...See you again")
            quit()


def get_user_choice():
    # Prompting user to choose a cipher algorithm or to quit.
    while True:
        print("\n-----------------------------")
        print("Choose your Cipher algorithm: \n\nPress (1) for RSA\nPress (2) for El-Gamal\nPress (0) to Exit")
        try:
            choice = int(input())
            if 0 <= choice <= 2:
                return choice
            print("Wrong input!\nPlease choose from the given options")
        except ValueError:
            print("Wrong input!\nPlease choose from the given options")


if __name__ == '__main__':
    mainFunction()
