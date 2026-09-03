"""
Pixie AI Setup Verification Script
Run this to check if all required components are configured correctly.
"""

import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path
from dotenv import dotenv_values

def check_mark(condition):
    return "✅" if condition else "❌"

def main():
    print("=" * 60)
    print("Pixie AI Setup Verification")
    print("=" * 60)
    print()
    
    # Check Python version
    python_version = sys.version_info
    python_ok = python_version >= (3, 8)
    print(f"{check_mark(python_ok)} Python Version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    if not python_ok:
        print("   ⚠️  Python 3.8+ required")
    print()
    
    # Check .env file
    env_path = Path(".env")
    env_exists = env_path.exists()
    print(f"{check_mark(env_exists)} .env file exists: {env_path.absolute()}")
    
    if not env_exists:
        print("   ❌ .env file not found!")
        print("   Create it with your API keys")
        return
    
    # Load environment variables
    env_vars = dotenv_values(env_path)
    print()
    
    # Check required variables
    print("Required API Keys:")
    print("-" * 60)
    
    username = env_vars.get("Username", "").strip()
    print(f"{check_mark(username and username != 'YourName')} Username: {username or 'NOT SET'}")
    
    assistantname = env_vars.get("Assistantname", "").strip()
    print(f"{check_mark(assistantname)} Assistantname: {assistantname or 'NOT SET'}")
    
    groq_key = env_vars.get("GroqAPIKey", "").strip()
    groq_ok = groq_key and groq_key != "your_groq_api_key_here" and len(groq_key) > 20
    print(f"{check_mark(groq_ok)} Groq API Key: {'Configured' if groq_ok else 'NOT SET'}")
    if not groq_ok:
        print("   ⚠️  Get from: https://console.groq.com/")
    
    cohere_key = env_vars.get("CohereAPIKey", "").strip()
    cohere_ok = cohere_key and cohere_key != "your_cohere_api_key_here" and len(cohere_key) > 20
    print(f"{check_mark(cohere_ok)} Cohere API Key: {'Configured' if cohere_ok else 'NOT SET'}")
    if not cohere_ok:
        print("   ⚠️  Get from: https://dashboard.cohere.com/")
    
    hf_key = env_vars.get("HuggingFaceAPIKey", "").strip()
    hf_ok = hf_key and hf_key != "your_huggingface_api_key_here" and len(hf_key) > 20
    print(f"{check_mark(hf_ok)} Hugging Face API Key: {'Configured' if hf_ok else 'NOT SET'}")
    if not hf_ok:
        print("   ⚠️  Get from: https://huggingface.co/settings/tokens")
    
    print()
    print("Optional Features:")
    print("-" * 60)
    
    telegram_token = env_vars.get("TelegramBotToken", "").strip()
    telegram_ok = telegram_token and len(telegram_token) > 20
    print(f"{check_mark(telegram_ok)} Telegram Bot: {'Configured' if telegram_ok else 'Not configured (optional)'}")
    
    print()
    
    # Check required directories
    print("Directory Structure:")
    print("-" * 60)
    
    data_dir = Path("Data")
    print(f"{check_mark(data_dir.exists())} Data/ directory: {data_dir.absolute()}")
    
    chatlog = Path("Data/ChatLog.json")
    print(f"{check_mark(chatlog.exists())} ChatLog.json: {chatlog.absolute()}")
    
    backend_dir = Path("Backend")
    print(f"{check_mark(backend_dir.exists())} Backend/ directory")
    
    frontend_dir = Path("Frontend")
    print(f"{check_mark(frontend_dir.exists())} Frontend/ directory")
    
    print()
    
    # Check critical Python packages
    print("Python Packages:")
    print("-" * 60)
    
    packages = [
        "groq",
        "cohere",
        "dotenv",
        "PyQt5",
        "edge_tts",
        "requests",
        "PIL",
        "bs4",
    ]
    
    missing_packages = []
    for package in packages:
        try:
            if package == "dotenv":
                __import__("dotenv")
            elif package == "PIL":
                __import__("PIL")
            elif package == "bs4":
                __import__("bs4")
            else:
                __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - NOT INSTALLED")
            missing_packages.append(package)
    
    print()
    print("=" * 60)
    
    # Final verdict
    all_required = groq_ok and cohere_ok and python_ok and env_exists
    
    if all_required and not missing_packages:
        print("✅ ALL CHECKS PASSED!")
        print()
        print("You're ready to run Pixie AI:")
        print("   python Main.py")
        if not hf_ok:
            print()
            print("⚠️  Note: Image generation won't work without Hugging Face API key")
    else:
        print("❌ SETUP INCOMPLETE")
        print()
        print("Please fix the issues above before running Pixie AI.")
        print()
        if missing_packages:
            print("Install missing packages:")
            print("   pip install -r Requirements.txt")
        if not groq_ok or not cohere_ok:
            print()
            print("Add missing API keys to .env file")
            print("See QUICK_START.md for instructions")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
