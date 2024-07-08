# Password Manager

## Overview

The Password Manager is a Python-based application that allows users to generate and save secure passwords and retrieve them when needed. This tool is particularly useful for managing multiple accounts and maintaining strong, unique passwords for each.

## Features

- **Password Generation:** Create strong, random passwords of customizable length.
- **Password Saving:** Save passwords securely with a description in an encrypted file.
- **Password Decryption:** Retrieve and decrypt stored passwords using their descriptions.

## Requirements

- Python 3.x
- `cryptography` library (for encryption and decryption)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/its-nikkk/Password-Manager.git
   ```
   Navigate to the project directory:
   ```bash
   cd password-manager
   ```

2. **Install Dependencies:**
   Install the `cryptography` library if it's not already installed:
   ```bash
   pip3 install cryptography
   ```

3. **Make the Script Executable:**
   Ensure the main script has executable permissions:
   ```bash
   chmod +x password_manager.py
   ```

## Usage

### Running the Script

You can run the script directly using the following command:

```bash
./password_manager.py
```

Alternatively, you can run it with Python:

```bash
python3 password_manager.py
```

### User Interaction

1. **Generating a Password:**
   - Choose to generate a password by entering `g`.
   - Provide the desired password length.
   - Provide a description for the password.
   - The generated password will be displayed and saved securely.

2. **Decrypting a Password:**
   - Choose to decrypt a password by entering `d`.
   - Provide the description of the password to retrieve.
   - The decrypted password will be displayed if found.

3. **Exiting the Script:**
   - Choose to quit by entering `q`.

### Example Sessions

**Generating a Password:**

```plaintext
Welcome to the Password Manager
Would you like to (g)enerate a password, (d)ecrypt a password, or (q)uit? g
Enter the desired password length: 16
Enter a description for the password: Email Account
Generated Password: !d1B2$e3R4%u5G6&h7
Password saved successfully.
```

**Decrypting a Password:**

```plaintext
Welcome to the Password Manager
Would you like to (g)enerate a password, (d)ecrypt a password, or (q)uit? d
Enter the description of the password to decrypt: Email Account
Decrypted Password for 'Email Account': !d1B2$e3R4%u5G6&h7
```

### File Structure

- **`password_manager.py`**: The main script containing all functionality for password management.
- **`key.key`**: The file where the encryption key is stored (generated on first run).
- **`passwords.txt`**: The file where encrypted passwords are saved.

### Security Considerations

- **Keep `key.key` Secure:** The `key.key` file is critical for encryption and decryption. Do not share this file and keep it safe.
- **Encrypted Storage:** Passwords are stored in `passwords.txt` in an encrypted format to ensure security.
- **Sensitive Operations:** Be cautious when decrypting and displaying passwords to avoid exposing sensitive information.
