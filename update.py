from pyrogram import Client, filters
import requests,os,csv
from time import time
import time
from datetime import datetime
from pytz import *
import pytz
from pyrogram import enums
from spdatabase import *
from threading import Thread
import random








api_id = 3702208
api_hash = "3ee1acb7c7622166cf06bb38a19698a9"
bot_token = "5030635324:AAEaM9t5WBQHUeUAfJJK4r39h5457YwuD1k"


app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)













links = []

with open("links.txt","r") as file:
    for i in file.readlines():
        if i == "links\n" or i =="links":
           pass
        else:
         links.append(i.strip())







link = random.choice(links)


with open("links.txt","r") as file:
    lines = file.readlines():
    with open("links.txt","w") as file2:
      for line in lines:
         if line!=link:
            file2.write(line)
       


def dled():
    links ='Downloaded Links\n'
    for i in read_links():
        links+=i[0] + "\n"
    return links
       









def stats(status,crtda,link,total):
    stats = f'<b>├  Status: </b>{status}\n'\
            f'<b>├  Uploaded Videos: </b>{total}\n'\
            f'<b>├  {link.split("/")[-2].capitalize()}: </b>{link.split("/")[-1].capitalize()}\n'\
            f'<b>╰  Updated Time: </b>{crtda}\n\n'
    return stats







async def main():
   async with app:
     if len(links)!=0:
            count = 0
            now=datetime.now(pytz.timezone("Asia/Kolkata"))
            crtda = now.strftime('%m/%d %H:%M %p')
            await app.edit_message_text(-1001984459303,11,text=stats("Active",crtda,link,"Uploading.."))
            insert_links(link)
            os.system("""yt-dlp --downloader aria2c --match-filter "duration>180" --max-downloads 100 -N 4  --download-archive dled.txt --playlist-random  -o '%(title)s.%(ext)s' -f '(mp4)[height=?480]' --write-thumbnail --embed-metadata """ + link)
            
            
            for  filename in os.listdir():
                if filename.endswith(".mp4") :
                    for j in read_db():
                        if j == filename:
                            break
                    else:
                            insert_db(filename)
                            count+=1
                            os.system(f'''vcsi """{filename}""" -g 2x6 --metadata-position hidden -o """{filename.replace('.mp4','.png')}""" ''')
                            await app.send_photo(-1001848025191, photo=filename.replace(".mp4",".png"))
                            video = await app.send_video(-1001585702100,video=filename,caption=filename.replace(".mp4",""),thumb=filename.replace(".mp4",".jpg"))
                            try:
                             os.remove(filename.replace(".mp4",".jpg"))
                             os.remove(filename.replace(".mp4",".png"))
                             os.remove(filename)
                            except:
                             print("File Moved I guess!!!") 
            await app.edit_message_text(-1001984459303,11,text=stats("Offline",crtda,link,count))
            await app.edit_message_text(-1001984459303,12,text=dled())     
            

app.run(main())
