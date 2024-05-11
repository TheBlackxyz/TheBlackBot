import pymongo
from database.users_chats_db import db
from pyrogram import Client, filters
from info import GET_DATA, COLLECTION_NAME, DATABASE_URL, DATABASE_NAME

# Define a function to handle the /getdata command
@Client.on_message(filters.private & filters.command('getdata'))
async def get_data(cilent, message):
    # Retrieve data from MongoDB
    data = collection.find_one({"user_id": message.chat.id})
    
    # If data is found, send it to the user
    if data:
        bot.reply_to(message, f"👋 Hey Buddy data is Found : {data}")
    else:
        bot.reply_to(message, "No data found for your user ID")
