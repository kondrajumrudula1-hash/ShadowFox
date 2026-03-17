import random

rolls = [random.randint(1, 6) for _ in range(20)]

print("Rolls:", rolls)

print("Number of 6s:", rolls.count(6))
print("Number of 1s:", rolls.count(1))

count = 0
for i in range(len(rolls) - 1):
    if rolls[i] == 6 and rolls[i+1] == 6:
        count += 1

print("Two 6s in a row:", count)
