"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio

from userbot import ALIVE_NAME

@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 18)

    input_str = event.pattern_match.group(1)
    
    DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Anonymous"

    if input_str == "call":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To Telegram Headquarters...`",
            "`Call Connected.`",
            "`Telegram: Hello This is Telegram HQ. Who is this?`",
            "`Me: Yo, this is` @ShityBrainOfficial ,`Please Connect me to any hore which sends nudes`",
            "`User Authorised.`",
            "`Calling Marie, your personal Nude`  `At +916969696969`",
            "`Private  Call Connected...`",
            "`Marie: Hey {DEFAULTUSER}, do u wanna see my nudes? It's free!`",    
            "`Me: Yeah, pls show them`",
            "`Marie: Okay, lemme clean my pussy... Give me 2 Minutes",
            "`Me: OMG yes!! Then take a few hot shots for me :D\nI will donate your great work with something good then ;D`",
            "`Marie: Okay, be ready..`",
            "`Me: Alright. I get ready2cum right now.`",
            "`Marie: Are you on the Phone right now? I wanna start a secret Chat to send my Nudes`",
            "`Me: Yeah, just search me on the Telegram search. It's me, {DEFAULTUSER}`",
            "`Marie: Okay, lemme go to the Toilet.. Take a sec...`",
            "`Me: Sure. \nSee u on TG :-)`",
            "`Private Call Disconnected.`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 18])
