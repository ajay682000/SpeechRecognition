import speech_recognition as sr
import time

r = sr.Recognizer()

# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

with sr.Microphone() as source:
    print('Speak Anything: ')
    audio = r.listen(source)
    time.sleep(5)
    print("Recognizing.....")

    try:
        text = r.recognize_google(audio)
        print('You said : {}'.format(text))
    except:
        print("Your voice was not clear")