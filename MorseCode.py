# Dictionary representing the Morse code chart
MorseCode = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', 
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

# Function to encrypt the string
def encrypt(message):
    txt = ''
    for letter in message:
        if letter.upper() in MorseCode:
            txt += MorseCode[letter.upper()] + ' '
        else:
            txt += 'Please enter a valid value. '  # Indicate error for unrecognized characters
    return txt

# Function to decrypt the string from morse to English
def decrypt(message):
    message += ' '
    morse = ''
    text = ''
    for letter in message:
        if letter != ' ':
            i = 0
            text += letter
        else:
            i += 1
            if i == 2:
                morse += ' '
            else:
                try:
                    if text in MorseCode.values():
                        morse += list(MorseCode.keys())[list(MorseCode.values()).index(text)]
                    else:
                        morse += 'Please enter a valid value. '  # Indicate error for unrecognized Morse sequences
                except ValueError:
                    morse += 'Please enter a valid value. '  # Indicate error if decoding fails unexpectedly
                text = ''
    return morse

# Main function to run the program
def main():
    print("Morse Code Translator")
    while True:
        choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()
        if choice == 'e':
            message = input("Enter the message to encrypt: ")
            result = encrypt(message)
            print(f"Encrypted message: {result}")
        elif choice == 'd':
            message = input("Enter the message to decrypt: ")
            result = decrypt(message)
            print(f"Decrypted message: {result}")
        elif choice == 'q':
            print("Exiting the Morse Code Translator.")
            break
        else:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")

if __name__ == "__main__":
    main()
