import os
import sys
from moviepy.editor import VideoFileClip
from pytube import YouTube
from ytmusicapi import YTMusic

def download_youtube(url,outpath):
    yt = YouTube(url)
    yt.streams.filter(file_extension="mp4").get_by_resolution("360p").download(outpath)

def cvta(video_file, output_ext="mp3"):
    vidfile = '/home/john/iPod Music/'+video_file
    filename, ext = os.path.splitext(vidfile)
    clip = VideoFileClip(vidfile)
    clip.audio.write_audiofile(f"{filename}.{output_ext}")


def search_music(srch):
    ytmusic = YTMusic()
    return ytmusic.search(srch)
['TobyMac', 'Help Is On The Way (Maybe Midnight)']
def add_metadata(metadata,filep):
    import eyed3
    audiofile = eyed3.load(filep)
    audiofile.tag.artist = metadata[0]
    audiofile.tag.title = metadata[1]
    audiofile.tag.save()

filesold = os.listdir('/home/john/iPod Music')
searchterm = search_music(input('What would you like to search for? '))
topres = searchterm[0]
vid = topres.get('videoId')
print(topres)
restype = topres.get('resultType')

songinfo = []
title = topres.get('title')
artistsdict = topres.get('artists')
artist = artistsdict[0].get('name')
songinfo.insert(0,title)
songinfo.insert(0,artist)
print(songinfo)
if restype == 'song':
    print(vid)
    urltodownload = 'https://www.youtube.com/watch?v='+vid
    download_youtube(urltodownload,'/home/john/iPod Music/')
    print('Done!')
else:
    topres = searchterm[1]
    vid = topres.get('videoId')
    restype = topres.get('resultType')
    print(vid)
    urltodownload = 'https://www.youtube.com/watch?v='+vid
    download_youtube(urltodownload,'/home/john/iPod Music/')
    print('Done!')
filesnew = os.listdir('/home/john/iPod Music/')
diff = set(filesold) ^ set(filesnew)
print(diff)
for x in diff:
    filen = '/home/john/iPod Music/'+x
    cvta(x)
os.remove(filen)
filen2 = filen.replace('.mp4','.mp3')
print(filen2)
add_metadata(songinfo, filen2)