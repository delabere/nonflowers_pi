#!/usr/bin/env python3

import sys

from PIL import Image
from inky.inky_uc8159 import Inky

def display_image():
    """puts the local image onto the screen"""
    image_filepath = "flower_images/edited.png"

    inky = Inky()
    saturation = 0.5 # need to consider this because my post processing is also increasing sat.

    # these could be useful later on to make this more dynamic
    # so I will leave them for now

    # if len(sys.argv) == 1:
    #     print("""
    # Usage: {file} image-file
    # """.format(file=sys.argv[0]))
    #     sys.exit(1)

    # image = Image.open(sys.argv[1])

    # if len(sys.argv) > 2:
    #     saturation = float(sys.argv[2])

    image = Image.open(image_filepath)

    inky.set_image(image, saturation=saturation)
    inky.show()

    return

if __name__ == "__main__":
    display_image()