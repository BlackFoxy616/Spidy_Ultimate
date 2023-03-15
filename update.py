from pyrogram import Client, filters
from time import time
import time
from datetime import datetime
from pytz import timezone
import requests,os,csv
import asyncio


now=datetime.now()
crtda = now.strftime('%d/%m/%y')
crtda2 = now.strftime('%d-%m-%y')




api_id = 3702208
api_hash = "3ee1acb7c7622166cf06bb38a19698a9"
bot_token = "5030635324:AAEaM9t5WBQHUeUAfJJK4r39h5457YwuD1k"




app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)


async def main():
     await app.send_message(-1001737315050, "Bot Started\nSend Any Page Link To Download And Upload To Drive")





@app.on_message(filters.text & filters.private)
async def start_command(client,message):
    link = message.text
    status = await app.send_message(message.chat.id, f"Downloading {link.split('/')[-1]} Page!!!!")      
    os.system("""yt-dlp --downloader aria2c  -I 1:50 --download-archive dl.txt -o '%(title)s.%(ext)s' -f '(mp4)[height=?480]' --write-thumbnail --embed-metadata """ + link)
    for  filename in os.listdir():
               if filename.endswith(".mp4")  :
                    await app.send_photo(message.chat.id, photo=filename.replace(".mp4",".jpg")) 
                    os.system(f'''rclone --config './rclone.conf' move """{filename.replace('.mp4','.jpg')}"""  'PH_Pics:/Pictures/Custom/{link.split('/')[-1]}'  ''')
                    os.system(f'''rclone --config './rclone.conf' move  """{filename}"""  'Drive:/Backup/Custom/{link.split('/')[-1]}'  ''')
                    os.system(f"""rclone --config './rclone.conf' move "Drive:/Backup/Custom/{link.split('/')[-1]}" "TD:Backup/Custom/{link.split('/')[-1]}" -vP --delete-empty-src-dirs --drive-server-side-across-configs=true """)
                    
    await app.send_message(message.chat.id, "Uploaded Successfully...", reply_to_message_id=status.id)      

@app.on_message(filters.command("update"))
async def start_command(client,message):
    link = message.text[8:]
    status = await app.send_message(-1001737315050, f"Downloading {link} Page!!!!")      
    os.system("""yt-dlp --downloader aria2c  -o '%(title)s.%(ext)s' -f b/bv+ba --write-thumbnail --embed-metadata """ + link)
    for  filename in os.listdir():
               if filename.endswith(".mp4")  :
                    await app.send_photo(-1001737315050, photo=filename.replace(".mp4",".jpg")) 
                    os.system(f'''rclone --config './rclone.conf' move """{filename.replace('.mp4','.jpg')}"""  'PH_Pics:/Pictures/Custom/{link.split('/')[-1]}'  ''')
                    os.system(f'''rclone --config './rclone.conf' move  """{filename}"""  'Drive:/'  ''')
                    os.system(f"""rclone --config './rclone.conf' move "Drive:/" "TD:/" -vP --delete-empty-src-dirs --drive-server-side-across-configs=true """)
                    
    await app.send_message(-1001737315050, "Uploaded Successfully...", reply_to_message_id=status.id)      




app.run()
