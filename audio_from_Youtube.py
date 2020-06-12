# Python program to download a audio file from Youtube
#error there
from  __future__ import unicode_literals
import youtube_dl
ydl_opts={
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192'
    }],
    'postprocessor_args':[
        '-ar','16000'
    ],
    'prefer_ffmpeg': True
    #'KeepVid ': True
    }
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=7ysFgElQtjI'])



