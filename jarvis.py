#!/usr/bin/env python3
# Simple Termux-friendly J.A.R.V.I.S (espeak if available, otherwise plain text)
import shutil
import subprocess
import datetime
import sys

# Check if espeak is available
ESPEAK = shutil.which("espeak") is not None

def speak(text):
    """Speak using espeak if present, otherwise print text."""
    if ESPEAK:
        try:
            # -ven+m3 = voice variant (optional). You can remove options if problematic.
            subprocess.run(["espeak", text], check=False)
        except Exception:
            # fallback to print if espeak call fails
            print(f"J.A.R.V.I.S (text): {text}")
    else:
        print(f"J.A.R.V.I.S (text): {text}")

def get_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def wish_me():
    hour = datetime.datetime.now().hour
    if hour < 12:
        greet = "Good Morning!"
    elif hour < 18:
        greet = "Good Afternoon!"
    else:
        greet = "Good Evening!"
    speak(greet)
    speak("I am JARVIS How can I help you? Type a command or 'help'.")

def show_help():
    help_text = (
        "Available commands:\n"
        "  time    - show current time\n"
        "  hello   - greet back\n"
        "  help    - show this help\n"
        "  exit    - quit\n"
    )
    speak(help_text)

def main_loop():
    wish_me()
    while True:
        try:
            cmd = input("You: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            speak("Goodbye.")
            sys.exit(0)

        if cmd in ("", " "):
            continue
        if cmd == "time":
            speak(f"The current time is {get_time()}.")
        elif cmd == "hello":
            speak("Hello! Nice to meet you.")
        elif cmd == "help":
            show_help()
        elif cmd == "exit":
            speak("Shutting down. Bye!")
            break
        else:
            speak("Sorry, I did not understand that. Type 'help' for commands.")

if __name__ == "__main__":
    main_loop()
