from spdatabase import *
from pyrogram import Client, filters
import requests,os,csv
from time import time
import time
from datetime import datetime
from pytz import timezone

#create_table()
now=datetime.now()
crtda = now.strftime('%y/%m/%d')
crtda2 = now.strftime('%y-%m-%d')

indexlink = "https://index.mrspidy616.workers.dev/"


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


@app.on_message(filters.text & filters.private)
async def echo(client, message):
    link = message.text
    os.system("""./yt-dlp --downloader aria2c -o '%(title)s.%(ext)s' -f '(mp4)[height=?240]' --write-thumbnail --embed-metadata """ + link)
    for  filename in os.listdir():
               print(filename)
               if filename.endswith(".mp4")  :
                    await app.send_video(-1001737315050, video=filename,caption=filename,thumb=filename,progress=progress)
                    os.system(f"""rclone --config "./rclone.conf" move '{filename}' "Drive:/{crtda2}_Videos/" """)
                    os.system(f"""rclone --config "./rclone.conf" move "Drive:/" "TD:/PH/" -vP --drive-server-side-across-configs=true """)






@app.on_message(filters.command("updateall"))
async def start_command(client,message):
     cmd = message.text
     channel_id = message.chat.id
     uph = await message.reply("Updating.....")
     filec = open("links.txt","r")
     read=csv.reader(filec)
     for link in read:
        os.system(f"""./yt-dlp --downloader aria2c -I 1:{cmd.split()[1]} -o '%(title)s.%(ext)s' --download-archive dllinks.txt -f '(mp4)[height=?240]' --write-thumbnail --embed-metadata """ + link[0])
        #await app.edit_message_text(channel_id, uph.msg.id,"Uploading.....")
        
        for  filename in os.listdir():
               if filename.endswith(".mp4"):
                    print(filename)
                    await app.send_video(-1001737315050, video=filename,caption=filename.replace(".mp4",""),thumb=filename.replace(".mp4",".jpg"),progress=progress)
                    os.system(f"""rclone --config "./rclone.conf" move '{filename}' "Drive:/{crtda2}/" """)
                    os.system(f"""rclone --config "./rclone.conf" move "Drive:/" "TD:/Backup/ForceBackups/" -vP --drive-server-side-across-configs=true """)





@app.on_message(filters.command("update"))
async def start_command(client,message):
     cmd  = message.text
     channel_id = message.chat.id
     await app.send_message(channel_id,"Updating.....\n"\
+cmd.split()[1])
     os.system("""./yt-dlp --downloader aria2c -I 10 -o '%(title)s.%(ext)s' --download-archive dllinks.txt -f '(mp4)[height=?240]' --write-thumbnail --embed-metadata """ + cmd.split()[1])
     for  filename in os.listdir():
               print(filename)
               if filename.endswith(".mp4") :
                    await app.send_video(-1001737315050, video=filename,caption=filename.replace(".mp4",""),thumb=filename.replace(".mp4",".jpg"),progress=progress)
                    os.system(f"""rclone --config "./rclone.conf" move '{filename}' "Drive:{crtda2}_Videos/" """)
                    os.system(f"""rclone --config "./rclone.conf" move "Drive:/" "TD:/PH/" -vP --drive-server-side-across-configs=true """)
               
    

async def main():
   async with app:
     db = read_db()
     loop = True
     p = 10
     link = "https://www.pornhub.com/playlist/263313231"
     await app.send_message(-1001737315050,f"Update Started!\nDate:{crtda}\nIndex Link: {indexlink}/Backup/{crtda2}")
     #await app.send_message(-1001373543632,f"Update Started!\nDate:{crtda}\nIndex Link: {indexlink}/Backup/{crtda2}")
     while loop:
       os.system(f"""./yt-dlp --downloader aria2c -I {p} --download-archive dled.txt -o '%(title)s.%(ext)s' -f '(mp4)[height=?480]' --write-thumbnail --embed-metadata """ + link)
       
       for  filename in os.listdir():
        if filename.endswith(".mp4"):
         for link in db:
          if filename not in link:
            insert_db(filename)
            #await app.send_video(-1001737315050, video=filename,caption=filename.replace(".mp4",""),thumb=filename.replace(".mp4",".jpg"),progress=progress)
            await app.send_photo(-1001737315050, photo=filename.replace(".mp4",".jpg"),caption=f"{indexlink}/{crtda}/{filename}")                    
            os.system(f"""rclone --config "./rclone.conf" move '{filename}' "Drive:{crtda2}/" """)
            os.system(f"""rclone --config "./rclone.conf" move "Drive:" "TD:Backup/" -vP --drive-server-side-across-configs=true """)
            try:
              os.remove(filename)
            except:
               print("File Moved I guess!!!")
          count+=1
     await app.stop()

 
           
app.run(main())  # Automatically start() and idle()
