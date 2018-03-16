#!/usr/bin/python3
# -*- coding: utf-8 -*-
#graphicalinterface.py

from tkinter import * 
from tkinter.filedialog import *
import os

#INITIALIZE THE WINDOW
root = Tk()
root.title("Easytube.py")
cmd = "python3 ./easytube.py"

def getFileName():
	global filepath
	filepath = askopenfilename()
	return filepath

def tocmd(cmd, filepath, formatv, resolution, convert) :
	if link.get() != "" :
		cmd = cmd + " -u " + link.get()
		if formatv.get() == "sound" :
			cmd = cmd + " --format sound"
			if convert.get() == 1 :
				cmd = cmd + " --convert"
		elif formatv.get() == "video" :
			cmd = cmd + " --format video"
			if resolution.get() == "l" :
				cmd = cmd + " --resolution l"
			elif resolution.get() == "m" :
				cmd = cmd + " --resolution m"
			elif resolution.get() == "h" :
				cmd = cmd + " --resolution g"
		elif formatv.get() == "playlist" :
			cmd = cmd + " --format playlist"
			if convert.get() == 1 :
				cmd = cmd + " --convert"
	elif link.get() == "" and filepath != None :
		cmd = cmd + " -f " + filepath
		if formatv.get() == "sound" :
			cmd = cmd + " --format sound"
			if convert.get() == 1 :
				cmd = cmd + " --convert"
			elif formatv.get() == "video" :
				cmd = cmd + " --format video"
				if resolution.get() == "l" :
					cmd = cmd + " --resolution l"
				elif resolution.get() == "m" :
					cmd = cmd + " --resolution m"
				elif resolution.get() == "h" :
					cmd = cmd + " --resolution g"
			elif formatv.get() == "playlist" :
				cmd = cmd + " --format playlist"
				if convert.get() == 1 :
					cmd = cmd + " --convert"
	os.system(cmd)
	return 0

filepath = ""

#Creating label
labeltarget = LabelFrame(root, text=  "Target", padx = 20, pady = 20)
labeltarget.grid(row = 1, column = 1)
labeltarget = LabelFrame(root, text = "Target", padx = 20, pady = 20)
labeltarget.grid(row = 1, column = 1)
labelformat= LabelFrame(root, text = "Format", padx = 20, pady = 20)
labelformat.grid(row = 2, column = 1)
labelresolution = LabelFrame(root, text = "Resolution", padx = 20, pady = 20)
labelresolution.grid(row = 4, column = 1)
labelconvert = LabelFrame(root, text = "Convert", padx = 20, pady = 20)
labelconvert.grid(row = 5, column = 1)
labelButton = LabelFrame(root, text = "Buttons", padx = 20, pady = 20)
labelButton.grid(row = 6, column = 1)

#LINKS
Label(labeltarget, text = "Enter the URL", borderwidth = 4).grid(row = 1, column = 1)
link = Entry(labeltarget, width = 30)
link.grid(row = 1, column = 2)

#FILE
Label(labeltarget, text = "Or select a text file", borderwidth = 4, pady = 5, padx = 5).grid(row = 2, column = 1)
button = Button(labeltarget, text = "Browse", command = (lambda: getFileName()))
button.grid(row = 2, column = 2)

#FORMAT
Label(labelformat, text = "Select the format", borderwidth = 4).grid(row = 3, column = 1, padx = 2, pady = 2)
formatvideo = StringVar() 
bouton1 = Radiobutton(labelformat, text = "Sound", variable = formatvideo, value = "sound", borderwidth = 4).grid(row = 4, column = 1, padx = 0)
bouton2 = Radiobutton(labelformat, text = "Video", variable = formatvideo, value = "video", borderwidth = 4).grid(row = 4, column = 2, padx = 0)
bouton3 = Radiobutton(labelformat, text = "Playlist", variable = formatvideo, value = "playlist", borderwidth = 4).grid(row = 4, column = 3, padx = 0)

#RESOLUTION
Label(labelresolution, text = "Select the resolution", borderwidth = 4).grid(row = 5, column = 1, padx = 2, pady = 2)
resolution = StringVar() 
bouton1 = Radiobutton(labelresolution, text = "low", variable = resolution, value = "l", borderwidth = 4).grid(row = 6, column = 1, padx = 0)
bouton2 = Radiobutton(labelresolution, text="medium", variable=resolution, value="m", borderwidth=4).grid(row=6, column=2, padx=0)
bouton3 = Radiobutton(labelresolution, text = "high", variable = resolution, value = "h", borderwidth = 4).grid(row = 6, column = 3, padx = 0)

#CONVERT
convertion = IntVar()
Label(labelconvert, text = "Convert to MP3", borderwidth = 4).grid(row = 7, column = 1, padx = 2, pady = 2)
convert = Checkbutton(labelconvert, text = "", variable = convertion)
convert.grid(row = 7, column = 2, padx = 2, pady = 2)

#DOWNLOAD / EXIT
Button(labelButton, text = "Download", width = "10", command = lambda : tocmd(cmd,filepath,formatvideo,resolution,convertion)).grid(row = 8 , column = 1, padx = 5)
Button(labelButton, text = "Exit", width = "10", command = root.quit).grid(row = 8 ,column = 2, padx = 5)

root.mainloop()
