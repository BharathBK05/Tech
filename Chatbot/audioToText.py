import speech_recognition as sr


AUDIO_FILE = 'audio123.WAV'

r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

try:
    textdata = r.recognize_google(audio)
    print("Text data: " + textdata)

except sr.UnknownValueError:
    print(" Audio Error")

except sr.RequestError as e:
    print("Could not request results from Google API; {0}".format(e))

  
   

#Write results to a txt file
file = open("result.txt","w")
file.writelines(textdata) 
file.close()
