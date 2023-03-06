from PIL import Image
import os, mimetypes

# # Open the image file
# img = Image.open('image.jpg')

# # Resize the image to reduce processing time
# img = img.resize((100, 100))

# # Get the RGB color values for each pixel in the image
# pixels = img.load()

# # Calculate the average color of the image
# r, g, b = 0, 0, 0
# for i in range(img.size[0]):
#     for j in range(img.size[1]):
#         r += pixels[i, j][0]
#         g += pixels[i, j][1]
#         b += pixels[i, j][2]

# total_pixels = img.size[0] * img.size[1]
# rgb_color = (r//total_pixels, g//total_pixels, b//total_pixels)
# avgcol = '{:02x}{:02x}{:02x}'.format(rgb_color[0], rgb_color[1], rgb_color[2])

# print(f"Average color of image: #{avgcol}")

imagesdir = "H:/System/Pictures/Saved Pictures"
flist = [] # list of images
for dirName, subdirList, fileList in os.walk(imagesdir):
    for fname in fileList:
        print(f'{dirName}/{fname}')