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



api_id = 3702208
api_hash = "3ee1acb7c7622166cf06bb38a19698a9"
bot_token = "5030635324:AAEaM9t5WBQHUeUAfJJK4r39h5457YwuD1k"




app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)




      


def stats(status,crtda,total):
    stats = f'<b>├  Status: </b>{status}\n'\
            f'<b>├  Uploaded Videos: </b>{total}\n'\
            f'<b>╰ Updated Time: </b>{crtda}\n\n'
    return stats



@app.on_message(filters.command("update"))
async def start_command(client,message):
     count = 0
     now=datetime.now(pytz.timezone("Asia/Kolkata"))
     crtda = now.strftime('%m/%d %H:%M %p')
     await app.edit_message_text(-1001984459303,11,text=stats("Active",crtda,"Uploading.."))
     cmd  = message.text
     channel_id = message.chat.id
     if "playlist" in cmd.split()[1] or  "model" in cmd.split()[1] or  "pornstar" in cmd.split()[1]:
        await app.send_message(channel_id,f"Downloading Videos of Playlist:\n{cmd.split()[1]}")
     else:
         await app.send_message(channel_id,f"Downloading:\n{cmd.split()[1]}")
     os.system("""yt-dlp --downloader aria2c --match-filter "duration>180" --max-downloads 100 -N 4 --playlist-random --download-archive dl.txt -o '%(title)s.%(ext)s' -f '(mp4)[height=?480]' --write-thumbnail --embed-metadata """ + cmd.split()[1])
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
     await app.edit_message_text(-1001984459303,11,text=stats("Offline",crtda,count))            


def run():

   app.run()

def keep_alive():  

    t = Thread(target=run)
    t.start()
    time.sleep(7)
    quit()

#app.run()
