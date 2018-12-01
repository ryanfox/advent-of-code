with open('1.txt') as f:
    nums = [int(num) for num in f.readlines()]

# part 1
print(sum(nums))

# part 2
curr = 0
seen = set()
stop = False

while not stop:
    for num in nums:
        curr += num
        if curr in seen:
            print(curr)
            stop = True
            break
        else:
            seen.add(curr)
