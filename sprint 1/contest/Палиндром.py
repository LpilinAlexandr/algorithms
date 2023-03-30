text = input()

word = ''

for i in text:
    if i.isalnum():
        word += i.lower()

print(word == word[::-1])
