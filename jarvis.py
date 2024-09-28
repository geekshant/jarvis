import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
if __name__ == "__main__":
    speak("initializing jarvis...")
    
    while True:
        r = sr.Recognizer()
        

        # Recognize speech using Google Web Speech API
        print("recognising...")
        try:
            with sr.Microphone() as source:
                print("listening")
                audio = r.listen(source, timeout=5, phrase_time_limit=1)
            command = r.recognize_google(audio)
            if(command.lower()== "jarvis"):
                speak("yes")
            with sr.Microphone() as source:
                print("listening")
                audio = r.listen(source)
        except Exception as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))  