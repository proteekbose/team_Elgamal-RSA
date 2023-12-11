# El-Gamal Cipher Machine
import random
from util import modularArithmetic as ma
from util import primalityTest_MR as ptmr
from util import keyGenerator_BSGS as kg
from util import factorizationAlgorithm_PR as fa
from util import pseudorandomGenerator_NR as pg_nr
from util import pseudorandomGenerator_BBS as pg_bbs


def alice_public_info(rand_gen, r):
    # Generates and display Alice's public information.
    p = max(ptmr.get_primes(5, rand_gen))
    b = fa.primitive_root_search(p)
    r = r or ptmr.get_primes(1, rand_gen)[0] % (p - 1)
    br = ma.fast_exponent(b, r, p)
    print(f"Public info: \n\nAlice's prime number: {p} \ngenerator: {b}, "
          f"\nAlice's public number : {br}.\nAlice's secret number: {r}, **[CONFIDENTIAL]***\n")


def bob_public_info(p, b, l):
    # Generates and display Bob's public information.
    l = l or ptmr.get_primes(1, 2)[0] % (p - 1)
    bl = ma.fast_exponent(b, l, p)
    print(f"\nBob's public number: {bl}\nBob's secret number : {l}, **[CONFIDENTIAL]***\n")


def encrypt(brl, message, p):
    # Encrypts a message.
    return (message * brl) % p


def decrypt(brl_rev, cipher, p):
    # Decrypts a message.
    return (cipher * brl_rev) % p


def alice():
    # Alice's actions in the El-Gamal crypto-system.
    print(f"\nMake a choice of action:\n\n")
    choice = input("Press (1) to Get Public Information\nPress (2) to Encrypt a message:\n").strip()
    if choice == '1':
        r = input("Enter your secret number?(y/n) :").lower().startswith('y') and int(
            input("Alice's secret number : "))
        alice_public_info(2, r)
    elif choice == '2':
        message, bl, r, p = (int(input(prompt)) for prompt in
                             ["Enter the message: ", "Enter Bob's public number: ", "Enter Alice's secret number: ",
                              "Enter the prime number: "])
        brl = ma.fast_exponent(bl, r, p)
        cipher = encrypt(brl, message, p)
        print(f"The encoded ciphertext is : {cipher}\n")


def bob():
    # Bob's actions in the El-Gamal crypto-system.
    print(f"\nMake a choice of action:\n\n")
    choice = input("Press (1) to Get Public Information\nPress (2) to Decrypt a message: ").strip()
    if choice == '1':
        p, b, br = map(int, input("Prime number : , generator : , public number : ").split())
        if not ptmr.is_prime(p):
            print(f"{p} is not a prime number.\n")
            return
        l = input("Enter your secret number?(y/n) :").lower().startswith('y') and int(
            input("Bob's secret number : "))
        bob_public_info(p, b, l)
    elif choice == '2':
        cipher, br, l, p = (int(input(prompt)) for prompt in
                            ["Enter the ciphertext: ", "Enter Alice's public number: ", "Enter Bob's secret number: ",
                             "Enter the prime number: "])
        brl = ma.fast_exponent(br, l, p)
        gcd, x, y = ma.extended_gcd(p, brl)
        brl_rev = y % p
        message = decrypt(brl_rev, cipher, p)
        print(f"The decoded message is {message}\n")


def eve():
    # Eve's actions in the El-Gamal crypto-system.
    cipher, b, br, bl, p = (int(input(prompt)) for prompt in
                            ["Enter the ciphertext: ", "Enter the generator: ", "Enter Alice's public number: ",
                             "Enter Bob's public number: ", "Enter the prime number: "])
    r, l = kg.baby_giant_step(br, b, p), kg.baby_giant_step(bl, b, p)
    brl = ma.fast_exponent(br, l, p)
    gcd, x, y = ma.extended_gcd(p, brl)
    brl_rev = y % p
    message = decrypt(brl_rev, cipher, p)
    print(f"Alice's secret number : {r}\nBob's secret number : {l}\nThe decoded message : {message}\n")


def controller_ElGamal():
    print("------------------------------------------")
    print("    Welcome to EL-GAMAL crypto system     ")
    print("------------------------------------------")
    # Main driver function for the El-Gamal crypto-system.
    print("\nChoose the role which you want to play:\n")
    while True:
        role = input("Press (1) for Alice\nPress (2) for Bob\nPress (3) for Eve\nPress (4) for COMPLETE DEMO\nPress ("
                     "0) to Exit \n").strip()
        if role == '1':
            alice()
        elif role == '2':
            bob()
        elif role == '3':
            eve()
        elif role == '4':
            selfDemo()
        elif role == '0':
            print("\nExiting the El-Gamal crypto-system.\n")
            break


def selfDemo():
    print("\n🌟 Starting EL-GAMAL DEMONSTRATION...")
    rand_gen = random.randint(1, 2)
    print("🔍 Generating random prime number...\n")

    # Select the largest prime from a set of randomly generated primes
    p = max(ptmr.get_primes(5, rand_gen))

    # Generate a primitive root b
    b = fa.primitive_root_search(p)

    # Generate random secret numbers r and l
    r, l = [ptmr.get_primes(1, rand_gen)[0] % (p - 1) for _ in range(2)]

    # Calculate public keys
    br, bl = [ma.fast_exponent(b, secret, p) for secret in [r, l]]
    shared_key = ma.fast_exponent(br, l, p)

    # Display public and private information
    print_public_private_info(p, b, br, bl, r, l, shared_key)

    # Alice sends a message to Bob
    message = pg_nr.rand_gen() if rand_gen == 1 else pg_bbs.rand_gen()
    cipher = encrypt(shared_key, message, p)
    plain = decrypt(shared_key, cipher, p)
    print_message_exchange(message, cipher, plain)

    # Eve's attempt to crack the ciphertext
    r2, l2 = [kg.baby_giant_step(pub, b, p) for pub in [br, bl]]
    plaintext2 = decrypt(shared_key, cipher, p)
    print_cracking_attempt(r2, l2, plaintext2)
    print("🎉 Congratulations! The DEMO is completed.\n")


def print_public_private_info(p, b, br, bl, r, l, shared_key):
    """Prints public and private information of Alice and Bob."""
    print("Alice and Bob both agreed on:\nprime number: ", p, "\ngenerator: ", b)
    print("\nAlice chooses her secret number:", r, "\nAlice calculates:", br)
    print("\nBob chooses his secret number:", l, "\nBob calculates:", bl, "\n")
    print("--------------------------")
    print("The public information:\n")
    print("Prime number:", p)
    print("The generator:", b)
    print("Alice's public number:", br)
    print("Bob's public number:", bl)
    print("\n--------------------------")
    print("The private information:\n")
    print("Alice's secret number:", r)
    print("Bob's secret number:", l)
    print("Alice and Bob both share the key:", shared_key)
    print("\n-------------------------------------------------")
    print("Now Alice and Bob can share messages between them.")
    print("--------------------------------------------------")


def print_message_exchange(message, cipher, plain):
    """Prints the message exchange process between Alice and Bob."""
    print("\nAlice calculates the cipher:", cipher)
    print("Bob receives the cipher and calculates the plaintext:", plain)
    print("They successfully exchanged information.\n")

    print("\nEve knows the public information and the ciphertext.")
    print("She can crack it without knowing the secrets.")
    print("She can crack it within few seconds with a 24-bit number\n")


def print_cracking_attempt(r2, l2, plaintext2):
    """Prints Eve's attempt to crack the ciphertext."""
    print("\nEve tries to crack the message [Baby-Step&Giant-Step].")
    print("She knows has the secret numbers:", r2, "and", l2)
    print("Using those information, she cracked the plaintext:", plaintext2, "\n")


