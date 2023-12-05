total = 0

with open("input.txt", "r") as f:
    for line in f:
        s = line.strip()
        i = 0
        a = None
        b = None
        while a is None or b is None:
            if a is None and s[i] in "0123456789":
                a = s[i]
            if b is None and s[-(i+1)] in "0123456789":
                b = s[-(i+1)]
            i += 1
        c = a + b
        d = int(a+b)
        # print(s, d)
        total += d

print(total)
# 54951