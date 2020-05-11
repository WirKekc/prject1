shift = int(input())
text = input().strip()
# alf = ' abcdefghijklmnopqrstuvwxyz'
encrypt = ""
start, end = 0x1F600, 0x1F64F

for i in range(len(text)):
    # letter = alf.find(text[i])
    encrypt += chr(start + (ord(text[i]) - start + shift) % (end - start + 1))
print('Result: "' + encrypt + '"')
