import random


def open_file(file_name):
    file = open(file_name)
    text = file.read()
    file.close()
    return text


def displayboard(array):
    for x in range(len(array)):
        row = []
        if (x % 3) == 0:
            print("-----------")
            # continue
        for y in range(len(array[x])):
            row.append(array[x][y])
            if (y % 3) == 2 and not y == 8:
                row.append('|')
        print(row)


def checkrow(array, nums, x):
    notin = []
    have = []
    for i in range(len(array[x])):
        if not array[x][i] in have:
            have.append(array[x][i])
    for i in range(len(nums)):
        if not nums[i] in have:
            notin.append(nums[i])
    return notin


def checkcolum(array, nums, y):
    notin = []
    have = []
    for i in range(len(array)):
        if not array[i][y] in have:
            have.append(array[i][y])
    for i in range(len(nums)):
        if not nums in have:
            notin.append(nums[i])
    return notin


def checkboth(row, colum):
    have = []
    for i in range(len(row)):
        if row[i] in colum:
            have.append(row[i])
    return have


def checkreprow(array, x, y):
    origin = array[x][y]
    have = []
    for i in range(len(array[x])):
        if array[x][i] in have:
            return '0'
        else:
            have.append(array[x][i])
    return origin


def checkrepcol(array, x, y):
    origin = array[x][y]
    have = []
    for i in range(len(array)):
        if array[i][y] in have:
            return '0'
        else:
            have.append(array[i][y])
    return origin


text = open_file('test.txt').split("\n")
array = []
for x in range(len(text)):
    rw = []
    for y in range(len(text[x])):
        rw.append(text[x][y])
    array.append(rw)


def checkroom(array, nums, x, y):
    if x < 3:
        minx = 0
        maxx = 3
    elif x > 5:
        minx = 6
        maxx = 9
    else:
        minx = 3
        maxx = 6

    if y < 3:
        miny = 0
        maxy = 3
    elif y > 5:
        miny = 6
        maxy = 9
    else:
        miny = 3
        maxy = 6
    room = []
    for i in range(minx, maxx):
        #row = []
        for z in range(miny, maxy):
            room.append(array[i][z])
            #print(array[i][z])
        #room.append(row)
    #print(room)
    have = []
    notin = []
    for i in range(len(room)):
        if not room[i] in have:
            have.append(room[i])
    for i in range(len(nums)):
        if not nums[i] in have:
            notin.append(nums[i])
    return notin


nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
solved = False
have = []
while solved == False:
    solved = True
    for x in range(len(array)):
        for y in range(len(array[x])):
            array[x][y] = checkreprow(array, x, y)
            array[x][y] = checkrepcol(array, x, y)
            row = checkrow(array, nums, x)
            colum = checkcolum(array, nums, y)
            room = checkroom(array, nums, x, y)
            notboth = checkboth(row, colum)
            notall = checkboth(notboth, room)
            if array[x][y] == '0':
                if len(notall) > 0:
                    array[x][y] = random.choice(notall)
    displayboard(array)
