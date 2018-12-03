import re

with open('3.txt') as f:
    lines = [line.strip() for line in f.readlines()]

num_cols = 0
num_rows = 0

for line in lines:
    # sample line: #1238 @ 27,663: 26x23
    match = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
    id, col, row, width, height = [int(thing) for thing in match.groups()]
    num_cols = max(col + width, num_cols)
    num_rows = max(row + height, num_rows)

col = [0] * num_cols
square = [col[:] for _ in range(num_rows)]

for line in lines:
    match = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
    id, col, row, width, height = [int(thing) for thing in match.groups()]
    
    for i in range(height):
        for j in range(width):
            square[row + i][col + j] += 1

print(sum(sum(cell >= 2 for cell in row) for row in square))

for line in lines:
    match = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
    id, col, row, width, height = [int(thing) for thing in match.groups()]
    
    rows = square[row:row + height]
    postage_stamp = [subrow[col:col + width] for subrow in rows]
    
    has_overlap = False
    for subrow in postage_stamp:
        if any(cell != 1 for cell in subrow):
            has_overlap = True
    
    if not has_overlap:
        print(id)
   
