import pyttsx3
import os
pyttsx3.speak("Welcome to my tools")
while True:
    print("Enter your choice: ", end=' ')
    p = input()
    if (("run" in p) or ("launch" in p) or ("execute" in p)) and (("chrome" in p) or ("browser" in p)):
        pyttsx3.speak("Opening chrome for you")
        os.system("chrome")
    elif ("run" in p  or ("launch" in p) or ("execute" in p)) and (("notepad" in p) or ("editor" in p)):
        pyttsx3.speak("Opening notepad for you")
        os.system("notepad")
    elif (("run" in p)  or ("launch" in p) or ("execute" in p)) and ("vlc" in p):
        pyttsx3.speak("Opening vlc for you")
        os.system("vlc")
    elif (("run" in p)  or ("launch" in p) or ("execute" in p)) and (("media" in p) or ("player" in p)):
        pyttsx3.speak("Opening Windows Media Player for you")
        os.system("wmplayer")
    elif (("run" in p)  or ("launch" in p) or ("execute" in p)) and ("camera" in p):
        pyttsx3.speak("Opening camera for you")
        os.system("start microsoft.windows.camera:")
    elif (("run" in p)  or ("launch" in p) or ("execute" in p)) and ("calculator" in p):
        pyttsx3.speak("Opening calculator for you")
        os.system("start calculator:")
    elif ("exit" in p) or ("quit" in  p):
        pyttsx3.speak("Signing off")
        break
    else:
        pyttsx3.speak("Wrong input")
