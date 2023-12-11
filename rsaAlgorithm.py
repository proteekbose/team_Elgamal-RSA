# CS789 Cryptography - RSA Cipher Machine by Zuowen Tang
import random
from util import modularArithmetic as ma
from util import primalityTest_MR as ptmr
from util import factorizationAlgorithm_PR as fa

is_prime = lambda val: ptmr.is_prime(val)


# Encryption Algorithm
def Encrypt(modulus, exponent):
    if is_prime(modulus):
        return
    message = int(input("The plaintext is: "))

    # Lambda function for calculating ciphertext
    calculate_ciphertext = lambda plaintext, exponent, modulus: ma.fast_exponent(plaintext, exponent, modulus)

    ciphertext = calculate_ciphertext(message, exponent, modulus)
    print("Ciphertext is: ", int(ciphertext), "\n")


# Algorithm for decryption without private key
def Decode(modulus, exponent):
    if is_prime(modulus):
        return
    factor1, factor2 = fa.find_factors(modulus)  # Perform factorization on modulus
    if factor1 == -1 and factor2 == -1:  # The factorization needs to be reinitialized
        print("Exiting...")
        return -1

    totient = (factor1 - 1) * (factor2 - 1)

    # Lambda function to compute the private key
    compute_private_key = lambda totient, exponent: ma.extended_gcd(totient, exponent)[2] % totient

    private_key = compute_private_key(totient, exponent)
    return private_key


# Decryption Algorithm
def Decrypt(modulus, exponent, use_given_key):
    if is_prime(modulus):
        return

    # Lambda function to determine the decryption key
    get_decryption_key = lambda modulus, exponent, use_given_key: exponent if use_given_key else Decode(modulus,
                                                                                                        exponent)

    decryption_key = get_decryption_key(modulus, exponent, use_given_key)
    if decryption_key == -1:
        return

    encrypted_message = int(input("The ciphertext is: "))

    if ma.gcd(encrypted_message, modulus) != 1:
        print("Ciphertext is not relatively prime to the modulus.")
        return

    decrypted_message = ma.fast_exponent(encrypted_message, decryption_key, modulus)
    print("The plaintext is: ", decrypted_message, "\n")


# Start the cipher machine
def controller_RSA():
    while True:
        user_selection = None
        print("-------------------------------------")
        print("    Welcome to RSA crypto system     ")
        print("-------------------------------------")

        print("\nChoose the actions that you want to take:\n")
        # Lambda function for input validation
        validate_input = lambda choice: choice if 0 <= choice <= 5 else None

        while user_selection is None:
            try:
                print("Press (1) to Encrypt\nPress (2) to Decrypt\nPress (3) to Crack")
                print("Press (4) to Generate Keys\nPress (5) for COMPLETE DEMO\nPress (0) to Exit")
                user_selection = validate_input(int(input("\nPlease select a function: ")))
            except ValueError:
                print("Invalid input. \n")
                continue

        if user_selection == 0:
            print("\nExiting RSA crypto-system.")
            return
        elif user_selection == 1:
            modulus, exponent = verify(1)
            Encrypt(int(modulus), int(exponent))
        elif user_selection == 2:
            modulus, exponent = verify(2)
            Decrypt(int(modulus), int(exponent), True)
        elif user_selection == 3:
            modulus, exponent = verify(3)
            Decrypt(int(modulus), int(exponent), False)
        elif user_selection == 4:
            getKey()
        elif user_selection == 5:
            selfDemoRSA()


def getKey():
    random_generator_choice = None

    # Lambda function for input validation
    validate_generator_choice = lambda choice: choice if 0 <= choice <= 2 else None

    while random_generator_choice is None:
        try:
            print("\nChoose your Pseudorandom Number Generator: \n")
            print("Press (1) for Naor-Reingold\nPress (2) for Blum-Blum-Shub\nPress (0) for python default")
            random_generator_choice = validate_generator_choice(int(input("Please select a generator: ")))
        except ValueError:
            print("Invalid input. \n")
            continue
        if random_generator_choice is None:
            print("Invalid input. \n")

    modulus, public_exp, private_exp, random_message = genRandKey(random_generator_choice)
    print("public key: (m =", modulus, ", e =", public_exp, ") \nprivate key: (m =", modulus, ", d =",
          private_exp, ")")
    print("random message:", random_message, "\n")
    return modulus, public_exp


def genRandKey(random_generator):
    private_key, public_key, random_message = -1, 0, 0
    modulus, prime1, prime2 = ptmr.get_modulus(2, random_generator)
    totient = (prime1 - 1) * (prime2 - 1)

    # Lambda function to generate a random number within a range
    generate_random_number = lambda lower, upper: random.randint(lower, upper)

    for i in range(10):
        public_key = generate_random_number(2, totient)
        if ma.gcd(public_key, totient) == 1:
            break

    for i in range(10):
        random_message = generate_random_number(1, modulus)
        if ma.gcd(random_message, totient) == 1:
            break

    gcd, x, inverse = ma.extended_gcd(totient, public_key)
    private_key = inverse % totient

    # print("public key: ", modulus, ",", public_key)
    # print("private key: ", modulus, ",", private_key % totient, ",", totient)

    return modulus, public_key, private_key, random_message


def verify(user_choice):
    modulus, exponent = "modulus", "exponent"

    # Lambda function for input prompt
    prompt_input = lambda message: input(message).split(" ")

    while not modulus.isdigit() or not exponent.isdigit():
        try:
            prompt_message = "Enter public key modulus and exponent (separated by space): " if user_choice in [1,
                                                                                                             3] else "Enter private key modulus and exponent (split with space): "
            modulus, exponent = prompt_input(prompt_message)
        except ValueError:
            print("Invalid input. \n")
            continue
        if not modulus.isdigit() or not exponent.isdigit():
            print("Invalid input. \n")
            continue

    return modulus, exponent


def selfDemoRSA():
    print("\n🚀 Starting RSA Demonstration...")
    print("🔐 Generating random keys...")
    random_generator = random.randint(1, 2)
    modulus, public_exp, private_exp, message = genRandKey(random_generator)

    print("\n👩‍💼 Alice's public key: (modulus: {}, exponent: {})".format(modulus, public_exp))
    print("🔑 Alice's private key: (modulus: {}, exponent: {})\n".format(modulus, private_exp))

    print("👨‍💼 Bob wants to send message '{}' to Alice.".format(message))
    print("🔒 Bob encrypts the message using Alice's public key.")

    # Lambda function for fast exponentiation
    fast_exponent = lambda base, exp, mod: ma.fast_exponent(base, exp, mod)

    ciphertext = fast_exponent(message, public_exp, modulus)
    print("💬 The encrypted ciphertext is: {}\n".format(ciphertext))

    print("📩 Alice receives the encrypted message and decrypts it with her private key.")
    plaintext = fast_exponent(ciphertext, private_exp, modulus)
    print("🔓 She gets the plaintext: {}\n".format(plaintext))

    print("🕵️‍♀ Eve also knows the encrypted message sent to Alice;")
    print("🔨 She attempts to crack it without the private key.")
    prime_factor1, prime_factor2 = fa.find_factors(modulus)
    totient = (prime_factor1 - 1) * (prime_factor2 - 1)

    gcd, x, cracked_private_exp = ma.extended_gcd(totient, public_exp)
    cracked_private_exp %= totient

    print("🧮 Calculating the factors of the modulus, Eve finds {} and {}".format(prime_factor1, prime_factor2))
    print("These are prime factors of the modulus {}".format(modulus))
    print("🔓 Eve now can find Alice's private key (modulus: {}, exponent: {})".format(modulus, cracked_private_exp))
    decrypted_message = fast_exponent(ciphertext, cracked_private_exp, modulus)
    print("🕵️‍♀ Eve decrypts the message: {}\n".format(decrypted_message))
    print("✅ RSA Demonstration Finished.\n")
