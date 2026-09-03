# Quick Start - Get Pixie AI Running in 5 Minutes

## Current Status ✅
- ✅ Groq API Key configured
- ✅ ChatLog.json created
- ✅ .env file in correct location

## What You Need to Do Now 🎯

### Step 1: Get Cohere API Key (2 minutes)
This is REQUIRED for Pixie to understand your commands.

1. Go to: https://dashboard.cohere.com/
2. Click "Sign Up" (free account)
3. After login, go to "API Keys"
4. Copy your API key
5. Open `Pixie_AI/.env` file
6. Replace `your_cohere_api_key_here` with your actual key

### Step 2: Get Hugging Face API Key (2 minutes)
This is REQUIRED for image generation feature.

1. Go to: https://huggingface.co/
2. Click "Sign Up" (free account)
3. After login, click your profile → Settings
4. Go to "Access Tokens"
5. Click "New token"
6. Give it a name like "Pixie AI"
7. Select "Read" access
8. Copy the token
9. Open `Pixie_AI/.env` file
10. Replace `your_huggingface_api_key_here` with your token

### Step 3: Run Pixie AI! 🚀

```bash
cd Pixie_AI
python Main.py
```

## What to Expect

1. A GUI window will open with a 3D fox character
2. You'll see status: "Available..."
3. Click the microphone button (or it may auto-activate)
4. Say: "Hello Pixie, how are you?"
5. Pixie will respond with voice and text!

## Quick Test Commands

Once running, try these:

### Basic Chat
- "Hello Pixie"
- "What's the weather like?"
- "Tell me a joke"

### Image Generation (needs Hugging Face key)
- "Generate image of a sunset over mountains"
- "Create a picture of a cute robot"

### Web Search
- "Who is the current president of USA?"
- "Latest news about AI"

### Automation
- "Open Chrome"
- "Search Google for Python tutorials"
- "Play Despacito on YouTube"

### Research (creates detailed reports)
- "Research quantum computing in 3 pages"
- "Make a research report on machine learning"

### System Control
- "Volume up"
- "Mute"

## Troubleshooting

### "Missing Cohere API key" error
→ You forgot Step 1. Get the Cohere key and add it to `.env`

### "Missing Hugging Face API key" error
→ You forgot Step 2. Get the HF key and add it to `.env`

### GUI doesn't open
→ Try: `pip install --upgrade PyQt5`

### "No module named Backend" error
→ Make sure you're in the Pixie_AI directory: `cd Pixie_AI`

### Voice recognition not working
→ Check your microphone permissions in Windows settings

## Optional: Telegram Remote Control

Want to control Pixie from your phone? 

1. Open Telegram
2. Search for @BotFather
3. Send: `/newbot`
4. Follow instructions
5. Copy the bot token
6. Add to `.env` as `TelegramBotToken`
7. Restart Pixie AI
8. Send `/start` to your bot

Now you can control Pixie from anywhere!

## File Structure Check

Make sure your files are organized like this:

```
Pixie_AI/
├── .env                    ← API keys here
├── Main.py                 ← Run this
├── Data/
│   └── ChatLog.json       ← Created ✅
├── Backend/
├── Frontend/
└── workspace/
```

## Need More Help?

Check `SETUP_GUIDE.md` for detailed documentation.

---

**Ready? Let's go!** 🚀

```bash
cd Pixie_AI
python Main.py
```
