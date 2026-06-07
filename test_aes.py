from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"Hello Cryptography!")
print("Encrypted:", token)
print("Decrypted:", f.decrypt(token))