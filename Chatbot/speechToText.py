import speech_recognition as sr

while True:
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("say something")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print(text)

            with open("text.txt",'a+') as t:
                    t.write(text)
                    t.write('\n')

            if text == 'bye':
                break
                
        except sr.UnknownValueError:
            print("Could not read")    