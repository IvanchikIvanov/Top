import asyncio
from aiogram import Router, Bot, Dispatcher
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder

async def start(message: Message) -> None:
    await message.reply(
        "Click! Click! Click!",
        reply_markup=webapp_builder()
    )

def webapp_builder() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="🔥 Let's Click!",
        web_app=WebAppInfo(url="YOUR_WEB_APP_URL_HERE")  # Change this URL to your web app's URL
    )
    return builder

async def main() -> None:
    bot = Bot("7065039219:AAF_2wPd985erqAYtmKd8p_tc-XhLbb6MCU", parse_mode=ParseMode.HTML)  # Replace with your bot's token
    dp = Dispatcher()
    router = Router()
    router.message.register(start, CommandStart())

    dp.include_router(router)
    
    await bot.delete_webhook(True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
