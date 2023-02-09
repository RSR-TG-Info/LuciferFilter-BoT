from pyrogram import filters
from LuciferFilter.luciferfilter import LuciferFilter-BoT
from LuciferFilter.modules.auto_filters import auto_filters, send_for_index
from LuciferFilter.modules.manual_filters import manual_filters
from LuciferFilter.functions.settings import get_settings
from LuciferFilter.database import db


@LuciferFilter-BoT.on_message(filters.group & filters.text & filters.incoming)
async def give_filter(client, message):

    k = await manual_filters(client, message)
    if k == False:
        settings = await get_settings(message.chat.id)
        if settings["autofilter"]:
            await auto_filters(client, message)

@LuciferFilter-BoT.on_message((filters.forwarded | (filters.regex("(https://)?(t\.me/|telegram\.me/|telegram\.dog/)(c/)?(\d+|[a-zA-Z_0-9]+)/(\d+)$")) & filters.text ) & filters.private & filters.incoming)
async def start_for_index(client, message):
    await send_for_index(client, message)
