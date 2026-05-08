n, m = map(int, input().split())

l = input().split()
a = set(input().split())
b = set(input().split())

happiness = 0

for x in l:
    if x in a:
        happiness += 1
    elif x in b:
        happiness -= 1

print(happiness)


##

from collections import Counter

n_words = int(input())

words = [input().strip() for _ in range(n_words)]

freq = Counter(words)

print(len(freq))
print(*freq.values())