import json
from PIL import Image, ImageDraw
import os

for file_path in os.listdir("./input_files/meta"):
    meta_file_path = "./input_files/meta/"+file_path
    img_path = "./input_files/img/"+file_path[:-5]

    print(meta_file_path)
    meta_edit = open(meta_file_path, "r", encoding="utf8").read()
    meta_edit2 = open(meta_file_path, "w", encoding="utf8")
    meta_edit2.write(meta_edit.replace("- ", ""))

    meta_file = open(meta_file_path, "r", encoding="utf8").readlines()
    json_file = open("./output.json", "w")
    json_file.write("{\n")
    once = False
    for i, l in enumerate(meta_file):
        if "rect" in l:
            if once:
                json_file.write(",\n")
            else:
                once = True
            json_file.write(f"\"{meta_file[i - 1][12:-1]}\":")
            json_file.write("{\n")
            json_file.write(f"\t\"{meta_file[i + 2][8]}\"{meta_file[i + 2][9:-1]},\n")
            json_file.write(f"\t\"{meta_file[i + 3][8]}\"{meta_file[i + 3][9:-1]},\n")
            json_file.write(f"\t\"{meta_file[i + 4][8:13]}\"{meta_file[i + 4][13:-1]},\n")
            json_file.write(f"\t\"{meta_file[i + 5][8:14]}\"{meta_file[i + 5][14:-1]}\n")
            json_file.write("}")
    json_file.write("\n}")
    json_file.close()

    img = Image.open(img_path)
    img = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    f = open('./output.json')
    data = json.load(f)
    for sprites in data:
        x: int = data[sprites]['x']
        y: int = data[sprites]['y']
        w: int = data[sprites]['width']
        h: int = data[sprites]['height']
        # shape = ((x, y), (w + x, h + y))
        # ImageDraw.Draw(img).rectangle(shape, outline="black")
        # ==========
        img_out = img.crop((x, y, w+x, h+y))
        img_out = img_out.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        img_out.save(("./output_img/" + sprites + ".png"))

    # img = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    # img.show()

