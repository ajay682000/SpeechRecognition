import speech_recognition as sr
import time


def main():


    r = sr.Recognizer()

    # for index, name in enumerate(sr.Microphone.list_microphone_names()):
    #     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Speak Anything: ')
        time.sleep(5)
        print("Now plug out your microphone for conversion")
        audio = r.listen(source)
        print("Recognizing now...")

        try:
            text = r.recognize_google(audio)
            print('You said : {}'.format(text))
            print("Successfull \n")
        except Exception as e:
            # print("Error : " + str(e))
            print("You have not said clearly")

        

    

if __name__ =="__main__":
    main()
