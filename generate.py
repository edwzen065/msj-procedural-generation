import random
import csv

sideL = 5
# tiles = ["ul","h","ur","l","r","v","x","u","b","bl","br","o","n","q1","ih","iv","mu","ho","q2","ph","pv","s","pc"]
tiles = ["u","b","l","r","ul","ur","bl","br","v","h","x","n"]

adj = {(el, g): [] for el in tiles for g in ["u","b","l","r"]}

top = ["u","l","r","ul","ur","v","x"]
bottom = ["b","l","r","bl","br","v","x"]
left = ["u","b","l","ur","br","h","x"]
right = ["u","b","r","ul","bl","h","x"]

for m in tiles:
    for l in tiles:
        if m in top and l in bottom:
            adj[(m, "b")].append(l)
            adj[(l, "u")].append(m)
        if m not in top and l not in bottom:
            adj[(m, "b")].append(l)
            adj[(l, "u")].append(m)
            
        if m in right and l in left:
            adj[(m, "l")].append(l)
            adj[(l, "r")].append(m)
        if m not in right and l not in left:
            adj[(m, "l")].append(l)
            adj[(l, "r")].append(m)


grid = [[[type for type in tiles] for i in range(sideL)] for j in range(sideL)]

def collapse():
    #sel = selected
    sel_list = []
    sel_length = len(tiles)
    for i in range(sideL):
        for j in range(sideL):
            if len(grid[i][j]) < sel_length and len(grid[i][j]) != 1:
                sel_list = [(i,j)]
                sel_length = len(grid[i][j])
            elif len(grid[i][j]) == sel_length:
                sel_list.append((i,j))

    if sel_list == []:
        return 0

    selected = random.choice(sel_list)

    grid[selected[0]][selected[1]] = [random.choice(grid[selected[0]][selected[1]])]
    return selected    

def propagate(selected):
    done = []
    to_do = [selected]
    while to_do != []:
        i = to_do[0][0]
        j = to_do[0][1]
        # grid[i][j] = [random.choice(grid[to_do[0][0]][to_do[0][1]])]

        to_do.pop(0)
        done.append((i,j))

        if (i > 0) and ((i-1, j) not in done and (i-1, j) not in to_do):
            allowed = set().union(*(adj[el, "u"] for el in grid[i][j]))
            grid[i-1][j] = [el for el in grid[i-1][j] if el in allowed]
            to_do.append((i-1, j))

        if (i < sideL-1) and ((i+1, j) not in done and (i+1, j) not in to_do):
            allowed = set().union(*(adj[el, "b"] for el in grid[i][j]))
            grid[i+1][j] = [el for el in grid[i+1][j] if el in allowed]
            to_do.append((i+1, j))
        
        if (j > 0) and ((i, j-1) not in done and (i, j-1) not in to_do):
            allowed = set().union(*(adj[el, "l"] for el in grid[i][j]))
            grid[i][j-1] = [el for el in grid[i][j-1] if el in allowed]
            to_do.append((i, j-1))
        
        if (j < sideL-1) and ((i, j+1) not in done and (i, j+1) not in to_do):
            allowed = set().union(*(adj[el, "r"] for el in grid[i][j]))
            grid[i][j+1] = [el for el in grid[i][j+1] if el in allowed]
            to_do.append((i, j+1))

for i in range(100):
    selected = collapse()
    if selected == 0:
        break
    propagate(selected)
    for el in grid:
        print(el)
    print(".")


for i in range(sideL):
    for j in range(sideL):
        grid[i][j] = grid[i][j][0]

with open("map.csv", "w") as f:
    csv.writer(f).writerows(grid)