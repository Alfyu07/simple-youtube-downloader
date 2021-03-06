import os
import sys
from pytube import YouTube
from pytube import Playlist

class Downloader:
  def __init__(self):
    #enter save directory here
    self.SAVE_PATH = '/home/alfyu/Unduhan/pytube/'
    self.DOWNLOAD_PLAYLIST = False
    self.DOWNLOAD_WITH_CAPTION= False
    self.yt = None
    self.p = None
  
  def singleDownload(self,link, index = ''):
    try:
      self.yt = YouTube(link)
      video = self.yt.streams.get_highest_resolution()
      filename = index+'. '+ self.yt.title
      
      print(filename + " Downloading...")
      video.download(self.SAVE_PATH, filename = filename)
      if(self.DOWNLOAD_WITH_CAPTION):
        self.captionDownload(filename)
      return True
    except:
      print("Connection Error")
      return False

  def playlistDownload(self, link):
    #create playlist object
    self.p = Playlist(link)
    print("creating " + self.p.title + " folder at " + self.SAVE_PATH)
    self.SAVE_PATH = self.SAVE_PATH + self.p.title
    if not os.path.isdir(self.SAVE_PATH):
      os.mkdir(self.SAVE_PATH)
    
    print("Start Downloading...")
    for index, url in enumerate(self.p.video_urls):
      self.singleDownload(url, index=str(index))
      print("Video Downloaded")
    return True
  
  def captionDownload(self, filename):
    completeName = os.path.join(self.SAVE_PATH,filename+'.srt')
    # print(completeName)
    try:
      caption = self.yt.captions['a.en']
      subtitle = open(completeName, 'w')
      subtitle.write(caption.generate_srt_captions())
      subtitle.close()
    except:
      print("no caption")

if __name__ == "__main__":
  print("Checking SAVE_PATH directory...")
  selectedIndex = 0
  finish = False
  downloader = Downloader()
  
  if not os.path.isdir(downloader.SAVE_PATH):
    print("Folder not Exist")
    sys.exit()
  
  print("Simple Youtube Downloader ")
  print("1. Single Download")
  print("2. Playlist Download")  
  selectedIndex = int(input("Select: "))
  
  downloadWithCaption = input('Download with caption? (yes/no) : ').lower()
  downloader.DOWNLOAD_WITH_CAPTION = True if downloadWithCaption == 'y' or downloadWithCaption == 'yes' or downloadWithCaption == '' else False 

  os.system('clear')
  if(selectedIndex == 1):
    url = input("Enter video url : ")
    try :
      downloader.DOWNLOAD_PLAYLIST = False
      print("Downloading...")
      finish = downloader.singleDownload(url)
    except:
      print("unknown error")
  else:
    url = input("Enter playlist url : ")
    try:
      downloader.DOWNLOAD_PLAYLIST = True
      finish = downloader.playlistDownload(url)
    except:
      print("unknown error")
  if(finish):
    print("Download Finished")
  