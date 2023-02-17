from pyrogram import Client, filters
import requests,os,csv,time
from time import time
from datetime import datetime
from pytz import timezone

api_id = 3702208
api_hash = "3ee1acb7c7622166cf06bb38a19698a9"
bot_token = "5102219510:AAHGCySOBy1AIYCnJiJeArX5lmOJ5nE7dh8"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)


async def progress(current, total):
    print(f"{current * 100 / total:.1f}%")

@app.on_message(filters.command("update"))
async def start_command(client,message):
     now=datetime.now()
     crtda = now.strftime('%m/%d/%y')
     print(crtda)
     channel_id = message.chat.id
     await app.send_message(channel_id,"Updating.....")
     filec = open("links.txt","r")
     read=csv.reader(filec)
     for link in read:
        os.system("""yt-dlp --downloader aria2c --playlist-items 1 -o %(%Y-%m-%d) --download-archive dllinks.txt -f '(480[vcodec~="^((he|a)vc|h26[45])"]+ba) / (480+ba/b)' --embed-thumbnail --embed-metadata """ + link[0])
     for  filename in os.listdir():
               print(filename)
               if filename.endswith(".mp4") :
                    await app.send_document(-1001737315050, document=filename+'/'+names,caption=names,progress=progress)



 
           
app.run()  # Automatically start() and idle()
