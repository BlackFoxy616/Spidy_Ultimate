from pyrogram import Client, filters
from time import time
import time
from datetime import datetime
from pytz import timezone
import requests,os,csv
import asyncio
from pyrogram import enums


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




      




@app.on_message(filters.command("updateall"))
async def start_command(client,message):
     cmd = message.text
     channel_id = message.chat.id
     #uph = await message.reply(f"Update Started!\nDate:{crtda}\nIndex Link: {indexlink}/Backup/ForceBackups/{crtda2}/")

     filec = open("links.txt","r")
     read=csv.reader(filec)
     for link in read:
        os.system(f"""yt-dlp --downloader aria2c -I 1:5 -o '%(title)s.%(ext)s' --download-archive dled.txt -f '(mp4)[height=?480]' --write-thumbnail --embed-metadata """ + link[0])
        for  filename in os.listdir():
               if filename.endswith(".mp4"):
                    print(filename)
                    #await app.send_video(-1001737315050, video=filename,caption=filename.replace(".mp4",""),thumb=filename.replace(".mp4",".jpg"),progress=progress)
                    os.system(f'''rclone --config "./rclone.conf" move """{filename}""" "Drive:/Backup/{crtda2}" ''')
                    os.system(f"""rclone --config "./rclone.conf" move "Drive:/Backup/{crtda2}" "TD:/Backup/ForceBackups/{crtda2}" -vP --drive-server-side-across-configs=true """)





@app.on_message(filters.command("update"))
async def start_command(client,message):
     cmd  = message.text
     channel_id = message.chat.id
     if "playlist" in cmd.split()[1]:
        await app.send_message(channel_id,f"Downloading 10 Videos of Playlist:\n{cmd.split()[1]}")
     else:
         await app.send_message(channel_id,f"Downloading:\n{cmd.split()[1]}")
     os.system("""yt-dlp --downloader aria2c --playlist-items 10 -o '%(title)s.%(ext)s' --download-archive dled.txt -f '(mp4)[height=?480]' --write-thumbnail --embed-metadata """ + cmd.split()[1])
     for  filename in os.listdir():
               print(filename)
               if filename.endswith(".mp4") :
                    await app.send_video(-1001737315050, video=filename,caption=filename.replace(".mp4",""),thumb=filename.replace(".mp4",".jpg"),progress=progress)
                    os.system(f'''rclone --config "./rclone.conf" move """{filename}""" "Drive:/Backup/{crtda2}_Videos" ''')
                    os.system(f'''rclone --config "./rclone.conf" move "Drive:/Backup/PH/{crtda2}_Videos" "TD:/Backup/PH/{crtda2}_Videos" -vP --drive-server-side-across-configs=true ''')
            
    
""".replace(".mp4",".jpg")"""



                  

@app.on_message(filters.text & filters.private)
async def start_command(client,message):
    link = message.text
    print(link)

    if "viewkey" not in link :
       status = await app.send_message(message.chat.id,f"Downloading :\n{link.split('/')[-1]}")

    else:
         status = await app.send_message(message.chat.id,f"Downloading:\n{link.split('=')[-1]}")
    # await app.send_message(message.chat.id, f"Downloading {link.split('/')[-1]} Page!!!!") 
    os.system("""yt-dlp --downloader aria2c  --match-filter "duration>90" --max-downloads 10 -N 4 --playlist-random --download-archive dl.txt -o '%(title)s.%(ext)s' -f '(mp4)[height=?720]' --write-thumbnail --embed-metadata """ + link)
    for  filename in os.listdir():
               if filename.endswith(".mp4") :
                    os.system(f'''vcsi """{filename}""" -g 2x6 --metadata-position hidden -o """{filename.replace('.mp4','.png')}""" ''')
                    video = await app.send_video(-1001585702100,video=filename,caption=filename.replace(".mp4",""),thumb=filename.replace(".mp4",".jpg"))
   
                    await app.send_photo(-1001848025191, photo=filename.replace(".mp4",".png"))
                 
                    os.system(f'''rclone --config './rclone.conf' move """{filename.replace('.mp4','.jpg')}"""  'PH_Pics:/Pictures/Custom/{link.split('/')[-1]}'  ''')
                    os.system(f'''rclone --config './rclone.conf' move  """{filename}"""  'Drive:/'  ''')
                    os.system(f"""rclone --config './rclone.conf' move "Drive:/" "TD:/" -vP --delete-empty-src-dirs --drive-server-side-across-configs=true """)
 
    await app.send_message(message.chat.id, "Uploaded Successfully...", reply_to_message_id=status.id) 
    


app.run()
