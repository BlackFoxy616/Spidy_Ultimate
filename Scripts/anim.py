from pyrogram import Client,filters
import os
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,InlineKeyboardButton)
import requests
import asyncio


base_url = "https://kisskh.co/api/"

def kissytdl(link):
   options = {
  "quiet":    True,
  "simulate": True,
  "forceurl": True,
  }
   with yt_dlp.YoutubeDL(options) as ytdl:
    ytdl.download(link)
       

def build_menu(buttons,n_cols,header_buttons=None,footer_buttons=None):
  menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
  if header_buttons:
    menu.insert(0, header_buttons)
  if footer_buttons:
    menu.append(footer_buttons)
  return menu
 


def kidl(query):
    URL = base_url + "DramaList/Search?q=" + query
    ks = requests.get(url=URL)
    data1 = ks.json()
    return data1



def did(query):
     json = kidl(query)
     for i in range(len(json)):
       title=json[i]['title']
       print(i+1,title)
     c = int(input("Select Wanted Drama:"))
     id=json[c-1]['id']
     return id

def dd(query):
   id = str(did(query))
   url = base_url + "DramaList/Drama/" +id
   data = requests.get(url)
   json= data.json()['episodes'][::-1]
   return json

def ddd(id):
   url = base_url + "DramaList/Drama/" +id
   data = requests.get(url)
   json= data.json()['episodes'][::-1]
   return json

def steam_url_json(query):
   ids = []
   json = dd(query)
   print (json)
   print(len(json))
   return
    
def  steam_url(query):
    for i in dd(query):
     id = str(i['id'])
     url = base_url + "DramaList/Episode/"+id+".png?err=false&ts=&time="
     steam_json= requests.get(url).json()
     print("https:" + steam_json['Video'])

def  steam_url(id):
    for i in ddd(id):
     id = str(i['id'])
     url = base_url + "DramaList/Episode/"+id+".png?err=false&ts=&time="
     steam_url= "https:" + requests.get(url).json()
    return steam_url

def kissdl(query):
  kissytdl(steam_url(query))






def get_subtitles(episode_id ):
        subtitle_api_url = f"{base_url}Sub/{episode_id}"
        response = requests.get(subtitle_api_url)
        res = response.json()
        subs =[]
        for sub in res:
           if "en" in sub["land"]:
                subs.append(sub["src"])
        return subs
                
async def read_stderr(start, msg, process):
    async for line in readlines(process.stderr):
            line = line.decode('utf-8')
            progress = parse_progress(line)
            if progress:
                #Progress bar logic
                now = time.time()
                diff = start-now
                text = 'PROGRESS\n'
                text += 'Size : {}\n'.format(progress['size'])
                text += 'Time : {}\n'.format(progress['time'])
                text += 'Speed : {}\n'.format(progress['speed'])

                if round(diff % 5)==0:
                    try:
                        await msg.edit( text )
                    except:
                        pass   

async def softmux_vid(vid_filename, sub_filename, msg):

    start = time.time()
    vid = vid_filename
    sub = sub_filename

    out_file = '.'.join(vid_filename.split('.')[:-1])
    output = out_file+'1.mkv'
    out_location = output
    sub_ext = sub_filename.split('.').pop()
    command = [
            'ffmpeg','-hide_banner',
            '-i',vid,
            '-i',sub,
            '-map','1:0','-map','0',
            '-disposition:s:0','default',
            '-c:v','copy',
            '-c:a','copy',
            '-c:s',sub_ext,
            '-y',out_location
            ]

    process = await asyncio.create_subprocess_exec(
            *command,
            # stdout must a pipe to be accessible as process.stdout
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            )

    # https://github.com/jonghwanhyeon/python-ffmpeg/blob/ccfbba93c46dc0d2cafc1e40ecb71ebf3b5587d2/ffmpeg/ffmpeg.py#L114
    
    await asyncio.wait([
            read_stderr(start,msg, process),
            process.wait(),
        ])
    
    if process.returncode == 0:
        await msg.edit('Muxing  Completed Successfully!\n\nTime taken : {} seconds'.format(round(start-time.time())))
    else:
        await msg.edit('An Error occured while Muxing!')
        return False
    time.sleep(2)
    return output

#search = input('Enter A Drama Name:')
#steam_url("Wednesday")
"""
key = []
info = kidl("Demon Slayer")
for i in range(len(info)):
     title = info[i]['title']
     btn = "InlineKeyboardButton(" + title + ",callback_data="+str(i)+")"
     key.append([btn])
print(key)

"""


# Create a client using your bot token
api_id = 3702208
api_hash = "3ee1acb7c7622166cf06bb38a19698a9"
bot_token = "6949923423:AAF6CnXxgA8I-xI_Wao-tTLAnVORxKiBsBw"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)




@app.on_message(filters.command("get"))
async def start_command(client,message):
         mess= message.text[4:]
         await app.delete_messages(message.chat.id,message.id)
         #print(mess)
         cdid= message.chat.id
         button_list =[]
         temp=[]
         for each in kidl(mess):
             if len(temp) ==2:
                button_list.append(temp)
                temp =[]
             temp.append(InlineKeyboardButton(each['title'], callback_data =f"{mess}_"+str(each['id'])))
             
         reply_markup=InlineKeyboardMarkup(button_list)
         await app.send_message(
            cdid,"Select The Required Drama:",reply_markup=reply_markup)

@app.on_callback_query()
async def answer(client, call):
      try:
         mess = call.data.split("_")[0]
         did = int(call.data.split("_")[1])
         for i in kidl(mess):
            if i["id"] == did:
               print(i["title"])
               name = i["title"]
         chat = -1001502224148
         #print(chat)
         await app.delete_messages(chat,call.message.id)
         data = ddd(call.data.split("_")[1])
         for url in data:
          #name = call.data.split("_")[0]
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
              os.system(f'''vcsi """{title}""" -g 2x2 --metadata-position hidden -o """{title.replace(title.split(".")[-1],"png")}""" ''')
              await app.send_video(chat,f"{title}",thumb=f"""{title.replace(title.split(".")[-1],"png")}""", caption=title,supports_streaming=True)
              
            elif filename in title:
                 print(filename)
                 await app.send_document(chat,filename)  
      except:
          pass


         
            
print("Bot Started")
app.run()


#if len(sub) > 0:
                
                #os.system(f'''ffmpeg -y -i "{title}" -i "{title.replace(title.split(".")[-1],sub.split(".")[-1])}" -c copy -c:s mov_text  "{title.replace(title.split(".")[-1],"en"+title.split(".")[-1])}"''')
 #               os.system(f"rm {title}")
#              os.system(f"""mv "{title.replace(title.split(".")[-1],"en"+title.split(".")[-1])}" "{title}"  """)
                
              
