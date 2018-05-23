#!/usr/bin/python3
# -*- coding: Latin-1 -*-
#easytube.py
#Written by Defte

#Importing needed librairies
import argparse
import sys
import os
from pytube import Playlist, YouTube
import time

#Colors code
white="\033[1;37m"
grey="\033[0;37m"
purple="\033[0;35m"
red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
purple="\033[0;35m"
blue="\033[1;34m"
end= "\033[m"

#Cleaning the terminal
os.system("clear")

#Argparse is used to receive the input of the users from the commande line
parser = argparse.ArgumentParser()
#Specify an URL
parser.add_argument("-u",help = "Specify the URL of the YouTube video you want to convert.", dest = "url")
#Specify a file that contains multiples URL's
parser.add_argument("-f", help = "Specify a file that contains multiple youtube URL's.", dest = "file")
#Specify whether you want to download the video, the sound, or a playlist
parser.add_argument("--format", help = "Specify if you want to download a video, a sound or a playlist.", dest = "format")
#Specify if you want to convert the mp4 files into mp3
parser.add_argument("--convert", help = "Specify if you want to convert from mp4 to mp3.",  nargs = "?", const = "yes", dest = "convert")
#Specify the resolution of the video
parser.add_argument("--resolution", help = "Specify the resolution of the video (l = 480, m = 720p, h = 1080p.", dest = "resolution")
args=parser.parse_args()

#Check if we can contact youtube.com
def connected():
	try :
		print("%s[?] Checking if we can contact YouTube...%s" % (yellow, end))
		hostname = "youtube.com"
		#Ping youtube.com
		response = os.system("ping -c 1 " + hostname + " >> /dev/null")
		#If we got a response then it's alright
		if response == 0 :
		    print("%s    [+] Yes, we can !%s\n" % (green, end))
		    return 0
		else:
			#Either we exit
		    sys.exit("%s[!] Damn... Something went wrong.%s\n" % (red, end))
	except KeyboardInterrupt :
		sys.exit("%s  [!] Check was interrupted. Exiting...%s" % (red, end))
	except :
		sys.exit("%s    [!] Error while checking connection. Exiting...%s" % (red, end))

#The tool needs two directories : mp3 and mp4 
def checkDirectory() :
	directories = ["mp4", "mp3"]
	print("%s[?] Checking if directories exist.%s" % (yellow, end))
	for directory in directories :
		#If they exist then nothing
		if os.path.isdir(directory) :
			print("%s    [+] %s directory exists.%s" % (green, directory, end))
		else :
			#If they don't we create them
			print("%s    [-] Creating %s directory.%s" % (white, directory, end))
			os.system("mkdir %s" % (directory))
	return 0

#This function downloads the YouTube video
def download(link, formatdl, resolution) :
	#We create a youtube object	
	yt = YouTube(link)
	#We get the name of the video and add the .mp4 extension
	title = yt.title + ".mp4"
	#It may happen that some title got caraters that mess up with the terminal so we delete them
	title = clean(title)
	#Here are the different format and resolution
	try :
		if formatdl == "sound" :
			print("%s\n[-] Downloading %s.%s" % (white, title, end))
			yt.streams.filter(only_audio = True).first().download(filename = "filename")
			os.rename("filename.mp4", title)
		elif formatdl == "playlist" :
			print("%s\n[-] Downloading the playlist.%s" % (white, end))
			try :
				pl = Playlist(link)
				pl.download_all()
			except KeyboardInterrupt :
				sys.exit("%s  [!] Downloading was interrupted. Exiting...%s" % (red, end))
			except :
				sys.exit("%s    [!] Error while downloading. Exiting...%s" % (red, end))
		elif formatdl == "video" :
			print("%s\n[-] Downloading %s.%s" % (white, title, end))
			#Low quality
			if resolution == "l" :
				yt.streams.filter(progressive = True, subtype = "mp4").desc().first().download()
			#Medium quality
			elif resolution == "m" :
				yt.streams.filter(subtype = "mp4", res = "480p").first().download()
			#Hihgest quality
			elif resolution == "h" :
				#Note that it will download the video that has the best quality
				#It might not be 1080p60fps tho
				yt.streams.filter().first().download()
			else :
				#If you don't specify any resolution then we download the highest quality
				yt.streams.filter().first().download()
		return title
	except KeyboardInterrupt :
		sys.exit("%s  [!] Download was interrupted. Exiting...%s" %(red, end))
	except :
		sys.exit("%s    [!] Error while downloading to mp3. Exiting...%s" %(red, end))

#This function deletes the forbidden caracters from the YouTube video title
#I was stuck for 3 hours because a video contained a / in its name...
#I wanted to make something a litle bit more professional but...
#I was so pissed off that i decided that "wth i don't care as long as it works"
def clean(title) :
	forbidden = ["/", '"', "'", "|"]
	for item in forbidden :
		title = title.replace(item,"")
	return title

#This function uses the ffmpeg tool to convert the mp4 files to mp3
#We don't want the output of the command so we redirect it to /dev/null
def convert2mp3(name) :
	try :
		namemp4 = name
		namemp3 = name.replace(".mp4",".mp3")
		os.system("ffmpeg -i " + '"' + namemp4 + '"' + " " + '"' + namemp3 + '"'" 2> /dev/null")
		return 0
	except KeyboardInterrupt :
		sys.exit("%s  [!] Convertion was interrupted. Exiting...%s" %(red, end))
	except :
		sys.exit("%s    [!] Error while converting to mp3. Exiting...%s" %(red, end))

#I had to create a new convert fonction because of the way the library works
#If you want to download a playlist you will download all videos from the first to the last
#The way i coded the convert2mp3 doesn't allow me to convert these songs once they are downloaded.
#So here is the function that works
def convertAll() :
	#for each files in /easytube
	files = os.listdir()
	try :
		for title in files :
			namemp4 = title
			namemp3 = title.replace(".mp4",".mp3")
			#This line equal to : "ffmpeg -i song.mp4 song.mp3 2> /dev/null"
			os.system("ffmpeg -i " + '"' + namemp4 + '"' + " " + '"' + namemp3 + '"'" 2> /dev/null")
		return 0
	except KeyboardInterrupt :
		sys.exit("%s  [!] Convertion was interrupted. Exiting...%s" %(red, end))
	except : 
		sys.exit("%s    [!] Error while converting to mp3. Exiting...%s" %(red, end))

#Once the files are downloaded/converted we move them to their respective directories (mp3 or mp4)
#We don't want the output of the command so we redirect it to /dev/null
def moveTo() :
	try :
		os.system("mv *.mp3 mp3 2> /dev/null") 
		os.system("mv *.mp4 mp4 2> /dev/null")
		return 0
	except :
		sys.exit("%s    [!] Error while moving files to directories. Exiting...%s" % (red, end))

print('''%s

 _____              _____     _                        
|  ___|            |_   _|   | |                       
| |__  __ _ ___ _   _| |_   _| |__   ___   _ __  _   _ 
|  __|/ _` / __| | | | | | | | '_ \ / _ \ | '_ \| | | |
| |__| (_| \__ \ |_| | | |_| | |_) |  __/_| |_) | |_| |
\____/\__,_|___/\__, \_/\__,_|_.__/ \___(_) .__/ \__, |
                 __/ |                    | |     __/ |
                |___/                     |_|    |___/             

Easy YouTube video downloader.
Written by Defte using pytube library and Python 3.6.\n%s'''% (white, end))

#Checks if args were set
if (args.url == None and args.file == None) :
	sys.exit("%s[!] No URL/file specified. Exiting...%s" % (red, end))
elif args.format == None :
	sys.exit("%s[!] No format specified. Exiting...%s" % (red, end))
elif args.format != "sound" and args.format != "video" and args.format != "playlist" :
	sys.exit("%s[!] Wrong format specified. Exiting...%s" % (red, end))
elif args.resolution != None :
	if args.resolution != "l" and args.resolution != "m" and args.resolution != "h" :
		sys.exit("%s[!] Wrong resolution specified. Exiting...%s" % (red, end))
	else :
		resolution = args.resolution
else :
	resolution = ""
	

#Checks if connected to internet and if directories exist
connected()
checkDirectory()

#Download using one URL
if args.url != None :
	title = download(args.url, args.format, resolution)
	print("%s    [+] File(s) downloaded.%s" % (green, end))
	if args.convert == "yes" and  args.format != "video" and args.format != "playlist" :
		convert2mp3(title)
		print("%s    [+] File converted to MP3.%s" % (green, end))
	elif args.convert == "yes" and args.format == "playlist" :
		convertAll()
		print("%s    [+] Playlist converted to MP3.%s" % (green, end))

#Download using a file that contains URL's
elif args.file != None :
	try :
		lines = open(args.file, "r")
		for link in lines :
			title = download(link, args.format, resolution)
			print("%s    [+] File downloaded.%s" % (green, end))
			if args.convert == "yes" and args.format != "video" :
				convert2mp3(title)
				print("%s    [+] File converted to MP3.%s" % (green, end))
	except  :
		sys.exit("\n%s[!] No file %s found. Exiting...%s" % (red, args.file, end))

moveTo()

print('''\n%s[-] Job's done :D ! You will find the files in the mp3/mp4 directories ;) !
[-] If you enjoyed the tool, please check my website : %s%shttp://whiteflagfr.wordpress.com/.%s''' % (white, end, blue, end ))
