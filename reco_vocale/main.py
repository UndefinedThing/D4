###########################################################################
#                   INSTALLATIONS FAITES :
#           -   speech_recognition
#           -   PySpeech
#           -   PyAudio


import speech_recognition as sr
import webbrowser as web
import os
import sys

isCalib = False

def johnResponse(audio):
    # audio.replace("é", "e")
    command = audio.split(" ")
    if (command[0] == "quitter") :
        return ([0, " \n ================================================================ \n \
            Merci d'avoir utilisé la commande vocale \
                \n ================================================================ \n"])
    elif (command[0] == "ouvre"):
        if len(command) > 2:
            return ([1, "Veuillez simplement préciser le nom du site"])
        elif len(command) < 2:
            return ([1, "Veuillez préciser le nom d'un site"])
        else :
            openSite(command[1])
    else :
        return ([1, "Désolé mais je n'ai pas compris votre demande ("+audio+")"])

def myCommand():

    global isCalib
    r  = sr.Recognizer()
    with sr.Microphone() as source:
        if not isCalib:
            print("Veuillez attendre la fin de l'autoréglage ...")
            r.adjust_for_ambient_noise(source, duration=6)
            print("Merci de votre patience")
            isCalib = True
        print("Dites quelque chose :")
        audio = r.listen(source, phrase_time_limit=2)
    try:
        text = r.recognize_google(audio, language="fr-FR")
        return johnResponse(text)

    except sr.UnknownValueError:
        return ([1, "L'audio n'as pas été compris"])
    except sr.RequestError as e:
        return ([1, "Le service Google Speech API ne fonctionne plus" + format(e)])

def openSite(siteName):
    return ([1, "J'ai atteint openSite avec le paramètre " + siteName])

while True:
    aled = myCommand()
    print(aled[1])
    if aled[0] == 0 :
        sys.exit()