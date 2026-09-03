# Pixie AI Troubleshooting Guide 🔧

## Voice Input Not Working

### Issue: No speech detected

**Causes:**
1. Microphone not connected or disabled
2. Chrome WebDriver issues
3. Microphone permissions not granted
4. Wrong microphone selected

**Solutions:**

#### Step 1: Check Microphone
```
1. Open Windows Settings
2. Go to System → Sound
3. Check "Input" section
4. Test your microphone
5. Make sure it's not muted
```

#### Step 2: Grant Microphone Permission
```
1. Open Chrome browser manually
2. Go to Settings → Privacy and Security → Site Settings
3. Click "Microphone"
4. Make sure "Sites can ask to use your microphone" is ON
5. Check "Allowed" list
```

#### Step 3: Test Voice Input Separately
```bash
cd Pixie_AI
python Backend/SpeechToText.py
```

Speak when the Chrome window opens. If this works, the issue is elsewhere.

#### Step 4: Check Chrome WebDriver
```bash
cd Pixie_AI
python -c "from selenium import webdriver; from webdriver_manager.chrome import ChromeDriverManager; print('WebDriver OK')"
```

If this fails:
```bash
pip uninstall selenium webdriver-manager
pip install selenium webdriver-manager
```

### Issue: Chrome window doesn't open

**Solution:**
```bash
# Reinstall Chrome WebDriver
pip uninstall selenium webdriver-manager
pip install selenium==4.15.0 webdriver-manager
```

### Issue: "Speech recognition not supported"

**Solution:**
- Make sure you're using Chrome (not Firefox or Edge)
- Update Chrome to latest version
- Check if microphone is connected

## App Opening Not Working

### Issue: Spotify won't open

**Causes:**
1. Spotify not installed
2. Installed in non-standard location
3. AppOpener can't find it

**Solutions:**

#### Method 1: Install Spotify
```
Download from: https://www.spotify.com/download/
```

#### Method 2: Check Installation Path
```bash
# Check if Spotify is installed
dir "C:\Users\%USERNAME%\AppData\Roaming\Spotify\Spotify.exe"
```

If found, it should work. If not found:
```bash
# Search for Spotify
where spotify
```

#### Method 3: Use Web Version
Say: "Open Spotify web" or just wait - it will automatically open web version if desktop app not found.

#### Method 4: Manual Test
```bash
cd Pixie_AI
python -c "from Backend.Automation import OpenApp; OpenApp('spotify')"
```

Check console output for debug messages.

### Issue: WhatsApp won't open

**Solutions:**

#### Method 1: Install WhatsApp Desktop
```
Download from: https://www.whatsapp.com/download
```

#### Method 2: Check Installation
```bash
dir "C:\Users\%USERNAME%\AppData\Local\WhatsApp\WhatsApp.exe"
```

#### Method 3: Use Web Version
The system will automatically open https://web.whatsapp.com/ if desktop app not found.

#### Method 4: Manual Test
```bash
cd Pixie_AI
python -c "from Backend.Automation import OpenApp; OpenApp('whatsapp')"
```

### Issue: Chrome/Firefox won't open

**Solution:**
```bash
# Test AppOpener
cd Pixie_AI
python -c "from AppOpener import open as appopen; appopen('chrome', output=True)"
```

If this fails:
```bash
pip uninstall AppOpener
pip install AppOpener
```

### Issue: No apps open at all

**Solution:**
```bash
# Reinstall AppOpener
pip uninstall AppOpener
pip install AppOpener

# Test it
python -c "from AppOpener import open as appopen; appopen('notepad')"
```

If notepad doesn't open, there's a system issue.

## GUI Not Opening

### Issue: PyQt5 window doesn't appear

**Solution:**
```bash
pip uninstall PyQt5
pip install PyQt5==5.15.10
```

### Issue: "No module named PyQt5"

**Solution:**
```bash
pip install PyQt5 PyQt5-Qt5 PyQt5-sip
```

## API Errors

### Issue: "Missing Groq API key"

**Solution:**
1. Check `.env` file location: `Pixie_AI/.env` (NOT parent directory)
2. Verify API key is correct
3. Check for extra spaces or quotes

```env
# WRONG
GroqAPIKey = "gsk_..."
GroqAPIKey= gsk_...

# CORRECT
GroqAPIKey=gsk_...
```

### Issue: "Missing Cohere API key"

**Solution:**
1. Get key from https://dashboard.cohere.com/
2. Add to `Pixie_AI/.env`:
```env
CohereAPIKey=your_key_here
```

### Issue: "Missing Hugging Face API key"

**Solution:**
1. Get key from https://huggingface.co/settings/tokens
2. Add to `Pixie_AI/.env`:
```env
HuggingFaceAPIKey=your_key_here
```

## Import Errors

### Issue: "No module named 'Backend'"

**Solution:**
```bash
# Make sure you're in the Pixie_AI directory
cd Pixie_AI
python Main.py
```

NOT:
```bash
# WRONG
cd Pixie_AI/Backend
python Main.py
```

### Issue: "No module named 'groq'"

**Solution:**
```bash
pip install -r Requirements.txt
```

## Network Errors

### Issue: "Connection timeout" during pip install

**Solution:**
```bash
pip install --default-timeout=100 -r Requirements.txt
```

### Issue: "Live search not working"

**Solution:**
1. Check internet connection
2. Try using "realtime search" instead
3. Check if Google is accessible

## Performance Issues

### Issue: Pixie is very slow

**Solutions:**
1. Close other Chrome instances
2. Restart Pixie AI
3. Check CPU usage in Task Manager
4. Reduce image generation requests (they're slow)

### Issue: Voice recognition is slow

**Solutions:**
1. Speak clearly and pause
2. Wait for "Listening..." status
3. Check microphone quality
4. Reduce background noise

## Complete Reset

If nothing works, try a complete reset:

```bash
# 1. Close Pixie AI completely
# 2. Delete temporary files
cd Pixie_AI
rmdir /s /q Data\temp
del Frontend\Files\*.data

# 3. Reinstall dependencies
pip uninstall -y groq cohere PyQt5 selenium AppOpener
pip install -r Requirements.txt

# 4. Verify .env file
type .env

# 5. Run test
python test_setup.py

# 6. Run Pixie
python Main.py
```

## Debug Mode

To see detailed debug output:

```bash
cd Pixie_AI
python Main.py
```

Watch the console for:
- `[DEBUG]` messages from app opening
- Error messages
- API responses
- Decision model output

## Common Error Messages

### "HTTPSConnectionPool: Max retries exceeded"
**Cause:** Network issue or API down
**Solution:** Check internet, wait a few minutes, try again

### "protobuf version conflict"
**Solution:**
```bash
pip install --upgrade protobuf
```

### "Read timed out"
**Solution:**
```bash
pip install --default-timeout=100 -r Requirements.txt
```

### "Unable to locate element"
**Cause:** Chrome WebDriver issue
**Solution:**
```bash
pip uninstall selenium
pip install selenium==4.15.0
```

## Getting Help

If you're still stuck:

1. **Check console output** - Look for error messages
2. **Run test scripts**:
   ```bash
   python test_setup.py
   python test_voice_and_apps.py
   ```
3. **Check file locations**:
   ```bash
   dir .env
   dir Data\ChatLog.json
   dir Backend\*.py
   ```
4. **Verify Python version**:
   ```bash
   python --version
   ```
   (Should be 3.8 or higher)

## Quick Fixes Checklist

- [ ] `.env` file in `Pixie_AI/.env` (not parent directory)
- [ ] All API keys added to `.env`
- [ ] Running from `Pixie_AI` directory
- [ ] Microphone connected and working
- [ ] Chrome browser installed
- [ ] Internet connection working
- [ ] All dependencies installed (`pip install -r Requirements.txt`)
- [ ] Python 3.8 or higher
- [ ] No other Pixie AI instances running

## Still Not Working?

Try the nuclear option:

```bash
# 1. Backup your .env file
copy Pixie_AI\.env .env.backup

# 2. Delete everything
rmdir /s /q Pixie_AI

# 3. Re-clone or re-download
# (get fresh copy)

# 4. Restore .env
copy .env.backup Pixie_AI\.env

# 5. Install dependencies
cd Pixie_AI
pip install -r Requirements.txt

# 6. Run
python Main.py
```

---

**Most Common Issues:**
1. ❌ `.env` in wrong location → Move to `Pixie_AI/.env`
2. ❌ Missing API keys → Add to `.env`
3. ❌ Running from wrong directory → `cd Pixie_AI`
4. ❌ Microphone not working → Check Windows settings
5. ❌ Apps not installed → Install or use web versions
