from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Updates Channel", url="https://t.me/Private_Bots")
      ],
      [ 
        InlineKeyboardButton(
            "Developer", url="https://t.me/Prime_Hritu")]
    ])  
    helptxt = f"<b> Just send a Youtube url to download it in video or audio format!\n\n ~ @Damantha_Jasinghe </b>"
    await message.reply_text(helptxt, reply_markup=joinButton)
