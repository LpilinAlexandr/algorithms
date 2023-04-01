s = input()
t = input()

set_t = set(t)
set_s = set(s)
letter = None

if len(set_s) != len(set_t):
    letter = (set_t - set_s).pop()

if not letter:
    d_s = dict(zip(set_t, [0] * len(set_t)))
    d_t = d_s.copy()

    len_s = len(s)

    for i in range(len(t)):
        if i < len_s:
            d_s[s[i]] += 1
        d_t[t[i]] += 1

    for i in set_t:
        if d_t[i] > d_s[i]:
            letter = i
            break

print(letter)
