import itertools
import time

ENCRYPT = 0
DECRYPT = 1
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vigenere_cipher(text, key, mode):
    text = text.upper()
    key = key.upper()
    result = ""
    j = 0
    for i in range(len(text)):
        char = text[i]
        if char in ALPHABET:
            shift = ALPHABET.index(key[j % len(key)])
            if mode == ENCRYPT:
                result += ALPHABET[(ALPHABET.index(char) + shift) % 26]
            elif mode == DECRYPT:
                result += ALPHABET[(ALPHABET.index(char) - shift + 26) % 26]
            j += 1
    return result

def decrypt(ciphertext, key):
    plaintext = ''
    key_len = len(key)
    key_int = [ord(k) - 65 for k in key]
    ciphertext_int = [ord(c) - 65 if c.isupper() else ord(c) - 97 for c in ciphertext]
    for i, c in enumerate(ciphertext_int):
        k = key_int[i % key_len]
        m = (c - k) % 26
        plaintext += chr(m + 65) if m < 26 else chr(m + 97)
    return plaintext

def vigenere_brute_force(ciphertext, key_length, first_word_length, dictionary):
    dictionary = open(dictionary, "r").read().split()
    tmpDict = []
    for word in dictionary:
        if len(word) >= first_word_length:
            tmpDict.append(word)
    dictionary = tmpDict
    start_time = time.time()
    results = ""
    key_candidates = [''.join(i) for i in itertools.product(ALPHABET, repeat = key_length)]
    for key in key_candidates:
        plaintext = decrypt(ciphertext, key)
        if plaintext[:first_word_length] in dictionary:
            results += ciphertext + ","+key+","+plaintext+","+str(time.time()-start_time)+"\n"
    return results

def driver():
    f = open("mp1_output.csv", "w")
    f.write("CipherText,Key,PlainText,Time\n")
    f.close()
    f = open("mp1_output.csv", "a")
    f.write(vigenere_brute_force("MSOKKJCOSXOEEKDTOSLGFWCMCHSUSGX", 2, 6, "MP1_dict.txt"))
    f.close()
    f = open("mp1_output.csv", "a")
    f.write(vigenere_brute_force("PSPDYLOAFSGFREQKKPOERNIYVSDZSUOVGXSRRIPWERDIPCFSDIQZIASEJVCGXAYBGYXFPSREKFMEXEBIYDGFKREOWGXEQSXSKXGYRRRVMEKFFIPIWJSKFDJMBGCC", 3, 7, "MP1_dict.txt"))
    f.close()
    f = open("mp1_output.csv", "a")
    f.write(vigenere_brute_force("MTZHZEOQKASVBDOWMWMKMNYIIHVWPEXJA", 4, 10, "MP1_dict.txt"))
    f.close()
    f = open("mp1_output.csv", "a")
    f.write(vigenere_brute_force("SQLIMXEEKSXMDOSBITOTYVECRDXSCRURZYPOHRG", 5, 11, "MP1_dict.txt"))
    f.close()
    f = open("mp1_output.csv", "a")
    f.write(vigenere_brute_force("LDWMEKPOPSWNOAVBIDHIPCEWAETYRVOAUPSINOVDIEDHCDSELHCCPVHRPOHZUSERSFS", 6, 9, "MP1_dict.txt"))
    f.close()

driver()