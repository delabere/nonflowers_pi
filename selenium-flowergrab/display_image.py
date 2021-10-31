#!/usr/bin/env python3

import sys
import hitherdither

from PIL import Image
from inky.inky_uc8159 import Inky

def display_image():
    """puts the local image onto the screen"""
    image_filepath = "flower_images/edited.png"

    inky = Inky()
    saturation = 1 # need to consider this because my post processing is also increasing sat.
    thresholds = [64, 64, 64]  # Threshold for snapping colours, I guess?

    palette = hitherdither.palette.Palette(inky._palette_blend(saturation, dtype='uint24'))

    image = Image.open(image_filepath).convert("RGB")

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

    # image = Image.open(image_filepath)

    print("setting image to screen...")
    # VERY slow (1m 40s on a Pi 4) - see https://github.com/hbldh/hitherdither for a list of methods
    # image_dithered = hitherdither.diffusion.error_diffusion_dithering(image, palette, method="stucki", order=2)

    # Usably quick, your vanilla dithering
    # image_dithered = hitherdither.ordered.bayer.bayer_dithering(image, palette, thresholds, order=8)

    # Usuably quick, half-tone comic-book feel, use order=4 for small dots and order=8 dot bigguns
    image_dithered = hitherdither.ordered.cluster.cluster_dot_dithering(image, palette, thresholds, order=4)

    # VERY slow
    # image_dithered = hitherdither.ordered.yliluoma.yliluomas_1_ordered_dithering(image, palette, order=8)

    inky.set_image(image_dithered.convert("P"))
    inky.show()

    return

if __name__ == "__main__":
    display_image()