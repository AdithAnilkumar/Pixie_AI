"""
Voice Input Diagnostic Tool
Helps identify microphone and speech recognition issues
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

def test_microphone_access():
    """Test if microphone is accessible"""
    print("=" * 60)
    print("Testing Microphone Access")
    print("=" * 60)
    
    try:
        import pyaudio
        p = pyaudio.PyAudio()
        
        print("\n✅ PyAudio installed")
        print(f"\nAvailable audio devices:")
        
        for i in range(p.get_device_count()):
            info = p.get_device_info_by_index(i)
            if info['maxInputChannels'] > 0:
                print(f"  [{i}] {info['name']} (Input channels: {info['maxInputChannels']})")
        
        p.terminate()
        return True
    except ImportError:
        print("⚠️  PyAudio not installed (optional)")
        return True
    except Exception as e:
        print(f"⚠️  Error checking microphone access: {e}")
        return False

if __name__ == "__main__":
    test_microphone_access()