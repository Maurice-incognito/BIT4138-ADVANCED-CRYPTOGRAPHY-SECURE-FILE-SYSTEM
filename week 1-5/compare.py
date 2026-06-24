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

word = "SECURITY"
print("Original word    :", word)
print("Caesar  (shift 4):", caesar_encrypt(word, 4))
print("Vigenere (key KEY):", vigenere_encrypt(word, "KEY"))
print()
print("Notice: Caesar always shifts by the same amount.")
print("Vigenere shifts each letter differently - harder to crack!")