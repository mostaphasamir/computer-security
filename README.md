# computer security GUI

## GUI for Cryptography Algorithms
This GUI application is built using Python and provides an easy-to-use interface for encrypting and decrypting text using various cryptography algorithms. The supported algorithms are:

* Caesar Cipher
* Monoalphabetic Cipher
* Playfair Cipher
* Hill Cipher
* Rail Fence Cipher
* Row Transposition Cipher


## Getting Started
To use this GUI application, you need to have Python 3 installed on your system. You can download Python from the official website: https://www.python.org/

Next, you need to install the required Python packages. You can do this by running the following command in your terminal:

``` pip install tkinter ``` <br>
``` pip install numpy ```


## How to Use
Once you have installed the required packages, you can run the application by executing the following command in your terminal:

python main.py
This will open the GUI window, where you can select the cryptography algorithm you want to use, enter the plaintext or ciphertext, and specify the key.

Once you have entered the required information, you can click on the "Encrypt" or "Decrypt" button to perform the encryption or decryption operation. The result will be displayed in the output area of the GUI.

Once you done you can click on "Clear" button to clear the input and the key .

## Cryptography Algorithms

### Caesar Cipher
The Caesar Cipher is a simple substitution cipher that shifts the letters of the plaintext by a fixed number of positions in the alphabet. For example, if the shift value is 3, then "A" is replaced by "D", "B" is replaced by "E", and so on.

#### example :
<img src="https://user-images.githubusercontent.com/115727397/230720099-364f998e-f74a-4baa-afce-447c0158f4ab.png" alt="Alt text" width="900">

### Monoalphabetic Cipher
The Monoalphabetic Cipher is a type of substitution cipher where each letter in the plaintext is replaced by a fixed letter in the ciphertext. This means that each letter in the plaintext is always replaced by the same corresponding letter in the ciphertext.<br>
**NOTE : the key must be 26 letters of unique alphabet**

#### example :
key = POUAVGCILFMSQZEKNWYTJBXRDH
<img src="https://user-images.githubusercontent.com/115727397/230720350-46e26f7b-0874-4786-ada0-7f1d72396f97.png" alt="Alt text" width="900">

### Playfair Cipher
The Playfair Cipher is a polygraphic substitution cipher that encrypts pairs of letters instead of single letters. The plaintext is divided into pairs of letters, and each pair is encrypted using a 5x5 matrix of letters.

#### example :
<img src="https://user-images.githubusercontent.com/115727397/230721315-7a3ed03c-3d89-45bf-8000-e5436765ce43.png" alt="Alt text" width="900">

### Hill Cipher
The Hill Cipher is a type of polygraphic substitution cipher that encrypts blocks of plaintext of a fixed size. The encryption is done using a matrix multiplication operation with a key matrix.
**u can use 2*2 key matrix and 3*3 key matrix ** 

#### example:
<img src="https://user-images.githubusercontent.com/115727397/230721604-058e9b90-46d0-453c-b73c-9c0f0ba2cba5.png" alt="Alt text" width="500">
<img src="https://user-images.githubusercontent.com/115727397/230721608-47e3ca0f-a04a-449d-902e-6051c0bb2e69.png" alt="Alt text" width="900">


### Rail Fence Cipher
The Rail Fence Cipher is a transposition cipher that writes the plaintext in a zigzag pattern across a number of rails or lines. The ciphertext is then read off from the rails in a specific order.

#### example:
<img src="https://user-images.githubusercontent.com/115727397/230724042-a327c8c7-f349-4115-ba5a-414984f6e984.png" alt="Alt text" width="900">

### Row Transposition Cipher
The Row Transposition Cipher is a type of transposition cipher that writes the plaintext in a row-based order and then rearranges the rows according to a specific key. The ciphertext is then read off from the rearranged rows.

#### example:
<img src="https://user-images.githubusercontent.com/115727397/230724045-6af78092-80e1-425e-9dd4-cad757169672.png" alt="Alt text" width="900">

### Conclusion
This GUI application provides a simple and intuitive way to use various cryptography algorithms for encrypting and decrypting text. By using this application, you can easily experiment with different algorithms and see how they work.
