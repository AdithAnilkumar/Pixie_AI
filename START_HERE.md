# 🚀 START HERE - Quick Setup & Run

## ✅ Fixed Issues
- ✅ Voice input now works
- ✅ Spotify opens correctly
- ✅ WhatsApp opens correctly
- ✅ All apps have web fallbacks

## 🎯 Quick Start (3 Steps)

### Step 1: Run Pre-flight Check
```bash
cd Pixie_AI
python start_pixie.py
```

This will:
- Check all requirements
- Verify API keys
- Create missing files
- Start Pixie AI automatically

### Step 2: Wait for "Listening..."
Look for this in the GUI window

### Step 3: Speak!
Try these commands:
- "Hello Pixie"
- "Open Spotify"
- "Open WhatsApp"
- "Live search weather today"

## 🧪 Test First (Optional)

Want to test before running?

```bash
cd Pixie_AI
python test_voice_and_apps.py
```

Choose:
1. Test app opening
2. Test voice input
3. Test both

## 📋 Requirements Checklist

Before running, make sure you have:

- [x] Python 3.8+ installed
- [x] All packages installed (`pip install -r Requirements.txt`)
- [x] `.env` file in `Pixie_AI/.env` with API keys
- [x] Microphone connected and working
- [x] Chrome browser installed
- [x] Internet connection

## 🎤 Voice Commands

### Open Apps
```
"Open Spotify"
"Open WhatsApp"  
"Open Chrome"
"Launch Spotify and WhatsApp"
```

### Search
```
"Live search weather today"
"Google search Python tutorials"
"YouTube search music"
```

### Chat
```
"Hello Pixie"
"How are you"
"Tell me a joke"
```

### Images
```
"Generate image of a sunset"
"Create a picture of a robot"
```

### Research
```
"Research AI in 3 pages"
"Make a report on quantum computing"
```

## 🔧 If Something Doesn't Work

### Voice Input Not Working?
```bash
# Test microphone
python Backend/SpeechToText.py

# Check Windows Settings → Sound → Input
```

### Apps Not Opening?
```bash
# Test directly
python -c "from Backend.Automation import OpenApp; OpenApp('spotify')"

# Check console for debug messages
```

### See Full Troubleshooting
```
Read: TROUBLESHOOTING.md
```

## 📁 Important Files

```
Pixie_AI/
├── start_pixie.py              ← Run this to start
├── test_voice_and_apps.py      ← Test functionality
├── Main.py                     ← Main application
├── .env                        ← Your API keys
├── TROUBLESHOOTING.md          ← Fix issues
├── FIXES_APPLIED.md            ← What was fixed
└── VOICE_COMMANDS_REFERENCE.md ← All commands
```

## 🎯 Three Ways to Run

### 1. Smart Start (Recommended)
```bash
python start_pixie.py
```
Checks everything first, then starts.

### 2. Direct Start
```bash
python Main.py
```
Starts immediately.

### 3. Test Mode
```bash
python test_voice_and_apps.py
```
Test before running.

## ⚡ Quick Fixes

### "Missing API key"
```
Edit: Pixie_AI/.env
Add your API keys
```

### "No module named..."
```bash
pip install -r Requirements.txt
```

### "Microphone not working"
```
Windows Settings → Sound → Input
Test your microphone
```

### "Apps not opening"
```
They will open web versions automatically
Or install desktop apps
```

## 🎉 What Works Now

✅ Voice recognition (with visible Chrome)
✅ Spotify (desktop or web)
✅ WhatsApp (desktop or web)
✅ Chrome, Firefox, Edge
✅ Live search
✅ All previous features

## 📚 Documentation

- `START_HERE.md` ← You are here
- `QUICK_START.md` - API key setup
- `VOICE_COMMANDS_REFERENCE.md` - All commands
- `TROUBLESHOOTING.md` - Fix issues
- `FIXES_APPLIED.md` - Technical details
- `NEW_FEATURES.md` - Feature guide

## 💡 Pro Tips

1. **Wait for "Listening..."** before speaking
2. **Speak clearly** into microphone
3. **Check console** for debug messages
4. **Use web versions** if desktop apps not installed
5. **Read TROUBLESHOOTING.md** if stuck

## 🚀 Ready to Go!

```bash
cd Pixie_AI
python start_pixie.py
```

Then say: **"Hello Pixie"**

---

**Need Help?**
- Check console output for errors
- Read TROUBLESHOOTING.md
- Run test_voice_and_apps.py
- Verify .env file has API keys

**Enjoy Pixie AI! 🦊**
