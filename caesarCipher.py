shift = int(input())
text = input().strip()
alf = ' abcdefghijklmnopqrstuvwxyz'
encrypt = ""

for i in range(len(text)):
    letter = alf.find(text[i])
    encrypt += alf[(letter + shift) % len(alf)]
print('Result: "' + encrypt + '"')