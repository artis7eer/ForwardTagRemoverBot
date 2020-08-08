#(c)Dan(Artis7eer)[2020]
#Copy With Credits
#

from telegram.ext import Filters,Updater,MessageHandler,CommandHandler
from commands.command_filter import *
from functions.bot_func import *
from caption.set_caption import *
import os

TOKEN=os.environ.get("BOT_TOKEN",None)

updater=Updater(TOKEN,use_context=True)
dp=updater.dispatcher


#/start
dp.add_handler(CommandHandler('start',start_text))
#/help
dp.add_handler(CommandHandler('help',help_text))

#Files
dp.add_handler(MessageHandler(Filters.document,frwrd_file))

#Media
dp.add_handler(MessageHandler(Filters.video,frwrd_media))

#Photos
dp.add_handler(MessageHandler(Filters.photo,frwrd_photo))

#Text & Caption
dp.add_handler(MessageHandler(Filters.text,set_caption))

#Stickers
dp.add_handler(MessageHandler(Filters.sticker,frwrd_sticker))

#Voice
dp.add_handler(MessageHandler(Filters.voice,frwrd_voice))

#Audio
dp.add_handler(MessageHandler(Filters.audio,frwrd_audio))

updater.start_polling()
updater.idle()
