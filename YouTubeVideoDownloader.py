from pytube import YouTube
from moviepy.editor import VideoFileClip
import os
import shutil


def download_video():
    video_url = input("Enter a YouTube video link: ")
    video_format = input("What format do you need (default:mp4/mp3)?: ")
    directory = input("Save to what directory?: ")
    print("Downloading...")

    mp4_file = YouTube(video_url).streams.get_highest_resolution().download()

    # Hello
    if video_format == "mp3":
        print("Converting to mp3...")

        mp3_file = mp4_file.split(".mp4", 1)[0] + f".{video_format}"

        video_clip = VideoFileClip(mp4_file)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(mp3_file)

        audio_clip.close()
        video_clip.close()

        os.remove(mp4_file)

        # Change file path e.g C:\Users\HP\Videos
        if directory:
            print("Moving to directory...")
            shutil.move(mp3_file, f"{directory}")

    else:
        YouTube(video_url).streams.get_highest_resolution().download()

        # Change file path e.g C:\Users\HP\Videos
        if directory:
            print("Moving to directory...")
            shutil.move(mp4_file, f"{directory}")


download_video()
