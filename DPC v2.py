# Randomly updates your Discord profile picture (and username if you want)
# Takes images from a folder (eg. random image from your saved pictures folder) and sets it as your profile pic

# v2 change log
# Opens discord (if unopened) and automatically switches to application (incomplete)
# gets average image colour and sets banner as colour

import pyautogui, time, ctypes, math, pywinauto, re, os, random, mimetypes
import pydirectinput as pdi
from pynput.mouse import Button, Controller
from win32gui import GetWindowText, GetForegroundWindow
from pywinauto import Desktop, Application
from PIL import Image

user32 = ctypes.windll.user32
res = user32.GetSystemMetrics(0),user32.GetSystemMetrics(1) # screen resolution
pyn_mouse = Controller() # pynput mouse

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




def clickicon(icon_name):
	icon = None
	while icon is None:
		icon = pyautogui.locateCenterOnScreen(f'images/{icon_name}.png', grayscale=True) # locates specified icon using screenshot
		# 08/04/23 Weird bug where the images stopped being recognised, fixed by replacing the files with new screenshots

	if icon_name == 'change':
		pyautogui.click((icon[0]-50, icon[1]))
	else:
		pyautogui.click((icon[0], icon[1])) # clicks icon
	time.sleep(1)

	print(f'clicked {icon_name}')

def pync(): # pynput click
	time.sleep(0.1)
	pyn_mouse.press(Button.left)
	time.sleep(0.1)
	pyn_mouse.release(Button.left)
	time.sleep(0.1)


while True:
	cw = GetWindowText(GetForegroundWindow()) # current window

	if re.search(r'\bDiscord\b\s*$',cw): 
		# Clicking settings
		clickicon('settings')

		# Clicking on edit profile pic
		# clickicon('edit') # Its not finding the edit button for some reason so I decided to use pydirectinput instead
		pdi.moveTo(round(res[0]*2/3),round(res[1]*2/9)) # edit button
		pync()
		clickicon('change')

		# Clicking upload
		# clickicon('upload') # not finding the upload button either, perhaps because its a pop-up
		pdi.moveTo(round(res[0]*0.45),round(res[1]*0.5)) # upload button
		pync()

		# Typing in directory path
		clickicon('addbar')
		pyautogui.typewrite(newpp[0])
		pyautogui.press("enter")
		time.sleep(2)

		# Typing in image name
		cursor = pyautogui.position()
		print(cursor)
		pdi.moveTo(cursor[0],cursor[1]+200) # file name bar
		pync()
		pyautogui.typewrite(newpp[1])
		pyautogui.press("enter")
		time.sleep(2)

		# Applying profile pic
		pdi.moveTo(round(res[0]*0.62),round(res[1]*0.72)) # apply button
		pync()
		time.sleep(0.5)

		# Changing banner colour
		pdi.moveTo(round(res[0]*0.4),round(res[1]*0.3)) # save changes button
		pync()
		time.sleep(0.1)
		pyautogui.hotkey("ctrl", "a")
		time.sleep(0.1)
		pyautogui.typewrite(avgcol)
		time.sleep(0.1)

		# Saving changes
		pdi.moveTo(round(res[0]*0.67),round(res[1]*0.92)) # save changes button
		time.sleep(0.5)
		pync()
		time.sleep(3) # waiting for changes to be applied

		# Returning to Discord homepage
		clickicon('escape')


		break
	else:
		print('>> Waiting for Discord...')

	time.sleep(5)