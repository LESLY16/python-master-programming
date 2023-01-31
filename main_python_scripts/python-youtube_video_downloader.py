from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occured")
    finally:
        print("Download is completed successfully")

if __name__ == "__main__":
    link = input("Enter the Youtube video URL: ")
    Download(link)