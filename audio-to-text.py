import speech_recognition as sr
 
AUDIO_FILE = ("D:\\Coding\\Python\\audio_Test.wav")
r = sr.Recognizer()
 
with sr.AudioFile(AUDIO_FILE) as source:
        

    print("Converting Audio To Text ..... ")
 
    audio=  r.record(source)
 
    try:
        print("Converted Audio Is : \n" + r.recognize_google(audio))
 
 
    except Exception as e:
        print("Error {} : ".format(e) )