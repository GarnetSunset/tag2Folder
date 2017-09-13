from mutagen.flac import FLAC
from mutagen.mp3 import MP3
from mutagen.ogg import OggFileType
from mutagen.oggopus import OggOpus
from shutil import move
import itertools
import os
import re
import sys
import threading
import time

def loading():
    for s in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + s)
        sys.stdout.flush()
        time.sleep(0.1)

done = False
ext = [".mp3", ".ogg", ".opus", ".flac"]
extVorbis = [".ogg", ".opus", ".flac"]
oops = False
owd = os.getcwd()

if os.path.isfile("directory.ini"):
    musicDir = open('directory.ini').read()
else:
    musicDir = owd + "/music"
    if not os.path.exists("music"):
        os.makedirs("music")

g = threading.Thread(target=loading)
g.start()

for dname, dirs, files in os.walk(musicDir):
    for fname in files:
        fpath = os.path.join(dname, fname)
        if fname.endswith(tuple(extVorbis)):
            if fname.endswith(tuple(extVorbis)):
                if fpath.endswith(".flac"):
                    try:
                        tags = FLAC(fpath)
                    except:
                        oops = True
                if fpath.endswith(".mp3"):
                    try:
                        tags = MP3(fpath)
                    except:
                        oops = True
                if fpath.endswith(".ogg"):
                    try:
                        tags = OggFileType(fpath)
                    except:
                        oops = True
                if fname.endswith(".opus"):
                    try:
                        tags = OggOpus(fpath)
                    except:
                        oops = True

                try:
                    tags = tags.pprint()

                    try:
                        artistStart = tags.index('artist=')
                    except:
                        try:
                            artistStart = tags.index('ARTIST=')
                        except:
                            artistStart = tags.index('Artist=')

                    loose = tags[artistStart+7:]
                    try:
                        stopPoint = loose.index('\n')
                    except:
                        print("")
                    artist = loose[:stopPoint]

                    try:
                        albumStart = tags.index('album=')
                    except:
                        try:
                            albumStart = tags.index('ALBUM=')
                        except:
                            albumStart = tags.index('Album=')

                    loose = tags[albumStart+6:]
                    try:
                        stopPoint = loose.index('\n')
                    except:
                        print("")
                    album = loose[:stopPoint]
                    artistStrip = re.sub('[!@#$:;]', '', artist)
                    albumStrip = re.sub('[!@#$:;]', '', album)
                    albumFolder = musicDir + "\\"  + artistStrip + "\\" + albumStrip + "\\"
                    try:
                        os.makedirs(albumFolder)
                    except:
                        if os.name == 'nt':
                            os.system('cls')
                        else:
                            os.system('clear')
                except:
                    oops = True
                try:
                    move(musicDir + "\\" + fname, musicDir + "\\"  + artistStrip + "\\" + albumStrip + "\\" + fname)
                except:
                    if os.name == 'nt':
                        os.system('cls')
                    else:
                        os.system('clear')

if oops == True:
    print("Something went wrong with some file names... nothing was lost though!")

done = True
