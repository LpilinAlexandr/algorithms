text = input()

opened = ('[', '(', '{')
closed = (']', ')', '}')
mapped = dict(zip(closed, opened))
stack = []

for sign in text:

    if sign in opened or not stack:
        stack.append(sign)
        continue

    if mapped[sign] != stack[-1]:
        break

    stack.pop(-1)

print(len(stack) == 0)
