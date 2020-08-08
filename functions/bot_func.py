#Send Video
def frwrd_media(u,c):
  u.message.reply_video(u.message.video.file_id)
 
#Send File
def frwrd_file(u,c): u.message.reply_document(u.message.document.file_id)

#Send Photo
def frwrd_photo(u,c):
  u.message.reply_photo(u.message.photo[-1].file_id)

#Send Text
def frwrd_text(u,c):
  u.message.reply_text(u.message.text)

#Send Sticker
def frwrd_sticker(u,c):
  u.message.reply_sticker(u.message.sticker.file_id)

#Send Voice
def frwrd_voice(u,c):
  u.message.reply_voice(u.message.voice.file_id)

#Send Audio
def frwrd_audio(u,c):
  u.message.reply_audio(u.message.audio.file_id)
  
