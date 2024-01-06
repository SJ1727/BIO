n = 1_000_000_000

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