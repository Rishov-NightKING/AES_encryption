
from BitVector import *
AES_modulus = BitVector(bitstring='100011011')

bv1 = BitVector(hexstring="03")

bv3 = bv1.gf_multiply_modular(BitVector(intVal=47), AES_modulus, 8)
print(bv3.int_val())