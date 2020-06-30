#Python program to download a video from youtube
import  pytube

video_link = "https://www.youtube.com/watch?v=XsX3ATc3FbA"
yt = pytube.YouTube(video_link)
videos = yt.streams.first()
videos.download('R:\VIDEOS')
