from AppOpener import close, open as appopen
from webbrowser import open as webopen
from dotenv import dotenv_values
from bs4 import BeautifulSoup
from rich import print
from groq import Groq
import webbrowser
import subprocess
import requests
import keyboard
import asyncio
import os
from pathlib import Path
from urllib.parse import quote_plus
import threading
from Backend.FolderContext import get_effective_folder
from Backend.ResearchTool import generate_research_report

# Load environment variables
PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = PROJECT_ROOT / ".env"
env_vars = dotenv_values(ENV_PATH)
GroqAPIKey = (
    env_vars.get("GroqAPIKey")
    or env_vars.get("GROQ_API_KEY")
    or os.getenv("GroqAPIKey")
    or os.getenv("GROQ_API_KEY")
)
GroqModel = (
    env_vars.get("GroqModel")
    or env_vars.get("GROQ_MODEL")
    or os.getenv("GroqModel")
    or os.getenv("GROQ_MODEL")
    or "llama-3.3-70b-versatile"
)

# CSS classes for Google scraping
classes = ["zCubwf", "hgKElc", "LTKOO sY7ric", "Z0LcW", "gsrt vk_bk FzvWSb YwPhnf", "pclqee", "tw-Data-text tw-text-small tw-ta",
           "IZ6rdc", "O5uR6d LTKOO", "vlzY6d", "webanswers-webanswers_table__webanswers-table", "dDoNo ikb4Bb gsrt", "sXLaOc",
           "LwkFKe", "VQF4g", "qv3Wpe", "kno-rdesc", "SPZz6b"]

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'

_client = None
_client_init_error = None
_client_lock = threading.Lock()


def _get_groq_client():
    global _client, _client_init_error
    if _client is not None:
        return _client
    if _client_init_error is not None:
        return None
    if not GroqAPIKey:
        _client_init_error = "Missing Groq API key."
        return None

    with _client_lock:
        if _client is not None:
            return _client
        if _client_init_error is not None:
            return None
        try:
            _client = Groq(api_key=GroqAPIKey)
        except Exception as exc:
            _client_init_error = str(exc)
            _client = None
    return _client

professional_responses = [
    "Your satisfaction is my top priority; feel free to reach out if there's anything else I can help you with.",
    "I'm at your service for any additional questions or support you may need—don't hesitate to ask."
]

messages = []
SystemChatBot = [{"role": "system", "content": f"Hello, I am {env_vars.get('Username')}, You're a content writer. You have to write content like letters."}]

def GoogleSearch(Topic):
    webbrowser.open(f"https://www.google.com/search?q={quote_plus(Topic)}")
    return True

def Content(Topic):
    def OpenNotepad(File):
        default_text_editor = 'notepad.exe'
        subprocess.Popen([default_text_editor, File])

    def ContentWriterAI(prompt):
        client = _get_groq_client()
        if client is None:
            return "Unable to generate content right now (Groq client unavailable)."
        messages.append({"role": "user", "content": f"{prompt}"})
        try:
            completion = client.chat.completions.create(
                model=GroqModel,
                messages=SystemChatBot + messages,
                max_tokens=2048,
                temperature=0.7,
                top_p=1,
                stream=True,
                stop=None
            )
            Answer = ""
            for chunk in completion:
                if chunk.choices[0].delta.content:
                    Answer += chunk.choices[0].delta.content
            Answer = Answer.replace("</s>", "")
            messages.append({"role": "assistant", "content": Answer})
            return Answer
        except Exception as exc:
            return f"Unable to generate content right now: {exc}"

    Topic = str(Topic).strip()
    if Topic.lower().startswith("content "):
        Topic = Topic[8:].strip()
    if not Topic:
        return False

    ContentByAI = ContentWriterAI(Topic)
    output_dir = get_effective_folder() / "content"
    file_path = output_dir / f"{Topic.lower().replace(' ', '')}.txt"
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(ContentByAI)
    
    OpenNotepad(str(file_path))
    return True


def Research(Topic):
    ok, message = generate_research_report(Topic)
    print(message)
    return message if ok else f"Research failed: {message}"

def YouTubeSearch(Topic):
    Url4Search = f"https://www.youtube.com/results?search_query={Topic}"
    webbrowser.open(Url4Search)
    return True

def PlayYouTube(query):
    webbrowser.open(f"https://www.youtube.com/results?search_query={quote_plus(query)}")
    return True

def OpenApp(AppName):
    """
    Opens an application by name. Tries multiple methods:
    1. AppOpener for installed desktop apps
    2. Direct executable launch for common apps
    3. Web version as fallback
    """
    AppName = AppName.lower().strip()
    
    print(f"[DEBUG] Attempting to open: {AppName}")
    
    # Direct executable paths for common Windows apps
    direct_paths = {
        'spotify': [
            r'C:\Users\{}\AppData\Roaming\Spotify\Spotify.exe',
            r'C:\Program Files\Spotify\Spotify.exe',
            r'C:\Program Files (x86)\Spotify\Spotify.exe',
        ],
        'whatsapp': [
            r'C:\Users\{}\AppData\Local\WhatsApp\WhatsApp.exe',
            r'C:\Program Files\WhatsApp\WhatsApp.exe',
            r'C:\Program Files (x86)\WhatsApp\WhatsApp.exe',
        ],
        'chrome': [
            r'C:\Program Files\Google\Chrome\Application\chrome.exe',
            r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
        ],
        'firefox': [
            r'C:\Program Files\Mozilla Firefox\firefox.exe',
            r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe',
        ],
        'edge': [
            r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
            r'C:\Program Files\Microsoft\Edge\Application\msedge.exe',
        ],
    }
    
    # Web fallbacks
    web_apps = {
        'spotify': 'https://open.spotify.com/',
        'whatsapp': 'https://web.whatsapp.com/',
        'facebook': 'https://www.facebook.com/',
        'instagram': 'https://www.instagram.com/',
        'twitter': 'https://twitter.com/',
        'x': 'https://twitter.com/',
        'youtube': 'https://www.youtube.com/',
        'gmail': 'https://mail.google.com/',
        'discord': 'https://discord.com/app',
        'reddit': 'https://www.reddit.com/',
        'linkedin': 'https://www.linkedin.com/',
    }
    
    # Normalize app name
    app_key = AppName
    for key in direct_paths.keys():
        if key in AppName or AppName in key:
            app_key = key
            break
    
    # Method 1: Try direct executable path
    if app_key in direct_paths:
        import os
        username = os.environ.get('USERNAME', '')
        for path_template in direct_paths[app_key]:
            path = path_template.format(username)
            if os.path.exists(path):
                try:
                    print(f"[DEBUG] Found executable: {path}")
                    subprocess.Popen([path], shell=False)
                    return True
                except Exception as e:
                    print(f"[DEBUG] Failed to launch {path}: {e}")
    
    # Method 2: Try AppOpener
    try:
        print(f"[DEBUG] Trying AppOpener for: {AppName}")
        appopen(AppName, match_closest=True, output=False)
        return True
    except Exception as e:
        print(f"[DEBUG] AppOpener failed: {e}")
    
    # Method 3: Try web version
    if app_key in web_apps:
        print(f"[DEBUG] Opening web version: {web_apps[app_key]}")
        webopen(web_apps[app_key])
        return True
    
    # Check if any web app key matches
    for key, url in web_apps.items():
        if key in AppName:
            print(f"[DEBUG] Opening web version: {url}")
            webopen(url)
            return True
    
    # Method 4: Search for app website
    print(f"[DEBUG] Searching for app website")
    try:
        search_query = quote_plus(f"{AppName} official website")
        url = f"https://www.google.com/search?q={search_query}"
        webopen(url)
        return True
    except Exception as e:
        print(f"[DEBUG] All methods failed: {e}")
        return False

def CloseApp(AppName):
    if "all" in AppName:
        return False
    try:
        close(AppName, match_closest=True, output=False)
        return True
    except:
        return False

def SystemAutomation(command):
    command = command.lower()
    if "unmute" in command:
        keyboard.press_and_release("volume mute")
    elif "mute" in command:
        keyboard.press_and_release("volume mute")
    elif "volume up" in command:
        keyboard.press_and_release("volume up")
    elif "volume down" in command:
        keyboard.press_and_release("volume down")
    return True

async def GoogleMaps(Topic):
    URL = f"https://www.google.com/search?q={quote_plus(Topic)}"
    headers = {'User-Agent': useragent}
    response = requests.get(URL, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    for class_name in classes:
        element = soup.find(class_=class_name)
        if element:
            return element.get_text()
    return "No direct result found."

def LiveSearch(query):
    """
    Performs a live search and returns instant answer from Google
    """
    try:
        URL = f"https://www.google.com/search?q={quote_plus(query)}"
        headers = {'User-Agent': useragent}
        response = requests.get(URL, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Try to find featured snippet or instant answer
        results = []
        
        # Check for featured snippet
        for class_name in classes:
            element = soup.find(class_=class_name)
            if element:
                text = element.get_text().strip()
                if text and len(text) > 10:
                    results.append(text)
        
        # Check for knowledge panel
        knowledge_panel = soup.find('div', {'class': 'kno-rdesc'})
        if knowledge_panel:
            text = knowledge_panel.get_text().strip()
            if text and len(text) > 10:
                results.append(text)
        
        # Get top search result snippets
        search_results = soup.find_all('div', {'class': 'VwiC3b'})
        for result in search_results[:3]:
            text = result.get_text().strip()
            if text and len(text) > 20:
                results.append(text)
        
        if results:
            # Return the most relevant result
            return results[0][:500]  # Limit to 500 chars
        
        return "No instant answer found. Opening browser for full results."
    except Exception as e:
        return f"Live search unavailable: {str(e)}"

async def TranslateAndExecute(Query):
    Query = str(Query).strip()
    lower_query = Query.lower()
    if lower_query.startswith("google search "):
        GoogleSearch(Query[14:].strip())
    elif lower_query.startswith("youtube search "):
        YouTubeSearch(Query[15:].strip())
    elif lower_query.startswith("live search ") or lower_query.startswith("quick search "):
        # Extract query after "live search" or "quick search"
        search_query = Query[12:].strip() if "live" in lower_query else Query[13:].strip()
        result = LiveSearch(search_query)
        print(result)
        return result
    elif lower_query.startswith("play "):
        PlayYouTube(Query[5:].strip())
    elif lower_query.startswith("open "):
        OpenApp(Query[5:].strip())
    elif lower_query.startswith("close "):
        CloseApp(Query[6:].strip())
    elif lower_query.startswith("content "):
        Content(Query)
    elif lower_query.startswith("research "):
        return Research(Query)
    elif "volume" in lower_query or "mute" in lower_query:
        SystemAutomation(Query)
    else:
        result = await GoogleMaps(Query)
        print(result)
        return result
    return "Done."

# Example Execution
if __name__ == "__main__":
    pass
