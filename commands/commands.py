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
from config import Config

#Inline Keyboard Button
keyboard = [
[
 InlineKeyboardButton("😌support group😌", url="https://t.me/disneyteamchat")
],
[
 InlineKeyboardButton("👨‍🔧updates channel👨‍🔧",url="https://t.me/disneygrou")
] ,
[
InlineKeyboardButton("👨‍💻developer👨‍💻" ,url="https://t.me/doreamonfans3")
]
]
#The Keyboard On Up👆
reply_markup = InlineKeyboardMarkup(keyboard)

#Send Start Message
def startMessage(update,context):
 try:
  update.message.reply_text(Config.START_TEXT.format(update.message.from_user.full_name,update.message.chat.id),reply_markup=reply_markup,
parse_mode=ParseMode.MARKDOWN)
 except Exception as e:
 	update.message.reply_text(e)

#Help Message
def helpMessage(update,context):
 try:
   update.message.reply_text(Config.HELP_TEXT,reply_markup=reply_markup,parse_mode=ParseMode.MARKDOWN)
 except Exception as e:
  	update.message.reply_text(e)
