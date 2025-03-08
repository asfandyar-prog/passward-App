import speech_recognition as sr


recognizer = sr.Recognizer()
start=True
while start:
    #
    with sr.Microphone() as source:
        print("Say something in Hungarian or English...")

        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source)


            text = recognizer.recognize_google(audio, language="hu-HU,en-US")
            print("You said:", text)

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")

        except sr.RequestError as e:
            print(f"Error with the speech recognition service: {e}")
