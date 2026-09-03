# Pixie AI - Complete Setup Guide

## Missing Files & Configurations

### 1. Missing Critical File
- `Data/ChatLog.json` - This file will be auto-created on first run

### 2. Environment Variables (.env file)

Your `.env` file needs the following API keys and configurations:

```env
# Required - User Information
Username=YourName
Assistantname=Pixie

# Required - Groq API (for AI chat and speech recognition)
GroqAPIKey=your_groq_api_key_here
GroqModel=llama-3.3-70b-versatile

# Required - Cohere API (for decision making model)
CohereAPIKey=your_cohere_api_key_here

# Required - Hugging Face API (for image generation)
HuggingFaceAPIKey=your_huggingface_api_key_here
HuggingFaceModel=black-forest-labs/FLUX.1-schnell

# Optional - Telegram Integration
TelegramBotToken=your_telegram_bot_token_here
TelegramChatID=your_chat_id_here
TelegramAllowedChatID=your_allowed_chat_id_here

# Optional - Text-to-Speech Voice
AssistantVoice=en-US-AriaNeural
```

## Step-by-Step Setup Instructions

### Step 1: Get Required API Keys

#### A. Groq API Key (REQUIRED)
1. Go to https://console.groq.com/
2. Sign up or log in
3. Navigate to "API Keys" section
4. Create a new API key
5. Copy and paste it in `.env` as `GroqAPIKey`

#### B. Cohere API Key (REQUIRED)
1. Go to https://dashboard.cohere.com/
2. Sign up or log in
3. Go to API Keys section
4. Copy your API key
5. Paste it in `.env` as `CohereAPIKey`

#### C. Hugging Face API Key (REQUIRED for image generation)
1. Go to https://huggingface.co/
2. Sign up or log in
3. Go to Settings → Access Tokens
4. Create a new token with "Read" access
5. Copy and paste it in `.env` as `HuggingFaceAPIKey`

#### D. Telegram Bot Token (OPTIONAL)
1. Open Telegram and search for @BotFather
2. Send `/newbot` command
3. Follow instructions to create your bot
4. Copy the bot token
5. Paste it in `.env` as `TelegramBotToken`
6. To get your Chat ID:
   - Send a message to your bot
   - Visit: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
   - Find your chat_id in the response
   - Add it to `.env` as `TelegramChatID`

### Step 2: Update Your .env File

Edit the `.env` file in the root `Pixie_AI` directory (NOT the parent directory) and add all your API keys.

### Step 3: Verify File Structure

Make sure your `.env` file is located at:
```
Pixie_AI/.env  (correct location)
```

NOT at:
```
.env  (wrong - this is in parent directory)
```

### Step 4: Create Missing Directories

The following will be auto-created, but you can create them manually:
```bash
mkdir -p Pixie_AI/Data
mkdir -p Pixie_AI/workspace/content
mkdir -p Pixie_AI/workspace/research_reports
mkdir -p Pixie_AI/workspace/images
```

### Step 5: Run the Application

```bash
cd Pixie_AI
python Main.py
```

## Features & What They Require

| Feature | Required API Keys | Optional |
|---------|------------------|----------|
| Voice Chat | Groq | - |
| Text Chat | Groq, Cohere | - |
| Image Generation | Hugging Face | - |
| Real-time Search | Groq | - |
| Research Reports | Groq | - |
| Telegram Control | Groq, Cohere | Telegram Bot Token |
| Speech Recognition | Groq | - |
| Text-to-Speech | - | Built-in (edge-tts) |
| Gesture Control | - | Built-in (MediaPipe) |
| Automation | Groq, Cohere | - |

## Common Issues & Solutions

### Issue 1: "Missing API key" errors
**Solution:** Make sure your `.env` file is in `Pixie_AI/.env` (not in parent directory)

### Issue 2: Import errors
**Solution:** Run `pip install -r Requirements.txt` again

### Issue 3: "No module named 'Backend'"
**Solution:** Make sure you're running from the `Pixie_AI` directory:
```bash
cd Pixie_AI
python Main.py
```

### Issue 4: PyQt5 GUI doesn't open
**Solution:** 
```bash
pip uninstall PyQt5
pip install PyQt5
```

### Issue 5: Protobuf version conflicts
**Solution:**
```bash
pip install --upgrade protobuf
```

### Issue 6: Network timeout during pip install
**Solution:**
```bash
pip install --default-timeout=100 -r Requirements.txt
```

## Testing Individual Components

### Test Chatbot Only
```bash
cd Pixie_AI
python Backend/Chatbot.py
```

### Test Image Generation
```bash
cd Pixie_AI
python Backend/ImageGeneration.py
```

### Test Speech Recognition
```bash
cd Pixie_AI
python Backend/SpeechToText.py
```

## Minimum Configuration to Run

To get Pixie AI running with basic features, you MUST have:

1. ✅ `GroqAPIKey` - For AI chat and speech
2. ✅ `CohereAPIKey` - For decision making
3. ✅ `Username` and `Assistantname` - For personalization

Optional but recommended:
- `HuggingFaceAPIKey` - For image generation
- `TelegramBotToken` - For remote control

## File Locations Reference

```
Pixie_AI/
├── .env                          ← Your API keys go here
├── Main.py                       ← Run this to start
├── Requirements.txt              ← Dependencies list
├── Data/
│   ├── ChatLog.json             ← Auto-created (conversation history)
│   ├── FolderContext.json       ← Auto-created (folder context state)
│   └── temp/                    ← Auto-created (temporary files)
├── workspace/
│   ├── content/                 ← Generated content files
│   ├── research_reports/        ← Research documents
│   └── images/                  ← Generated images
├── Backend/                     ← Core AI modules
└── Frontend/                    ← GUI components
```

## Next Steps After Setup

1. Run `python Main.py` from the `Pixie_AI` directory
2. The GUI should open with a 3D fox character
3. Click the microphone button to start voice interaction
4. Try saying: "Hello Pixie"
5. Try: "Generate image of a sunset"
6. Try: "Research artificial intelligence in 2 pages"

## Getting Help

If you encounter issues:
1. Check that all API keys are valid
2. Verify `.env` file location
3. Ensure all dependencies are installed
4. Check Python version (3.8+ required)
5. Look at console output for specific error messages
