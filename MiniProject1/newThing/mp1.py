import itertools
import time
import re

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

def vigenere_brute_force(ciphertext, key_length, first_word_length, dictionary):
    dictionary = open(dictionary, "r").read().split()
    start_time = time.time()
    results = ""
    key_candidates = [''.join(i) for i in itertools.product(ALPHABET, repeat = key_length)]
    for key in key_candidates:
        plaintext = vigenere_cipher(ciphertext, key, DECRYPT)
        if plaintext[:first_word_length] in dictionary:
            results += ciphertext + ","+key+","+plaintext+","+str(time.time()-start_time)+"\n"
    return results

def driver():
    bruteForceTxt = "CipherText,Key,PlainText,Time\n"
    bruteForceTxt += vigenere_brute_force("MSOKKJCOSXOEEKDTOSLGFWCMCHSUSGX", 2, 6, "MP1_dict.txt")
    bruteForceTxt += vigenere_brute_force("PSPDYLOAFSGFREQKKPOERNIYVSDZSUOVGXSRRIPWERDIPCFSDIQZIASEJVCGXAYBGYXFPSREKFMEXEBIYDGFKREOWGXEQSXSKXGYRRRVMEKFFIPIWJSKFDJMBGCC", 3, 7, "MP1_dict.txt")
    bruteForceTxt += vigenere_brute_force("MTZHZEOQKASVBDOWMWMKMNYIIHVWPEXJA", 4, 10, "MP1_dict.txt")
    bruteForceTxt += vigenere_brute_force("SQLIMXEEKSXMDOSBITOTYVECRDXSCRURZYPOHRG", 5, 11, "MP1_dict.txt")
    bruteForceTxt += vigenere_brute_force("LDWMEKPOPSWNOAVBIDHIPCEWAETYRVOAUPSINOVDIEDHCDSELHCCPVHRPOHZUSERSFS", 6, 9, "MP1_dict.txt")
    f = open("mp1_output.csv", "w")
    f.write(bruteForceTxt)
    f.close()

# print(vigenere_cipher("MSOKKJCOSXOEEKDTOSLGFWCMCHSUSGX", "KS", DECRYPT))
# print(vigenere_brute_force("MSOKKJCOSXOEEKDTOSLGFWCMCHSUSGX", 2, 6, "MP1_dict.txt"))
driver()