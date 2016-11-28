#langton's ant

Dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

(x, y) = (4, 4)
w, h = 10, 10
Matrix = [[0 for x in range(w)] for y in range(h)] 
Dir2 = 0
t = 0
rounds = int(input("rounds"))
while t < rounds:
    newround = input("")
    x2 = x - Dir[Dir2][0]
    y2 = y - Dir[Dir2][1]
    if Matrix[x2][y2] == 0:
       Dir2 = Dir2 + 1
       trail = 1
    if Matrix[x2][y2] == 1:
       Dir2 = Dir2 - 1
       trail = 0
    if Dir2 > 3:
       Dir2 = 0
    if Dir2 < 0:
       Dir2 = 1
    Matrix[x2][y2] = 2
    Matrix[x][y] = trail
    x = x2
    y = y2
    for i in range(0,w):
        print(Matrix[i])
    print(t)
    t = t + 1