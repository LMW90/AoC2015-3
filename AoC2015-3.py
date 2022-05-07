filename = 'inputDay-3.txt'
try:
    with open(filename) as data:
        text = data.readline()
except:
    print(f'Could not open: {filename}')
    exit()
num = input('Enter number of Santas (1 or 2): ')
if num == '1':
    # create a list of visited grid position tuples (x, y)
    posList = [(0, 0)]
    # mutable variable to perform steps
    prev = [0, 0]
    # loop through each move and in/decrement corresponding coordinate in prev
    for char in text:
        if char == '<':
            prev[0] -= 1
        elif char == '>':
            prev[0] += 1
        elif char == '^':
            prev[1] += 1
        else:
            prev[1] -= 1
        # if tupled mutable not yet in a list add it to a list
        if tuple(prev) not in posList:
            posList.append(tuple(prev))
elif num == '2':
    # create a shared list of visited grid position tuples (x, y)
    posList = [(0, 0)]
    # mutable variables to perform steps
    sanPrev = [0, 0]
    roboPrev = [0, 0]
    # variable to alternate moves
    step = 1
    # loop through each move and in/decrement corresponding coordinate in prev
    for char in text:
        if step % 2:
            if char == '<':
                sanPrev[0] -= 1
            elif char == '>':
                sanPrev[0] += 1
            elif char == '^':
                sanPrev[1] += 1
            else:
                sanPrev[1] -= 1
            # if tupled mutable not yet in a list add it to a list
            if tuple(sanPrev) not in posList:
                posList.append(tuple(sanPrev))
        else:
            if char == '<':
                roboPrev[0] -= 1
            elif char == '>':
                roboPrev[0] += 1
            elif char == '^':
                roboPrev[1] += 1
            else:
                roboPrev[1] -= 1
            # if tupled mutable not yet in a list add it to a list
            if tuple(roboPrev) not in posList:
                posList.append(tuple(roboPrev))
        step += 1
# print results
print(posList)
print(len(posList))
