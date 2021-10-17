from PIL import Image, ImageEnhance, ImageFilter
import PIL

file = r"manual_downloads\resized_sat1.png"
img = Image.open(file)


#converter = PIL.ImageEnhance.Color(img)
converter = PIL.ImageEnhance.Sharpness(img)
img2 = converter.enhance(8)
colour_converter = PIL.ImageEnhance.Color(img2)
img2 = colour_converter.enhance(1.5)


#img.show()
img2.show()
img2.save("manual_downloads/resized_sharp_as_fuck_with_colour.png")