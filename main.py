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
         await app.delete_messages(message.chat.id,message.id)
         #print(mess)
         cdid= message.chat.id
         button_list =[]
         for each in kidl(mess):
             button_list.append([InlineKeyboardButton(each['title'], callback_data =str(each['title'])+"_"+str(each['id']))]) 
             reply_markup=InlineKeyboardMarkup(button_list)
         await app.send_message(
            cdid,"Select The Required Drama:",reply_markup=reply_markup)

@app.on_callback_query()
async def answer(client, call):
         chat = -1001502224148
         #print(chat)
         await app.delete_messages(chat,call.message.id)
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




          filename = f"{name}-Ep-{int(data.index(url))+1}"
          os.system(f"""yt-dlp --downloader aria2c -o '{filename}.%(ext)s' {st}""")
          #os.system(f'''aria2c '{sub}' -o "{filename}.{sub.split(".")[-1]}" ''')
          for title in os.listdir():
            if filename in title and ("mkv" in title or "mp4" in title):
              os.system(f'''vcsi """{title}""" -g 2x6 --metadata-position hidden -o """{title.replace(title.split(".")[-1],"png")}""" ''')
              await app.send_video(chat,f"{title}",thumb=f"""{title.replace(title.split(".")[-1],"png")}""")
              
            elif filename in title:
                 print(filename)
                 await app.send_document(chat,filename)  



         
            
print("Bot Started")
app.run()


#if len(sub) > 0:
                
                #os.system(f'''ffmpeg -y -i "{title}" -i "{title.replace(title.split(".")[-1],sub.split(".")[-1])}" -c copy -c:s mov_text  "{title.replace(title.split(".")[-1],"en"+title.split(".")[-1])}"''')
 #               os.system(f"rm {title}")
#              os.system(f"""mv "{title.replace(title.split(".")[-1],"en"+title.split(".")[-1])}" "{title}"  """)
                
              
