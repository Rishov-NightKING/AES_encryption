# -*- coding: utf-8 -*-
"""BitVector Demo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18MOtTMOl78t08PSpHkEQBQ7rmFk9Z8l6

Install The BitVector Library
"""

# pip install BitVector


"""Tables"""

from BitVector import *
import time

Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02")]
]

InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E")]
]

KEY_LENGTH = 16
round_constant = [1, 00, 00, 00]


# FUNCTIONS
def operationOnKey(strkey):
    if len(strkey) < KEY_LENGTH:
        temp = 16 - len(strkey)
        for i in range(temp):
            strkey += "0"
    elif len(strkey) > KEY_LENGTH:
        # ignore if the length is greater than 16
        strkey = strkey[:16]

    return strkey


def operationOnPlainText(text):
    if len(text) % 16 != 0:
        temp = 16 - len(text) % 16
        for i in range(temp):
            text += " "  # pad spaces
    # handle text blocks
    return text


def shiftRows(s):
    # first row doesnt change
    s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]


def inverseShiftRows(s):
    # first row doesnt change
    s[0][1], s[1][1], s[2][1], s[3][1] = s[3][1], s[0][1], s[1][1], s[2][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[1][3], s[2][3], s[3][3], s[0][3]


def circularleftshift(li):
    li[0], li[1], li[2], li[3] = li[1], li[2], li[3], li[0]

    return li


def printlistinHEX(li):
    count = 0
    for i in li:
        for j in i:
            print(hex(j), end=" ")
            count += 1
            if count % 16 == 0:
                print()


def printTextBlocks(textblocks):
    print("[ In HEX ]:")
    for i in range(len(textblocks)):
        printlistinHEX(textblocks[i])
    print()


def decipherText(li):
    strtext = ""
    for i in li:
        for j in i:
            strtext += chr(j)
            #print(chr(j))
    return strtext


def convertToText(texts):
    decstr = ""
    for i in range(len(texts)):
        decstr += decipherText(texts[i])

    print(decstr + "  [ In ASCII ]\n\n")


def byteSubstitution(li):
    for i in range(len(li)):
        li[i] = Sbox[li[i]]

    return li


def inverseByteSubstitution(li):
    for i in range(len(li)):
        li[i] = InvSbox[li[i]]

    return li


def xorlist(li1, li2):
    return [a ^ b for a, b in zip(li1, li2)]


def updateRoundConstant():
    if round_constant[0] < 128:  # 80(hex)
        round_constant[0] *= 2
    elif round_constant[0] >= 128:
        round_constant[0] = 2 * round_constant[0] ^ 283  # 11B(hex)


def mixColumn(matrix):
    temp = [[0, 0, 0, 0] for i in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                AES_modulus = BitVector(bitstring='100011011')
                temp[j][i] ^= Mixer[i][k].gf_multiply_modular(BitVector(intVal=matrix[j][k]), AES_modulus, 8).int_val()
    return temp


def inverseMixColumn(matrix):
    temp = [[0, 0, 0, 0] for i in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                AES_modulus = BitVector(bitstring='100011011')
                temp[j][i] ^= InvMixer[i][k].gf_multiply_modular(BitVector(intVal=matrix[j][k]), AES_modulus,
                                                                 8).int_val()
    return temp


# 16 character PLAINTEXT MATRIX GENERATE
def sixteenCharacterPlaintextMatrixGenerator(plaintext):
    j = 0
    count = 0
    temp = [[] for i in range(4)]
    for i in plaintext:
        temp[j].append(ord(i))
        count += 1
        if count % 4 == 0:
            j += 1
    # print("Input plaintext hex:")
    # printlistinHEX(textmatrix)
    return temp


def sixteenElementfilematrixGenerator(list):
    j = 0
    count = 0
    temp = [[] for i in range(4)]
    for i in list:
        temp[j].append(i)
        count += 1
        if count % 4 == 0:
            j += 1
    return temp


# KEY_MATRIX_GENERATE
def keymatrixgenerate(modifiedkey):
    j = 0
    count = 0
    temps = [[] for i in range(4)]
    for i in modifiedkey:
        # s.append(i)
        # ord() gives ascii value
        temps[j].append(ord(i))
        count += 1
        if count % 4 == 0:
            j += 1

    # printlistinHEX(words)
    # end_for_loop
    return temps


def AES_Schedule():
    # round (1 - 10)
    for round in range(1, 11):
        # circular byte left shift
        temp = circularleftshift(words[round * 4 - 1].copy())

        # Byte Substitution (S-Box):
        temp = byteSubstitution(temp)

        # Adding round constant
        temp = xorlist(temp.copy(), round_constant.copy())
        updateRoundConstant()

        firstword = xorlist(temp.copy(), words[round * 4 - 4].copy())
        words.append(firstword)

        secondword = xorlist(words[round * 4].copy(), words[round * 4 - 3].copy())
        words.append(secondword)

        thirdword = xorlist(words[round * 4 + 1].copy(), words[round * 4 - 2].copy())
        words.append(thirdword)

        fourthword = xorlist(words[round * 4 + 2].copy(), words[round * 4 - 1].copy())
        words.append(fourthword)

    # end_for_loop


def Encryption(textmatrix):
    # INITIALIZE ADD_ROUND_KEY(PLAINTEXT XOR ROUND_KEY_0)
    stateMatrix = [[] for i in range(4)]
    for i in range(4):
        stateMatrix[i] = xorlist(textmatrix[i].copy(), words[i].copy())

    # printlistinHEX(stateMatrix)

    # ROUND(1-9)
    for round in range(1, 10):
        # Substitution Bytes
        for i in range(4):
            byteSubstitution(stateMatrix[i])
        # Shift Row
        shiftRows(stateMatrix)

        # Mix Column
        stateMatrix = mixColumn(stateMatrix)

        # Add Roundkey
        for i in range(4):
            stateMatrix[i] = xorlist(stateMatrix[i].copy(), words[round * 4 + i].copy())

        # printlistinHEX(stateMatrix)
    # outer_for_loop_end

    # ROUND 10
    # Substitution Bytes
    for i in range(4):
        byteSubstitution(stateMatrix[i])
    # Shift Row
    shiftRows(stateMatrix)

    # Add Roundkey
    round = 10
    for i in range(4):
        stateMatrix[i] = xorlist(stateMatrix[i].copy(), words[round * 4 + i].copy())

    return stateMatrix


def Decryption(ciphertextmatrix):
    # ciphertext + roundkey w(40,43) initialization
    # ciphertextmatrix = stateMatrix.copy()
    for i in range(4):
        ciphertextmatrix[i] = xorlist(ciphertextmatrix[i].copy(), words[40 + i].copy())
    # printlistinHEX(ciphertextmatrix)

    for round in range(9, 0, -1):
        # Inverse shift row
        inverseShiftRows(ciphertextmatrix)

        # Inverse sub bytes
        for i in range(4):
            inverseByteSubstitution(ciphertextmatrix[i])

        # Add round key
        for i in range(4):
            ciphertextmatrix[i] = xorlist(ciphertextmatrix[i].copy(), words[round * 4 + i].copy())

        # Inverse mix cols
        ciphertextmatrix = inverseMixColumn(ciphertextmatrix)

        # printlistinHEX(ciphertextmatrix)

    # end outer for loop
    # Inverse shift row
    inverseShiftRows(ciphertextmatrix)

    # Inverse sub bytes
    for i in range(4):
        inverseByteSubstitution(ciphertextmatrix[i])

    # Add round key
    for i in range(4):
        ciphertextmatrix[i] = xorlist(ciphertextmatrix[i].copy(), words[i].copy())  # w(0,3)

    return ciphertextmatrix


# CODE MAIN FUNCTION

words = [[] for i in range(4)]
textmatrix = [[] for i in range(4)]
initialtextblocks = []
textblocks = []
decryptedtextblocks = []

#key = input("Enter Key: ")
key = "BUET CSE16 Batch"
modifiedkey = operationOnKey(key)
print("Key in English:\n" + modifiedkey + " [ In ASCII ]")
print("[ In HEX ]:")
words = keymatrixgenerate(modifiedkey)
printlistinHEX(words)
print()
# print(decipherText(words))

option = int(input("What do u want to encrypt-decrypt?\n1. Plaintext   2. File\nEnter input: \n"))
if option == 1:
    #plaintext = "WillGraduateSoon"
    plaintext = input("Enter plaintext: ")
    #plaintext = operationOnPlainText(plaintext)
    plaintext = operationOnPlainText(plaintext)
    print("Plaintext in English:\n" + plaintext + " [ In ASCII ]")

    # TEXT BLOCK MATRIX GENERATE
    for i in range(0, len(plaintext), 16):
        textmatrix = sixteenCharacterPlaintextMatrixGenerator(plaintext[i:i + 16])
        textblocks.append(textmatrix)
elif option == 2:
    a = []
    filename = input("Enter filename: ")
    #filename = "pic1.png"
    with open(filename, 'rb') as f:
        while 1:
            byte_s = f.read(1)
            if not byte_s:
                break
            byte = byte_s[0]
            a.append(byte)
    # padding
    for i in range(16 - len(a) % 16):
        a.append(20)

    # FOR FILE TEXT BLOCK GENERATE
    for i in range(0, len(a), 16):
        textmatrix = sixteenElementfilematrixGenerator(a[i:i + 16])
        textblocks.append(textmatrix)




initialtextblocks = textblocks.copy()
printTextBlocks(initialtextblocks)

aes_start_time = time.time()

AES_Schedule()

aes_end_time = time.time()

aes_time = aes_end_time - aes_start_time
# printlistinHEX(words)


# AES_SCHEDULE_END #################################################


# ENCRYPTION_CODE_START #################################################

encryption_start_time = time.time()

for i in range(len(textblocks)):
    textblocks[i] = Encryption(textblocks[i].copy())

encryption_end_time = time.time()
encryption_time = encryption_end_time - encryption_start_time

print("CipherText: ")
printTextBlocks(textblocks)  # textblocks holds the encrypted cipher text
convertToText(textblocks.copy())

# ENCRYPTION_CODE_END #################################################


# DECRYPTION_CODE_START #################################################

decryption_start_time = time.time()
decryptedtextblocks = textblocks.copy()
for i in range(len(textblocks)):
    decryptedtextblocks[i] = Decryption(decryptedtextblocks[i])

decryption_end_time = time.time()
decryption_time = decryption_end_time - decryption_start_time

print("After decryption plaintext:")
if option == 1:
    printTextBlocks(decryptedtextblocks)
    convertToText(decryptedtextblocks.copy())
elif option == 2:
    printTextBlocks(decryptedtextblocks)
    with open("decryptedFile", 'wb') as f:
        f.write(bytes(a))
# DECRYPTION_CODE_END #################################################


# EXECUTION TIME
print("Execution Time")
print("Key Scheduling: {} seconds".format(aes_time))
print("Encryption Time: {} seconds".format(encryption_time))
print("Decryption Time:: {} seconds".format(decryption_time))
