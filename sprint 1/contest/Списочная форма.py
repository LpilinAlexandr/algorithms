count = int(input())
array_number = input().split()
number = input()

num_len = len(number)

left_part = array_number[0:num_len - 1] if num_len < count else []
right_part = array_number[num_len - 1:] if num_len < count else array_number

result = str(
    int(''.join(right_part)) + int(number)
)

print(' '.join(left_part) + ' ' + ' '.join(result))
