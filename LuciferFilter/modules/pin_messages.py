from LuciferFilter.luciferfilter import LuciferFilter_BoT
from LuciferFilter.functions.handlers import Pin

@LuciferFilter_BoT.on_message(Pin.a)
async def pin(_, message):
    if not message.reply_to_message:
        return
    args = message.text.lower().split()
    notify = not any(arg in args for arg in ('loud', 'notify'))
    await message.reply_to_message.pin(disable_notification=notify)

@LuciferFilter_BoT.on_message(Pin.b)
async def unpin(_, message):
    if not message.reply_to_message:
        return
    await message.reply_to_message.unpin()
