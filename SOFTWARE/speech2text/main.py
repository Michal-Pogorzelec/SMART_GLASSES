# speech to text program
# when you have problem with installing pyaudio use this: https://stackoverflow.com/questions/53866104/pyaudio-failed-to-install-on-windows-10

import speech_recognition as sr
import pyttsx3
import pyaudio
import keyboard

r = sr.Recognizer()


def Text2Speech(command: str) -> None:
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def main() -> None:
    global MyText
    MyText = ""

    while True:
        if MyText == "koniec":
            break
        try:

            with sr.Microphone() as source:
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source, duration=0.2)

                audio = r.listen(source)

                MyText = r.recognize_google(audio, language="pl-PL")
                MyText = MyText.lower()

                print("Did you say " + MyText + "?")
                # Text2Speech(MyText)

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occured")


if __name__ == "__main__":
    main()
