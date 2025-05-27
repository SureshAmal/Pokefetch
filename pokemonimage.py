import random
import pandas
import os
import sys

rand = random.randint(1, 898)

csv_path = os.path.expanduser("~/gitclones/Pokemon/pokemon.csv")
pokecsv = pandas.read_csv(csv_path, index_col="id")


image_dir = "./assets/thumbnails/"

if len(sys.argv) > 1:
    arg = sys.argv[1]
    if arg.startswith("n") and arg[1:].isdigit():
        rand = int(arg[1:])
    else:
        match arg:
            case "thm":
                image_dir = "./assets/thumbnails/"
            case "thbc":
                image_dir = "./assets/thumbnails-compressed/"
            case "hr":
                image_dir = "./assets/imagesHQ/"
            case "st":
                image_dir = "./assets/images/"

image_dir = os.path.expanduser(os.path.join("~/gitclones/Pokemon", image_dir[2:]))


def get_image_paths(source_dir, index):
    matches = []
    for filename in os.listdir(source_dir):
        if filename.startswith(str(index).zfill(3)):
            matches.append(filename)
    return matches


imgidex = pokecsv[pokecsv["species_id"] == rand]
pokename = imgidex["identifier"].iloc[0]

image_files = get_image_paths(image_dir, rand)
image_path = os.path.join(image_dir, image_files[0])

print(pokename + "," + image_path)
