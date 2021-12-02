import pyttsx3
import speech_recognition as sr 
import datetime
import webbrowser
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1]) to check the voice avalible in the desktop 
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(" good morning , how can i help you , just tell me i can do anything for you ")
    elif hour>=12 and hour<18:
        speak(" good afternoon ashish how's your day is going on ")
    else :
        speak("good evening ashish , how can i help you ")
    speak(" i am  your asistent ")  
def takecommand():   # it take the input from the user and return string output 
    r= sr.Recognizer() # recognizer class help to recognizer
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold =1  
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query =r.recognize_google(audio,language='en-in' )
        print(f"user said :{query}\n")     
    except Exception as e :
        print(e)
        print("say that again please ...")
        return "None" 
    return query

if __name__ =="__main__":
    wishme()
    # takecommand()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query= query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences =2)
            speak("Accoding to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'microsoft edge' in query:
            webbrowser.open("bing.com")
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")
        elif 'open github' in query:
            webbrowser.open("github.com")        
        elif 'open mail' in query:
            webbrowser.open("gmail.com")
        elif 'open slack' in query:
            webbrowser.open("slack.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif ' hello' in query:
            speak("hey")
        elif 'how are you' in query:
            speak("i am good ")                         
        elif 'quit' in query:
            exit()           