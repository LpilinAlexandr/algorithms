length = int(input())
array = input().strip().split()

max_word = ''
max_word_length = 0
for word in array:

    new_word_length = len(word)
    if new_word_length > max_word_length:
        max_word = word
        max_word_length = new_word_length

print(max_word)
print(max_word_length)
