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

a1 , b1 = pomerade("LRL")
a2, b2 = pomerade("LLLL")
print(f"{a1 + a2} / {b1 + b2}")