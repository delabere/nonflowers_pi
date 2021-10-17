from PIL import Image, ImageEnhance, ImageFilter
import PIL

file = r"manual_downloads\resized_sat1.png"
img = Image.open(file)


#converter = PIL.ImageEnhance.Color(img)
converter = PIL.ImageEnhance.Sharpness(img)
img2 = converter.enhance(15)


#img.show()
img2.show()
img2.save("resized_sharp_as_fuck.png")