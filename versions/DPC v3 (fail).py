# Randomly updates your Discord profile picture (and username if you want)
# Takes images from a folder (eg. random image from your saved pictures folder) and sets it as your profile pic

# v3 change log
# Recoded to use discord API instead of manually controlling GUI

import pyautogui, time, ctypes, math, pywinauto, re, os, random, mimetypes, discord
import pydirectinput as pdi
from pynput.mouse import Button, Controller
from win32gui import GetWindowText, GetForegroundWindow
from pywinauto import Desktop, Application
from PIL import Image

## Choosing image

imagesdir = "H:/System/Pictures/Saved Pictures"
flist = [] # list of images
for dirName, subdirList, fileList in os.walk(imagesdir):
	for fname in fileList:
		filemimetype, _ = mimetypes.guess_type(fname)
		if filemimetype and filemimetype.startswith('image/'):
			if filemimetype and filemimetype.startswith('image/gif'):
				pass
			else:
				flist.append((dirName,fname))
# image_filenames = os.listdir(imagesdir)
newpp = random.choice(flist)

## Getting average image colour:
# Open the image file
img = Image.open(f'{newpp[0]}/{newpp[1]}')

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
rgb_color = (r//total_pixels, g//total_pixels, b//total_pixels)
avgcol = '{:02x}{:02x}{:02x}'.format(rgb_color[0], rgb_color[1], rgb_color[2])


## Selenium code

user = input('>> Please enter your Discord username:   ')
passw = input('>> Please enter your Discord password:   ')