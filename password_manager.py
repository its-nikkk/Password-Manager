#!/usr/bin/env python3

import random
import string
from cryptography.fernet import Fernet
import os

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

key_file = 'key.key'

def generate_key():
    if not os.path.exists(key_file):
        key = Fernet.generate_key()
        with open(key_file, 'wb') as key_out:
            key_out.write(key)

def load_key():
    return open(key_file, 'rb').read()

def save_password(description, password):
    generate_key()
    key = load_key()
    cipher_suite = Fernet(key)

    with open('passwords.txt', 'ab') as f:
        encrypted_password = cipher_suite.encrypt(password.encode())
        f.write(f'{description}: {encrypted_password.decode()}\n'.encode())

def decrypt_password(description):
    generate_key()
    key = load_key()
    cipher_suite = Fernet(key)

    with open('passwords.txt', 'rb') as f:
        for line in f:
            desc, encrypted_password = line.decode().split(': ')
            if desc == description:
                decrypted_password = cipher_suite.decrypt(encrypted_password.encode()).decode()
                return decrypted_password

    return None  # If no matching description is found

def main():
    print("Welcome to the Password Manager")
    while True:
        choice = input("Would you like to (g)enerate a password, (d)ecrypt a password, or (q)uit? ")

        if choice.lower() == 'g':
            length = int(input("Enter the desired password length: "))
            description = input("Enter a description for the password: ")
            password = generate_password(length)
            print(f"Generated Password: {password}")
            save_password(description, password)
            print("Password saved successfully.")
        elif choice.lower() == 'd':
            description = input("Enter the description of the password to decrypt: ")
            decrypted_password = decrypt_password(description)
            if decrypted_password:
                print(f"Decrypted Password for '{description}': {decrypted_password}")
            else:
                print("No password found with that description.")
        elif choice.lower() == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 'g', 'd', or 'q'.")

if __name__ == "__main__":
    main()
