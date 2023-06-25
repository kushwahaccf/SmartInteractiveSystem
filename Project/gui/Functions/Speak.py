import pyttsx3

class Speak:

    def __init__(self,text):
        self.text=text


    def speak(self):
    # Initialize the speech engine
        engine = pyttsx3.init()

        # Set the speech rate (optional)
        engine.setProperty('rate', 150)

        # Set the speech volume (optional)
        engine.setProperty('volume', 0.7)

        # Convert the text to speech
        engine.say(self.text)

        # Wait for the speech to complete
        engine.runAndWait()
