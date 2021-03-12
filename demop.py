
#f = open("Git essential command.pdf", "rb").read(10)

#s = int.from_bytes(f, byteorder='little')
a = []
with open("small.pdf", 'rb') as f:
   while 1:
      byte_s = f.read(1)
      if not byte_s:
         break
      byte = byte_s[0]
      a.append(byte)


print(len(a))
a.append(8)
a.append(8)
a.append(8)

with open("dpCopy.jpg", 'wb') as f:
    f.write(bytes(a))
