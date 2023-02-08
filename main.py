from pyrogram import Client, filters
import requests,os,csv,time


app = Client("my_account")


params = {
    'chat_id': '-1001874651113',
    'text': "/update" ,
}

def selfping():
    time.sleep(5)
    response = requests.get(
    'https://api.telegram.org/bot5703964169:AAEn_l-MSzjMwu9X9hPeyx0ZIjw4Qm0oIvY/sendMessage',
    params=params,
)

             

@app.on_message(filters.command("update"))
async def start_command(client,message):
     channel_id = message.chat.id
     await app.send_message(channel_id,"Updating.....")
     filec = open("links.txt","r")
     read=csv.reader(filec)
     for link in read:
        os.system("""yt-dlp -I 1:1 -o '%(uploader)s/%(title)s.%(ext)s' --download-archive dllinks.txt -f '(480[vcodec~="^((he|a)vc|h26[45])"]+ba) / (480+ba/b)' --embed-thumbnail --embed-metadata """ + link[0])
    
     for  filename in os.listdir():
          if os.path.isdir(filename):
             for names in os.listdir(filename):
               if names.endswith(".mp4") :
                    await app.send_document(channel_id=-1001737315050, document=fliename+'/'+names,caption=names )



 
           
app.run()  # Automatically start() and idle()
selfping()
