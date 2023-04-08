from tkinter import *
import numpy as np
import string

root = Tk()
root.geometry("1000x600")
root.title("Computer Security")


def encypt():
    alg = selected.get()
    textdata = text1.get('1.0', END)
    keydata = key.get()
    if (alg == algorithms[0]):
        def caeser_encrypt_text(plaintext, n):
            n = int(n)
            ans = ""
            for i in range(len(plaintext)-1):
                ch = plaintext[i]
                if ch == " ":
                    ans += " "
                elif (ch.isupper()):
                    ans += chr((ord(ch) + n-65) % 26 + 65)
                else:
                    ans += chr((ord(ch) + n-97) % 26 + 97)
            return ans

        text2.insert(INSERT, caeser_encrypt_text(textdata, keydata))
    elif (alg == algorithms[1]):
        def monoalphabetic_encrypt(plaintext, key):
            alphabet = string.ascii_uppercase
            key = key.upper()
            plaintext = plaintext.upper()
            substitution_map = str.maketrans(alphabet, key)
            return plaintext.translate(substitution_map)

        text2.insert(INSERT, monoalphabetic_encrypt(textdata, keydata))

    elif (alg == algorithms[2]):
        def playfair_encrypt(plaintext, key):
            key = key.replace(" ", "").upper()
            key_square = ""
            for c in key:
                if c not in key_square:
                    key_square += c
            for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
                if c not in key_square:
                    key_square += c
            plaintext = plaintext.upper().replace(" ", "")
            plaintext = "".join([c for c in plaintext if c in key_square])
            if len(plaintext) % 2 == 1:
                plaintext += "X"
            digraphs = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]
            ciphertext = ""
            for d in digraphs:
                r1, c1 = divmod(key_square.index(d[0]), 5)
                r2, c2 = divmod(key_square.index(d[1]), 5)
                if r1 == r2:
                    ciphertext += key_square[r1*5 +
                                             (c1+1) % 5] + key_square[r2*5+(c2+1) % 5]
                elif c1 == c2:
                    ciphertext += key_square[((r1+1) % 5)*5+c1] + \
                        key_square[((r2+1) % 5)*5+c2]
                else:
                    ciphertext += key_square[r1*5+c2] + key_square[r2*5+c1]

            return ciphertext

        text2.insert(INSERT, playfair_encrypt(textdata, keydata))

    elif (alg == algorithms[3]):
        keydata = list(keydata.split(" "))
        for i in range(0, len(keydata)):
            keydata[i] = int(keydata[i])

        if (len(keydata) == 4):
            def hill_cipher_2x2_encrypt(plaintext, key_matrix):

                plaintext = plaintext.upper().replace(" ", "")
                if len(plaintext) % 2 != 0:
                    plaintext += "X"
                plaintext_matrix = np.array(
                    [ord(char) - ord("A") for char in plaintext])
                plaintext_matrix = plaintext_matrix.reshape(-1, 2)
                key_matrix = np.array(key_matrix).reshape(2, 2)
                ciphertext_matrix = np.dot(plaintext_matrix, key_matrix) % 26
                ciphertext = "".join([chr(int(char) + ord("A"))
                                      for row in ciphertext_matrix for char in row])

                return ciphertext
            text2.insert(INSERT, hill_cipher_2x2_encrypt(textdata, keydata))

        elif (len(keydata) == 9):
            def hill_cipher_3x3_encrypt(plaintext, key_matrix):
                plaintext = plaintext.upper().replace(" ", "")
                if len(plaintext) % 3 != 0:
                    padding_length = 3 - len(plaintext) % 3
                    plaintext += "X" * padding_length
                plaintext_matrix = np.array(
                    [ord(char) - ord("A") for char in plaintext])
                plaintext_matrix = plaintext_matrix.reshape(-1, 3)
                key_matrix = np.array(key_matrix).reshape(3, 3)
                ciphertext_matrix = np.dot(plaintext_matrix, key_matrix) % 26
                ciphertext = "".join([chr(int(char) + ord("A"))
                                      for row in ciphertext_matrix for char in row])

                return ciphertext
            text2.insert(INSERT, hill_cipher_3x3_encrypt(textdata, keydata))

    elif (alg == algorithms[4]):
        def railFenceEncrypt(plaintext, rails):
            rails = int(rails)
            plaintext = plaintext.replace(" ", "").upper()
            fence = [[] for i in range(rails)]
            rail = 0
            direction = 1
            for c in plaintext:
                fence[rail].append(c)
                rail += direction
                if rail == 0 or rail == rails-1:
                    direction = -direction
            ciphertext = ""
            for r in fence:
                ciphertext += "".join(r)

            return ciphertext

        text2.insert(INSERT, railFenceEncrypt(textdata, keydata))

    elif (alg == algorithms[5]):
        def row_transposition_encrypt(plaintext, key):
            plaintext = plaintext.replace(" ", "")
            num_rows = (len(plaintext) + len(key) - 1) // len(key)
            padded_plaintext = plaintext.ljust(num_rows * len(key), "X")
            ciphertext = ""
            for i in range(len(key)):
                col_index = key.index(str(i+1))
                for j in range(num_rows):
                    ciphertext += padded_plaintext[j*len(key)+col_index]

            return ciphertext

        text2.insert(INSERT, row_transposition_encrypt(textdata, keydata))


def decrypt():
    alg = selected.get()
    textdata = text1.get('1.0', END)
    keydata = key.get()
    if (alg == algorithms[0]):
        def caeser_decrypt_text(plaintext, n):
            n = int(n)
            ans = ""
            for i in range(len(plaintext)-1):
                ch = plaintext[i]
                if ch == " ":
                    ans += " "
                elif (ch.isupper()):
                    ans += chr((ord(ch) - n-65) % 26 + 65)
                else:
                    ans += chr((ord(ch) - n-97) % 26 + 97)
            print(ans)
            return ans

        text2.insert(INSERT, caeser_decrypt_text(textdata, keydata))
    elif (alg == algorithms[1]):
        def monoalphabetic_decrypt(ciphertext, key):
            alphabet = string.ascii_uppercase
            key = key.upper()
            ciphertext = ciphertext.upper()
            substitution_map = str.maketrans(key, alphabet)
            return ciphertext.translate(substitution_map)

        text2.insert(INSERT, monoalphabetic_decrypt(textdata, keydata))

    elif (alg == algorithms[2]):

        def playfair_decrypt(ciphertext, key):
            key = key.replace(" ", "").upper()
            key_square = ""
            for c in key:
                if c not in key_square:
                    key_square += c
            for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
                if c not in key_square:
                    key_square += c
            ciphertext = ciphertext.upper().replace(" ", "")
            ciphertext = "".join([c for c in ciphertext if c in key_square])
            digraphs = [ciphertext[i:i+2]
                        for i in range(0, len(ciphertext), 2)]
            plaintext = ""
            for d in digraphs:
                r1, c1 = divmod(key_square.index(d[0]), 5)
                r2, c2 = divmod(key_square.index(d[1]), 5)
                if r1 == r2:
                    plaintext += key_square[r1*5+(c1-1) %
                                            5] + key_square[r2*5+(c2-1) % 5]
                elif c1 == c2:
                    plaintext += key_square[((r1-1) % 5)*5+c1] + \
                        key_square[((r2-1) % 5)*5+c2]
                else:
                    plaintext += key_square[r1*5+c2] + key_square[r2*5+c1]

            return plaintext
        text2.insert(INSERT, playfair_decrypt(textdata, keydata))

    elif (alg == algorithms[3]):
        keydata = list(keydata.split(" "))
        for i in range(0, len(keydata)):
            keydata[i] = int(keydata[i])

        if (len(keydata) == 4):
            def hill_cipher_2x2_decrypt(ciphertext, key_matrix):
                ciphertext = ciphertext.upper().replace(" ", "")
                if len(ciphertext) % 2 != 0:
                    ciphertext += "X"
                ciphertext_matrix = np.array(
                    [ord(char) - ord("A") for char in ciphertext])
                ciphertext_matrix = ciphertext_matrix.reshape(-1, 2)
                key_matrix = np.array(key_matrix).reshape(2, 2)
                determinant = key_matrix[0, 0] * key_matrix[1,
                                                            1] - key_matrix[0, 1] * key_matrix[1, 0]
                inverse_determinant = None
                for i in range(26):
                    if (determinant * i) % 26 == 1:
                        inverse_determinant = i
                        break
                if inverse_determinant is None:
                    return None
                key_matrix_inverse = np.array([
                    [key_matrix[1, 1], -key_matrix[0, 1]],
                    [-key_matrix[1, 0], key_matrix[0, 0]]
                ]) * inverse_determinant % 26
                plaintext_matrix = np.dot(
                    ciphertext_matrix, key_matrix_inverse) % 26
                plaintext = "".join([chr(int(char) + ord("A"))
                                    for row in plaintext_matrix for char in row])
                return plaintext

            text2.insert(INSERT, hill_cipher_2x2_decrypt(textdata, keydata))

        elif (len(keydata) == 9):
            def hill_cipher_3x3_decrypt(ciphertext, key_matrix):
                ciphertext = ciphertext.upper().replace(" ", "")
                if len(ciphertext) % 3 != 0:
                    padding_length = 3 - len(ciphertext) % 3
                    ciphertext += "X" * padding_length
                ciphertext_matrix = np.array(
                    [ord(char) - ord("A") for char in ciphertext])
                ciphertext_matrix = ciphertext_matrix.reshape(-1, 3)
                key_matrix = np.array(key_matrix).reshape(3, 3)
                determinant = (
                    key_matrix[0, 0] * (key_matrix[1, 1] * key_matrix[2,
                                        2] - key_matrix[1, 2] * key_matrix[2, 1])
                    - key_matrix[0, 1] * (key_matrix[1, 0] * key_matrix[2,
                                                                        2] - key_matrix[1, 2] * key_matrix[2, 0])
                    + key_matrix[0, 2] * (key_matrix[1, 0] * key_matrix[2,
                                                                        1] - key_matrix[1, 1] * key_matrix[2, 0])
                )
                inverse_determinant = None
                for i in range(26):
                    if (determinant * i) % 26 == 1:
                        inverse_determinant = i
                        break
                if inverse_determinant is None:
                    return None
                key_matrix_inverse = np.zeros((3, 3))
                key_matrix_inverse[0, 0] = (key_matrix[1, 1] * key_matrix[2, 2] -
                                            key_matrix[1, 2] * key_matrix[2, 1]) * inverse_determinant % 26
                key_matrix_inverse[1, 0] = - (key_matrix[1, 0] * key_matrix[2, 2] -
                                              key_matrix[1, 2] * key_matrix[2, 0]) * inverse_determinant % 26
                key_matrix_inverse[2, 0] = (key_matrix[1, 0] * key_matrix[2, 1] -
                                            key_matrix[1, 1] * key_matrix[2, 0]) * inverse_determinant % 26
                key_matrix_inverse[0, 1] = - (key_matrix[0, 1] * key_matrix[2, 2] -
                                              key_matrix[0, 2] * key_matrix[2, 1]) * inverse_determinant % 26
                key_matrix_inverse[1, 1] = (key_matrix[0, 0] * key_matrix[2, 2] -
                                            key_matrix[0, 2] * key_matrix[2, 0]) * inverse_determinant % 26
                key_matrix_inverse[2, 1] = - (key_matrix[0, 0] * key_matrix[2, 1] -
                                              key_matrix[0, 1] * key_matrix[2, 0]) * inverse_determinant % 26
                key_matrix_inverse[0, 2] = (key_matrix[0, 1] * key_matrix[1, 2] -
                                            key_matrix[0, 2] * key_matrix[1, 1]) * inverse_determinant % 26
                key_matrix_inverse[1, 2] = - (key_matrix[0, 0] * key_matrix[1, 2] -
                                              key_matrix[0, 2] * key_matrix[1, 0]) * inverse_determinant % 26
                key_matrix_inverse[2, 2] = (key_matrix[0, 0] * key_matrix[1, 1] -
                                            key_matrix[0, 1] * key_matrix[1, 0]) * inverse_determinant % 26
                plaintext_matrix = np.dot(
                    ciphertext_matrix, key_matrix_inverse) % 26
                plaintext = "".join([chr(int(char) + ord("A"))
                                    for row in plaintext_matrix for char in row])
                if "X" in plaintext:
                    plaintext = plaintext[:plaintext.index("X")]

                return plaintext
            text2.insert(INSERT, hill_cipher_3x3_decrypt(textdata, keydata))

    elif (alg == algorithms[4]):
        def decryptRailFence(cipher, key):
            key = int(key)
            rail = [['\n' for i in range(len(cipher))]
                    for j in range(key)]
            dir_down = None
            row, col = 0, 0
            for i in range(len(cipher)):
                if row == 0:
                    dir_down = True
                if row == key - 1:
                    dir_down = False
                rail[row][col] = '*'
                col += 1
                if dir_down:
                    row += 1
                else:
                    row -= 1
            index = 0
            for i in range(key):
                for j in range(len(cipher)):
                    if ((rail[i][j] == '*') and
                            (index < len(cipher))):
                        rail[i][j] = cipher[index]
                        index += 1
            result = []
            row, col = 0, 0
            for i in range(len(cipher)):
                if row == 0:
                    dir_down = True
                if row == key-1:
                    dir_down = False
                if (rail[row][col] != '*'):
                    result.append(rail[row][col])
                    col += 1
                if dir_down:
                    row += 1
                else:
                    row -= 1
            return ("".join(result))

        text2.insert(INSERT, decryptRailFence(textdata, keydata))

    elif (alg == algorithms[5]):
        def row_transposition_decrypt(ciphertext, key):
            num_rows = (len(ciphertext) + len(key) - 1) // len(key)
            indices = [int(i) - 1 for i in key]
            rows = [''] * num_rows
            for i, index in enumerate(indices):
                rows = [row + ciphertext[index*num_rows+j]
                        for j, row in enumerate(rows)]
            last_row = rows[-1]
            last_row = last_row.rstrip('X')
            plaintext = ''.join(rows[:-1]) + last_row

            return plaintext

        text2.insert(INSERT, row_transposition_decrypt(textdata, keydata))


def clear():
    text1.delete('1.0', END)
    text2.delete('1.0', END)
    key.delete(0, END)


algorithms = ["Caesar Cipher", "Monoalphabetic Cipher", "Playfair Cipher",
              "Hill Cipher", "Rail Fence Cipher", "Row Transposition Cipher"]
selected = StringVar()
selected.set(algorithms[0])
lable = Label(text="Choose Alogrithm", font="10")

text1 = Text(root, height=15, width=25)
text2 = Text(root, height=15, width=25)


lable.grid(row=1, column=3)
drop = OptionMenu(root, selected, *algorithms)
drop.config(font="8",)
drop.grid(row=2, column=3)


keyLable = Label(root, text="key :", pady=10)
key = Entry(root,)


keyLable.grid(row=3, column=3, padx=10)
key.grid(row=4, column=3)

labelT1 = Label(text="Input Text", font=20)
lableT2 = Label(text="Result", font=20)

labelT1.grid(row=5, column=2, padx=150)
lableT2.grid(row=5, column=6, padx=50)

text1.grid(row=6, column=2, padx=100)
text2.grid(row=6, column=6, padx=50)

b1 = Button(text="Encrypt", font=20, command=encypt, height=1, width=10)
b2 = Button(text="Decrypt", font=20,
            command=decrypt, height=1, width=10)
b3 = Button(text="Clear", font=20, command=clear, height=1, width=10)

b1.grid(row=7, column=3, padx=10)
b2.grid(row=8, column=3, padx=10)
b3.grid(row=9, column=3, padx=10)
root.mainloop()
