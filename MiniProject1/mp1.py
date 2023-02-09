import sys
import itertools
import string
import time

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
    start_time = time.time()
    for subset in itertools.product(alphabet, repeat=keyLength):
        key = ''.join(subset)
        plaintext = decrypt(ciphertext, key)
        if plaintext[0:firstWordLength] in content:
            possibleWords.append([plaintext, key, ciphertext])
            print(plaintext + "    " + key)
    outFile = ''
    for i in possibleWords:
        outFile += i[0] + ',' + i[1] + ',' + i[2] + ',' + str(time.time() - start_time) + '\n'
    return outFile

def main():
    print("Welcome to the Vigenere Cipher Program!")
    print("We strip the message of all whitespace and convert it to uppercase.")
    while True:
        mode = input("Would you like to encrypt (0), decrypt (1), or brute force (2)? ").strip().lower()
        if mode == "0":
            print("Encrypting...")
            plaintext = input("Enter a message: ").strip().upper()
            key = input("Enter a key: ").strip().upper()
            ciphertext = encrypt(plaintext, key)
            print("Encrypted message:", ciphertext)
            break
        elif mode == "1":
            print("Decrypting...")
            ciphertext = input("Enter a cipher: ").strip().upper()
            key = input("Enter a key: ").strip().upper()
            plaintext = decrypt(ciphertext, key)
            print("Decrypted message:", plaintext)
            break
        elif mode == "2":
            print("Brute forcing...")
            fileStreamIn()
            break
        else:
            print("Invalid input. Try again.")
    print("Created by Tanner Helton. Goodbye!")

def audrey_brute(ciphertext, key_length, first_word_length, dict_file):
    with open (dict_file, 'r') as f:
        words = set(word.strip().upper() for word in f)
    result = []
    start_time = time.time()
    for i in range (26**key_length):
        key = ""
        for j in range (key_length):
            key += chr(i // (26**i) % 26 + ord('A'))
        plaintext = decrypt(ciphertext, key)
        first_word = plaintext [:first_word_length].upper()
        if all(char in string.ascii_letters for char in first_word) and first_word in words:
            result.append(plaintext + "," + key + "," + ciphertext + "," + str(time.time() - start_time) + "\n")
    return result

def fileStreamIn():
    inPath = input("Enter the path to the input file: ").strip()
    outPath = input("Enter the path to the output file: ").strip()
    f = open(inPath)
    content = f.read().strip().split('\n')
    f.close()
    decryptedCiphers = 'Plaintext,Key,Ciphertext,Time\n'
    decryptedAudrey = 'Plaintext,Key,Ciphertext,Time\n'
    for word in content:
        cipher = word.split(',')[0]
        key = word.split(',')[1]
        wordLen = word.split(',')[2]
        decryptedCiphers += bruteForce(cipher, int(key), int(wordLen))
        decryptedAudrey += audrey_brute(cipher, int(key), int(wordLen), 'MP1_dict.txt')
    f = open(outPath, "w")
    f.write(decryptedCiphers)
    f.close()
    f = open("audrey.csv", "w")
    f.write(decryptedAudrey)
    f.close()

main()