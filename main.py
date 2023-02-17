from pyrogram import Client, filters
import requests,os,csv,time

api_id = 3702208
api_hash = "3ee1acb7c7622166cf06bb38a19698a9"
bot_token = "5300188722:AAFlruACp00Hv2ZD1RPjE9P0FahI52swqpU"

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
     channel_id = message.chat.id
     await app.send_message(channel_id,"Updating.....")
     filec = open("links.txt","r")
     read=csv.reader(filec)

     for link in read:
        os.system("""yt-dlp --downloader aria2c --playlist-items 1 -o '%(title)s.%(ext)s' --download-archive dllinks.txt -f '(240+ba/b)' --embed-thumbnail --embed-metadata """ + link[0])
     for  filename in os.listdir():
               print(filename)
               if filename.endswith(".mp4") :
                    await app.send_document(-1001737315050, document=filename,caption=filename,progress=progress)



 
           
app.run()  # Automatically start() and idle()
