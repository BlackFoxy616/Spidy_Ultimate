from pyrogram import Client, filters
import requests,os,csv,time

api_id = 3702208
api_hash = "3ee1acb7c7622166cf06bb38a19698a9"
bot_token = "5102219510:AAHGCySOBy1AIYCnJiJeArX5lmOJ5nE7dh8"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)


@app.on_message(filters.command("update"))
async def start_command(client,message):
     channel_id = message.chat.id
     await app.send_message(channel_id,"Updating.....")
     filec = open("links.txt","r")
     read=csv.reader(filec)
     for link in read:
        os.system("""yt-dlp --downloader aria2c -I 1:1 -o '%(uploader)s/%(title)s.%(ext)s' --download-archive dllinks.txt -f '(480[vcodec~="^((he|a)vc|h26[45])"]+ba) / (480+ba/b)' --embed-thumbnail --embed-metadata """ + link[0])
    
     for  filename in os.listdir():
          if os.path.isdir(filename):
             for names in os.listdir(filename):
               if names.endswith(".mp4") :
                    await app.send_document(-1001737315050, document=filename+'/'+names,caption=names )



 
           
app.run()  # Automatically start() and idle()
