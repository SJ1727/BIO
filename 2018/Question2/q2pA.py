n, word = input().split()
n = int(n)

temp = [chr(i + ord("A")) for i in range(26)]
dial = []

index = -1
while temp != []:
    index += n
    index %= len(temp)
    
    dial.append(temp[index])
    temp.pop(index)
    index -= 1

print("".join(dial[:6]))

encrypted = ""
for i, letter in enumerate(word):
    encrypted += dial[(ord(letter) - ord("A") + i) % 26]
    
print(encrypted)