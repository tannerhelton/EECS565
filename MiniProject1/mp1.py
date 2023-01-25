alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(plaintext, key):
    keyLength = len(key)
    keyChars = [ord(i) for i in key]
    plaintextChars = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintextChars)):
        shift = (plaintextChars[i] + keyChars[i % keyLength]) % 26
        ciphertext += chr(shift + 65)
    return ciphertext

def decrypt(ciphertext, key):
    keyLength = len(key)
    keyChars = [ord(i) for i in key]
    ciphertextChars = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertextChars)):
        shift = (ciphertextChars[i] - keyChars[i % keyLength]) % 26
        plaintext += chr(shift + 65)
    return plaintext

def main():
    print("Welcome to the Vigenere Cipher Program!")
    print("We strip the message of all whitespace and convert it to uppercase.")
    plaintext = input("Enter a message: ").strip().upper()
    key = input("Enter a key: ").strip().upper()
    ciphertext = encrypt(plaintext, key)
    print("Encrypted message:", ciphertext)
    plaintext = decrypt(ciphertext, key)
    print("Decrypted message:", plaintext)
    print("Created by Tanner Helton. Goodbye!")

main()