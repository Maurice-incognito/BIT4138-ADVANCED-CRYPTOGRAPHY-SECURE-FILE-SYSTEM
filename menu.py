# Student: [Your Name] - BIT4138

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def vigenere_encrypt(text, key):
    result, ki = "", 0
    for char in text:
        if char.isalpha():
            shift = ord(key[ki % len(key)].upper()) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            ki += 1
        else:
            result += char
    return result

print("=== Cipher Menu ===")
print("1. Caesar Cipher")
print("2. Vigenere Cipher")
choice = input("Choose an option (1 or 2): ")

text = input("Enter text to encrypt: ")

if choice == "1":
    shift = int(input("Enter shift number: "))
    result = caesar_encrypt(text.upper(), shift)
    print("Encrypted:", result)
elif choice == "2":
    key = input("Enter keyword: ")
    result = vigenere_encrypt(text.upper(), key)
    print("Encrypted:", result)
else:
    print("Invalid option")