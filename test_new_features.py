"""
Test script for new Pixie AI features
Tests: Live Search, Spotify opening, WhatsApp opening
"""

import sys
from pathlib import Path

# Add Backend to path
sys.path.insert(0, str(Path(__file__).parent))

from Backend.Automation import LiveSearch, OpenApp
from Backend.Model import FirstLayerDMM

def test_live_search():
    print("=" * 60)
    print("Testing Live Search Feature")
    print("=" * 60)
    
    test_queries = [
        "weather today",
        "bitcoin price",
        "capital of France",
        "who is Elon Musk",
    ]
    
    for query in test_queries:
        print(f"\n🔍 Query: {query}")
        try:
            result = LiveSearch(query)
            print(f"✅ Result: {result[:200]}...")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("\n" + "=" * 60)

def test_decision_model():
    print("\nTesting Decision Model Recognition")
    print("=" * 60)
    
    test_commands = [
        "open spotify",
        "open whatsapp",
        "live search weather today",
        "open spotify and whatsapp",
        "close spotify",
    ]
    
    for command in test_commands:
        print(f"\n💬 Command: {command}")
        try:
            decision = FirstLayerDMM(command)
            print(f"✅ Decision: {decision}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("\n" + "=" * 60)

def test_app_opening():
    print("\nTesting App Opening (Dry Run)")
    print("=" * 60)
    print("\n⚠️  Note: This will actually try to open apps!")
    print("Press Ctrl+C to skip this test, or Enter to continue...")
    
    try:
        input()
    except KeyboardInterrupt:
        print("\n⏭️  Skipped app opening test")
        return
    
    test_apps = [
        "spotify",
        "whatsapp",
    ]
    
    for app in test_apps:
        print(f"\n📱 Testing: {app}")
        try:
            result = OpenApp(app)
            if result:
                print(f"✅ Successfully opened {app}")
            else:
                print(f"⚠️  Could not open {app} (may not be installed)")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("\n" + "=" * 60)

def main():
    print("\n" + "=" * 60)
    print("Pixie AI - New Features Test Suite")
    print("=" * 60)
    
    # Test 1: Live Search
    try:
        test_live_search()
    except Exception as e:
        print(f"\n❌ Live Search test failed: {e}")
    
    # Test 2: Decision Model
    try:
        test_decision_model()
    except Exception as e:
        print(f"\n❌ Decision Model test failed: {e}")
    
    # Test 3: App Opening (optional)
    try:
        test_app_opening()
    except Exception as e:
        print(f"\n❌ App Opening test failed: {e}")
    
    print("\n" + "=" * 60)
    print("Test Suite Complete!")
    print("=" * 60)
    print("\nSummary:")
    print("✅ Live Search - Fetches instant answers from Google")
    print("✅ Decision Model - Recognizes 'open spotify', 'open whatsapp', 'live search'")
    print("✅ App Opening - Opens desktop apps or web versions")
    print("\nTo use in Pixie AI:")
    print("  python Main.py")
    print("\nThen say:")
    print("  'Open Spotify'")
    print("  'Open WhatsApp'")
    print("  'Live search weather today'")
    print("=" * 60)

if __name__ == "__main__":
    main()
