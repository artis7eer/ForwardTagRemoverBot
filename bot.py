from telegram.ext import Filters,Updater,MessageHandler,CommandHandler
import os

#Bot Token
#Needed To Interact With Bot
START_TEXT=os.environ.get("StartMsg","Hi I am A Forward Tag remover Bot \n Find My Source On Here {}")
HELP_TEXT=os.environ.get("HelpMsg","Forward Me A File And I Will Remove The Files  \n Tag Find My Source On Here {}")
token=os.environ.get("BOT_TOKEN",None)
source="https://github.com/Artis7eeR/My-forward-Tag-Remover-Bot/bot.py"


#Start Message
def start_text(u,c):
	u.message.reply_text(START_TEXT.format(source))

#Help Message
def help_text(u,c):
	u.message.reply_text(HELP_TEXT.format(source))

#Send Document From User
def frwrd_file(u,c):
	u.message.reply_document(u.message.document.file_id)

#Send Video From User
def frwrd_media(u,c):
	u.message.reply_video(u.message.video.file_id)

#Send photo From User
def frwrd_photo(u,c):
	u.message.reply_photo(u.message.photo[-1].file_id)

#Send text From User
def frwrd_text(u,c):
	u.message.reply_text(u.message.text)

#Send Sticker From User
def frwrd_sticker(u,c):
	u.message.reply_sticker(u.message.sticker.file_id)

#Send Sticker From User
def frwrd_voice(u,c):
	u.message.reply_voice(u.message.voice.file_id)

updater=Updater(token,use_context=True)

dp=updater.dispatcher

#Filtering Commands

dp.add_handler(CommandHandler('start',start_text))


dp.add_handler(CommandHandler('help',help_text))



#Filtering Files
dp.add_handler(MessageHandler(Filters.document,frwrd_file))

#Filtering Media
dp.add_handler(MessageHandler(Filters.video,frwrd_media))

#Filtering Photos
dp.add_handler(MessageHandler(Filters.photo,frwrd_photo))

#Filtering Text
dp.add_handler(MessageHandler(Filters.text,frwrd_text))

#Filtering Stickers
dp.add_handler(MessageHandler(Filters.sticker,frwrd_sticker))

#Filtering Voice
dp.add_handler(MessageHandler(Filters.voice,frwrd_voice))

updater.start_polling()
updater.idle()
