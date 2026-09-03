# Pixie_AI 🦊

An intelligent 3D AI assistant featuring real-time voice interaction, Groq & Cohere AI models, WhatsApp messaging automation, FLUX image & diagram generation, MediaPipe gesture control, deep academic research exporter, Telegram remote control, and a modern 3D GUI interface.

## ✨ Core Features

### 🎤 Voice & Speech

- **High-Speed Speech-to-Text**: Instant voice recognition with 0.4s fast pause detection (Web Speech API & Groq Whisper)
- **Natural Text-to-Speech**: High-speed (+25% rate) neural voice output using Edge TTS with automatic markdown symbol filtering
- **Full Response Speech**: Complete response spoken out loud cleanly without truncating or skipping sentences
- **Voice Commands**: Hands-free control for app launching, web search, messaging, research, and system control

### 🤖 AI Intelligence

- **Conversational AI**: Powered by Groq (`groq/compound`) for ultra-fast, high-accuracy conversational intelligence
- **Respectful & Direct**: Addresses the user as "Sir" naturally with concise, bold key points and zero robotic headers
- **Decision Engine**: Intent classification powered by Cohere Command-R model (`Backend/Model.py`)
- **Real-time Web Search**: Live web search integration with Google and real-time financial market snapshots
- **Folder Context**: Inject entire local folder codebases into AI system context for instant code assistance

### 💬 WhatsApp & Application Automation

- **WhatsApp Voice Messaging**: Send pre-composed WhatsApp messages to contacts or phone numbers via voice/text (`SendWhatsAppMessage`)
- **Multi-Path App Control**: Open/close desktop applications (Spotify, WhatsApp, Chrome, Edge, Firefox) with web fallback
- **Content Exporter**: Write letters, emails, code, and documents directly to local files and open in Notepad
- **System Controls**: Control volume (up/down/mute/unmute) via hands-free automation

### 🖼️ Image & Diagram Generation

- **AI Image Creation**: Generate images using Hugging Face models (FLUX.1 Schnell, Stable Diffusion 3.5 Large, SDXL)
- **Diagram Support**: Auto-optimized prompt engineering for 2D flowcharts, infographics, mind maps, and architecture diagrams
- **Batch Generation**: Create multiple variations simultaneously and view instantly in workspace

### 🖐️ Gesture Control

- **Hand Tracking**: MediaPipe-powered gesture recognition (`Backend/GestureControl.py`)
- **Window Switching**: Palm swipe left/right to switch active windows (`Alt+Tab`)
- **Tab Navigation**: Two-finger swipe to switch browser tabs (`Ctrl+Tab`)
- **Scroll Control**: Palm up/down for page scrolling
- **Pinch Zoom**: Zoom in/out with pinch gesture (`Ctrl+Scroll`)
- **Minimize All**: Hold closed fist for 0.8s to minimize all windows (`Win+M`)

### 📚 Deep Research Tool

- **Comprehensive Reports**: Multi-source aggregation combining Google, arXiv papers, Crossref/IEEE metadata, and YouTube tutorials
- **Formatted Export**: Professional `.docx` document generation with numbered academic citations
- **Custom Constraints**: Specify target length in pages (1-500) or lines (20-20000)

### 📱 Telegram Remote Control Bridge

- **Full Remote Access**: Access and control Pixie from your phone anywhere via Telegram bot
- **Voice Message Processing**: Send voice notes on Telegram; Pixie transcribes with Groq Whisper and sends voice replies back
- **Desktop Screenshots**: Receive instant live desktop screenshots by sending `/screenshot` to your bot
- **Interactive File Browser**: Paginated file system browser with filters to download files and folders to your phone

## 🏗️ Architecture

```
Pixie_AI/
├── Backend/           # Core AI services
│   ├── Model.py              # Cohere decision engine
│   ├── Chatbot.py            # Conversational AI (Groq compound)
│   ├── SpeechToText.py       # Instant voice recognition (0.4s stability)
│   ├── TextToSpeech.py       # Speech synthesis (+25% rate & markdown cleaner)
│   ├── ImageGeneration.py    # AI image & diagram creation (FLUX.1)
│   ├── RealtimeSearchEngine.py # Live web search & financial snapshots
│   ├── ResearchTool.py       # Deep research report generator (.docx)
│   ├── GestureControl.py     # MediaPipe hand tracking & gestures
│   ├── TelegramBridge.py     # Remote control Telegram bot service
│   ├── FolderContext.py      # Workspace folder context loader
│   └── Automation.py         # App opener & WhatsApp messaging automation
├── Frontend/          # User interface
│   ├── GUI.py                # PyWebview application & System Tray integration
│   ├── Graphics/             # 3D assets (Fox_draco.glb & icons)
│   └── Files/                # UI state management
├── Data/              # Application data
│   └── ChatLog.json          # Persistent conversation history
├── start_pixie.py     # Startup script with pre-flight verification
└── Main.py            # Main application entry point
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

1. Clone the repository:

```bash
git clone https://github.com/AdithAnilkumar/Pixie_AI.git
cd Pixie_AI
```

2. Install dependencies:

```bash
pip install -r Requirements.txt
```

3. Configure environment variables in `.env`:

```ini
Username=Adith
Assistantname=Pixie

# Required API Keys
GroqAPIKey=your_groq_api_key
GroqModel=groq/compound
CohereAPIKey=your_cohere_api_key
HuggingFaceAPIKey=your_huggingface_api_key

# Optional Telegram Bot Remote Control
TelegramBotToken=your_telegram_bot_token
```

### Running the Application

```bash
python start_pixie.py
```

*Note: On launch, Pixie runs quietly in your Windows System Tray (icon near clock) with voice input enabled automatically. Right-click the Pixie icon and click **Pixie UI** to view the 3D GUI window anytime.*

## 👤 Author

**AdithAnilkumar**

- GitHub: [@AdithAnilkumar](https://github.com/AdithAnilkumar)

## 📄 License

This project is licensed under the [MIT License](LICENSE).
