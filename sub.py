import requests


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
