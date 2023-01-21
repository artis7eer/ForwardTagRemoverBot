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


async def handleCaption(_, bot):
    if _.message.reply_to_message is not None:
        # Get Caption from message 
        file_caption = _.message.text or ""
        await _.message.reply_copy(_.effective_user.id,message_id = _.message.reply_to_message.message_id,caption = file_caption)
