# Randomly updates your Discord profile picture (and username if you want)
# Takes images from a folder (eg. random image from your saved pictures folder) and sets it as your profile pic

import pyautogui, time, ctypes, math, pywinauto, re, os, random, mimetypes
import pydirectinput as pdi
from pynput.mouse import Button, Controller
from win32gui import GetWindowText, GetForegroundWindow
from pywinauto import Desktop, Application

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
				flist.append(fname)
# image_filenames = os.listdir(imagesdir)
newpp = random.choice(flist)


def clickicon(icon_name):
	icon = None
	while icon is None:
		icon = pyautogui.locateCenterOnScreen(f'images/{icon_name}.png', grayscale=True) # locates specified icon using screenshot

	print(icon)
	if icon_name == 'change':
		pyautogui.click((icon[0]-50, icon[1]))
	else:
		pyautogui.click((icon[0], icon[1])) # clicks icon
	time.sleep(1)

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
		pyautogui.typewrite(f'{imagesdir}')
		pyautogui.press("enter")
		time.sleep(0.5)

		# Typing in image name
		cursor = pyautogui.position()
		print(cursor)
		pdi.moveTo(cursor[0],cursor[1]+200) # file name bar
		pync()
		pyautogui.typewrite(newpp)
		pyautogui.press("enter")
		time.sleep(0.5)

		# Applying profile pic
		pdi.moveTo(round(res[0]*0.62),round(res[1]*0.72)) # apply button
		pync()
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