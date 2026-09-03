   # Pixie AI - Complete Learning Guide & Reference Manual

**Version:** 1.1.0  
**Date:** March 18, 2026  
**Author:** AI Assistant  
**Purpose:** Comprehensive offline reference for Pixie AI project

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Architecture & Concepts](#architecture--concepts)
3. [Setup & Installation](#setup--installation)
4. [Features & Capabilities](#features--capabilities)
5. [Voice Commands Reference](#voice-commands-reference)
6. [Troubleshooting Guide](#troubleshooting-guide)
7. [Code Structure Explained](#code-structure-explained)
8. [API Integration Guide](#api-integration-guide)
9. [Advanced Usage](#advanced-usage)
10. [Development & Customization](#development--customization)

---


## 1. Project Overview

### What is Pixie AI?

Pixie AI is an intelligent voice-controlled AI assistant with the following capabilities:

- **Voice Interaction:** Speak naturally and get voice responses
- **App Control:** Open/close applications like Spotify, WhatsApp, Chrome
- **Real-time Search:** Get instant answers from the web
- **Image Generation:** Create AI-generated images and diagrams
- **Research Tool:** Generate comprehensive research reports
- **Telegram Integration:** Control Pixie remotely from your phone
- **Gesture Control:** Control your computer with hand gestures
- **Content Creation:** Write emails, code, documents

### Key Technologies

- **Python 3.8+:** Core programming language
- **Groq API:** AI chat and speech recognition (Llama 3.3 70B model)
- **Cohere API:** Decision-making and command understanding
- **Hugging Face:** AI image generation (FLUX, Stable Diffusion)
- **PyQt5:** Graphical user interface
- **Selenium:** Web automation for voice recognition
- **Edge TTS:** Text-to-speech conversion
- **MediaPipe:** Hand gesture recognition

### Project Structure

```
Pixie_AI/
├── Backend/              # Core AI logic
│   ├── Chatbot.py       # Conversational AI
│   ├── Model.py         # Decision-making model
│   ├── SpeechToText.py  # Voice recognition
│   ├── TextToSpeech.py  # Voice synthesis
│   ├── Automation.py    # App control & automation
│   ├── ImageGeneration.py    # AI image creation
│   ├── RealtimeSearchEngine.py  # Web search
│   ├── ResearchTool.py  # Research report generation
│   ├── GestureControl.py     # Hand gesture control
│   ├── TelegramBridge.py     # Telegram integration
│   └── FolderContext.py      # Folder context management
├── Frontend/            # User interface
│   ├── GUI.py          # Main GUI application
│   └── Graphics/       # 3D models and assets
├── Data/               # Application data
│   ├── ChatLog.json    # Conversation history
│   └── FolderContext.json  # Folder state
├── workspace/          # Output files
│   ├── content/        # Generated content
│   ├── research_reports/    # Research documents
│   └── images/         # Generated images
├── Main.py             # Application entry point
├── .env                # API keys and configuration
└── Requirements.txt    # Python dependencies
```


---

## 2. Architecture & Concepts

### How Pixie AI Works

#### 1. Voice Input Flow

```
User Speaks → Microphone → Chrome WebDriver → Web Speech API
→ Text Recognition → Language Translation (if needed) → Query Processing
```

**Key Concepts:**
- Uses Chrome's Web Speech API for voice recognition
- Runs Chrome in background (positioned off-screen)
- Supports multiple languages with auto-translation
- 20-second timeout per recognition session

#### 2. Decision-Making Process

```
Voice Query → Query Modifier → Decision Model (Cohere)
→ Command Classification → Action Execution → Response Generation
```

**Command Types:**
- `general` - Conversational queries (handled by Groq LLM)
- `realtime` - Current information queries (web search + AI)
- `open` - Open applications
- `close` - Close applications
- `play` - Play media on YouTube
- `generate image` - Create AI images
- `live search` - Instant web answers
- `google search` - Open browser with search
- `youtube search` - Search YouTube
- `research` - Generate research reports
- `content` - Write content (emails, code, etc.)
- `system` - System control (volume, mute, etc.)

#### 3. Response Generation Flow

```
Classified Command → Backend Module → API Call (if needed)
→ Response Processing → Text-to-Speech → Voice Output
→ GUI Display
```

### Core Concepts Explained

#### A. Decision-Making Model (Cohere)

**Purpose:** Understands user intent and classifies commands

**How it works:**
1. Receives user query
2. Analyzes intent using AI
3. Returns command type and parameters
4. Example: "open spotify" → `["open spotify"]`

**Why it's important:** Without this, Pixie can't understand what you want to do.

#### B. Conversational AI (Groq)

**Purpose:** Handles general chat and questions

**How it works:**
1. Receives classified "general" queries
2. Uses Llama 3.3 70B model for responses
3. Maintains conversation history
4. Provides context-aware answers

**Why it's important:** Makes Pixie feel like a real assistant, not just a command executor.


#### C. Real-time Search Engine

**Purpose:** Gets current information from the web

**How it works:**
1. Searches Google for relevant information
2. Scrapes featured snippets and results
3. Feeds data to AI for synthesis
4. Returns comprehensive answer

**Why it's important:** Provides up-to-date information that AI models don't have.

#### D. Live Search Feature

**Purpose:** Instant answers without AI processing

**How it works:**
1. Scrapes Google directly
2. Extracts featured snippet or knowledge panel
3. Returns immediate answer
4. Faster than full realtime search

**When to use:** Quick facts, weather, prices, definitions

#### E. App Opening System

**Purpose:** Opens desktop and web applications

**How it works:**
1. **Method 1:** Check direct executable paths
2. **Method 2:** Use AppOpener library
3. **Method 3:** Open web version as fallback
4. **Method 4:** Search for app website

**Supported apps:**
- Desktop: Spotify, WhatsApp, Chrome, Firefox, Edge
- Web: Facebook, Instagram, Twitter, YouTube, Gmail, Discord

#### F. Image Generation

**Purpose:** Create AI-generated images

**How it works:**
1. Receives image prompt
2. Enhances prompt for better quality
3. Calls Hugging Face API (FLUX or Stable Diffusion)
4. Generates 4 variations
5. Saves to workspace/images/
6. Opens images automatically

**Use cases:** Art, diagrams, flowcharts, infographics

#### G. Research Tool

**Purpose:** Generate comprehensive research reports

**How it works:**
1. Searches multiple sources (Google, arXiv, IEEE, Crossref)
2. Collects papers, articles, videos
3. AI synthesizes information
4. Generates structured report
5. Exports to DOCX format

**Output includes:**
- Executive summary
- Core concepts
- Implementation guide
- Tools and libraries
- Architecture patterns
- Code examples
- Testing strategies
- Security considerations
- References and citations


---

## 3. Setup & Installation

### Prerequisites

- **Operating System:** Windows 10/11
- **Python:** 3.8 or higher
- **RAM:** 4GB minimum (8GB recommended)
- **Internet:** Required for API calls
- **Microphone:** For voice input
- **Chrome Browser:** For voice recognition

### Step-by-Step Installation

#### Step 1: Install Python

1. Download Python from https://www.python.org/downloads/
2. Run installer
3. ✅ Check "Add Python to PATH"
4. Click "Install Now"
5. Verify installation:
   ```bash
   python --version
   ```

#### Step 2: Install Dependencies

```bash
cd Pixie_AI
pip install -r Requirements.txt
```

**If you get timeout errors:**
```bash
pip install --default-timeout=100 -r Requirements.txt
```

**If you get protobuf errors:**
```bash
pip install --upgrade protobuf
pip install -r Requirements.txt
```

#### Step 3: Get API Keys

##### A. Groq API Key (REQUIRED)

1. Go to https://console.groq.com/
2. Sign up for free account
3. Navigate to "API Keys"
4. Click "Create API Key"
5. Copy the key (starts with `gsk_`)
6. Add to `.env` file

##### B. Cohere API Key (REQUIRED)

1. Go to https://dashboard.cohere.com/
2. Sign up for free account
3. Click "API Keys" in sidebar
4. Copy your API key
5. Add to `.env` file

##### C. Hugging Face API Key (REQUIRED for images)

1. Go to https://huggingface.co/
2. Sign up for free account
3. Go to Settings → Access Tokens
4. Click "New token"
5. Select "Read" access
6. Copy the token
7. Add to `.env` file

##### D. Telegram Bot Token (OPTIONAL)

1. Open Telegram app
2. Search for @BotFather
3. Send `/newbot` command
4. Follow instructions
5. Copy bot token
6. Add to `.env` file


#### Step 4: Configure .env File

Edit `Pixie_AI/.env`:

```env
# User Information
Username=YourActualName
Assistantname=Pixie

# Groq API (REQUIRED)
GroqAPIKey=gsk_your_actual_groq_key_here
GroqModel=llama-3.3-70b-versatile

# Cohere API (REQUIRED)
CohereAPIKey=your_actual_cohere_key_here

# Hugging Face API (REQUIRED for images)
HuggingFaceAPIKey=hf_your_actual_huggingface_key_here
HuggingFaceModel=black-forest-labs/FLUX.1-schnell

# Telegram (OPTIONAL)
TelegramBotToken=your_telegram_bot_token
TelegramChatID=your_chat_id
TelegramAllowedChatID=your_chat_id

# Voice (OPTIONAL)
AssistantVoice=en-US-AriaNeural
InputLanguage=en
```

**Important Notes:**
- No quotes around values
- No spaces around `=`
- Replace ALL placeholder text with actual keys
- File must be at `Pixie_AI/.env` (not parent directory)

#### Step 5: Verify Setup

```bash
cd Pixie_AI
python test_setup.py
```

This checks:
- Python version
- .env file location
- API keys configured
- Required packages installed
- Directory structure

#### Step 6: Test Components

```bash
python test_voice_and_apps.py
```

Choose options to test:
1. App opening (Spotify, WhatsApp, Chrome)
2. Voice input
3. Both

#### Step 7: Run Pixie AI

```bash
python start_pixie.py
```

Or directly:
```bash
python Main.py
```

### First Run Checklist

- [ ] Python 3.8+ installed
- [ ] All packages installed
- [ ] .env file in correct location
- [ ] Groq API key added
- [ ] Cohere API key added
- [ ] Hugging Face API key added (for images)
- [ ] Microphone connected
- [ ] Chrome browser installed
- [ ] Internet connection active
- [ ] test_setup.py passes all checks


---

## 4. Features & Capabilities

### Voice Interaction

**How to use:**
1. Wait for "Listening..." status
2. Speak clearly into microphone
3. Wait for response

**Supported languages:**
- English (default)
- Auto-translation for other languages

**Voice commands are natural:**
- "Open Spotify" ✅
- "Hey Pixie, can you open Spotify for me?" ✅
- "Launch Spotify please" ✅

### App Control

**Open Applications:**
```
"Open Spotify"
"Open WhatsApp"
"Open Chrome"
"Launch Firefox"
"Start Calculator"
"Open Notepad"
```

**Close Applications:**
```
"Close Spotify"
"Close WhatsApp"
"Close Chrome"
```

**Multiple Apps:**
```
"Open Spotify and WhatsApp"
"Launch Chrome, Firefox, and Notepad"
"Open Spotify, WhatsApp, and Chrome"
```

**How it works:**
1. Checks for desktop app in standard locations
2. Uses AppOpener if not found
3. Opens web version as fallback
4. Shows debug output in console

### Search Features

#### Live Search (Instant Answers)
```
"Live search weather today"
"Quick search Bitcoin price"
"What is the capital of France"
"Live search time in Tokyo"
```

**Best for:** Quick facts, weather, prices, definitions

#### Realtime Search (AI Analysis)
```
"Who is the current president"
"Tell me about the latest iPhone"
"What's the news about AI"
```

**Best for:** Detailed current information with AI synthesis

#### Google Search (Browser)
```
"Google search best restaurants near me"
"Search Google for Python tutorials"
```

**Best for:** Manual browsing and exploration

#### YouTube Search
```
"YouTube search funny cats"
"Search YouTube for guitar tutorials"
```


### Image Generation

**Create Images:**
```
"Generate image of a sunset over mountains"
"Create a picture of a cute robot"
"Make an image of a futuristic city"
```

**Create Diagrams:**
```
"Generate a flowchart for login process"
"Create a mind map about artificial intelligence"
"Make an architecture diagram for microservices"
```

**Output:**
- 4 variations per request
- Saved to `workspace/images/`
- Automatically opened for viewing
- High quality (4K, maximum sharpness)

**Time:** 30-60 seconds per generation

### Research Tool

**Generate Reports:**
```
"Research artificial intelligence in 3 pages"
"Make a research report on quantum computing"
"Research machine learning in 5 pages"
"Create a report about climate change in 10 pages"
```

**Output includes:**
- Executive summary
- Core concepts explained
- Step-by-step implementation
- Tools and libraries
- Architecture patterns
- Code examples
- Testing strategies
- Security considerations
- Tutorial videos
- Research papers
- References and citations

**Output format:** DOCX (Microsoft Word)
**Location:** `workspace/research_reports/`
**Time:** 2-5 minutes depending on length

### Content Creation

**Write Content:**
```
"Write an email about meeting tomorrow"
"Create a job application letter"
"Write Python code for a calculator"
"Write a story about space exploration"
```

**Output:**
- Saved to `workspace/content/`
- Automatically opened in Notepad
- AI-generated based on your request

### System Control

**Volume Control:**
```
"Volume up"
"Volume down"
"Mute"
"Unmute"
```

### Conversation

**General Chat:**
```
"Hello Pixie"
"How are you"
"Tell me a joke"
"What's the time"
"Help me with this math problem"
```

**Context-aware:** Pixie remembers conversation history


### Telegram Integration (Optional)

**Setup:**
1. Get bot token from @BotFather
2. Add to `.env` file
3. Restart Pixie AI
4. Send `/start` to your bot

**Remote Commands:**
```
/screenshot - Take screenshot
/sendfile <path> - Send file
/sendfolder <path> - Send folder as ZIP
/voice <text> - Send voice message
/browse - File browser
```

**Natural commands:**
```
"Send me screenshot"
"Send file document.pdf"
"Send folder MyProject"
"Browse photos"
```

**Features:**
- Control Pixie from anywhere
- File sharing
- Voice messages
- Interactive file browser
- Folder zipping and sending

### Folder Context

**Load Folder:**
```
"Use folder C:\Projects\MyApp"
"Set folder D:\Documents"
```

**Benefits:**
- Pixie reads all code files in folder
- Provides context-aware coding help
- Understands your project structure

**Clear Context:**
```
"Clear folder context"
"Disable folder context"
```

**Check Active Folder:**
```
"Which folder"
"Active folder"
```

### Gesture Control (Advanced)

**Hand Gestures:**
- Palm swipe left/right - Switch windows (Alt+Tab)
- Two-finger swipe - Switch browser tabs (Ctrl+Tab)
- Palm up/down - Scroll page
- Pinch - Zoom in/out (Ctrl+Scroll)
- Closed fist - Minimize all windows (Win+M)

**Requires:** Webcam

---

## 5. Voice Commands Reference

### Complete Command List

#### Opening Apps
```
✅ "Open Spotify"
✅ "Open WhatsApp"
✅ "Open Chrome"
✅ "Open Firefox"
✅ "Open Edge"
✅ "Open Notepad"
✅ "Open Calculator"
✅ "Open Paint"
✅ "Open Facebook"
✅ "Open Instagram"
✅ "Open YouTube"
✅ "Open Gmail"
✅ "Open Discord"
✅ "Open Twitter"
```


#### Closing Apps
```
✅ "Close Spotify"
✅ "Close WhatsApp"
✅ "Close Chrome"
✅ "Close Firefox"
```

#### Search Commands
```
✅ "Live search weather today"
✅ "Quick search Bitcoin price"
✅ "Google search Python tutorials"
✅ "YouTube search funny cats"
✅ "Who is Elon Musk" (realtime)
✅ "What's the latest news" (realtime)
```

#### Media
```
✅ "Play Despacito"
✅ "Play Let Her Go"
✅ "Play Bohemian Rhapsody"
```

#### Image Generation
```
✅ "Generate image of a sunset"
✅ "Create a picture of a robot"
✅ "Make a flowchart"
✅ "Generate a mind map"
```

#### Research
```
✅ "Research AI in 3 pages"
✅ "Make a report on quantum computing"
✅ "Research machine learning in 5 pages"
```

#### Content Creation
```
✅ "Write an email about meeting"
✅ "Create a job application letter"
✅ "Write Python code for calculator"
```

#### System Control
```
✅ "Volume up"
✅ "Volume down"
✅ "Mute"
✅ "Unmute"
```

#### Conversation
```
✅ "Hello Pixie"
✅ "How are you"
✅ "Tell me a joke"
✅ "What's the time"
✅ "Help me with math"
```

#### Folder Context
```
✅ "Use folder C:\Projects\MyApp"
✅ "Clear folder context"
✅ "Which folder"
```

#### Exit
```
✅ "Bye Pixie"
✅ "Exit"
✅ "Goodbye"
```

### Command Patterns

**Natural Language:**
- "Hey Pixie, can you open Spotify?"
- "Pixie, I need weather information"
- "Could you please search for Python tutorials?"

**Direct Commands:**
- "Open Spotify"
- "Search weather"
- "Generate image"

**Multiple Actions:**
- "Open Spotify and WhatsApp"
- "Search Google for news and open Chrome"


---

## 6. Troubleshooting Guide

### Voice Input Issues

#### Problem: No speech detected

**Causes:**
- Microphone not connected
- Microphone muted
- Wrong microphone selected
- Chrome WebDriver issues

**Solutions:**

1. **Check Microphone:**
   - Windows Settings → System → Sound → Input
   - Test your microphone
   - Ensure it's not muted
   - Set as default device

2. **Test Voice Input:**
   ```bash
   cd Pixie_AI
   python Backend/SpeechToText.py
   ```
   Speak when Chrome window opens

3. **Reinstall Selenium:**
   ```bash
   pip uninstall selenium webdriver-manager
   pip install selenium==4.15.0 webdriver-manager
   ```

4. **Check Chrome:**
   - Make sure Chrome is installed
   - Update to latest version
   - Check microphone permissions in Chrome

#### Problem: Chrome window doesn't open

**Solution:**
```bash
pip uninstall selenium webdriver-manager
pip install selenium==4.15.0 webdriver-manager
```

#### Problem: "Speech recognition not supported"

**Solutions:**
- Use Chrome (not Firefox or Edge)
- Update Chrome to latest version
- Check if microphone is connected

### App Opening Issues

#### Problem: Spotify won't open

**Solutions:**

1. **Install Spotify:**
   Download from https://www.spotify.com/download/

2. **Check Installation:**
   ```bash
   dir "C:\Users\%USERNAME%\AppData\Roaming\Spotify\Spotify.exe"
   ```

3. **Use Web Version:**
   System automatically opens https://open.spotify.com/ if desktop app not found

4. **Manual Test:**
   ```bash
   python -c "from Backend.Automation import OpenApp; OpenApp('spotify')"
   ```
   Check console for debug messages

#### Problem: WhatsApp won't open

**Solutions:**

1. **Install WhatsApp Desktop:**
   Download from https://www.whatsapp.com/download

2. **Check Installation:**
   ```bash
   dir "C:\Users\%USERNAME%\AppData\Local\WhatsApp\WhatsApp.exe"
   ```

3. **Use Web Version:**
   System automatically opens https://web.whatsapp.com/


#### Problem: No apps open at all

**Solution:**
```bash
pip uninstall AppOpener
pip install AppOpener

# Test
python -c "from AppOpener import open as appopen; appopen('notepad')"
```

### API Errors

#### Problem: "Missing Groq API key"

**Solutions:**
1. Check `.env` file location: `Pixie_AI/.env`
2. Verify API key is correct (no extra spaces)
3. No quotes around the key

```env
# WRONG
GroqAPIKey = "gsk_..."
GroqAPIKey= gsk_...

# CORRECT
GroqAPIKey=gsk_...
```

#### Problem: "Incorrect API key provided"

**Solutions:**
1. Get new key from respective service
2. Copy entire key (no truncation)
3. Paste without quotes or spaces
4. Restart Pixie AI

#### Problem: "Message must be at least 1 token long"

**Cause:** Voice recognition returned empty string

**Solutions:**
1. Speak louder and clearer
2. Check microphone is working
3. Test with `python Backend/SpeechToText.py`
4. Ensure microphone permissions granted

### GUI Issues

#### Problem: PyQt5 window doesn't appear

**Solution:**
```bash
pip uninstall PyQt5
pip install PyQt5==5.15.10
```

#### Problem: "No module named PyQt5"

**Solution:**
```bash
pip install PyQt5 PyQt5-Qt5 PyQt5-sip
```

### Import Errors

#### Problem: "No module named 'Backend'"

**Solution:**
```bash
# Make sure you're in Pixie_AI directory
cd Pixie_AI
python Main.py
```

NOT:
```bash
# WRONG
cd Pixie_AI/Backend
python Main.py
```

#### Problem: "No module named 'groq'"

**Solution:**
```bash
pip install -r Requirements.txt
```

### Network Errors

#### Problem: Connection timeout during pip install

**Solution:**
```bash
pip install --default-timeout=100 -r Requirements.txt
```

#### Problem: "Max retries exceeded"

**Causes:**
- Network issue
- API service down
- Firewall blocking

**Solutions:**
1. Check internet connection
2. Wait a few minutes
3. Try again
4. Check firewall settings


### Performance Issues

#### Problem: Pixie is very slow

**Solutions:**
1. Close other Chrome instances
2. Restart Pixie AI
3. Check CPU usage in Task Manager
4. Reduce image generation requests
5. Clear temporary files:
   ```bash
   rmdir /s /q Data\temp
   ```

#### Problem: Voice recognition is slow

**Solutions:**
1. Speak clearly and pause
2. Wait for "Listening..." status
3. Check microphone quality
4. Reduce background noise
5. Move closer to microphone

### Complete Reset

If nothing works:

```bash
# 1. Close Pixie AI
# 2. Backup .env
copy Pixie_AI\.env .env.backup

# 3. Delete temporary files
cd Pixie_AI
rmdir /s /q Data\temp
del Frontend\Files\*.data

# 4. Reinstall dependencies
pip uninstall -y groq cohere PyQt5 selenium AppOpener
pip install -r Requirements.txt

# 5. Restore .env
copy .env.backup .env

# 6. Run test
python test_setup.py

# 7. Run Pixie
python Main.py
```

### Common Error Messages

| Error | Cause | Solution |
|-------|-------|----------|
| "HTTPSConnectionPool: Max retries" | Network issue | Check internet, wait, retry |
| "protobuf version conflict" | Package conflict | `pip install --upgrade protobuf` |
| "Read timed out" | Slow connection | `pip install --default-timeout=100 -r Requirements.txt` |
| "Unable to locate element" | Chrome WebDriver | `pip install selenium==4.15.0` |
| "Incorrect API key" | Wrong key | Check .env file, get new key |
| "Message must be 1 token" | Empty voice input | Check microphone, speak louder |

### Debug Mode

To see detailed output:

```bash
cd Pixie_AI
python Main.py
```

Watch console for:
- `[DEBUG]` messages
- Error messages
- API responses
- Decision model output

### Getting Help

1. Check console output for errors
2. Run `python test_setup.py`
3. Run `python test_voice_and_apps.py`
4. Check file locations
5. Verify Python version: `python --version`


---

## 7. Code Structure Explained

### Main.py - Application Entry Point

**Purpose:** Orchestrates all components

**Key Functions:**

```python
InitialExecution()
# - Starts Telegram service
# - Initializes microphone status
# - Loads chat history
# - Sets up GUI

MainExecution()
# - Captures voice input
# - Processes commands
# - Executes actions
# - Generates responses

FirstThread()
# - Monitors microphone status
# - Triggers MainExecution when active

SecondThread()
# - Runs GUI interface
```

**Flow:**
```
Start → InitialExecution() → FirstThread() + SecondThread()
→ Wait for voice → MainExecution() → Process → Respond → Repeat
```

### Backend/Model.py - Decision Making

**Purpose:** Classifies user commands

**Key Components:**

```python
FirstLayerDMM(prompt)
# Input: User query
# Output: List of classified commands
# Example: "open spotify" → ["open spotify"]
```

**Supported Classifications:**
- `general` - Chat queries
- `realtime` - Current info
- `open` - Open apps
- `close` - Close apps
- `play` - Play media
- `generate image` - Create images
- `live search` - Quick search
- `google search` - Browser search
- `youtube search` - YouTube search
- `research` - Generate reports
- `content` - Write content
- `system` - System control
- `exit` - Close Pixie

**How it works:**
1. Receives user query
2. Sends to Cohere API
3. AI analyzes intent
4. Returns command type + parameters
5. Main.py executes appropriate action


### Backend/Chatbot.py - Conversational AI

**Purpose:** Handles general chat

**Key Functions:**

```python
chatBot(query)
# Input: User question
# Output: AI response
# Uses: Groq API (Llama 3.3 70B)
```

**Features:**
- Maintains conversation history
- Context-aware responses
- Personality (friendly, helpful)
- Real-time information (date, time)
- Folder context integration

**System Prompt:**
- Defines Pixie's personality
- Sets response format
- Provides guidelines

### Backend/SpeechToText.py - Voice Recognition

**Purpose:** Converts speech to text

**Key Functions:**

```python
SpeechRecognition()
# Input: Microphone audio
# Output: Recognized text
# Uses: Chrome Web Speech API
```

**How it works:**
1. Opens Chrome with voice.html
2. Starts Web Speech API
3. Captures audio from microphone
4. Converts to text
5. Translates if needed
6. Returns formatted query

**Configuration:**
- Language: Set in .env (InputLanguage)
- Timeout: 20 seconds
- Stability: 1 second of silence

### Backend/Automation.py - App Control

**Purpose:** Opens/closes apps, executes tasks

**Key Functions:**

```python
OpenApp(AppName)
# Tries multiple methods to open app
# 1. Direct executable path
# 2. AppOpener library
# 3. Web version fallback

CloseApp(AppName)
# Closes running application

LiveSearch(query)
# Quick web search for instant answers

GoogleSearch(topic)
# Opens browser with Google search

YouTubeSearch(topic)
# Opens browser with YouTube search

Content(topic)
# Generates content using AI

SystemAutomation(command)
# Controls system (volume, mute, etc.)
```


### Backend/ImageGeneration.py - AI Images

**Purpose:** Generates AI images

**Key Functions:**

```python
generate_images(prompt)
# Input: Image description
# Output: 4 image variations
# Uses: Hugging Face API
```

**Supported Models:**
- FLUX.1-schnell (fast, high quality)
- FLUX.1-dev (detailed)
- Stable Diffusion 3.5
- Stable Diffusion XL

**Process:**
1. Receives prompt
2. Enhances prompt for quality
3. Generates 4 variations
4. Saves to workspace/images/
5. Opens images automatically

### Backend/RealtimeSearchEngine.py - Web Search

**Purpose:** Gets current information

**Key Functions:**

```python
RealtimeSearchEngine(prompt)
# Input: Query needing current info
# Output: AI-synthesized answer
# Uses: Google Search + Groq AI
```

**Process:**
1. Searches Google
2. Scrapes results
3. Feeds to AI
4. AI synthesizes answer
5. Returns comprehensive response

**Features:**
- Featured snippets
- Knowledge panels
- Top search results
- Finance data (stocks, market cap)
- Context-aware synthesis

### Backend/ResearchTool.py - Research Reports

**Purpose:** Generates research documents

**Key Functions:**

```python
generate_research_report(query)
# Input: Research topic + constraints
# Output: DOCX research report
```

**Data Sources:**
- Google Search (web articles)
- arXiv (academic papers)
- IEEE (engineering papers)
- Crossref (scholarly articles)
- YouTube (tutorial videos)

**Report Sections:**
- Quick Summary
- Core Concepts
- Implementation Guide
- Tools & Libraries
- Architecture & Design
- Code Blueprint
- Testing & Debugging
- Security & Ethics
- Practical Checklist
- FAQ & Common Mistakes
- Tutorial Videos
- Research Papers
- References


### Backend/TextToSpeech.py - Voice Output

**Purpose:** Converts text to speech

**Key Functions:**

```python
TextToSpeech(text)
# Input: Text to speak
# Output: Audio playback
# Uses: Edge TTS
```

**Features:**
- Natural-sounding voices
- Multiple voice options
- Adjustable pitch and rate
- Async processing

**Configuration:**
- Voice: Set in .env (AssistantVoice)
- Default: en-US-AriaNeural
- Options: en-US-GuyNeural, en-GB-SoniaNeural, etc.

### Backend/FolderContext.py - Folder Management

**Purpose:** Loads folder context for coding help

**Key Functions:**

```python
set_active_folder(path)
# Sets folder to load

get_folder_context_message()
# Returns folder content as context

handle_folder_command(query)
# Processes folder-related commands
```

**How it works:**
1. Scans folder for code files
2. Reads file contents
3. Truncates large files
4. Provides context to AI
5. AI uses context for answers

**Supported Files:**
- Code: .py, .js, .ts, .java, .cpp, .cs, etc.
- Config: .json, .yaml, .toml, .ini, .env
- Docs: .txt, .md, .rst, .log

**Limits:**
- Max 120 files
- Max 1800 chars per file
- Max 36000 chars total
- Max 512KB per file

### Backend/TelegramBridge.py - Remote Control

**Purpose:** Telegram bot integration

**Key Features:**
- Remote command execution
- File sharing
- Screenshot capture
- Voice messages
- Interactive file browser
- Folder zipping

**Commands:**
- `/start` - Connect bot
- `/help` - Show commands
- `/screenshot` - Take screenshot
- `/sendfile <path>` - Send file
- `/sendfolder <path>` - Send folder
- `/voice <text>` - Voice message
- `/browse` - File browser


### Frontend/GUI.py - User Interface

**Purpose:** Graphical interface

**Key Components:**

```python
GraphicalUserInterface()
# Main GUI window with 3D fox character

SetMicrophoneStatus(status)
# Controls microphone on/off

ShowTextToScreen(text)
# Displays conversation

SetAssistantStatus(status)
# Shows Pixie's current state
```

**Features:**
- 3D animated fox character
- Chat window
- Microphone control
- System tray integration
- Drag-and-drop
- Minimize to tray

**Status Messages:**
- "Available..." - Ready for input
- "Listening..." - Capturing voice
- "Thinking..." - Processing command
- "Searching..." - Looking up information
- "Answering..." - Speaking response

---

## 8. API Integration Guide

### Groq API

**Purpose:** AI chat and speech recognition

**Model:** Llama 3.3 70B Versatile

**Usage:**
```python
from groq import Groq
client = Groq(api_key=GroqAPIKey)

completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"}
    ],
    temperature=0.6,
    max_tokens=2048
)
```

**Rate Limits:**
- Free tier: Generous limits
- Streaming supported
- Fast response times

**Best Practices:**
- Use streaming for real-time responses
- Keep temperature 0.6-0.7 for balanced creativity
- Limit max_tokens to control costs
- Maintain conversation history


### Cohere API

**Purpose:** Command classification and decision making

**Model:** Command-R-08-2024

**Usage:**
```python
import cohere
co = cohere.Client(api_key=CohereAPIKey)

response = co.chat(
    model="command-r-08-2024",
    message="open spotify",
    temperature=0.3,
    preamble="You are a decision-making model..."
)
```

**Rate Limits:**
- Trial: 20 calls per endpoint
- Monthly: 1000 calls
- Upgrade for more

**Best Practices:**
- Use low temperature (0.3) for consistent decisions
- Provide clear preamble instructions
- Include examples in chat history
- Handle empty messages gracefully

### Hugging Face API

**Purpose:** AI image generation

**Models:**
- FLUX.1-schnell (fast)
- FLUX.1-dev (detailed)
- Stable Diffusion 3.5
- Stable Diffusion XL

**Usage:**
```python
import requests

api_url = "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-schnell"
headers = {"Authorization": f"Bearer {HF_API_KEY}"}
payload = {"inputs": "a sunset over mountains"}

response = requests.post(api_url, headers=headers, json=payload)
image_bytes = response.content
```

**Rate Limits:**
- Free tier available
- Rate limits vary by model
- Consider using multiple models as fallbacks

**Best Practices:**
- Enhance prompts for better quality
- Generate multiple variations
- Use appropriate model for use case
- Handle timeouts gracefully

### Edge TTS

**Purpose:** Text-to-speech

**Usage:**
```python
import edge_tts
import asyncio

async def text_to_speech(text):
    comm = edge_tts.Communicate(text, "en-US-AriaNeural")
    await comm.save("output.mp3")

asyncio.run(text_to_speech("Hello world"))
```

**Available Voices:**
- en-US-AriaNeural (female)
- en-US-GuyNeural (male)
- en-GB-SoniaNeural (British female)
- Many more languages

**Best Practices:**
- Use async for non-blocking
- Adjust pitch and rate for naturalness
- Cache common phrases
- Handle network errors


---

## 9. Advanced Usage

### Custom Voice Commands

**Add new commands to Model.py:**

1. Add to `funcs` list:
```python
funcs = [
    # ... existing ...
    "my_custom_command",  # Add here
]
```

2. Update `preamble`:
```python
preamble = """
...
-> Respond with 'my_custom_command (params)' if query asks for...
...
"""
```

3. Handle in Main.py:
```python
elif "my_custom_command" in Queries:
    # Your custom logic here
    pass
```

### Custom App Paths

**Add to Automation.py:**

```python
direct_paths = {
    # ... existing ...
    'myapp': [
        r'C:\Path\To\MyApp.exe',
        r'D:\Another\Path\MyApp.exe',
    ],
}
```

### Custom Voices

**Change in .env:**

```env
AssistantVoice=en-GB-SoniaNeural
```

**Available voices:**
- en-US-AriaNeural (US female)
- en-US-GuyNeural (US male)
- en-GB-SoniaNeural (UK female)
- en-GB-RyanNeural (UK male)
- en-AU-NatashaNeural (Australian)
- en-IN-NeerjaNeural (Indian)

### Custom Input Language

**Change in .env:**

```env
InputLanguage=es  # Spanish
InputLanguage=fr  # French
InputLanguage=de  # German
```

Pixie will auto-translate to English.

### Folder Context for Projects

**Load your project:**
```
"Use folder C:\Projects\MyWebApp"
```

**Ask coding questions:**
```
"How does the authentication work in this project?"
"Where is the database connection defined?"
"Explain the user model"
```

Pixie reads your code and provides context-aware answers.

### Batch Operations

**Open multiple apps:**
```
"Open Spotify, WhatsApp, Chrome, and Discord"
```

**Multiple searches:**
```
"Google search Python tutorials and YouTube search coding videos"
```


### Research Report Customization

**Specify length:**
```
"Research AI in 5 pages"
"Research quantum computing in 100 lines"
```

**Specify topic:**
```
"Research machine learning algorithms"
"Make a report on blockchain technology"
"Research cybersecurity best practices"
```

### Image Generation Tips

**Be specific:**
```
"Generate image of a sunset over mountains with purple sky"
```

**Use style keywords:**
```
"Generate image of a robot in cyberpunk style"
"Create a watercolor painting of a forest"
```

**For diagrams:**
```
"Generate a flowchart for user authentication process"
"Create a system architecture diagram for microservices"
```

### Telegram Remote Control

**Setup:**
1. Get bot token from @BotFather
2. Add to .env
3. Restart Pixie
4. Send `/start` to bot

**Use cases:**
- Control Pixie from phone
- Get files while away
- Take screenshots remotely
- Send voice messages
- Browse files on PC

### Performance Optimization

**Reduce startup time:**
- Keep Chrome open in background
- Use SSD for faster file access
- Close unnecessary programs

**Reduce response time:**
- Use "live search" for quick facts
- Cache common queries
- Use local models when possible

**Reduce API costs:**
- Use appropriate models
- Limit max_tokens
- Cache responses
- Use streaming

---

## 10. Development & Customization

### Adding New Features

**1. Add new backend module:**

Create `Backend/MyFeature.py`:
```python
def my_feature(query):
    # Your logic here
    return result
```

**2. Update Model.py:**

Add to funcs and preamble.

**3. Update Main.py:**

Handle the new command:
```python
elif "my_feature" in Queries:
    result = my_feature(query)
    ShowTextToScreen(result)
    TextToSpeech(result)
```

