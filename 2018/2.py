from collections import Counter

with open('2.txt') as f:
    serials = [line.strip() for line in f.readlines()]

twos = []
threes = []

for serial in serials:
    c = Counter(serial)
    if 2 in c.values():
        twos.append(serial)
    if 3 in c.values():
        threes.append(serial)

print(len(twos) * len(threes))

# part 2
for i in range(len(serials)):
    curr = serials[i]
    for other in serials[i:]:
        diff = [a != b for a, b in zip(curr, other)]
        if sum(diff) == 1:
            print(curr)
            print(other)