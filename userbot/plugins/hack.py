"""Emoji
Available Commands:
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "hack":

        await event.edit(input_str)

        animation_chars = [
        
            
		    "`Connecting to Dropbox to store the files...`",
			"`Searching the Telegram-Server you are located on...`",
			"`Breaking the encryption and performing SSL-Handshake...`",
			"`You are currently located on the Telegram-Server 12 #Russia`",
			"`This TG-Server is based on Ubuntu 16.04 Cosmic Cuttlefish.`",
            "`Target Selected.`",
            "`Transferring Data 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Transferring Data 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Transferring Data 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Transferring Data 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Transferring Data 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Transferring Data 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Transferring Data 84%\n█████████████████████▒▒▒▒ `",
            "`Transferring Data 100%\n█████████HACKED███████████ `",
            "`Targeted Account Hacked...\n\nI also Logged your IP"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])
