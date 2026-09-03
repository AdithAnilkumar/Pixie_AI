"""
Quick test for voice input and app opening
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

def test_app_opening():
    print("=" * 60)
    print("Testing App Opening")
    print("=" * 60)
    
    from Backend.Automation import OpenApp
    
    test_apps = [
        ("Spotify", "spotify"),
        ("WhatsApp", "whatsapp"),
        ("Chrome", "chrome"),
    ]
    
    print("\n⚠️  This will actually try to open apps!")
    print("Press Enter to continue or Ctrl+C to skip...")
    try:
        input()
    except KeyboardInterrupt:
        print("\n⏭️  Skipped")
        return
    
    for name, app in test_apps:
        print(f"\n📱 Testing: {name}")
        try:
            result = OpenApp(app)
            if result:
                print(f"✅ {name} opened successfully")
            else:
                print(f"⚠️  {name} - check console for details")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print("   (Close the app before continuing)")
        input("   Press Enter to continue...")

def test_voice_input():
    print("\n" + "=" * 60)
    print("Testing Voice Input")
    print("=" * 60)
    
    print("\n⚠️  This will open a small Chrome window for voice recognition")
    print("Press Enter to continue or Ctrl+C to skip...")
    try:
        input()
    except KeyboardInterrupt:
        print("\n⏭️  Skipped")
        return
    
    from Backend.SpeechToText import SpeechRecognition
    
    print("\n🎤 Speak now (you have 20 seconds)...")
    print("   Say something like: 'Hello Pixie'")
    
    try:
        text = SpeechRecognition()
        if text:
            print(f"\n✅ Recognized: {text}")
        else:
            print(f"\n⚠️  No speech detected")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

def main():
    print("\n" + "=" * 60)
    print("Pixie AI - Voice & App Opening Test")
    print("=" * 60)
    
    print("\nWhat would you like to test?")
    print("1. App Opening (Spotify, WhatsApp, Chrome)")
    print("2. Voice Input")
    print("3. Both")
    print("4. Exit")
    
    choice = input("\nEnter choice (1-4): ").strip()
    
    if choice == "1":
        test_app_opening()
    elif choice == "2":
        test_voice_input()
    elif choice == "3":
        test_app_opening()
        test_voice_input()
    else:
        print("Exiting...")
        return
    
    print("\n" + "=" * 60)
    print("Test Complete!")
    print("=" * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user")
    except Exception as e:
        print(f"\n\nTest failed: {e}")
        import traceback
        traceback.print_exc()
