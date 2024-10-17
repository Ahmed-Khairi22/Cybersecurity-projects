def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Handle uppercase and lowercase letters separatelyD
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Non-alphabetical characters are not changed
    return result

# Input message and shift
mode = input("Do you want to (E)ncrypt or (D)ecrypt? ").lower()
message = input("Enter your message: ")
shift_value = int(input("Enter shift value: "))
if mode == 'd':
    shift_value = -shift_value  # Reverse shift for decryption

encrypted_message = caesar_cipher(message, shift_value)
print("Result:", encrypted_message)
