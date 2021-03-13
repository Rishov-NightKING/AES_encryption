# f = open("Git essential command.pdf", "rb").read(10)

# s = int.from_bytes(f, byteorder='little')
# a = []
# with open("small.pdf", 'rb') as f:
#    while 1:
#       byte_s = f.read(1)
#       if not byte_s:
#          break
#       byte = byte_s[0]
#       a.append(byte)
#
#
# print(len(a))
# a.append(8)
# a.append(8)
# a.append(8)
#
# with open("dpCopy.jpg", 'wb') as f:
#     f.write(bytes(a))

from BitVector import *



def generateSbox():
    sbox = [i for i in range(256)]
    sbox[0] = 0x63
    AES_modulus = BitVector(bitstring='100011011')
    for i in sbox[1:]:
        b = BitVector(intVal=i).gf_MI(AES_modulus, 8)
        s = BitVector(intVal=99) ^ b ^ (b << 1) ^ (b << 1) ^ (b << 1) ^ (b << 1)
        sbox[i] = s.int_val()
    return sbox

def generateInvSbox():
    invSbox = [i for i in range(256)]
    for i in range(256):
        b = sbox[i]
        invSbox[b] = i
    return invSbox



sbox = generateSbox()
sbox = tuple(sbox)
inv = generateInvSbox()
print(sbox)
print(inv)