from process_image import process_image
from flower_grower import get_flower
from display_image import display_image

if __name__ == "__main__":
    get_flower()     # get new flower image
    process_image()  # process that into something which looks better on screen
    display_image()  # put it on the screen