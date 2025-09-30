# VocabBot - Telegram Dictionary Bot

A Telegram bot that provides word definitions, pronunciations, and examples using the Free Dictionary API.

## Features

- 📚 Word Definitions: Get detailed definitions for any English word
- 🔊 Pronunciations: View phonetic pronunciations
- 📖 Multiple Meanings: See different meanings grouped by parts of speech (noun, verb, adjective, etc.)
- 💡 Usage Examples: Real-world examples for better understanding
- ✨ Clean Formatting: Well-organized responses with emoji indicators

## Requirements

- Python 3.x
- `pyrogram` - Telegram client library
- `TgCrypto` - For better performance with Pyrogram
- `requests` - For making API calls

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/VocabBot.git
cd VocabBot
```

2. Install the required packages:
```bash
pip install pyrogram TgCrypto requests
```

3. Configure your Telegram API credentials:
   - Get your `API_ID` and `API_HASH` from [my.telegram.org](https://my.telegram.org)
   - Create a bot and get your `BOT_TOKEN` from [@BotFather](https://t.me/BotFather)
   - Update these values in `bot.py`

## Usage

1. Start the bot:
```bash
python bot.py
```

2. Open Telegram and search for your bot

3. Start chatting:
   - Send `/start` to get the welcome message
   - Send any English word to get its definition

## Example Response

When you send a word like "hello", the bot responds with:
```
hello
🔊 /həˈləʊ/

📖 Definitions:

Interjection:
• A greeting (salutation) said when meeting someone or acknowledging someone's arrival or presence.
  💡 Example: Hello, everyone.
• A greeting used when answering the telephone.
  💡 Example: Hello? How may I help you?

Noun:
• "Hello!" or an equivalent greeting.
```

## API Used

This bot uses the [Free Dictionary API](https://dictionaryapi.dev/) for fetching word definitions and related information.

## Project Structure

- `bot.py` - Main bot file containing Telegram bot logic
- `dictionary_api.py` - Module for interacting with the Dictionary API
