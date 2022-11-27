import pytube

try:
    link = input("Enter video link : ")
    yt = pytube.YouTube(link)
    stream = yt.streams.first()
    stream.download()
except Exception as e :
    print(e)

print("Downloaded Successfully")
print("Thanks for using our video downloader")