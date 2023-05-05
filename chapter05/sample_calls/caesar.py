

# caesar.py


# Option 1: shift=3


class CaesarCipher:
    # Class for doing encryption and decryption using a Caesar cipher.
    def __init__(self, shift):
        # Construct Caesar cipher using given integer shift for rotation.
        encoder = [None] * 26                # temp array for encryption
        decoder = [None] * 26                # temp array for decryption
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)     # will store as string
        self._backward = ''.join(decoder)    # since fixed
    def encrypt(self, message):
        # Return string representing encripted message.
        return  self._transform(message, self._forward)
    def decrypt(self, secret):
        # Return decrypted message given encrypted secret.
        return  self._transform(secret, self._backward)
    def _transform(self, original, code):
        # Utility to perform transformation based on given code string.
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')   # index from 0 to 25
                msg[k] = code[j]             # replace this character
        return ''.join(msg)


if __name__ == '__main__':
    cipher = CaesarCipher(shift=3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
    coded = cipher.encrypt(message)
    print('Secret: ', coded)
    answer = cipher.decrypt(coded)
    print('Message:', answer)


# Output:

"""
Secret:  WKH HDJOH LV LQ SODB; PHHW DW MRH'V.
Message: THE EAGLE IS IN PLAY; MEET AT JOE'S.
>>> 
"""

#---------------------------------------------------------------------------------------------------------


# Option 2: shift=3
# Insert 4 prints for showing the result 


class CaesarCipher:
    # Class for doing encryption and decryption using a Caesar cipher.
    def __init__(self, shift):
        # Construct Caesar cipher using given integer shift for rotation.
        encoder = [None] * 26                # temp array for encryption
        decoder = [None] * 26                # temp array for decryption
        for k in range(26):
            # 编码: 用(k + shift) mod 26替换每个字母k，执行整除后返回余数；　
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            print(encoder[k])
            # 解码: 用(k - shift) mod 26替换每个字母k，执行整除后返回余数；
            decoder[k] = chr((k - shift) % 26 + ord('A'))
            print(decoder[k])
        # 前向
        self._forward = ''.join(encoder)     # will store as string
        # 反向
        self._backward = ''.join(decoder)    # since fixed
    def encrypt(self, message):
        # Return string representing encripted message.
        return  self._transform(message, self._forward)
    def decrypt(self, secret):
        # Return decrypted message given encrypted secret.
        return  self._transform(secret, self._backward)
    def _transform(self, original, code):
        # Utility to perform transformation based on given code string.
        msg = list(original)
        print(msg)
        for k in range(len(msg)):
            if msg[k].isupper():
                # 把字符'A'~'Z'分别映射为0~25的整型，若msg[k]为'A', 则j=0;
                # 若msg[k]='B', 则j=1, 以此类推。。。
                j = ord(msg[k]) - ord('A')   # index from 0 to 25
                msg[k] = code[j]             # replace this character
                print(msg[k])
        return ''.join(msg)


if __name__ == '__main__':
    # shift = 3
    cipher = CaesarCipher(shift=3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
    coded = cipher.encrypt(message)
    print('Secret: ', coded)
    answer = cipher.decrypt(coded)
    print('Message:', answer)


# Output:

"""
>>> # print(encoder[k])
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
Z
A
B
C
>>> # print(decoder[k])
X
Y
Z
A
B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
>>>
>>> # print(msg)
['T', 'H', 'E', ' ', 'E', 'A', 'G', 'L', 'E', ' ', 'I', 'S', ' ', 'I', 'N', ' ', 'P', 'L', 'A', 'Y', ';', ' ', 'M', 'E', 'E', 'T', ' ', 'A', 'T', ' ', 'J', 'O', 'E', "'", 'S', '.']
W
K
H
H
D
J
O
H
L
V
L
Q
S
O
D
B
P
H
H
W
D
W
M
R
H
V
>>>
# print('Secret: ', coded)
Secret:  WKH HDJOH LV LQ SODB; PHHW DW MRH'V.
>>>
>>> # print(msg[k])
['W', 'K', 'H', ' ', 'H', 'D', 'J', 'O', 'H', ' ', 'L', 'V', ' ', 'L', 'Q', ' ', 'S', 'O', 'D', 'B', ';', ' ', 'P', 'H', 'H', 'W', ' ', 'D', 'W', ' ', 'M', 'R', 'H', "'", 'V', '.']
T
H
E
E
A
G
L
E
I
S
I
N
P
L
A
Y
M
E
E
T
A
T
J
O
E
S
>>>
# print('Message:', answer)
Message: THE EAGLE IS IN PLAY; MEET AT JOE'S.
>>> 
"""

#---------------------------------------------------------------------------------------------------------

# Option 2: shift=6

class CaesarCipher:
    # Class for doing encryption and decryption using a Caesar cipher.
    def __init__(self, shift):
        # Construct Caesar cipher using given integer shift for rotation.
        encoder = [None] * 26                # temp array for encryption
        decoder = [None] * 26                # temp array for decryption
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            print(encoder[k])
            decoder[k] = chr((k - shift) % 26 + ord('A'))
            print(decoder[k])
        self._forward = ''.join(encoder)     # will store as string
        self._backward = ''.join(decoder)    # since fixed
    def encrypt(self, message):
        # Return string representing encripted message.
        return  self._transform(message, self._forward)
    def decrypt(self, secret):
        # Return decrypted message given encrypted secret.
        return  self._transform(secret, self._backward)
    def _transform(self, original, code):
        # Utility to perform transformation based on given code string.
        msg = list(original)
        print(msg)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')   # index from 0 to 25
                msg[k] = code[j]             # replace this character
                print(msg[k])
        return ''.join(msg)


if __name__ == '__main__':
    # shift = 6
    cipher = CaesarCipher(shift=6)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
    coded = cipher.encrypt(message)
    print('Secret: ', coded)
    answer = cipher.decrypt(coded)
    print('Message:', answer)


# Outoput:

"""
>>> # shift 6 alphabet 
G
U
H
V
I
W
J
X
K
Y
L
Z
M
A
N
B
O
C
P
D
Q
E
R
F
S
G
T
H
U
I
V
J
W
K
X
L
Y
M
Z
N
A
O
B
P
C
Q
D
R
E
S
F
T
['T', 'H', 'E', ' ', 'E', 'A', 'G', 'L', 'E', ' ', 'I', 'S', ' ', 'I', 'N', ' ', 'P', 'L', 'A', 'Y', ';', ' ', 'M', 'E', 'E', 'T', ' ', 'A', 'T', ' ', 'J', 'O', 'E', "'", 'S', '.']
Z
N
K
K
G
M
R
K
O
Y
O
T
V
R
G
E
S
K
K
Z
G
Z
P
U
K
Y
Secret:  ZNK KGMRK OY OT VRGE; SKKZ GZ PUK'Y.
['Z', 'N', 'K', ' ', 'K', 'G', 'M', 'R', 'K', ' ', 'O', 'Y', ' ', 'O', 'T', ' ', 'V', 'R', 'G', 'E', ';', ' ', 'S', 'K', 'K', 'Z', ' ', 'G', 'Z', ' ', 'P', 'U', 'K', "'", 'Y', '.']
T
H
E
E
A
G
L
E
I
S
I
N
P
L
A
Y
M
E
E
T
A
T
J
O
E
S
Message: THE EAGLE IS IN PLAY; MEET AT JOE'S.
>>> 
"""