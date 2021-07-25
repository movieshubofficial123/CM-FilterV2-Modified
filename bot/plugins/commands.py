#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG
# Modified by @Leos_tg

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation # hmmm
from bot.database import Database # hmmm
 # removed ForceSub
db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption =f"<code>{file_name}</code>\n \n<b>T̷h̷a̷n̷k̷ ̷y̷o̷u̷ ̷f̷o̷r̷ ̷U̷s̷i̷n̷g̷ ̷T̷h̷i̷s̷ ꪖᡶꪑꪉ Version 2.9\n ꪖᡶꪑꪉ =Any Time Movie Bot😜🤣</b>",
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'S̵̶̮̬͖̄͑͟h̶̯̰̝̻̿̓͢ă̶̸̝ͦ͊̿͋͞r̶̷̲͍̭͐̾̀͟ę̷̵̧̖̫̗̆̊ N̰̜͉͔ͬ̽͢ȍ̸̢̢̮͚̐̚ẅ̷̷̢̟͇͈̒', url="https://t.me/share/url?url=%20https://t.me/leos_tg"
                                )
                        ]
                    ]
                )
            )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'Developers', url="https://t.me/share/url?url=%20https://t.me/leos_tg"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'S̵̶̮̬͖̄͑͟h̶̯̰̝̻̿̓͢ă̶̸̝ͦ͊̿͋͞r̶̷̲͍̭͐̾̀͟ę̷̵̧̖̫̗̆̊ N̰̜͉͔ͬ̽͢ȍ̸̢̢̮͚̐̚ẅ̷̷̢̟͇͈̒', url="https://t.me/share/url?url=%20https://t.me/leos_tg"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('ᗰ⊙ᕲ♗Ϝ♗€ᕲ ♭⚧', url='https://t.me/leos_tg'),
        InlineKeyboardButton('𝕄𝕆𝕍𝕀𝔼 𝔾ℝ𝕆𝕌ℙ', url ='https://t.me/XeQuIsT')
    ],[
        InlineKeyboardButton('Questions?😏', url='https://www.google.com')
    ],[
        InlineKeyboardButton('🅷🅴🅻🅿', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_photo(
        chat_id=update.chat.id,
        photo = 'https://telegra.ph/file/e76d40ed899c2abd87209.jpg',
        caption=Translation.START_TEXT.format(
                update.from_user.first_name),
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('B̟̈́̆̐̄̚͜ă̶̸̝ͦ͊̿͋͞c̷̹͖͋́̃k̶̸͙̭̹͆͟û̶͙̽̿͆̈p̶̸̨̺͊̍̒̓̀ ⚡', callback_data='start'),
        InlineKeyboardButton('A҉҉̦̣̤͔̟̩̋̿̏ͦ̈́̍͟͠b҉͙̺̻̥̅̎͋̕͜͝͡͞͠o҉̢̡̲͇̌͗̀͢͝u̶͖̖͆̊̈́͡͡t҉̷҉̢͖͔̹͛̌͊͘͜͢͠͡͡ 🧞', callback_data='about')
    ],[
        InlineKeyboardButton('🌜☾↳⊙∫€', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('B̵̴҉̞̠̘̩͍̱́͊͗͜͠͠͠͠a҉͖̟̜̞̂̃̑̽͢͢͠͡c̷̶҉̵̢͚̣̻̲̬͑̑͛͐̀͜͜͜͝͡͝͠k҉̴̶̬͈̫̹͖̾̎ͭ́̍̐͜͜͝͠ ⚡', callback_data='start'),
        InlineKeyboardButton('☾↳⊙∫€  ', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
