import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "WoW, u don't even know how to set a Name on Heroku..."

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.client.send_message(
            alive.chat_id,
            f"Python Version: 3.7.4\nHeroku-Dyno: Premium-2\n\nThis lit shit was made by [ShityBrain](https://t.me/ShityBrainOfficial)\nI currently run on {DEFAULTUSER}",
            file="https://i.imgur.com/T60vNl1.jpg"
        )
    await alive.delete()
