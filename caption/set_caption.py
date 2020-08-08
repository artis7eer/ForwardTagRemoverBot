#Reply to media file or Document
def set_caption(u,c):
  if u.message.reply_to_message is not None:
   file_caption= u.message.text
  file_type=f"{u.message.reply_to_message}"
  if "document" in file_type:
   u.message.reply_document(u.message.reply_to_message.document.file_id,
  caption=file_caption)
  elif "video" in file_type:
    u.message.reply_video(u.message.reply_to_message.video.file_id,
    caption=file_caption)
  elif '"voice":' in file_type:
    u.message.reply_voice(u.message.reply_to_message.voice.file_id,
    caption=file_caption)
  elif '"audio":' in file_type:
    u.message.reply_audio(u.message.reply_to_message.audio.file_id,
    caption=file_caption)
  elif "photo" in file_type:
    u.message.reply_photo(u.message.reply_to_message.photo[-1].file_id,
    caption=file_caption)
  else:
  	u.message.reply_text(u.message.text)
