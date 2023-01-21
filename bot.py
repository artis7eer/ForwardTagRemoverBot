# ForwardTagRemoverBot - A Telegram Bot To Hide Forward Source
# Copyright (C) 2023 by Abdul Razaq <https://github.com/Artis7eeR>
# ForwardTagRemoverBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# ForwardTagRemoverBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import logging
from telegram.ext import (
    filters,
    ApplicationBuilder,
    CommandHandler,
    MessageHandler
)

from plugins.__main__ import *
from config import Config

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def main():
    bot = ApplicationBuilder().token(Config.BOT_TOKEN).build()
    bot.add_handler(CommandHandler('start', startMessage))
    bot.add_handler(CommandHandler('help', helpMessage))
    bot.add_handler(MessageHandler(filters.REPLY, handleCaption))
    bot.add_handler(MessageHandler(
        filters.ALL & ~filters.COMMAND, handleMessage))
    bot.run_polling()


if __name__ == '__main__':
    main()
