def check_char_freq(s):
    s = s.replace(" ", "").lower()
    ch = {}
    for i in range(len(s)):
        if s[i] not in ch:
            ch[s[i]] = 1
        else:
            ch[s[i]] += 1
    print(ch)

check_char_freq("My name is Aniket")