numbers = [11,56,33,4,3,5,10]
odds = []

for n in numbers :
    if not n % 2 == 0 :
        odds.append(n)

print(*odds)
