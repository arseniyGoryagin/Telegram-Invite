
from dotenv import load_dotenv
from telethon.sync import TelegramClient
from telethon import functions, types, errors
import os

load_dotenv()

api_id : str = os.getenv("TELEGRAM_API_ID")
api_hash_id : str = os.getenv("TELEGRAM_API_HASH")
phone_number : str = os.getenv("TELEGRAM_PHONE_NUMBER")
target_chat_name : str = os.getenv("TARGET_CHAT")
target_file : str  = os.getenv("TARGET_FILENAME")

client = TelegramClient("session", api_id, api_hash_id)
client.start(phone_number)



def get_chat_id(chat_name :str) -> str:

    dialogs = client.get_dialogs()

    for dialog in dialogs:
        if dialog.name == chat_name:
            if dialog.is_channel == True:
                continue
            return dialog.entity.id


    return None 
     



def main():

    target_chat : str = get_chat_id(target_chat_name)

    if(target_chat == None):
        print("No such chat")
        return 

   

    with open(target_file, 'r')as file:

        username : str = file.readline()

        while username:


            try:
                client(
                functions.messages.AddChatUserRequest(
                    chat_id = target_chat,
                    user_id = username,
                    fwd_limit=42
                ))
            except Exception as e:
                print(e)

            username =  file.readline()





main()