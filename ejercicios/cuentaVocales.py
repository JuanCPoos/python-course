word = 'ChAnchitoFeliz'
vocals = 0

for x in word:
    y = x.lower()
    vocals += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0

print(vocals)