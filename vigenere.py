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

def vigenere_decrypt(text, key):
    result, ki = "", 0
    for char in text:
        if char.isalpha():
            shift = ord(key[ki % len(key)].upper()) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
            ki += 1
        else:
            result += char
    return result

print(vigenere_decrypt("RIJVS LOXUYVI", "KEY"))