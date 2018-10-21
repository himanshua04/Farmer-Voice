from gtts import gTTS
import speech_recognition as sr
import os 

r=sr.Recognizer()
with sr.Microphone() as source:
    audio=r.listen(source)
    mytext=" "
    mytext=r.recognize_google(audio)
    print(mytext)
    

language = 'hi'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("welcome.mp3")  
os.system("welcome.mp3") 
