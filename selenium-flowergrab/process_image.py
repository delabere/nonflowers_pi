import os

from PIL import Image, ImageEnhance, ImageFilter

def main():
    # get the latest png by modified_date and work on that
    latest_date = 0
    latest_filename = ""
    for file in os.listdir("."):
        if file.endswith(".png"):
            if os.path.getmtime(file) > latest_date:
                latest_date = os.path.getmtime(file)
                latest_filename = file

    print(latest_filename)

    # handle the case where there is no png in the directory
    if latest_filename == "":
        print("there is no file in the directory!")
        return

    latest_filename = Image.open(latest_filename)


    #converter = PIL.ImageEnhance.Color(img)
    converter = ImageEnhance.Sharpness(latest_filename)
    new_image = converter.enhance(8)
    colour_converter = ImageEnhance.Color(new_image)
    new_image = colour_converter.enhance(1.5)
    new_image = new_image.resize((600, 448))


    #new_image.show()
    new_image.save("edited.png")

if __name__ == "__main__":
    main()