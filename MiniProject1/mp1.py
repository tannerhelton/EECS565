import sys
import itertools

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

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


def bruteForce(ciphertext, keyLength, firstWordLength):
    print("Brute forcing " + ciphertext + " with key length " + str(keyLength) + " and first word length " + str(firstWordLength) + "...")
    f = open('MP1_dict.txt')
    content = f.read().split()
    f.close()
    possibleWords = []
    for subset in itertools.product(alphabet, repeat=keyLength):
        key = ''.join(subset)
        plaintext = decrypt(ciphertext, key)
        if plaintext[0:firstWordLength] in content:
            possibleWords.append([plaintext, key])
            print(plaintext + "    " + key)
    f = open("output.txt", "w")
    for i in possibleWords:
        f.write(i[0] + '\t' + i[1] + '\n')
    f.close()

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

# main()
# bruteForce("TEST",1,4)

fPath = sys.argv[1]
f = open(fPath)
content = f.read().strip().split('\n')
f.close()
for word in content:
    cipher = word.split('\t')[0]
    key = word.split('\t')[1]
    wordLen = word.split('\t')[2]
    bruteForce(cipher, int(key), int(wordLen))