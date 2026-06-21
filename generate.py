import random
import csv

sideL = 5
# tiles = ["ul","h","ur","l","r","v","x","u","b","bl","br","o","n","q1","ih","iv","mu","ho","q2","ph","pv","s","pc"]
tiles = ["u","b","l","r","ul","ur","bl","br","v","h","x","n"]

adj = {(el, g): [] for el in tiles for g in ["u","b","l","r"]}

top = ["u","l","r","ul","ur","v","x"]
bottom = ["b","l","r","bl","br","v","x"]
left = ["u","b","l","ul","bl","h","x"]
right = ["u","b","r","ur","br","h","x"]

for m in tiles:
    for l in tiles:
        if m in top and l in bottom:
            adj[(m, "b")].append(l)
            adj[(l, "u")].append(m)
        if m not in top and l not in bottom:
            adj[(m, "b")].append(l)
            adj[(l, "u")].append(m)
            
        if m in right and l in left:
            adj[(m, "r")].append(l)
            adj[(l, "l")].append(m)
        if m not in right and l not in left:
            adj[(m, "r")].append(l)
            adj[(l, "l")].append(m)


grid = [[[type for type in tiles] for i in range(sideL)] for j in range(sideL)]

def collapse(tiles):
    #sel = selected
    sel_list = []
    sel_length = len(grid[0][0])
    for i in range(sideL):
        for j in range(sideL):
            if len(grid[i][j]) > sel_length:
                sel_list = [(i,j)]
                sel_length = len(grid[i][j])
            elif len(grid[i][j]) == sel_length:
                sel_list.append((i,j))

    selected = random.choice(sel_list)
    return selected    

def propagate(selected):
    done = []
    to_do = [selected]
    while to_do != []:
        i = to_do[0][0]
        j = to_do[0][1]
        grid[i][j] = [random.choice(grid[to_do[0][0]][to_do[0][1]])]

        to_do.pop(0)
        done.append((i,j))
        if (i > 0) and ((i-1, j) not in done):
            allowed = adj[(grid[i][j][0], "u")]
            grid[i-1][j] = [el for el in grid[i-1][j] if el in allowed]
            to_do.append((i-1, j))

        if (i < sideL-1) and ((i+1, j) not in done):
            allowed = adj[(grid[i][j][0], "b")]
            grid[i+1][j] = [el for el in grid[i+1][j] if el in allowed]
            to_do.append((i+1, j))

        if (j > 0) and ((i, j-1) not in done):
            allowed = adj[(grid[i][j][0], "l")]
            grid[i][j-1] = [el for el in grid[i][j-1] if el in allowed]
            to_do.append((i, j-1))

        if (j < sideL-1) and ((i, j+1) not in done):
            allowed = adj[(grid[i][j][0], "r")]
            grid[i][j+1] = [el for el in grid[i][j+1] if el in allowed]
            to_do.append((i, j+1))

for i in range(10):
    selected = collapse(tiles)
    propagate(selected)

for i in range(sideL):
    for j in range(sideL):
        grid[i][j] = grid[i][j][0]

with open("map.csv", "w") as f:
    csv.writer(f).writerows(grid)