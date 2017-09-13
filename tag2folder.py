import itertools
import mut
import os
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

ext = [".mp3", ".ogg", ".m4a"]
owd = os.getcwd()

if os.path.isfile("directory.ini"):
    musicDir = open('directory.ini').read()
else:
    musicDir = owd + "/music"
    if not os.path.exists("music"):
        os.makedirs("music")
