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

from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ParseMode
from config.Config import SOURCE,START_TEXT,HELP_TEXT

source="https://github.com/Artis7eeR/ForwardTagRemoverBot"
START_TEXT="Hi [{}](tg://user?id={})\nI am A Forward Tag remover Bot.Send /help To Know What I Can Do \n ©Artis7eeR"
HELP_TEXT="Forward Me A File,Video,Audio,Photo or Anything And \nI will Send You the File Back\n\n`How to Set Caption?`\nReply Caption to a File,Photo,Audio,Media"

#Inline Keyboard Button
keyboard = [
[
 InlineKeyboardButton("Source Code", url=source)
],
[
 InlineKeyboardButton("How To Create A Bot Like Me",url="https://youtu.be/swg6un2N4Fk")
]
]
reply_markup = InlineKeyboardMarkup(keyboard)

#Send Start Message
def startMessage(update,context):
 try:
  update.message.reply_text(START_TEXT.format(update.message.from_user.full_name,update.message.chat.id),reply_markup=reply_markup,
parse_mode=ParseMode.MARKDOWN)
 except Exception as e:
 	update.message.reply_text(e)

#Help Message
def helpMessage(update,context):
 try:
   update.message.reply_text(HELP_TEXT,reply_markup=reply_markup,parse_mode=ParseMode.MARKDOWN)
  except Exception as e:
  	update.message.reply_text(e)
