from PIL import Image
import csv 

game_map = []

with open("map.csv", mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        game_map.append(row)

sideL = len(game_map)

tile_size = 8
canvas_width = sideL * tile_size
canvas_height = sideL * tile_size

master_canvas = Image.new("RGBA", (canvas_width, canvas_height), (0, 0, 0, 0))

image_cache = {}

for row_i, row in enumerate(game_map):
    for col_i, tile in enumerate(row):
        if tile not in image_cache:
            image_cache[tile] = Image.open(f"styleA/{tile}.png")

        img = image_cache[tile]

        x_pixel = col_i * sideL
        y_pixel = row_i * sideL

        master_canvas.paste(img, (x_pixel, y_pixel))

master_canvas.save("map.png")

