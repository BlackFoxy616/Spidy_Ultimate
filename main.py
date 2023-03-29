#from spdatabase import *
from pyrogram import Client, filters
import requests,os,csv
from time import time
import time
from datetime import datetime
from pytz import timezone
from pyrogram import enums

#create_table()

api_id = 3702208
api_hash = "3ee1acb7c7622166cf06bb38a19698a9"
bot_token = "5030635324:AAEaM9t5WBQHUeUAfJJK4r39h5457YwuD1k"




app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)


file = open("ids.csv","a+")
write = csv.writer(file)
read = csv.reader(file)



def stats(status,crtda,total):
    stats = f'<b>├  Status: </b>{status}\n'\
            f'<b>├  Uploaded Videos: </b>{total}\n'\
            f'<b>╰ Updated Time: </b>{crtda}\n\n'
    return stats


async def progress(current, total):
    print(f"{current * 100 / total:.1f}%")

async def main():
   async with app:
     count = 0
     now=datetime.now()
     crtda = now.strftime('%m/%d %I:%M:%S %p')
     await client.edit_message_text(-1001984459303,1,text=stats("Active",crtda,"Uploading..")[0])
     link = "https://www.pornhub.com/playlist/263313231"
     #status = await app.send_message(-1001737315050,f"Update Started!\nDate:{crtda}")
     #await app.send_message(-1001373543632,f"Update Started!\nDate:{crtda}\nIndex Link: {indexlink}/Backup/{crtda2}/")
     os.system(f"""yt-dlp   --downloader aria2c -I 400:600 --download-archive dled.txt  -o '%(title)s.%(ext)s' -f '(mp4)[height=?480]' --write-thumbnail --embed-metadata """ + link)
     #os.system(f"""./yt-dlp   --downloader aria2c -I 1:1 -o '%(title)s.%(ext)s' -f '(mp4)[height=?720]' --write-thumbnail --embed-metadata """ + link)
     for  filename in os.listdir():
      if filename.endswith(".mp4"):
            count+=1
            os.system(f'''vcsi """{filename}""" -g 2x6 --metadata-position hidden -o """{filename.replace('.mp4','.png')}""" ''')
            #os.system(f'''ffmpeg -i """{filename}""" -vcodec libx264 -crf 18 -o """{fliename.replace('.mp4','H.264.mp4')}""" ''')
            video = await app.send_video(-1001737315050, video=filename,caption=filename.replace(".mp4",""),thumb=filename.replace(".mp4",".jpg"),progress=progress)
            vid = f"https://t.me/c/1737315050/{video.id}"
            pic = await app.send_photo(-1001945634929, photo=filename.replace(".mp4",".png"),caption=vid)   
            os.system(f'''rclone --config './rclone.conf' move """{filename.replace('.mp4','.jpg')}"""  'PH_Pics:/Pictures/'  ''')
            os.system(f'''rclone --config './rclone.conf' move """{filename.replace('.mp4','.png')}"""  'PH_Pics:/Pictures/Caps/'  ''')
            os.system(f'''rclone --config './rclone.conf' move  """{filename.replace('.mp4','.jpg')}"""  'Drive:/Pictures/'  ''')
            os.system(f'''rclone --config './rclone.conf' move  """{filename.replace('.mp4','.png')}"""  'Drive:/Pictures/Caps'  ''')
            #os.system(f'''rclone --config './rclone.conf' move """{filename}"""  'PH_Pics:/Pictures/'  ''')
            #os.system(f'''rclone --config './rclone.conf' move  """{filename}"""  'Drive:/Backup/'  ''')
            #os.system(f"""rclone --config './rclone.conf' move "Drive:/Backup/" "TD:Backup/" -vP --delete-empty-src-dirs --drive-server-side-across-configs=true """)
            try:
              os.remove(filename.replace(".mp4",".jpg"))
              os.remove(filename.replace(".mp4",".png"))
              os.remove(filename)
            except:
               print("File Moved I guess!!!")        
     #await app.send_message(-1001737315050,f"Update Completed Successfully...", reply_to_message_id=status.id)
     await client.edit_message_text(-1001984459303,1,text=stats("Offline",crtda,count)[0])

app.run(main())
