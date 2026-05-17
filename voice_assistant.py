import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import time

def txtspeech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)  # Added timeout to prevent infinite waiting
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(f"You said: {data}")
            return data.lower()  # Convert to lowercase for comparison
        except sr.UnknownValueError:
            print("Not understanding...")
            return None
        except sr.RequestError:
            print("Could not connect to the speech recognition service.")
            return None

def speechtxt(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # 0 = Male, 1 = Female
    engine.setProperty('rate', 150)

    print(f"Jarvis: {text}")  # Debugging: Print to console
    engine.say(text)
    engine.runAndWait()

def open_application(app_name):
    """ Opens an application based on the command. """

    # Predefined paths of installed applications
    apps = {
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "notepad": r"C:\Windows\system32\notepad.exe",
        "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
        "excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
        "spotify": r"C:\Users\YourUsername\AppData\Roaming\Spotify\Spotify.exe"
    }

    if app_name in apps:
        speechtxt(f"Opening {app_name}")
        os.startfile(apps[app_name])
    else:
        speechtxt(f"Sorry, I don't know how to open {app_name}")

if __name__ == '__main__':
    print("Say 'Hey Jarvis' to activate...")

    while True:
        wake_word = txtspeech()
        if wake_word and ("hey jarvis" in wake_word or "jarvis" in wake_word):
            speechtxt("Yes, how can I assist you?")
            break  # Exit wake word loop and start main loop

    while True:
        data1 = txtspeech()
        if data1:
            data1 = data1.lower()

            if "your name" in data1:
                speechtxt("My name is Jarvis.")

            elif "old are you" in data1:
                speechtxt("I am two years old.")

            elif 'time' in data1:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                speechtxt(f"The time is {current_time}")

            elif 'youtube' in data1:
                speechtxt("Opening YouTube.")
                webbrowser.open("https://www.youtube.com/")

            elif 'web' in data1:
                speechtxt("Opening Netflix.")
                webbrowser.open("https://www.netflix.com/latest")

            elif "jokes" in data1:
                joke = pyjokes.get_joke(language='en', category="neutral")
                print(joke)
                speechtxt(joke)

            elif 'play song' in data1:
                music_dir = r"C:\Users\heman\Music"
                if os.path.exists(music_dir):
                    songs = os.listdir(music_dir)
                    if songs:
                        print(songs)
                        os.startfile(os.path.join(music_dir, songs[0]))
                        speechtxt("Playing music.")
                    else:
                        speechtxt("No songs found in your music folder.")
                else:
                    speechtxt("Music folder not found.")

            elif "exit" in data1:
                speechtxt("Thank you! Exiting now.")
                break
        else:
            print("No speech detected. Try again.")
