# import pyttsx3 #to convert text to audio
# en=pyttsx3.init()
# name=input("enter your name: ")
# en.say(f"hello {name} i'm mohamed amr a new friend")
# en.runAndWait()
##############################################################
#talk to machine
# import speech_recognition as sp
# import sys

# rec=sp.Recognizer()
# with sp.Microphone()as mic:
#     while True:
#         print("say something...")
#         audio=rec.listen(mic)
#         text=rec.recognize_google(audio)
#         if text in "hello":
#             print(text)
#             print("hello mohamed ,how are you ?")
#         elif text in "not fine":
#             print(text)
#             print("also me..... same my friend")
#         elif text in "where is my project":
#             print(text)
#             print("Yesterday I was sad so I deleted it ")
#         elif text in "close":
#             sys.exit(0)   
########################################
#make qr code for anything     
# import qrcode
# from PIL import *
# img =qrcode.make("https://www.linkedin.com/in/mohamed-amr-2b4480230/")
# img.save("profile qrcode.png")