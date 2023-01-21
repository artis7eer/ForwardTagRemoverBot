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

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from config import Config

keyboard = [
    [
        InlineKeyboardButton("Source Code", url=Config.SOURCE)
    ],
    [
        InlineKeyboardButton("How To Create A Bot Like Me",
                             url="https://youtu.be/swg6un2N4Fk")
    ]
]

reply_markup = InlineKeyboardMarkup(keyboard)


async def startMessage(_, bot):
    await _.message.reply_text(Config.START_TEXT.format(_.message.from_user.full_name, _.message.chat.id), reply_markup=reply_markup,
                               parse_mode=ParseMode.MARKDOWN)


async def helpMessage(_, bot):
    await _.message.reply_text(Config.HELP_TEXT, reply_markup=reply_markup, parse_mode=ParseMode.MARKDOWN)


async def handleMessage(_, bot):
    
    await _.message.copy(_.effective_user.id)
