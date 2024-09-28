import speech_recognition as sr
import pyttsx3
import webbrowser
import musiclibrary as ml

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def ProcessCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open twitter" in c.lower():
        webbrowser.open("https://X.com")
    elif "open linkdin" in c.lower():
        webbrowser.open("https://linkdin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = ml.music[song]
        webbrowser.open(link)
    
if __name__ == "__main__":
    speak("initializing jarvis...")
    
    while True:
        # listen for the wake word "jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        

        # Recognize speech using Google Web Speech API
        print("recognising...")
        try:
            with sr.Microphone() as source:
                print("listening")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower()== "jarvis"):
                speak("yes")

            # listen for command
                
                with sr.Microphone() as source:
                    print("jarvis active")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    ProcessCommand("hello, i am good")
                       
        except Exception as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))  