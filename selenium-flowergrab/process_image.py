import os
import hitherdither
import inky
from PIL import Image, ImageEnhance, ImageFilter

def process_image():
    # get the latest png by modified_date and work on that
    latest_date = 0
    latest_filename = ""
    for file in os.listdir("./flower_images"):
        if file.endswith(".png") and file != "edited.png":
            filepath = os.path.join("flower_images", file)
            if os.path.getmtime(filepath) > latest_date:
                latest_date = os.path.getmtime(filepath)
                latest_file = filepath

    # handle the case where there is no png in the directory
    if latest_file == "":
        print("there is no file in the directory!")
        return

    img = Image.open(latest_file)


    #converter = PIL.ImageEnhance.Color(img)
    converter = ImageEnhance.Sharpness(img)
    new_image = converter.enhance(1.2)
    colour_converter = ImageEnhance.Color(new_image)
    new_image = colour_converter.enhance(1.2)
    new_image = new_image.resize((600, 448))


    #new_image.show()
    # saturation = 0.8
    # palette = hitherdither.palette.Palette(inky._palette_blend(saturation, dtype='uint24'))
    # new_image = new_image.convert('P', palette=palette, colors=7)
    new_image.save("./flower_images/edited.png")
if __name__ == "__main__":
    process_image()