import hashlib


door = 'cxdnnyjw'

# part 1
# i = 0
# password = []
# while len(password) < 8:
#     md5 = hashlib.md5(bytes(door + str(i), 'ascii')).hexdigest()
#     if md5[:5] == '00000':
#         password.append(md5[5])
#     i += 1
#
# print(''.join(password))


# part 2
i = 0
password = [None] * 8
while not all(password):
    md5 = hashlib.md5(bytes(door + str(i), 'ascii')).hexdigest()
    if md5[:5] == '00000' and md5[5].isdigit() and int(md5[5]) < 8 and password[int(md5[5])] is None:
        password[int(md5[5])] = md5[6]
    i += 1

print(''.join(password))
