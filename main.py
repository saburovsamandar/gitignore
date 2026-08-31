import  asyncio
from  aiogram import  Bot, Dispatcher
from aiogram.types import  Message
from  aiogram.filters import CommandStart

TOKEN = 'jhgfsredtfgyhuijo4i239t8yq34w87ergierfdlsglsdv'
bot = Bot(token=TOKEN)
dp = Dispatcher()
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Hello {message.from_user.first_name}!")

async def main():
    await  dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())









