import re

text = open('regex_sum_973278.txt')

numbers = []
for line in text:
    line = line.rstrip()
    nums = re.findall('[0-9]+',line)
    for num in nums:
        numbers.append(int(num))

print('Sum = ' + str(sum(numbers)))
