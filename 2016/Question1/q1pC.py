def pomerade(seq):
    l = 1
    m = 0
    r = 0
    s = 1

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

    return a, b

a, b = pomerade("L" * 999_999)

print(f"{a} / {b}")