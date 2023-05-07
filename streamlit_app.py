from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.emoji import emojize
from aiogram.utils.markdown import bold, code, italic, text
import os 
from keep_alive import keep_alive
from aiogram.types import ReplyKeyboardMarkup , ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from dotenv import load_dotenv
import config
import logging 
from aiogram.types.message import ContentType

#log
logging.basicConfig(level=logging.INFO)
keep_alive()
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN') 
bot = Bot(token=BOT_TOKEN)
PAYMENT_TOKEN=os.getenv('PAYMENT_TOKEN') 
dp=Dispatcher(bot)

button1= InlineKeyboardButton(text="Begin",callback_data="Shopping")
keyboard_inline=InlineKeyboardMarkup().add(button1)
button2=InlineKeyboardButton(text="Travel_Bags",callback_data="Travel Bags" )
button3=InlineKeyboardButton(text="Hand_Bags",callback_data="Hand_Bags" )
button4=InlineKeyboardButton(text="Sling_Bags",callback_data="Sling_Bags" )
button5=InlineKeyboardButton(text="Pencil_pouches",callback_data="Pencil_pouches" )
button6=InlineKeyboardButton(text="Samosa_bags",callback_data="Samosa_bags" )
button7=InlineKeyboardButton(text="Mobile_pouch",callback_data="Mobile_pouch" )
button8=InlineKeyboardButton(text="File_holder",callback_data="File_holder" )
button9=InlineKeyboardButton(text="Lunch_bags",callback_data="Lunch_bags" )
button10=InlineKeyboardButton(text="Gift_bags",callback_data="Gift" )
button11=InlineKeyboardButton(text="Vegetable_bags",callback_data="Vegetable" )
Back=InlineKeyboardButton(text="Back",callback_data="Back" )
Pay=InlineKeyboardButton(text="Pay",callback_data="Pay",pay=True )
back_keyboard=InlineKeyboardMarkup().add(Back,Pay)
keyboard_inline2=InlineKeyboardMarkup().add(button2,button3,button4,button5,button6,button7,button8,button9,button10,button11)


@dp.message_handler(commands=['start','help'])
async def welcome(message:types.Message):
    await message.reply("Hello, Welcome to Vishvm Jute World. \nExplore the world of Jute products and Become a part of eco friendly community!!  ")
    await message.answer_photo(types.InputFile('Images/logo.png'))

    await message.answer(text="😄",reply_markup=keyboard_inline)

@dp.callback_query_handler(text=['Shopping','Travel Bags',"Hand_Bags","Sling_Bags","Pencil_pouches","Samosa_bags","Mobile_pouch","File_holder","Lunch_bags","Gift","Vegetable",'Back','Pay' ])
async def options(call:types.CallbackQuery):
    if call.data=='Shopping':
        await call.message.answer(text="Here is our Catalog",reply_markup=keyboard_inline2)
    elif call.data=='Travel Bags':
        await call.message.answer_photo(types.InputFile('Images/Travel bag.jpeg'))
        await call.message.answer_photo(types.InputFile('Images/Travel bags (2).jpeg'))
        await call.message.answer(text="Cost : Rs.100",reply_markup=back_keyboard)
    elif call.data=='Hand_Bags':
        await call.message.answer_photo(types.InputFile('Images/Hand Bag.jpeg'))
        await call.message.answer_photo(types.InputFile('Images/Hand Bag (2).jpeg'))
        await call.message.answer(text="Cost : Rs.100",reply_markup=back_keyboard)
    elif call.data=='Sling_Bags':
        await call.message.answer_photo(types.InputFile('Images/Sling bag.jpeg'))
        await call.message.answer_photo(types.InputFile('Images/Sling-Bags.jpeg'))
        await call.message.answer(text="Cost : Rs.100",reply_markup=back_keyboard)
    elif call.data=='Pencil_pouches':
        await call.message.answer_photo(types.InputFile('Images/Pencil Pouch (2).jpeg'))
        await call.message.answer_photo(types.InputFile('Images/Pencil pouch (3).jpeg'))
        await call.message.answer(text="Cost : Rs.100",reply_markup=back_keyboard)
    elif call.data=='Samosa_bags':
        await call.message.answer_photo(types.InputFile('Images/Samosa bag.jpeg'))
        await call.message.answer(text="Cost : Rs.100",reply_markup=back_keyboard)
    elif call.data=='Mobile_pouch':
        await call.message.answer_photo(types.InputFile('Images/Mobile Pouch (2).jpeg'))
        await call.message.answer_photo(types.InputFile('Images/Mobile pouch.jpeg'))
        await call.message.answer(text="Cost : Rs.100",reply_markup=back_keyboard)
    elif call.data=='File_holder':
        await call.message.answer_photo(types.InputFile('Images/File holder (2).jpeg'))
        await call.message.answer_photo(types.InputFile('Images/File holder.jpeg'))
        await call.message.answer(text="Cost : Rs.100",reply_markup=back_keyboard)
    elif call.data=='Lunch_bags':
        await call.message.answer_photo(types.InputFile('Images/Lunch bag (2).jpeg'))
        await call.message.answer_photo(types.InputFile('Images/Lunch bag (3).jpeg'))
        await call.message.answer(text="Cost : Rs.100",reply_markup=back_keyboard)
    elif call.data=='Gift':
        await call.message.answer_photo(types.InputFile('Images/Gift Bags (2).jpeg'))
        await call.message.answer_photo(types.InputFile('Images/Gift Bags (4).jpeg'))
        await call.message.answer(text="Cost : Rs.100",reply_markup=back_keyboard)
    elif call.data=='Vegetable':
        await call.message.answer_photo(types.InputFile('Images/Vegetable bag (2).jpeg'))
        await call.message.answer_photo(types.InputFile('Images/Vegetable Bag.jpeg'))
        await call.message.answer(text="Cost : Rs.100",reply_markup=back_keyboard)
    elif call.data=='Back':
        await call.message.answer(text="Here is our Catalog",reply_markup=keyboard_inline2)
    elif call.data=='Pay':
        Price=types.LabeledPrice(label="Jute Bag",amount=100*100)
        if PAYMENT_TOKEN.split(":")[1] == "TEST":
            await call.message.reply(text="Payment Initiation")
        await bot.send_invoice(
            call.message.chat.id,
            title="Jute Bag",
            description="Payment of 100 USD",
            provider_token=PAYMENT_TOKEN,
            currency="inr",
            is_flexible=False,
            prices=[Price],
            start_parameter='one-month-subscription',
            payload='test-invoice-payload'
        )
        @dp.pre_checkout_query_handler(lambda query : True)
        async def pre_checkout_query(pre_checkout_q : types.PreCheckoutQuery):
          await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)
        @dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
        async def successful_payment(message: types.Message):
            print("SUCCESSFUL PAYMENT:")
            payment_info=message.successful_payment.to_python()
            for key,value in payment_info.items():
                print(f"{key} = {value}")
            
            await bot.send_message(message.chat.id,f'Payment for amount {message.successful_payment.total_amount //100} {message.successful_payment.currency} Passed Successfully!!!!')
            await message.answer(text="👍")

executor.start_polling(dp,skip_updates=False)
