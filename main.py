from pyrogram import Client,filters
from sub import *
import os
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                            InlineKeyboardButton)

# Create a client using your bot token
api_id = 3702208
api_hash = "3ee1acb7c7622166cf06bb38a19698a9"
bot_token = "5300188722:AAFlruACp00Hv2ZD1RPjE9P0FahI52swqpU"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)




@app.on_message(filters.command("kh"))
async def start_command(client,message):
         mess= message.text[4:]
         print(mess)
         cdid= message.chat.id
         button_list =[]
         for each in kidl(mess):
             button_list.append([InlineKeyboardButton(each['title'], callback_data =str(each['title'])+"_"+str(each['id']))]) 
             reply_markup=InlineKeyboardMarkup(button_list)
         await app.send_message(
            cdid,"Select The Required Drama:",reply_markup=reply_markup)

@app.on_callback_query()
async def answer(client, call):
         data = ddd(call.data.split("_")[1])
         for url in data:
          name = call.data.split("_")[0]
          id = str(url['id'])
          URL = base_url + "DramaList/Episode/"+id+".png?err=false&ts=&time="
          sub = get_subtitles(id)
          if len(sub) > 0:
               sub = get_subtitles(id)[0]
          sturl= requests.get(URL).json()['Video']
          if sturl.startswith("http") or sturl.startswith("https"):
                   st=sturl
          else:
               st = "http:"+sturl
    
          #await app.send_message(call.message.chat.id,st)
          title = f"{name}-Ep-{int(data.index(url))+1}old"
          os.system(f"yt-dlp --downloader aria2c -o '{title}.%(ext)s'")
          os.system(f'''aria2c '{sub}' -o "{title}.{sub.split(".")[-1]}" ''')
          for file in os.listdir():
              if title in file and not (file.endswith("srt")) :
                 os.system(f'''ffmpeg -i {file} -i {file.replace(file.split(".")[-1],"srt")} -c copy -c:s mov_text language=eng {file.replace("old","")}''')
                 os.system(f'''vcsi """{file}""" -g 2x6 --metadata-position hidden -o """{file.replace(file.split(".")[-1],'.png')}""" ''')
                 await send_video(call.chat.id,file.replace("old",""))
                 await app.send_photo(call.chat.id, photo=file.replace(file.split(".")[-1],".png"))
                 try:
                  os.remove(file)
                 except:
                    pass
                 
print("Bot Started")
app.run()


