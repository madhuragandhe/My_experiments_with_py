#Python program to convert a video to audio file
import moviepy.editor as mp
video=mp.VideoFileClip("Lady Gaga- Million Reasons.mp4")
video.audio.write_audiofile("successful.mp3")
