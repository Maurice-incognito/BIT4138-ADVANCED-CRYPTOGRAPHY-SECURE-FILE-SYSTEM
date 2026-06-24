# Student: [Your Name] - BIT4138

def rc4(key, text):
    # Key Scheduling Algorithm (KSA)
    key_bytes = [ord(c) for c in key]
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key_bytes[i % len(key_bytes)]) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo-Random Generation Algorithm (PRGA)
    i = j = 0
    keystream = []
    for _ in range(len(text)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        keystream.append(S[(S[i] + S[j]) % 256])

    # XOR plaintext with keystream
    encrypted = bytes([ord(c) ^ k for c, k in zip(text, keystream)])
    return encrypted

key       = "SECRETKEY"
plaintext = "Hello BIT4138"

encrypted = rc4(key, plaintext)
print("Plaintext :", plaintext)
print("Key       :", key)
print("Encrypted :", encrypted.hex())
print("(Encrypted bytes shown in hex format)")