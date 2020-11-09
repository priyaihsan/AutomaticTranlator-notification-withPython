

# google translate
import googletrans
from googletrans import Translator
Trans = Translator()

# notification
import time
from win10toast import ToastNotifier
toaster = ToastNotifier()

# autocopypaste
import sys
import os
import pyperclip
sys.path.append(os.path.abspath("SO_site-packages"))


# if you want to know anycode of your country just write : 
# print(googletrans.LANGUAGES)
FromLanguage = 'en' # en = english
ToLanguage = 'id' # id = indonesia

# empty value
recent_value = ""

while True :
    value = pyperclip.paste() # value of paste in google or anything
    if value != recent_value:
        recent_value = value
        print("Value changed: %s" % str(recent_value)[:20])
        Translated = Trans.translate(value,src= FromLanguage,dest= ToLanguage)
        toaster.show_toast("Automatic Translator",
                            Translated.text,
                            duration=15)
    elif value == 'exit':
        value = pyperclip.copy("Welcome to the automatic translator notification")
        break

    time.sleep(0.1)
