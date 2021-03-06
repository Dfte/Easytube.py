# Easytube.py

Easytube.py is a Python 3.6 script that allows you to download contents (sounds and/or videos) from YouTube very easily.
The tool is using the pytube library and the ffmpeg tool. You will need both these items to run the script so before doing anything please launch the instal.sh script.

You can download three types of contents : audios, videos and playlists.

<h2>Audio</h2>

The easiest way to only download the audio part is by lauching this command :

<img src="https://github.com/Dfte/Easytube.py/blob/master/images/0.png"></img>

I strongly advice you to double quote the link since i had a lot of problems with invalid caracters such as " / " that break the terminal when it comes to converting the song to mp3. This command means that you will download a content using the URL (-u) and you only want the audio part (--format sound).

By default, YouTube audio files are using .mp4 extension. You might want to convert the .mp4 files to .mp3. To do so just add the argument --convert and it will be done.

<img src="https://github.com/Dfte/Easytube.py/blob/master/images/1.png"></img>
<img src="https://github.com/Dfte/Easytube.py/blob/master/images/2.png"></img>

To convert the files from .mp4 to .mp3 the tool uses ffmpeg.

Note that you can also create a .txt file in which you will put all your YouTube URL's :

<img src="https://github.com/Dfte/Easytube.py/blob/master/images/3.png"></img>

And then download them all using -f "file that contains the links" :

<img src="https://github.com/Dfte/Easytube.py/blob/master/images/7.png"></img>
<img src="https://github.com/Dfte/Easytube.py/blob/master/images/4.png"></img>

<h2>Videos</h2>

As much as for the audio part, you can either download a single video or multiples ones using the -u and -f arguments. This time, you will have to add the --format video in order to download it :

<img src="https://github.com/Dfte/Easytube.py/blob/master/images/5.png"></img>

However you can also specify the resolution of the video that you want.
There are 3 resolutions available :<br>
-(l)ow<br>

<img src="https://github.com/Dfte/Easytube.py/blob/master/images/low.png"></img>

-(m)edium<br>

<img src="https://github.com/Dfte/Easytube.py/blob/master/images/medium.png"></img>

-(h)igh<br>

<img src="https://github.com/Dfte/Easytube.py/blob/master/images/high.png"></img>

If you don't specify any resolution then the programm will by default download the highest resolution available.

There is a <b>huge trick</b> in that part of the programm. In fact you can not predefine the resolutions that will be available for a video on YouTube (it will all depend of the source video resolution) so i had to hack something up :

-If you choose the (l)ow argument then the programm will check for the lowest resolution available that has a .mp4 extension and download it.<br>
-If you choose the (m)edium argument then it will look for the 720p resolution. If it is not available it will download the 480p resolution.<br>
-If you choose the (h)igh argument then it will download the highest resolution available (1080p or 720p).

Whatever resolution you choose you will always end up with a .mp4 file.

<h2>Playlist</h2>
 
You can download an entire playlist very easily. To download a playlist you will have to specify that the --format is playlist :

<img src="https://github.com/Dfte/Easytube.py/blob/master/images/playlist.png"></img>
<img src="https://github.com/Dfte/Easytube.py/blob/master/images/playlistdownloaded.png"></img>

This time you will not be able to specify the resolution, it will automatically download the highest resolution availabe. However you can still convert the videos into .mp3 if you only want the audio part (using --convert).

<h1>Graphical User Interface</h1>

I've heard that people prefer graphical interface so i made one :

<img src="https://github.com/Dfte/Easytube.py/blob/master/images/graphical.png"></img>

So yeah i know it is not beautiful but it works and if you are a Linux user then you shoudln't be using this è-é !
To launch the GUI just launch the graphicalinterface.py

<h1>Windows Users</h1>

First of all i wanted to convert the tool for Windows but it would take me too much time. So i decided not to do it... 
But ! A friend of mine reminded me that now there is the new ubuntu shell available on Windows so i might create a tutoriel about how to use the tool with the Ubuntu shell.

<h1>Conclusion</h1>

The downloads might take some times (depending of your connection speed). Originaly i wanted to add a progress bar but i had to remove it because it was feezing the tool way too much. I did a lot of tests, had to patch a lot of things and yet there might be some errors. 

If you find one, if you would like something to be upgraded or if you just want to talk about this tool please feel free to contact me on : <a href="https://www.facebook.com/DefteWhiteFlag/">Facebook</a>

-Defte







