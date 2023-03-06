from PIL import Image

# Open the image file
img = Image.open('image.jpg')

# Resize the image to reduce processing time
img = img.resize((100, 100))

# Get the RGB color values for each pixel in the image
pixels = img.load()

# Calculate the average color of the image
r, g, b = 0, 0, 0
for i in range(img.size[0]):
    for j in range(img.size[1]):
        r += pixels[i, j][0]
        g += pixels[i, j][1]
        b += pixels[i, j][2]

total_pixels = img.size[0] * img.size[1]
avg_color = (r//total_pixels, g//total_pixels, b//total_pixels)

print(f"Average color of image: {avg_color}")