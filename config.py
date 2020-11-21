import os


class Config:
	
 TOKEN=os.environ.get("BOT_TOKEN",None)
 SOURCE="https://github.com/Artis7eeR/ForwardTagRemoverBot"
 START_TEXT="Hi [{}](tg://user?id={})\nI am A Forward Tag remover Bot.Send /help To Know What I Can Do \n ©Artis7eeR"
 HELP_TEXT="Forward Me A File,Video,Audio,Photo or Anything And \nI will Send You the File Back\n\n`How to Set Caption?`\nReply Caption to a File,Photo,Audio,Media"
	