l = 1
m = 0
r = 0
s = 1

seq = input()

a = 1
b = 1

for direct in seq:
    if direct == "R":
        r = a
        s = b
    if direct == "L":
        l = a
        m = b
    a = l + r
    b = m + s
print(f"{a} / {b}")