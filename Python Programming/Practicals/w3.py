# Secret Code Generator (Caesar Cipher)


# Function to encode a message
def encode_message(message, shift):
    encoded = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Wrap around the alphabet
            new_char = chr((ord(char) - base + shift) % 26 + base)
            encoded += new_char
        else:
            # Keep punctuation, numbers, spaces as-is
            encoded += char
    return encoded

# Function to decode a message
def decode_message(message, shift):
    # Decoding is simply encoding in reverse
    return encode_message(message, -shift)

# Function to show user menu
def menu():
    print("\n--- Secret Code Generator ---")
    print("1. Encode a message")
    print("2. Decode a message")
    print("3. Exit")

# Main program loop
def main():
    while True:
        menu()
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            message = input("Enter the message to encode: ")
            try:
                shift = int(input("Enter the shift number: "))
                result = encode_message(message, shift)
                print("Encoded Message:", result)
            except ValueError:
                print("Invalid shift. Please enter a number.")
        
        elif choice == '2':
            message = input("Enter the message to decode: ")
            try:
                shift = int(input("Enter the shift number: "))
                result = decode_message(message, shift)
                print("Decoded Message:", result)
            except ValueError:
                print("Invalid shift. Please enter a number.")
        
        elif choice == '3':
            print("Exit")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Run the program
if __name__ == "__main__":
    main()
