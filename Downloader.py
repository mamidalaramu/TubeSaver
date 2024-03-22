import os
import sys
from pytube import YouTube
import argparse

VALID_RESOLUTIONS = ["480p", "720p", "1080p"]
DOWNLOAD_PATH = r"C:\Users\mamid\Downloads\Videos"


def clear_terminal():

    if os.name == "nt":  # for Windows
        os.system("cls")
    else:  # for Linux and Mac
        os.system("clear")


def main():
    clear_terminal()
    parser = argparse.ArgumentParser(description="Youtube Video downloader!")
    parser.add_argument("url", nargs="?", help="The URL of the video to be downloaded.")
    parser.add_argument(
        "--resolution",
        "-r",
        default="720p",
        choices=VALID_RESOLUTIONS,
        help="Resolution of the video (default: 720p)",
    )
    args = parser.parse_args()

    if args.url:
        downloadVideo(args.url, args.resolution)
    else:
        video_url = input("Enter the URL of the video to download: ")
        downloadVideo(video_url, args.resolution)


def progress_func(stream, chunk, bytes_remaining):
    progress = (stream.filesize - bytes_remaining) / stream.filesize * 100
    sys.stdout.write(f"\rDownloading... {progress:.2f}% complete")
    sys.stdout.flush()


def complete_func(stream, DOWNLOAD_PATH):
    print(f"\nDownload completed...\nFile_Path: {DOWNLOAD_PATH}")


def downloadVideo(url, resolution):
    yt = YouTube(url)
    print("===================================================================")
    print("Provided URL: ", url)
    print("Title: ", yt.title)
    print("Views: ", yt.views)
    print(
        "Length: ",
        str(yt.length // 60) + " minutes and " + str(yt.length % 60) + " seconds",
    )

    yt.register_on_progress_callback(progress_func)
    yt.register_on_complete_callback(complete_func)

    yDownload = yt.streams.filter(res=f"{resolution}")

    if yDownload:
        print(f"Downloading video '{yt.title}' with resolution {resolution}")
        yDownload[0].download(DOWNLOAD_PATH)

    else:
        print(f"No available stream with resolution {resolution}")


if __name__ == "__main__":
    main()
