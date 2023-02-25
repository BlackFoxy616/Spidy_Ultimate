#from spdatabase import *
from pyrogram import Client, filters
import requests,os,csv
from time import time
import time
from datetime import datetime
from pytz import timezone

#create_table()
now=datetime.now()
crtda = now.strftime('%d/%m/%y')
crtda2 = now.strftime('%d-%m-%y')

indexlink = "https://index.mrspidy616.workers.dev"


api_id = 3702208
api_hash = "3ee1acb7c7622166cf06bb38a19698a9"
bot_token = "5030635324:AAEaM9t5WBQHUeUAfJJK4r39h5457YwuD1k"




app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)


async def progress(current, total):
    print(f"{current * 100 / total:.1f}%")



async def main():
   async with app:
     status = await app.send_message(-1001737315050,f"Update Started!\nDate:{crtda}\nIndex Link: {indexlink}/Backup/FullBackups/{crtda2}/")
     filec = open("links.txt","r")
     read=csv.reader(filec)
     for link in read:
        os.system(f"""yt-dlp --downloader aria2c -I 1:10--min-filesize 20M -o '%(title)s.%(ext)s' --download-archive dl.txt -f '(mp4)[height=?480]' --write-thumbnail --embed-metadata """ + link[0])
        for  filename in os.listdir():
               if filename.endswith(".mp4"):
                    await app.send_video(-1001585702100, video=filename,caption=filename.replace(".mp4",""),thumb=filename.replace(".mp4",".jpg"),progress=progress)
                    os.system(f'''rclone --config './rclone.conf' move """{filename.replace('.mp4','.jpg')}"""  'PH_Pics:PH-Pictures/'  ''')
                    os.system(f'''rclone --config "./rclone.conf" move """{filename}""" "Drive:/Backup/{crtda2}" ''')
                    os.system(f"""rclone --config "./rclone.conf" move "Drive:/Backup/{crtda2}" "TD:/Backup/FullBackups/{crtda2}" -vP --drive-server-side-across-configs=true """)
                    try:
                     os.remove(filename)
                    except:
                      print("File Moved I guess!!!")
        await app.send_message(-1001585702100,f"Updated Successfully:\n{link[0]}", reply_to_message_id=status.id)       



app.run(main())
