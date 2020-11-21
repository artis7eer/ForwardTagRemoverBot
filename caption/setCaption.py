# ForwardTagRemoverBot - A Telegram Bot To Hide Forward Source
#Copyright (C) 2020 by Rasak <https://github.com/Artis7eeR>
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



#Function for adding caption
#to media such as audio,image,gifs and files
def setCaption(update,context):
  if update.message.reply_to_message is not None:
   fileCaption= update.message.text
   fileType=update.message.reply_to_message
   if fileType.document!=None:
     update.message.reply_document(
       update.message.reply_to_message.document.file_id,caption=fileCaption)
   elif fileType.video!=None:
     update.message.reply_video(
       update.message.reply_to_message.video.file_id,caption=fileCaption)
   elif fileType.audio!=None:
     update.message.reply_audio(
       update.message.reply_to_message.audio.file_id,caption=fileCaption)
   elif fileType.voice!=None:
     update.message.reply_voice(
       update.message.reply_to_message.voice.file_id,caption=fileCaption)
   elif fileType.photo!=None:
     update.message.reply_photo(update.message.reply_to_message.photo[-1].file_id,caption=fileCaption)
  else:
    update.message.reply_text(update.message.text)
