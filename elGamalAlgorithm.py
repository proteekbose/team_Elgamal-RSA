# El-Gamal Cipher Machine
import random
from util import modularArithmetic as ma
from util import primalityTest_MR as ptmr
from util import keyGenerator_BSGS as kg
from util import factorizationAlgorithm_PR as fa
from util import pseudorandomGenerator_NR as pg_nr
from util import pseudorandomGenerator_BBS as pg_bbs


def alice_public_information(rand_gen, r):
    max_prime = 0
    # Generate 5 prime numbers using Miller-Rabin primality test and select the largest
    primes = ptmr.get_primes(5, rand_gen)
    for prime in primes:
        if prime > max_prime:
            max_prime = prime
    p = max_prime

    # Generate one of the primitive roots of p
    b = fa.primitive_root_search(p)

    # Generate a random number r if not provided
    if r is None:
        r = ptmr.get_primes(1, rand_gen)[0] % p - 1

    # Calculate b raised to the power of r modulo p
    br = ma.fast_exponent(b, r, p)
    print(f"Public information:\nAlice's prime number: {p}\nGenerator: {b}\nPublic number: {br}.")
    print(f"\nKeep Alice's secret number: {r}")


# Function to generate public information for Bob
def bob_pub_info(rand_gen, r):
    max_prime = 0
    # Generate 5 prime numbers using Miller-Rabin primality test and select the largest
    primes = ptmr.get_primes(5, rand_gen)
    for prime in primes:
        if prime > max_prime:
            max_prime = prime
    p = max_prime

    # Generate one of the primitive roots of p
    b = fa.primitive_root_search(p)

    # Generate a random number r if not provided
    if r is None:
        r = ptmr.get_primes(1, rand_gen)[0] % p - 1

    # Calculate b raised to the power of r modulo p
    br = ma.fast_exponent(b, r, p)
    print(f"Public information:\nBob's prime number: {p}\nGenerator: {b}\nPublic number: {br}.")
    print(f"\nKeep Bob's secret number: {r}")


def encrypt(g, h, message, p):
    """
    Encrypt a message using ElGamal encryption.
    Parameters:
    g (int): A primitive root modulo p.
    h (int): The recipient's public key (h = g^x mod p).
    message (int): The plaintext message to be encrypted.
    p (int): A large prime number.
    Returns:
    tuple: A pair (c1, c2) representing the encrypted message.
    """
    k = random.randint(2, p - 2)
    calculate_c1 = lambda base, exponent, modulus: pow(base, exponent, modulus)
    calculate_c2 = lambda msg, h_val, k_val, modulus: (msg * pow(h_val, k_val, modulus)) % modulus

    c1 = calculate_c1(g, k, p)
    c2 = calculate_c2(message, h, k, p)

    print(f"🔐 Encrypted Message: (c1: {c1}, c2: {c2})")
    return c1, c2


def decrypt(c1, c2, x, p):
    """
    Decrypt a message using ElGamal decryption.
    Parameters:
    c1 (int): The first component of the ciphertext.
    c2 (int): The second component of the ciphertext.
    x (int): The recipient's private key.
    p (int): A large prime number.
    Returns:
    int: The decrypted plaintext message.
    """
    calculate_s = lambda c1_val, x_val, modulus: pow(c1_val, x_val, modulus)
    calculate_message = lambda c2_val, s_inv_val, modulus: (c2_val * s_inv_val) % modulus

    s = calculate_s(c1, x, p)
    s_inv = ma.multiplicative_inverse(s, p)
    message = calculate_message(c2, s_inv, p)

    print(f"🔓 Decrypted Message: {message}")
    return message


def alice():
    get_choice = lambda: int(input(
        "\n🌟 Alice, choose your action: \n1 - Get Public Information \n2 - Encrypt a Message\nSelect (1/2): "))
    get_secret_number = lambda: int(input("\nEnter Alice's secret number: "))
    encrypt_message = lambda g, bl, msg, p: encrypt(g, bl, msg, p)

    print("\n🔮 You have chosen Alice")

    p, message, bl, g = None, None, None, None
    while None in [p, message, bl, g]:
        try:
            message = int(input("\n💬 Enter the message you want to send: "))
            bl = int(input("🔑 Enter Bob's public key (h): "))
            g = int(input("🌀 Enter the generator (g): "))
            p = int(input("🔢 Enter the prime number: "))
        except ValueError:
            print("⚠️ Invalid input. Please try again.\n")

    c1, c2 = encrypt_message(g, bl, message, p)
    #print(f"📧 Encrypted Message: (c1: {c1}, c2: {c2})\n")


# Interactive function for Bob to generate public information or decrypt a message
def bob():
    get_choice = lambda: int(input("\n🌟 Bob, what would you like to do? \n1 - Get Public Info \n2 - Decrypt a Message\nSelect (1/2): "))
    get_secret_number = lambda: int(input("\nEnter Bob's secret number: "))
    decrypt_message = lambda c1, c2, x, p: decrypt(c1, c2, x, p)

    print("\n🔮 You have chosen Bob")

    choice = None
    while choice not in [1, 2]:
        try:
            choice = get_choice()
        except ValueError:
            print("⚠️ Invalid input. Please try again.\n")

    if choice == 1:
        print("\n🔑 Generating Bob's Public Information...")
        rand = input("Do you want to enter your own secret key? (y/n): ").lower()
        r = get_secret_number() if rand == "y" else None
        bob_pub_info(2, r)

    elif choice == 2:
        p, c1, c2, x = None, None, None, None
        while None in [p, c1, c2, x]:
            try:
                c1 = int(input("\n🔒 Enter the first component of the ciphertext (c1): "))
                c2 = int(input("🔒 Enter the second component of the ciphertext (c2): "))
                x = int(input("🔐 Enter your secret number: "))
                p = int(input("🔢 Enter the prime number: "))
            except ValueError:
                print("⚠️ Invalid input. Please try again.\n")

        message = decrypt_message(c1, c2, x, p)
        print(f"📜 Decrypted Message: {message}\n")



# Interactive function for Eve to attempt to eavesdrop and decrypt a message
def eve():
    p, c1, c2, b, bl = None, None, None, None, None
    while None in [p, c1, c2, b, bl]:
        try:
            c1 = int(input("Enter the first component of the ciphertext (c1): "))
            c2 = int(input("Enter the second component of the ciphertext (c2): "))
            b = int(input("Enter the generator: "))
            # br = int(input("Enter Alice's public number: "))
            bl = int(input("Enter Bob's public number: "))
            p = int(input("Enter the prime number: "))
        except ValueError:
            print("Invalid input.")

    # Attempt to retrieve private keys using Baby-Step Giant-Step algorithm
    # r = BBstepGNstep.baby_step_giant_step(br, b, p)
    l = kg.baby_giant_step(bl, b, p)

    # Since Eve does not know the private key directly, she attempts to crack it
    # Assuming Eve has found the secret number 'x' (Bob's private key) through some means
    x = l  # or r, depending on whose key she found

    # Crack the ciphertext
    message = decrypt(c1, c2, x, p)

    # print(f"Alice's secret number is: {r}")
    print(f"Bob's secret number is: {l}")
    print(f"The decrypted message is: {message}\n")


def controller_ElGamal():
    print("------------------------------------------")
    print("    Welcome to EL-GAMAL crypto system     ")
    print("------------------------------------------")
    # Main driver function for the El-Gamal crypto-system.
    print("\nChoose the role which you want to play:\n")
    while True:
        role = input("Press (1) for Alice\nPress (2) for Bob\nPress (3) for Eve\nPress (4) for COMPLETE DEMO [Self "
                     "Run]\nPress (0) to Exit \n").strip()
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
    print("\n🌠 Starting EL-GAMAL DEMONSTRATION... 🌠")

    # Random generator selection
    rand_gen = random.randint(1, 2)
    print(f"🎲 Selecting Random Generator: {'Naor-Reingold' if rand_gen == 1 else 'Blum-Blum-Shub'}\n")

    # Lambda functions
    get_largest_prime = lambda rand: max(ptmr.get_primes(5, rand))
    get_primitive_root = lambda p: fa.primitive_root_search(p)
    calculate_public_key = lambda base, secret, prime: ma.fast_exponent(base, secret, prime)

    # Generate prime and primitive root
    p = get_largest_prime(rand_gen)
    b = get_primitive_root(p)

    # Generate secret numbers
    r, l = [ptmr.get_primes(1, rand_gen)[0] % (p - 1) for _ in range(2)]

    # Calculate public keys
    br, bl = calculate_public_key(b, r, p), calculate_public_key(b, l, p)

    # Display public and private information
    print(f"🔑 Alice and Bob agree on Prime Number: {p} and Generator: {b}\n")
    print(f"🔏 Alice's Secret Number: {r} ➡️ Public Key: {br}")
    print(f"🔏 Bob's Secret Number: {l} ➡️ Public Key: {bl}\n")
    print("⚙️ Generating Message...\n")

    # Generate and encrypt message
    message = pg_nr.rand_gen() if rand_gen == 1 else pg_bbs.rand_gen()
    c1, c2 = encrypt(b, bl, message, p)
    print(f"📨 Alice sends encrypted message: (c1: {c1}, c2: {c2}) to Bob")

    # Bob decrypts the message
    plain = decrypt(c1, c2, l, p)
    print(f"📬 Bob decrypts the message: {plain}\n")

    # Eve's attempt to eavesdrop
    print("🕵️‍♀️ Eve intercepts the message and attempts to decrypt it...")
    r2, l2 = kg.baby_giant_step(br, b, p), kg.baby_giant_step(bl, b, p)
    plaintext2 = decrypt(c1, c2, l2, p)
    print(f"Eve's cracked secret numbers: {r2}, {l2}")
    print(f"🔓 Eve decrypts the message: {plaintext2}\n")

    print("🌈 EL-GAMAL DEMONSTRATION COMPLETED SUCCESSFULLY! 🎉")
