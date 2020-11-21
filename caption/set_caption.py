# ForwardTagRemoverBot - A Telegram Bot To Hide Forward Source
#Copyright (C) 2020 by Rasak < https://github.com/Artis7eeR >
#ForwardTagRemoverBot is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#ForwardTagRemoverBot is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.



#Reply to media file or Document
def set_caption(u,c):
 if u.message.reply_to_message is not None:
   file_caption= u.message.text
   file_type=f"{u.message.reply_to_message}"
   if "document" in file_type:
    u.message.reply_document(u.message.reply_to_message.document.file_id,
  caption=file_caption)
   elif "voice" in file_type:  
    u.message.reply_voice(u.message.reply_to_message.voice.file_id,
    caption=file_caption)
   elif "video" in file_type:
    u.message.reply_video(u.message.reply_to_message.video.file_id,
    caption=file_caption)
   elif "photo" in file_type:
    u.message.reply_photo(u.message.reply_to_message.photo[-1].file_id,
    caption=file_caption)
 else:
    u.message.reply_text(u.message.text)
  
