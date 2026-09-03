# New Features & Enhancements in Pixie AI 🎉

## 1. WhatsApp Messaging Automation 💬

### What's New
Send pre-composed WhatsApp messages to phone numbers or contacts using simple voice or text commands.

### How to Use
- *"Send WhatsApp message to +1234567890 saying Hello Sir"*
- *"Send WhatsApp to +919876543210 saying Meeting is rescheduled"*
- *"WhatsApp message saying I will be home soon"*

### How It Works
- Detects recipient phone number & message body automatically.
- Pre-fills WhatsApp Web or Desktop application with recipient and message.

---

## 2. Groq `groq/compound` Model Integration 🧠

### What's New
Migrated model API calls to Groq's high-speed active model (`groq/compound`) to replace legacy deprecated model strings.

### Performance
- High-accuracy conversational AI.
- Instant response synthesis without model deprecation errors.

---

## 3. High-Speed Speech & Natural TTS Pipeline ⚡

### Instant Speech-to-Text (STT)
- Silence pause threshold reduced from `1.0s` down to **`0.4s`**.
- Submits your query instantly as soon as you finish speaking.

### Natural Spoken Audio (TTS)
- Increased speech rate to **`+25%`** (`rate='+25%'`).
- Added markdown symbol cleaner so symbols (`#`, `**`, `*`, backticks) are stripped out before speech synthesis.
- Full response spoken out loud cleanly without truncating or skipping sentences.

---

## 4. Respectful "Sir" Addressing & Clean Formatting 👔

### Behavior Rules
- Addresses the user respectfully as **"Sir"**.
- Delivers concise, direct responses with key terms highlighted in **bold** or short bullet lists.
- Stripped robotic section headers (`## Quick Answer`, `## Steps`, `## Tips`).
- Strict negative prompt rule preventing system instructions from appearing on screen.

---

## 5. System Tray Launch Mode 🖥️

### What's New
When starting Pixie (`python start_pixie.py`), it launches quietly in the Windows System Tray (icon near clock) with voice input enabled automatically.

### Accessing the 3D UI
- Right-click the Pixie fox icon near your Windows clock and click **Pixie UI** anytime.

---

## 6. Live Search & App Launcher 🎵

- **Live Search**: Instant Google scraping for featured snippets (`"Live search weather today"`).
- **Multi-Path App Control**: Launches desktop apps (Spotify, WhatsApp, Chrome, Edge, Firefox) with web fallback.
- **Deep Research Exporter**: Multi-source academic research report generator (.docx with citations).
- **Telegram Remote Control**: Full mobile control bridge with voice replies, screenshot capture, and file browser.
