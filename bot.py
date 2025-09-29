from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery
from dictionary_api import get_definition


API_ID = ××××××
API_HASH = "××××××"
BOT_TOKEN = "××××××"

app = Client(
    "Vocab_Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)



@app.on_message(filters.command("start") & filters.private)
async def start(app, message):
    await app.send_message(
        chat_id=message.chat.id,
        text="Hi! I’m VocabBot.\nSend me any word and I’ll show you its definition, pronunciation, and examples."
    )

    

@app.on_message(filters.private)
async def send_word(app, message):
    
    word = message.text
    result = get_definition(word)
    if "error" in result:
        response = result["error"]
    else:
        # Word and pronunciation
        response = f"{result['word']}"
        if result['phonetics']:
            response += f"\n🔊 {result['phonetics']}"
        
        # Definitions section
        response += "\n\n📖 Definitions:"
        
        # Group meanings by part of speech
        meanings_by_pos = {}
        for meaning in result['meanings']:
            pos = meaning['part_of_speech']
            if pos not in meanings_by_pos:
                meanings_by_pos[pos] = []
            meanings_by_pos[pos].append(meaning)
        
        # Add definitions grouped by part of speech
        for pos, meanings in meanings_by_pos.items():
            response += f"\n\n{pos.capitalize()}:"
            # Limit to 2 meanings per part of speech
            for meaning in meanings[:2]:
                response += f"\n• {meaning['definition']}"
                if meaning['example']:
                    response += f"\n  💡 Example: _{meaning['example']}_"
                    
    await app.send_message(chat_id=message.chat.id, text=response)


if __name__=="__main__":
    app.run()
