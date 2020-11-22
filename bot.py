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


from telegram.ext import Filters,Updater,MessageHandler,CommandHandler
from commands.commands import *
from functions.functions import *
from caption.setCaption import setCaption
import os
from config import Config

updater=Updater(Config.TOKEN,use_context=True)
dp=updater.dispatcher


#/start
dp.add_handler(CommandHandler('start',startMessage))
#/help
dp.add_handler(CommandHandler('help',helpMessage))

#Files
dp.add_handler(MessageHandler(Filters.document,sendFile))

#Media
dp.add_handler(MessageHandler(Filters.video,sendMedia))

#Photos
dp.add_handler(MessageHandler(Filters.photo,sendPhoto))

#Text & Caption
dp.add_handler(MessageHandler(Filters.text,setCaption))

#Stickers
dp.add_handler(MessageHandler(Filters.sticker,sendSticker))

#Voice
dp.add_handler(MessageHandler(Filters.voice,sendVoice))

#Audio
dp.add_handler(MessageHandler(Filters.audio,sendAudio))

updater.start_polling()
updater.idle()
