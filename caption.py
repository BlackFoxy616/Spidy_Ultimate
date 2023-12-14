from pyrogram import Client, filters, enums
import pickle
import os

api_id = 12725757
api_hash = "29e30e8d134c122f3733cc52891edd48"
bot_token = "5634634120:AAF4-pPK3rvRLadLhLCiAVuob7A5ZNuvr7Q"

app = Client("Spidy_CapBot",
             api_id=api_id,
             api_hash=api_hash,
             bot_token=bot_token)


def get_caption():
 try:
    with open("caption.dat", "rb") as f:
      try:
        while True:
          caption = pickle.load(f)
          return caption
      except:
        return None
 except:
    pass

def add_caption(caption):
  with open("caption.dat", "wb+") as f:
    pickle.dump(caption, f)


@app.on_message(filters.command("start") & filters.private)
async def startcommand(bot, message):
  await message.reply_text(
      "Welcome To Spidy Caption Bot\nSend Me Video To Add Caption")


@app.on_message(filters.command("add") & filters.private)
async def addcaption(bot, message):
  if message.from_user.id not in [5443081541, 1702497470]:
    return
  caption = message.text.split(' ', 1)[1]
  if len(caption) == 1:
    await message.reply_text("Please Provide caption")
  else:
    await message.reply_text(f"--Your Caption--:\n{caption}")
    add_caption(caption)


@app.on_message((filters.document | filters.video | filters.audio))
async def main_caption(bot, message):
  caption_text = get_caption()
  if not caption_text:
    await message.reply_text("Please Add Caption First")
  else:
    caption_position = "bottom"
    if (message.document or message.video or message.audio):
      if message.caption:
        file_caption = f"**{message.caption}**"
      else:
        file_caption = ""
        if caption_position == "top":
          await bot.edit_message_caption(chat_id=message.chat.id,
                                         message_id=message.id,
                                         caption=caption_text + "\n" +
                                         file_caption,
                                         parse_mode=enums.ParseMode.MARKDOWN)
        elif caption_position == "bottom":
          await bot.edit_message_caption(chat_id=message.chat.id,
                                         message_id=message.id,
                                         caption=file_caption + "\n" +
                                         caption_text,
                                         parse_mode=enums.ParseMode.MARKDOWN)
        elif caption_position == "nil":
          await bot.edit_message_caption(chat_id=message.chat.id,
                                         message_id=message.id,
                                         caption=caption_text,
                                         parse_mode=enums.ParseMode.MARKDOWN)


print("Bot Started ..!!")
os.system("echo Bot Started")
app.run()
