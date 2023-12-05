total = 0

with open("input.txt", "r") as f:
    for line in f:
        s = line.strip()
        a = None
        b = None

        i = 0
        while a is None and i <= len(s):
            if s[i] in "0123456789":
                a = s[i]
                break
            if s[i:i+3] == "one":
                a = "1"
                break
            if s[i:i+3] == "two":
                a = "2"
                break
            if s[i:i+5] == "three":
                a = "3"
                break
            if s[i:i+4] == "four":
                a = "4"
                break
            if s[i:i+4] == "five":
                a = "5"
                break
            if s[i:i+3] == "six":
                a = "6"
                break
            if s[i:i+5] == "seven":
                a = "7"
                break
            if s[i:i+5] == "eight":
                a = "8"
                break
            if s[i:i+4] == "nine":
                a = "9"
                break
            i += 1

        j = len(s) - 1
        while b is None and j >= 0:
            if s[j] in "0123456789":
                b = s[j]
                break
            if s[j-2:j+1] == "one":
                b = "1"
                break
            if s[j-2:j+1] == "two":
                b = "2"
                break
            if s[j-3:j+1+1] == "three":
                b = "3"
                break
            if s[j-3:j+1] == "four":
                b = "4"
                break
            if s[j-3:j+1] == "five":
                b = "5"
                break
            if s[j-2:j+1] == "six":
                b = "6"
                break
            if s[j-3:j+1+1] == "seven":
                b = "7"
                break
            if s[j-3:j+1+1] == "eight":
                b = "8"
                break
            if s[j-3:j+1] == "nine":
                b = "9"
                break
            j -= 1

        c = a + b
        d = int(a+b)
        # print(s, d)
        total += d

print(total)
# 55218