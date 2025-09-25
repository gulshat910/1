def shift_string(s):
    out = ""
    for ch in s:
        if ch.isalpha():
            base = 'A' if ch.isupper() else 'a'
            out += chr((ord(ch) - ord(base) + 3) % 26 + ord(base))
        else:
            out += ch
    return out

print(shift_string(input("Введите строку: ")))
