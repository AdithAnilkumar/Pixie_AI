"""
Pixie AI Startup Script with Pre-flight Checks
"""

import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
import os
from pathlib import Path

def check_environment():
    """Check if environment is properly set up"""
    print("=" * 60)
    print("Pixie AI - Pre-flight Checks")
    print("=" * 60)
    
    issues = []
    
    # Check Python version
    if sys.version_info < (3, 8):
        issues.append("❌ Python 3.8+ required")
    else:
        print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}")
    
    # Check .env file
    env_path = Path(".env")
    if not env_path.exists():
        issues.append("❌ .env file not found")
    else:
        print("✅ .env file found")
        
        # Check API keys
        from dotenv import dotenv_values
        env_vars = dotenv_values(env_path)
        
        groq_key = env_vars.get("GroqAPIKey", "").strip()
        if not groq_key or groq_key == "your_groq_api_key_here":
            issues.append("❌ Groq API key not configured")
        else:
            print("✅ Groq API key configured")
        
        cohere_key = env_vars.get("CohereAPIKey", "").strip()
        if not cohere_key or cohere_key == "your_cohere_api_key_here":
            issues.append("⚠️  Cohere API key not configured (required for commands)")
        else:
            print("✅ Cohere API key configured")
    
    # Check required directories
    data_dir = Path("Data")
    if not data_dir.exists():
        print("⚠️  Creating Data directory...")
        data_dir.mkdir(parents=True, exist_ok=True)
    else:
        print("✅ Data directory exists")
    
    # Check ChatLog.json
    chatlog = Path("Data/ChatLog.json")
    if not chatlog.exists():
        print("⚠️  Creating ChatLog.json...")
        chatlog.write_text("[]")
    else:
        print("✅ ChatLog.json exists")
    
    # Check required packages
    required_packages = [
        "groq",
        "cohere",
        "dotenv",
        "PyQt5",
        "selenium",
        "AppOpener",
        "edge_tts",
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            if package == "dotenv":
                __import__("dotenv")
            elif package == "AppOpener":
                __import__("AppOpener")
            else:
                __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        issues.append(f"❌ Missing packages: {', '.join(missing_packages)}")
    else:
        print(f"✅ All required packages installed")
    
    print("=" * 60)
    
    if issues:
        print("\n⚠️  Issues Found:")
        for issue in issues:
            print(f"  {issue}")
        print("\nPlease fix these issues before running Pixie AI.")
        print("See TROUBLESHOOTING.md for help.")
        return False
    else:
        print("\n✅ All checks passed! Starting Pixie AI...")
        return True

def main():
    # Change to script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    if not check_environment():
        print("\nRun this to fix missing packages:")
        print("  pip install -r Requirements.txt")
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("Starting Pixie AI...")
    print("=" * 60)
    print("\nTips:")
    print("- Wait for 'Listening...' status before speaking")
    print("- Speak clearly into your microphone")
    print("- Try: 'Open Spotify', 'Open WhatsApp', 'Hello Pixie'")
    print("\nPress Ctrl+C to stop Pixie AI")
    print("=" * 60)
    print()
    
    # Import and run Main
    try:
        import Main
    except KeyboardInterrupt:
        print("\n\nPixie AI stopped by user")
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        print("\nCheck TROUBLESHOOTING.md for help")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
