import speech_recognition as sr

r = sr.Recognizer()

def voice_to_text():
    while(True):
        print("Start speaking: ")
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = text.lower()
            return text
