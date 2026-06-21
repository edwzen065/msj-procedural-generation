from PIL import Image
import csv 

#CHANGE STYLES FROM A TO F HERE
style = "styleB"
#CHANGE STYLES FROM A TO F HERE

game_map = []
with open("map.csv", mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        game_map.append(row)

sideL = len(game_map)

scale = 10
tile_size = 8 * scale
canvas_width = sideL * tile_size
canvas_height = sideL * tile_size

master_canvas = Image.new("RGBA", (canvas_width, canvas_height), (0, 0, 0, 0))

image_cache = {}

for row_i, row in enumerate(game_map):
    for col_i, tile in enumerate(row):
        if tile not in image_cache:
            image_cache[tile] = Image.open(f"Tiles/{style}/{tile}.png").resize((tile_size,tile_size))

        img = image_cache[tile]

        x_pixel = col_i * tile_size
        y_pixel = row_i * tile_size

        master_canvas.paste(img, (x_pixel, y_pixel))

master_canvas.save("map.png")

