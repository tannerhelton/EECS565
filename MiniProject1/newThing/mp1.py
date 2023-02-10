import string
import time

def vigenere_cipher_func(text, key, mode):
    key_length = len(key)
    key_index = 0
    result = ""
    for char in text:
        char = char.upper()
        if char.isalpha():
            key_char = key[key_index % key_length].upper()
            key_index += 1
            if mode == 0:
                result += chr((ord(char)+ord(key_char)-2*ord('A'))%26+ord('A'))
            else:
                result += chr((ord(char)-ord(key_char)+26)%26+ord('A'))
    return result

def encrypt(plaintext, key):
    return vigenere_cipher_func(plaintext, key, 0)

def decrypt(plaintext, key):
    return vigenere_cipher_func(plaintext, key, 1)

def brute_force_cracker(ciphertext, key_length, first_word_length, dict_file):
    with open(dict_file, 'r') as f:
        words = set(word.strip().upper() for word in f)
    results = []
    for i in range(26**key_length):
        key = ""
        for j in range(key_length):
            key += chr(i // (26**j) % 26 + ord('A'))
        plaintext = decrypt(ciphertext, key)
        first_word = plaintext[:first_word_length].upper()
        if first_word in words:
            results.append((plaintext,key))
    return results

def brute_force_executive(ciphertext, key_length, first_word_length):
    dict_file = ("MP1_dict.txt")
    start_time = time.time()
    result = brute_force_cracker(ciphertext, key_length, first_word_length, dict_file)
    end_time = time.time()-start_time
    brute_str = ""
    for plaintext, key in result:
        brute_str += ciphertext + ", " + key + ", " + plaintext + ", " + str(end_time) + "\n"
        print(ciphertext + ", " + key + ", " + plaintext + ", " + str(end_time))
    return brute_str

def main():
    print("Welcome to the Vigenere Cipher Cracker!")
    mode = int(input("Do you want to encrypt (0), decrypt (1) a message, or brute force a ciphertext (2): "))
    if mode == 0:
        plaintext = input("Enter the plaintext you would like to encrypt: ").strip().upper()
        key = input("Enter the key you would like to use: ").strip().upper()
        print("The ciphertext is: " + encrypt(plaintext, key))
    elif mode == 1:
        ciphertext = input("Enter the ciphertext you would like to decrypt: ").strip().upper()
        key = input("Enter the key you would like to use: ").strip().upper()
        print("The plaintext is: " + decrypt(ciphertext, key))
    elif mode == 2: 
        start_total_time = time.time()
        result = "Ciphertext, Key, Plaintext, Time\n"
        result += brute_force_executive("MSOKKJCOSXOEEKDTOSLGFWCMCHSUSGX",2,6)
        result += brute_force_executive("PSPDYLOAFSGFREQKKPOERNIYVSDZSUOVGXSRRIPWERDIPCFSDIQZIASEJVCGXAYBGYXFPSREKFMEXEBIYDGFKREOWGXEQSXSKXGYRRRVMEKFFIPIWJSKFDJMBGCC",3,7)
        result += brute_force_executive("MTZHZEOQKASVBDOWMWMKMNYIIHVWPEXJA",4,10)
        result += brute_force_executive("SQLIMXEEKSXMDOSBITOTYVECRDXSCRURZYPOHRG",5,11)
        result += brute_force_executive("LDWMEKPOPSWNOAVBIDHIPCEWAETYRVOAUPSINOVDIEDHCDSELHCCPVHRPOHZUSERSFS",6,9)
        open("output.csv", "w").write(result)
        print("Done! Output has been saved to output.csv")
        print("Total Time:",str(time.time()-start_total_time))
    print("Thank you for using the Vigenere Cipher Cracker! Goodbye!")
    print("Made by Tanner Helton.")

if __name__ == '__main__':
    main()